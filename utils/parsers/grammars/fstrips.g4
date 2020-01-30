
/* Functional STRIPS grammar, adapted from PDDL 3.1

  See https://helios.hud.ac.uk/scommv/IPC-14/repository/kovacs-pddl-3.1-2011.pdf

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
    : '(' K_DEFINE domainName
      requireDef ?
      declaration_of_types ?
      constant_declaration ?
      predicate_definition_block ?
      function_definition_block ?
      structureDef*
      ')'
    ;

domainName
    : '(' 'domain' NAME ')'
    ;

requireDef
	: '(' ':requirements' REQUIRE_KEY* ')'
	;

declaration_of_types
	: '(' ':types' possibly_typed_type_list ')'
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


possibly_typed_name_list
    : NAME*                        # SimpleNameList
    // If there is a mixture of names with and without types,
    // those *with* types need to come first:
    | name_list_with_type+ NAME*   # ComplexNameList
    ;

name_list_with_type
    : NAME+ '-' typename
	;
	
// A possibly_typed_type_list is different from a possibly_typed_name_list in that it can include 'object'
// in the *untyped* part of the list (note that 'object' will get tokenized as an OBJECT_T even if it 
// is also a NAME simply because of the priority of OBJECT_T
possibly_typed_type_list
    : (NAME | OBJECT_T)*                       # UntypedTypenameList
    // If there is a mixture of names with and without types,
    // those *with* types need to come first:
    | name_list_with_type+ (NAME | OBJECT_T)*  # TypedTypenameList
    ;

// If have any typed variables, they must come FIRST!
possibly_typed_variable_list
    : VARIABLE*                               # UntypedVariableList
    // If there is a mixture of names with and without types,
    // those *with* types need to come first:
    | variable_list_with_type+ VARIABLE*      # TypedVariableList
    ;

variable_list_with_type
    : VARIABLE+ '-' typename
    ;


typename
	: '(' 'either' primitive_type+ ')'  # EitherTypename
	| primitive_type                    # PrimitiveTypename
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
    : '(' logical_symbol_name possibly_typed_variable_list ')' '-' primitive_type
    ;

untyped_function_definition
    : '(' logical_symbol_name possibly_typed_variable_list ')'
    ;

logical_symbol_name : NAME | EXTNAME;


constant_declaration
	: '(' ':constants' possibly_typed_name_list ')'
	;

predicate_definition_block
	: '(' ':predicates' single_predicate_definition* ')'
	;

single_predicate_definition
	: '(' predicate possibly_typed_variable_list ')'
	;

predicate : NAME;
function_name: NAME;

structureDef
	: actionDef
    | eventDef
	| derivedDef
	| constraintDef
//    | processDef
	;


/************* ACTIONS ****************************/

actionDef
	: '(' K_ACTION actionName
	      ':parameters'  '(' possibly_typed_variable_list ')'
           actionDefBody ')'
    ;

constraintDef
	: '(' ':constraint' constraintSymbol
	      ':parameters'  '(' possibly_typed_variable_list ')'
          ':condition' goalDesc ')'
    ;


eventDef
	: '(' ':event' eventSymbol
	      ':parameters'  '(' possibly_typed_variable_list ')'
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
	| '(' K_AND goalDesc* ')'                                # AndGoalDesc
	| '(' K_OR goalDesc* ')'                                 # OrGoalDesc
	| '(' K_NOT goalDesc ')'                                 # NotGoalDesc
	| '(' K_IMPLY goalDesc goalDesc ')'                      # ImplyGoalDesc
	| '(' K_EXISTS '(' possibly_typed_variable_list ')' goalDesc ')'         # ExistentialGoalDesc
	| '(' K_FORALL '(' possibly_typed_variable_list ')' goalDesc ')'         # UniversalGoalDesc
    | '(' builtin_binary_predicate term term ')'             # BuiltinBinaryAtom
  ;

atomicTermFormula
	: '(' predicate term* ')'
	;

term
  : NAME              #TermObject
  | NUMBER            #TermNumber
  | VARIABLE          #TermVariable
  | '#t'              #TermTimeStep
  | functionTerm      #TermFunction
  ;

functionTerm
  : '(' logical_symbol_name term* ')'           # GenericFunctionTerm
  | '(' builtin_binary_function term term ')'   # BinaryArithmeticFunctionTerm
  | '(' builtin_unary_function term ')'         # UnaryArithmeticFunctionTerm
  ;

/************* PROCESSES ****************************/

/*
processDef
	: '(' ':process' actionName
	      ':parameters'  '(' possibly_typed_variable_list ')'
           processDefBody ')'
    ;

processDefBody
  : K_PRECONDITION precondition K_EFFECT processEffectList
  ;

processEffectList
	: '(' K_AND processEffect* ')'       #ProcessConjunctiveEffectFormula
	| processEffect                      #ProcessSingleEffect
	;

processEffect
	: '(' processEffectOp functionTerm processEffectExp ')' # ProcessAssignEffect
	;
*/

/************* DERIVED DEFINITIONS ****************************/
// TODO Not fully implemented yet

derivedDef
	: '(' ':derived' '(' NAME possibly_typed_variable_list ')' goalDesc ')'
	;

/************* EXPRESSIONS ****************************/
/*
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
*/

effect
	: '(' K_AND single_effect* ')'       # ConjunctiveEffectFormula
	| single_effect                      # SingleEffect
	;

single_effect
	: '(' K_FORALL '(' possibly_typed_variable_list ')' effect ')'         # UniversallyQuantifiedEffect
	| '(' K_WHEN goalDesc atomic_effect ')'                # SingleConditionalEffect
	| '(' K_WHEN goalDesc '(' K_AND atomic_effect* ')' ')' # MultipleConditionalEffect
	| atomic_effect                                        # AtomicEffect
	;

atomic_effect
    : '(' 'assign' functionTerm term ')'                 # AssignConstant // TODO GFM THIS DOES NOT SEEM CORRECT - WILL PARSE E.G. (assign (+ 1 2) 5)
    // TODO: Reactivate this... when clarified
	| '(' assignOp functionTerm term ')'                 # AssignEffect  // TODO GFM THIS DOES NOT SEEM CORRECT - WILL PARSE E.G. (assign (+ 1 2) 5) ?? DO WE REALLY NEED TWO DIFFERENT ASSIGNMENT RULES?
	| '(' K_NOT atomicTermFormula ')'                    # DeleteAtomEffect
	| atomicTermFormula                                  # AddAtomEffect
	;


// TODO: should these be uppercase & lexer section?
builtin_binary_function : '*' | '+' | '-' | '/' | '^' | 'max' | 'min' ;

builtin_unary_function : '-' | 'sin' | 'cos' | 'sqrt' | 'tan' | 'acos' | 'asin' | 'atan' | 'exp' | 'abs';

builtin_binary_predicate : '>' | '<' | '=' | '>=' | '<=' ;

assignOp : K_SCALEUP | K_SCALEDOWN | K_INCREASE | K_DECREASE ;

//processEffectOp : K_INCREASE | K_DECREASE;


/************* PROBLEMS ****************************/

problem
	: '(' K_DEFINE problemDecl
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
	: '(' ':objects' possibly_typed_name_list ')'
	;


boundsDecl
  : '(' ':bounds' typeBoundsDefinition+ ')'
  ;

typeBoundsDefinition
  : '(' NAME '-' numericBuiltinType '[' NUMBER '..' NUMBER ']' ')'
  ;

init
	: '(' K_INIT init_element* ')'
	;

init_element
	: flat_atom                            # InitPositiveLiteral
	| '(' K_NOT flat_atom ')'              # InitNegativeLiteral
	| '(' '=' flat_term constant_name ')'  # InitFunctionAssignment
	;

flat_term : '(' function_name constant_name* ')';

flat_atom
	: '(' predicate constant_name* ')'
	;

constant_name
  : NAME           # symbolic_constant
  | NUMBER         # numeric_constant
  ;


// Should allow preGD instead of goalDesc -
// but I can't get the LL(*) parsing to work
// This means 'preference' preconditions cannot be used
goal : '(' ':goal' goalDesc ')'  ;

probConstraints
	: '(' ':constraints'  prefConGD ')'
	;

prefConGD
	: '(' K_AND prefConGD* ')'                                 # ConjunctionOfConstraints
	| '(' K_FORALL '(' possibly_typed_variable_list ')' prefConGD ')'     # UniversallyQuantifiedConstraint
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
	: '(' K_AND conGD+ ')'                                 # ConjunctiveConstraint
	| '(' K_FORALL '(' possibly_typed_variable_list ')' conGD ')'          # ForallConstraint
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
//    | '(' EXTNAME flat_term+ ')'                  # ExtensionalConstraintGD
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
    | ':action-costs'
    ;

// NOTE that the order of the lexer rules matters, esp. when there might be overlapping
// See e.g. https://stackoverflow.com/q/29777778
// This means that any token that goes below the `NAME` token will likely be ignored, as `NAME` will capture
// most character sequences.
K_AND: A N D;
K_NOT: N O T;
K_OR:  O R;
K_IMPLY: I M P L Y;
K_EXISTS: E X I S T S;
K_FORALL: F O R A L L;
K_WHEN: W H E N;

K_INIT: ':' I N I T;
K_PRECONDITION: ':' P R E C O N D I T I O N;
K_EFFECT : ':' E F F E C T;
K_DEFINE : D E F I N E;
K_ACTION: ':' A C T I O N;

K_INCREASE: I N C R E A S E;
K_DECREASE: D E C R E A S E;
K_SCALEUP: 'scale-up';
K_SCALEDOWN: 'scale-down';

INT_T:    'int';
FLOAT_T:  'float';
OBJECT_T: 'object';
NUMBER_T: 'number';

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