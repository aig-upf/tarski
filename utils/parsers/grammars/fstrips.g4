
/* Functional STRIPS grammar, adapted from PDDL 3.1

  To keep in mind: https://stackoverflow.com/a/29780284
*/

grammar fstrips;

tokens {
    DOMAIN,
    DOMAIN_NAME,
    REQUIREMENTS,
    TYPES,
    EITHER_TYPE,
    CONSTANTS,
    FUNCTIONS,
    FREE_FUNCTIONS,
    PREDICATES,
    ACTION,
    CONSTRAINT,
    EVENT,
    GLOBAL_CONSTRAINT,
    DURATIVE_ACTION,
    PROBLEM,
    PROBLEM_NAME,
    PROBLEM_DOMAIN,
    OBJECTS,
    INIT,
    FUNC_HEAD,
    PRECONDITION,
    EFFECT,
    AND_GD,
    OR_GD,
    NOT_GD,
    IMPLY_GD,
    EXISTS_GD,
    FORALL_GD,
    COMPARISON_GD,
    AND_EFFECT,
    FORALL_EFFECT,
    WHEN_EFFECT,
    ASSIGN_EFFECT,
    NOT_EFFECT,
    PRED_HEAD,
    GOAL,
    BINARY_OP,
    EQUALITY_CON,
    MULTI_OP,
    MINUS_OP,
    UNARY_MINUS,
    INIT_EQ,
    INIT_AT,
    NOT_PRED_INIT,
    PRED_INST,
    PROBLEM_CONSTRAINT,
    PROBLEM_METRIC
}

/************* Start of grammar *******************/

pddlDoc : domain | problem;

/************* DOMAINS ****************************/

domain
    : '(' 'define' domainName
      requireDef ?
      typesDef ?
      constantsDef ?
      predicate_definition_block ?
      function_definition_block ?
      structureDef*
      ')'
    ;

domainName
    : '(' 'domain' NAME ')'
    ;

requireDef
	: '(' ':requirements' REQUIRE_KEY+ ')'
	;

typesDef
	: '(' ':types' typedNameList ')'
	;

numericBuiltinType
  : INT_T             # Integer
  | FLOAT_T           # Float
  | NUMBER_T          # Number
  ;

builtinType
  : numericBuiltinType  # NumericBuiltin
  | OBJECT_T            # ObjectBuiltin
  ;


// If have any typed names, they must come FIRST!
nameList : NAME*;

typedNameList
    : nameList                     # SimpleNameList
    | nameListWithType+ nameList   # ComplexNameList
    ;

nameListWithType
    : NAME nameList '-' theType=typename
	  ;

typename
	: '(' 'either' primitive_type+ ')'
	| primitive_type
	;

primitive_type : NAME | builtinType;

function_definition_block
	: '(' ':functions' single_function_definition* ')'
	;

single_function_definition
    : typed_function_definition
    | untyped_function_definition
    ;

typed_function_definition
    : '(' logical_symbol_name variableList ')' '-' primitive_type
    ;

untyped_function_definition
    : '(' logical_symbol_name variableList ')'
    ;

logical_symbol_name : NAME | EXTNAME;


constantsDef
	: '(' ':constants' typedNameList ')'
	;

predicate_definition_block
	: '(' ':predicates' single_predicate_definition* ')'
	;

single_predicate_definition
	: '(' predicate variableList ')'
	;

predicate : NAME;

// If have any typed variables, they must come FIRST!
variableList
    : VARIABLE*                               # UntypedVariableList
    | variableListWithType+ VARIABLE*         # TypedVariableList
    ;

variableListWithType
    : VARIABLE+ '-' primitive_type
    ;

structureDef
	: actionDef
    | eventDef
	| derivedDef
	| constraintDef
    | processDef
	;


/************* ACTIONS ****************************/

actionDef
	: '(' ':action' actionName
	      ':parameters'  '(' variableList ')'
           actionDefBody ')'
    ;

constraintDef
	: '(' ':constraint' constraintSymbol
	      ':parameters'  '(' variableList ')'
          ':condition' goalDesc ')'
    ;


eventDef
	: '(' ':event' eventSymbol
	      ':parameters'  '(' variableList ')'
           actionDefBody ')'
    ;

actionName : NAME | EXTNAME ;

constraintSymbol : NAME ;

eventSymbol : NAME | EXTNAME;

// Should allow preGD instead of goalDesc for preconditions -
// but I can't get the LL(*) parsing to work
// This means 'preference' preconditions cannot be used
actionDefBody
  : K_PRECONDITION precondition K_EFFECT effect
  ;

precondition
  : '(' ')'        # TrivialPrecondition
  | goalDesc       # RegularPrecondition
  ;

// A goalDesc is just a FOL formula
goalDesc
	:  atomicTermFormula                                     # TermGoalDesc
	| '(' 'and' goalDesc* ')'                                # AndGoalDesc
	| '(' 'or' goalDesc* ')'                                 # OrGoalDesc
	| '(' 'not' goalDesc ')'                                 # NotGoalDesc
	| '(' 'imply' goalDesc goalDesc ')'                      # ImplyGoalDesc
	| '(' 'exists' '(' variableList ')' goalDesc ')'         # ExistentialGoalDesc
	| '(' 'forall' '(' variableList ')' goalDesc ')'         # UniversalGoalDesc
    | fComp                                                  # ComparisonGoalDesc
	| equality                                               # EqualityGoalDesc
  ;

equality
	: '(' '=' term term ')'
	;
fComp
	: '(' binaryComp fExp fExp ')'
	;

atomicTermFormula
	: '(' predicate term* ')'
	;

term :
  NAME                #TermObject
  | NUMBER            #TermNumber
  | VARIABLE          #TermVariable
  | '#t'              #TermTimeStep
  | functionTerm      #TermFunction
  ;

functionTerm :
  '(' logical_symbol_name term* ')'        #GenericFunctionTerm
  | '(' binaryOp term term ')'        #BinaryArithmeticFunctionTerm
  | '(' unaryBuiltIn term ')'         #UnaryArithmeticFunctionTerm
  ;

/************* PROCESSES ****************************/

processDef
	: '(' ':process' actionName
	      ':parameters'  '(' variableList ')'
           processDefBody ')'
    ;

processDefBody
  : K_PRECONDITION precondition K_EFFECT processEffectList
  ;

processEffectList
	: '(' 'and' processEffect* ')'       #ProcessConjunctiveEffectFormula
	| processEffect                      #ProcessSingleEffect
	;

processEffect
	: '(' processEffectOp functionTerm processEffectExp ')' # ProcessAssignEffect
	;


/************* DERIVED DEFINITIONS ****************************/

derivedDef
	: '(' ':derived' variableList goalDesc ')'
	;

/************* EXPRESSIONS ****************************/

fExp
  : functionTerm  #FunctionExpr
  | NUMBER        #NumericConstantExpr
  | VARIABLE      #VariableExpr
  ;

processEffectExp
    : '(' '*' processFunctionEff ')' #FunctionalProcessEffectExpr
    | '(' '*' processConstEff ')'    #ConstProcessEffectExpr
    | '(' '*' processVarEff ')'      #VariableProcessEffectExpr
    ;

processFunctionEff
    : functionTerm '#t'
    | '#t' functionTerm
    ;

processConstEff
    : NUMBER '#t'
    | '#t' NUMBER
    ;

processVarEff
    : VARIABLE '#t'
    | '#t' VARIABLE
    ;


fHead
	: '(' logical_symbol_name term* ')'
	;

effect
	: '(' 'and' cEffect* ')'       # ConjunctiveEffectFormula
	| cEffect                      # SingleEffect
	;

cEffect
	: '(' 'forall' '(' variableList ')' effect ')'         # UniversallyQuantifiedEffect
	| '(' 'when' goalDesc atomic_effect ')'                # SingleConditionalEffect
	| '(' 'when' goalDesc '(' 'and' atomic_effect* ')' ')' # MultipleConditionalEffect
	| atomic_effect                                        # AtomicEffect
	;

atomic_effect
	: '(' assignOp functionTerm fExp ')'                 # AssignEffect  // TODO GFM THIS DOES NOT SEEM CORRECT - WILL PARSE E.G. (assign (+ 1 2) 5) ?? DO WE REALLY NEED TWO DIFFERENT ASSIGNMENT RULES?
	| '(' 'not' atomicTermFormula ')'                    # DeleteAtomEffect
	| atomicTermFormula                                  # AddAtomEffect
    | '(' 'assign' functionTerm term ')'                 # AssignConstant
	;


// TODO: should these be uppercase & lexer section?
binaryOp : '*' | '+' | '-' | '/' | '^' | 'max' | 'min' ;

unaryBuiltIn : '-' | 'sin' | 'cos' | 'sqrt' | 'tan' | 'acos' | 'asin' | 'atan' | 'exp' | 'abs';

binaryComp : '>' | '<' | '=' | '>=' | '<=' ;

assignOp : 'assign' | 'scale-up' | 'scale-down' | 'increase' | 'decrease' ;

processEffectOp : 'increase' | 'decrease';


/************* PROBLEMS ****************************/

problem
	: '(' 'define' problemDecl
	  problemDomain
      requireDef?
      object_declaration?
      init
      goal
      problemMeta*
      ')'
    ;

problemMeta
    : probConstraints
    | boundsDecl
    | metricSpec
    ;

problemDecl
    : '(' 'problem' NAME ')'
    ;

problemDomain
	: '(' ':domain' NAME ')'
	;

object_declaration
	: '(' ':objects' typedNameList ')'
	;


boundsDecl
  : '(' ':bounds' typeBoundsDefinition+ ')'
  ;

typeBoundsDefinition
  : '(' NAME '-' numericBuiltinType '[' NUMBER '..' NUMBER ']' ')'
  ;

init
	: '(' K_INIT initEl* ')'
	;


groundTerm :
  NAME                      #GroundTermObject
  | NUMBER                  #GroundTermNumber
  | groundFunctionTerm      #GroundTermFunction
  ;

groundFunctionTerm : '(' logical_symbol_name groundTerm* ')';

initEl
	: nameLiteral                             #InitLiteral
	| '(' '=' groundFunctionTerm NUMBER ')'   #InitAssignmentNumeric
    | '(' '=' groundFunctionTerm NAME ')'     #InitAssignmentObject
	;

nameLiteral
	: groundAtomicFormula                        #InitPositiveLiteral
	| '(' 'not' groundAtomicFormula ')'          #InitNegativeLiteral
	;

groundAtomicFormula
	: '(' predicate groundTerm* ')'
	;

// Should allow preGD instead of goalDesc -
// but I can't get the LL(*) parsing to work
// This means 'preference' preconditions cannot be used

goal : '(' ':goal' goalDesc ')'  ;

probConstraints
	: '(' ':constraints'  prefConGD ')'
	;

prefConGD
	: '(' 'and' prefConGD* ')'                                 # ConjunctionOfConstraints
	| '(' 'forall' '(' variableList ')' prefConGD ')'     # UniversallyQuantifiedConstraint
	| '(' 'preference' NAME? conGD ')'                         # PreferenceConstraint
	| conGD+                                                   # PlainConstraintList
	;

metricSpec
	: '(' ':metric' optimization metricFExp ')' # ProblemMetric
	;

optimization : 'minimize' | 'maximize' ;

metricFExp
	: functionTerm                                 #FunctionalExprMetric
    | terminalCost stageCost                       #CompositeMetric
    | stageCost terminalCost                       #CompositeMetric
    | '(total-time)'                               #TotalTimeMetric
	| '(' 'is-violated' NAME ')'                   #IsViolatedMetric
	;

terminalCost
    : '(' ':terminal' functionTerm ')'
    ;

stageCost
    : '(' ':stage' functionTerm ')'
    ;

/************* CONSTRAINTS ****************************/

conGD
	: '(' 'and' conGD+ ')'                                 # ConjunctiveConstraint
	| '(' 'forall' '(' variableList ')' conGD ')'          # ForallConstraint
	// The standard says "at end", but that conflicts with 50% of PDDL benchmarks which use "at" as an identifier:
	| '(' 'at-end' goalDesc ')'                            # AtEndConstraint
    | '(' 'always' goalDesc ')'                            # AlwaysConstraint
	| '(' 'sometime' goalDesc ')'                          # SometimeConstraint
 	| '(' 'within' NUMBER goalDesc ')'                     # WithinConstraint
	| '(' 'at-most-once' goalDesc ')'                      # AtMostOnceConstraint
	| '(' 'sometime-after' goalDesc goalDesc ')'           # SometimeAfterConstraint
	| '(' 'sometime-before' goalDesc goalDesc ')'          # SometimeBeforeConstraint
	| '(' 'always-within' NUMBER goalDesc goalDesc ')'     # AlwaysWithinConstraint
	| '(' 'hold-during' NUMBER NUMBER goalDesc ')'         # HoldDuringConstraint
	| '(' 'hold-after' NUMBER goalDesc ')'                 # HoldAfterConstraint
    | '(' EXTNAME groundFunctionTerm+ ')'                  # ExtensionalConstraintGD
    | goalDesc                                             # AlternativeAlwaysConstraint
	;



/************* LEXER ****************************/

REQUIRE_KEY
    : ':strips'
    | ':typing'
    | ':negative-preconditions'
    | ':disjunctive-preconditions'
    | ':equality'
    | ':existential-preconditions'
    | ':universal-preconditions'
    | ':quantified-preconditions'
    | ':conditional-effects'
    | ':object-fluents'
    | ':numeric-fluents'
    | ':fluents'
    | ':adl'
    | ':durative-actions'
    | ':derived-predicates'
    | ':timed-initial-literals'
    | ':preferences'
    | ':constraints'
    ;

NAME:    LETTER ANY_CHAR* ;

EXTNAME: '@' LETTER ANY_CHAR* ;


fragment DIGIT: '0'..'9';

fragment LETTER:	'a'..'z' | 'A'..'Z';

fragment ANY_CHAR_WO_HYPHEN: LETTER | DIGIT | '_';

fragment ANY_CHAR: ANY_CHAR_WO_HYPHEN | '-';


VARIABLE : '?' NAME ;

NUMBER : ('-')? DIGIT+ ('.' DIGIT+)? ;

LINE_COMMENT
    : (';' ~('\n'|'\r')* '\r'? '\n') -> channel(HIDDEN)
    ;

WHITESPACE
    :   (   ' '
        |   '\t'
        |   '\r'
        |   '\n'
        )+ -> channel(HIDDEN)
    ;


// Keywords
K_INIT: ':' I N I T;
K_PRECONDITION: ':' P R E C O N D I T I O N;
K_EFFECT : ':effect';
//K_EFFECT : ':' E F F E C T;

INT_T:    'int';
FLOAT_T:  'float';
OBJECT_T: 'object';
NUMBER_T: 'number';

// Case-insensitive lexing, see e.g. https://github.com/antlr/antlr4/blob/master/doc/case-insensitive-lexing.md
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];