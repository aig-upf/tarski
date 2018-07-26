# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by fstripsParser.

class fstripsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fstripsParser#pddlDoc.
    def visitPddlDoc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#domain.
    def visitDomain(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#domainName.
    def visitDomainName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#requireDef.
    def visitRequireDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#declaration_of_types.
    def visitDeclaration_of_types(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#Integer.
    def visitInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#Float.
    def visitFloat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#Number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#NumericBuiltin.
    def visitNumericBuiltin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ObjectBuiltin.
    def visitObjectBuiltin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SimpleNameList.
    def visitSimpleNameList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ComplexNameList.
    def visitComplexNameList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#name_list_with_type.
    def visitName_list_with_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UntypedVariableList.
    def visitUntypedVariableList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TypedVariableList.
    def visitTypedVariableList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#variable_list_with_type.
    def visitVariable_list_with_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#typename.
    def visitTypename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#primitive_type.
    def visitPrimitive_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#function_definition_block.
    def visitFunction_definition_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#single_function_definition.
    def visitSingle_function_definition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#typed_function_definition.
    def visitTyped_function_definition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#untyped_function_definition.
    def visitUntyped_function_definition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#logical_symbol_name.
    def visitLogical_symbol_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#constant_declaration.
    def visitConstant_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#predicate_definition_block.
    def visitPredicate_definition_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#single_predicate_definition.
    def visitSingle_predicate_definition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#predicate.
    def visitPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#function_name.
    def visitFunction_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#structureDef.
    def visitStructureDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#actionDef.
    def visitActionDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#constraintDef.
    def visitConstraintDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#eventDef.
    def visitEventDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#actionName.
    def visitActionName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#constraintSymbol.
    def visitConstraintSymbol(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#eventSymbol.
    def visitEventSymbol(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#actionDefBody.
    def visitActionDefBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TrivialPrecondition.
    def visitTrivialPrecondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#RegularPrecondition.
    def visitRegularPrecondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermGoalDesc.
    def visitTermGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AndGoalDesc.
    def visitAndGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#OrGoalDesc.
    def visitOrGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#NotGoalDesc.
    def visitNotGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ImplyGoalDesc.
    def visitImplyGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ExistentialGoalDesc.
    def visitExistentialGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UniversalGoalDesc.
    def visitUniversalGoalDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#BuiltinBinaryAtom.
    def visitBuiltinBinaryAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#atomicTermFormula.
    def visitAtomicTermFormula(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermObject.
    def visitTermObject(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermNumber.
    def visitTermNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermVariable.
    def visitTermVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermTimeStep.
    def visitTermTimeStep(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermFunction.
    def visitTermFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#GenericFunctionTerm.
    def visitGenericFunctionTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#BinaryArithmeticFunctionTerm.
    def visitBinaryArithmeticFunctionTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UnaryArithmeticFunctionTerm.
    def visitUnaryArithmeticFunctionTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#derivedDef.
    def visitDerivedDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ConjunctiveEffectFormula.
    def visitConjunctiveEffectFormula(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SingleEffect.
    def visitSingleEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UniversallyQuantifiedEffect.
    def visitUniversallyQuantifiedEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SingleConditionalEffect.
    def visitSingleConditionalEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#MultipleConditionalEffect.
    def visitMultipleConditionalEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AtomicEffect.
    def visitAtomicEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AssignConstant.
    def visitAssignConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AssignEffect.
    def visitAssignEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#DeleteAtomEffect.
    def visitDeleteAtomEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AddAtomEffect.
    def visitAddAtomEffect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#builtin_binary_function.
    def visitBuiltin_binary_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#builtin_unary_function.
    def visitBuiltin_unary_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#builtin_binary_predicate.
    def visitBuiltin_binary_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#assignOp.
    def visitAssignOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problem.
    def visitProblem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problemMeta.
    def visitProblemMeta(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problemDecl.
    def visitProblemDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problemDomain.
    def visitProblemDomain(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#object_declaration.
    def visitObject_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#boundsDecl.
    def visitBoundsDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#typeBoundsDefinition.
    def visitTypeBoundsDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#init.
    def visitInit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#InitPositiveLiteral.
    def visitInitPositiveLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#InitNegativeLiteral.
    def visitInitNegativeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#InitFunctionAssignment.
    def visitInitFunctionAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#flat_term.
    def visitFlat_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#flat_atom.
    def visitFlat_atom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#symbolic_constant.
    def visitSymbolic_constant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#numeric_constant.
    def visitNumeric_constant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#goal.
    def visitGoal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#probConstraints.
    def visitProbConstraints(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ConjunctionOfConstraints.
    def visitConjunctionOfConstraints(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UniversallyQuantifiedConstraint.
    def visitUniversallyQuantifiedConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#PreferenceConstraint.
    def visitPreferenceConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#PlainConstraintList.
    def visitPlainConstraintList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ProblemMetric.
    def visitProblemMetric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#optimization.
    def visitOptimization(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#FunctionalExprMetric.
    def visitFunctionalExprMetric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#CompositeMetric.
    def visitCompositeMetric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TotalTimeMetric.
    def visitTotalTimeMetric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#IsViolatedMetric.
    def visitIsViolatedMetric(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#terminalCost.
    def visitTerminalCost(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#stageCost.
    def visitStageCost(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ConjunctiveConstraint.
    def visitConjunctiveConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ForallConstraint.
    def visitForallConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AtEndConstraint.
    def visitAtEndConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AlwaysConstraint.
    def visitAlwaysConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SometimeConstraint.
    def visitSometimeConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#WithinConstraint.
    def visitWithinConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AtMostOnceConstraint.
    def visitAtMostOnceConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SometimeAfterConstraint.
    def visitSometimeAfterConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SometimeBeforeConstraint.
    def visitSometimeBeforeConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AlwaysWithinConstraint.
    def visitAlwaysWithinConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#HoldDuringConstraint.
    def visitHoldDuringConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#HoldAfterConstraint.
    def visitHoldAfterConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AlternativeAlwaysConstraint.
    def visitAlternativeAlwaysConstraint(self, ctx):
        return self.visitChildren(ctx)


