
/* Grammar pddl 3.0. Starting to update towards pddl 3.1 */

grammar pddl3;

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
      requireDef?
      typesDef?
      constantsDef?
      predicatesDef?
      functionsDef?
      free_functionsDef?
      constraints?
      structureDef*
      ')'
    ;

free_functionsDef
	: '(' ':free_functions' functionList ')'
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

// If have any typed names, they must come FIRST!
typedNameList
    : (NAME* | singleTypeNameList+ NAME*)
    ;

singleTypeNameList
    : NAME+ '-' t=typename
	;

typename
	: '(' 'either' primType+ ')'
	| primType
	;

primType : NAME ;

functionsDef
	: '(' ':functions' functionList ')'
	;

functionList
	: (atomicFunctionSkeleton+ ('-' functionType)? )*
	;

atomicFunctionSkeleton
	: '(' functionSymbol typedVariableList ')'
	;

functionSymbol : NAME ;

functionType : 'number' ; // Currently in PDDL only numeric functions are allowed

constantsDef
	: '(' ':constants' typedNameList ')'
	;

predicatesDef
	: '(' ':predicates' atomicFormulaSkeleton+ ')'
	;

atomicFormulaSkeleton
	: '(' predicate typedVariableList ')'
	;

predicate : NAME ;

// If have any typed variables, they must come FIRST!
typedVariableList
    : (VARIABLE* | singleTypeVarList+ VARIABLE*)
    ;

singleTypeVarList
    : (VARIABLE+ '-' t=typename)
    ;

constraints
	: '(' ':constraints' conGD ')'
	;

structureDef
	: actionDef
	| durativeActionDef
	| derivedDef
	| constraintDef
	;


/************* ACTIONS ****************************/

actionDef
	: '(' ':action' actionSymbol
	      ':parameters'  '(' typedVariableList ')'
           actionDefBody ')'
    ;

constraintDef
	: '(' ':constraint' constraintSymbol
	      ':parameters'  '(' typedVariableList ')'
           constraintDefBody ')'
    ;


actionSymbol : NAME ;

constraintSymbol : NAME ;

// Should allow preGD instead of goalDesc for preconditions -
// but I can't get the LL(*) parsing to work
// This means 'preference' preconditions cannot be used
actionDefBody
	: ( ':precondition' (('(' ')') | goalDesc))?
	  ( ':effect' (('(' ')') | effect))?
	;

constraintDefBody
	: ( ':condition' (('(' ')') | goalDesc))?
	;


//preGD
//	: prefGD
//	| '(' 'and' preGD* ')'
//	| '(' 'forall' '(' typedVariableList ')' preGD ')'
//	;
//
//prefGD
//	: '(' 'preference' NAME? goalDesc ')'
//	| goalDesc
//	;

goalDesc
	: atomicTermFormula
	| '(' 'and' goalDesc* ')'
	| '(' 'or' goalDesc* ')'
	| '(' 'not' goalDesc ')'
	| '(' 'imply' goalDesc goalDesc ')'
	| '(' 'exists' '(' typedVariableList ')' goalDesc ')'
	| '(' 'forall' '(' typedVariableList ')' goalDesc ')'
  | fComp
	| equality
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

term : NAME | VARIABLE ;

/************* DURATIVE ACTIONS ****************************/

durativeActionDef
	: '(' ':durative-action' actionSymbol
	      ':parameters'  '(' typedVariableList ')'
           daDefBody ')'
    | '(' ':durative-action' actionSymbol
  	      ':parameters'  '(' ')'
             daDefBody ')'
    ;

daDefBody
	: ':duration' durationConstraint
	| ':condition' (('(' ')') | daGD)
  | ':effect' (('(' ')') | daEffect)
  ;

daGD
	: prefTimedGD
	| '(' 'and' daGD* ')'
	| '(' 'forall' '(' typedVariableList ')' daGD ')'
	;

prefTimedGD
	: timedGD
	| '(' 'preference' NAME? timedGD ')'
	;

timedGD
	: '(' 'at' timeSpecifier goalDesc ')'
	| '(' 'over' interval goalDesc ')'
	;

timeSpecifier : 'start' | 'end' ;
interval : 'all' ;

/************* DERIVED DEFINITIONS ****************************/

derivedDef
	: '(' ':derived' typedVariableList goalDesc ')'
	;

/************* EXPRESSIONS ****************************/

fExp
	: NUMBER
	| '(' binaryOp fExp fExp ')'
	| '(' '-' fExp ')'
	| fHead
	;

fHead
	: '(' functionSymbol term* ')'
	| functionSymbol
	;

effect
	: '(' 'and' cEffect* ')'
	| cEffect
	;

cEffect
	: '(' 'forall' '(' typedVariableList ')' effect ')'
	| '(' 'when' goalDesc condEffect ')'
	| pEffect
	;

pEffect
	: '(' assignOp fHead fExp ')'
	| '(' 'not' atomicTermFormula ')'
	| atomicTermFormula
	;


// TODO: why is this different from the "and cEffect" above? Does it matter?
condEffect
	: '(' 'and' pEffect* ')'
	| pEffect
	;

// TODO: should these be uppercase & lexer section?
binaryOp : '*' | '+' | '-' | '/' ;

multiOp	: '*' | '+' ;

binaryComp : '>' | '<' | '=' | '>=' | '<=' ;

assignOp : 'assign' | 'scale-up' | 'scale-down' | 'increase' | 'decrease' ;


/************* DURATIONS  ****************************/

durationConstraint
	: '(' 'and' simpleDurationConstraint+ ')'
	| '(' ')'
	| simpleDurationConstraint
	;

simpleDurationConstraint
	: '(' durOp '?duration' durValue ')'
	| '(' 'at' timeSpecifier simpleDurationConstraint ')'
	;

durOp : '<=' | '>=' | '=' ;

durValue : NUMBER | fExp ;

daEffect
	: '(' 'and' daEffect* ')'
	| timedEffect
	| '(' 'forall' '(' typedVariableList ')' daEffect ')'
	| '(' 'when' daGD timedEffect ')'
	| '(' assignOp fHead fExpDA ')'
	;

timedEffect
	: '(' 'at' timeSpecifier daEffect ')'     // BNF has a-effect here, but not defined anywhere
	| '(' 'at' timeSpecifier fAssignDA ')'
	| '(' assignOp fHead fExp ')'         // BNF has assign-op-t and f-exp-t here, but not defined anywhere
	;

fAssignDA
	: '(' assignOp fHead fExpDA ')'
	;

fExpDA
	: '(' ((binaryOp fExpDA fExpDA) | ('-' fExpDA)) ')'
	| '?duration'
	| fExp
	;

/************* PROBLEMS ****************************/

problem
	: '(' 'define' problemDecl
	  problemDomain
      requireDef?
      objectDecl?
      init
      goal
      probConstraints?
      metricSpec?
      // lengthSpec? This is not defined anywhere in the BNF spec
      ')'
    ;

problemDecl
    : '(' 'problem' NAME ')'
    ;

problemDomain
	: '(' ':domain' NAME ')'
	;

objectDecl
	: '(' ':objects' typedNameList ')'
	;

init
	: '(' ':init' initEl* ')'
	;

initEl
	: nameLiteral
	| '(' '=' fHead NUMBER ')'
	| '(' 'at' NUMBER nameLiteral ')'
	;

nameLiteral
	: atomicNameFormula
	| '(' 'not' atomicNameFormula ')'
	;

atomicNameFormula
	: '(' predicate NAME* ')'
	;

// Should allow preGD instead of goalDesc -
// but I can't get the LL(*) parsing to work
// This means 'preference' preconditions cannot be used
//goal : '(' ':goal' preGD ')'  -> ^(GOAL preGD);
goal : '(' ':goal' goalDesc ')'  ;

probConstraints
	: '(' ':constraints'  prefConGD ')'
	;

prefConGD
	: '(' 'and' prefConGD* ')'
	| '(' 'forall' '(' typedVariableList ')' prefConGD ')'
	| '(' 'preference' NAME? conGD ')'
	| conGD
	;

metricSpec
	: '(' ':metric' optimization metricFExp ')'
	;

optimization : 'minimize' | 'maximize' ;

metricFExp
	: '(' binaryOp metricFExp metricFExp ')'
	| '(' multiOp metricFExp metricFExp+ ')'
	| '(' '-' metricFExp ')'
	| NUMBER
	| fHead
        /*| 'total-time'*/
	| '(' 'is-violated' NAME ')'
	;

/************* CONSTRAINTS ****************************/

conGD
	: '(' 'and' conGD* ')'
	| '(' 'forall' '(' typedVariableList ')' conGD ')'
	| '(' 'at' 'end' goalDesc ')'
  | '(' 'always' goalDesc ')'
	| '(' 'sometime' goalDesc ')'
 	| '(' 'within' NUMBER goalDesc ')'
	| '(' 'at-most-once' goalDesc ')'
	| '(' 'sometime-after' goalDesc goalDesc ')'
	| '(' 'sometime-before' goalDesc goalDesc ')'
	| '(' 'always-within' NUMBER goalDesc goalDesc ')'
	| '(' 'hold-during' NUMBER NUMBER goalDesc ')'
	| '(' 'hold-after' NUMBER goalDesc ')'
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
    | ':fluents'
    | ':adl'
    | ':durative-actions'
    | ':derived-predicates'
    | ':timed-initial-literals'
    | ':preferences'
    | ':constraints'
    ;


NAME:    LETTER ANY_CHAR* ;

fragment LETTER:	'a'..'z' | 'A'..'Z';

fragment ANY_CHAR: LETTER | '0'..'9' | '-' | '_';

VARIABLE : '?' LETTER ANY_CHAR*  ;

NUMBER : ('-')? DIGIT+ ('.' DIGIT+)? ;

fragment DIGIT: '0'..'9';

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
