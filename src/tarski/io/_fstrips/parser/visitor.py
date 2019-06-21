# Generated from /home/frances/projects/code/tarski/utils/parsers/grammars/fstrips.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .parser import fstripsParser
else:
    from parser import fstripsParser

# This class defines a complete generic visitor for a parse tree produced by fstripsParser.

class fstripsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fstripsParser#pddlDoc.
    def visitPddlDoc(self, ctx:fstripsParser.PddlDocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#domain.
    def visitDomain(self, ctx:fstripsParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#domainName.
    def visitDomainName(self, ctx:fstripsParser.DomainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#requireDef.
    def visitRequireDef(self, ctx:fstripsParser.RequireDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#declaration_of_types.
    def visitDeclaration_of_types(self, ctx:fstripsParser.Declaration_of_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#Integer.
    def visitInteger(self, ctx:fstripsParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#Float.
    def visitFloat(self, ctx:fstripsParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#Number.
    def visitNumber(self, ctx:fstripsParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#NumericBuiltin.
    def visitNumericBuiltin(self, ctx:fstripsParser.NumericBuiltinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ObjectBuiltin.
    def visitObjectBuiltin(self, ctx:fstripsParser.ObjectBuiltinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SimpleNameList.
    def visitSimpleNameList(self, ctx:fstripsParser.SimpleNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ComplexNameList.
    def visitComplexNameList(self, ctx:fstripsParser.ComplexNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#name_list_with_type.
    def visitName_list_with_type(self, ctx:fstripsParser.Name_list_with_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UntypedTypenameList.
    def visitUntypedTypenameList(self, ctx:fstripsParser.UntypedTypenameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TypedTypenameList.
    def visitTypedTypenameList(self, ctx:fstripsParser.TypedTypenameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UntypedVariableList.
    def visitUntypedVariableList(self, ctx:fstripsParser.UntypedVariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TypedVariableList.
    def visitTypedVariableList(self, ctx:fstripsParser.TypedVariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#variable_list_with_type.
    def visitVariable_list_with_type(self, ctx:fstripsParser.Variable_list_with_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#EitherTypename.
    def visitEitherTypename(self, ctx:fstripsParser.EitherTypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#PrimitiveTypename.
    def visitPrimitiveTypename(self, ctx:fstripsParser.PrimitiveTypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#primitive_type.
    def visitPrimitive_type(self, ctx:fstripsParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#function_definition_block.
    def visitFunction_definition_block(self, ctx:fstripsParser.Function_definition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#single_function_definition.
    def visitSingle_function_definition(self, ctx:fstripsParser.Single_function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#typed_function_definition.
    def visitTyped_function_definition(self, ctx:fstripsParser.Typed_function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#untyped_function_definition.
    def visitUntyped_function_definition(self, ctx:fstripsParser.Untyped_function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#logical_symbol_name.
    def visitLogical_symbol_name(self, ctx:fstripsParser.Logical_symbol_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#constant_declaration.
    def visitConstant_declaration(self, ctx:fstripsParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#predicate_definition_block.
    def visitPredicate_definition_block(self, ctx:fstripsParser.Predicate_definition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#single_predicate_definition.
    def visitSingle_predicate_definition(self, ctx:fstripsParser.Single_predicate_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#predicate.
    def visitPredicate(self, ctx:fstripsParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#function_name.
    def visitFunction_name(self, ctx:fstripsParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#structureDef.
    def visitStructureDef(self, ctx:fstripsParser.StructureDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#actionDef.
    def visitActionDef(self, ctx:fstripsParser.ActionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#constraintDef.
    def visitConstraintDef(self, ctx:fstripsParser.ConstraintDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#eventDef.
    def visitEventDef(self, ctx:fstripsParser.EventDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#actionName.
    def visitActionName(self, ctx:fstripsParser.ActionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#constraintSymbol.
    def visitConstraintSymbol(self, ctx:fstripsParser.ConstraintSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#eventSymbol.
    def visitEventSymbol(self, ctx:fstripsParser.EventSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#actionDefBody.
    def visitActionDefBody(self, ctx:fstripsParser.ActionDefBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TrivialPrecondition.
    def visitTrivialPrecondition(self, ctx:fstripsParser.TrivialPreconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#RegularPrecondition.
    def visitRegularPrecondition(self, ctx:fstripsParser.RegularPreconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermGoalDesc.
    def visitTermGoalDesc(self, ctx:fstripsParser.TermGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AndGoalDesc.
    def visitAndGoalDesc(self, ctx:fstripsParser.AndGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#OrGoalDesc.
    def visitOrGoalDesc(self, ctx:fstripsParser.OrGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#NotGoalDesc.
    def visitNotGoalDesc(self, ctx:fstripsParser.NotGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ImplyGoalDesc.
    def visitImplyGoalDesc(self, ctx:fstripsParser.ImplyGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ExistentialGoalDesc.
    def visitExistentialGoalDesc(self, ctx:fstripsParser.ExistentialGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UniversalGoalDesc.
    def visitUniversalGoalDesc(self, ctx:fstripsParser.UniversalGoalDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#BuiltinBinaryAtom.
    def visitBuiltinBinaryAtom(self, ctx:fstripsParser.BuiltinBinaryAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#atomicTermFormula.
    def visitAtomicTermFormula(self, ctx:fstripsParser.AtomicTermFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermObject.
    def visitTermObject(self, ctx:fstripsParser.TermObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermNumber.
    def visitTermNumber(self, ctx:fstripsParser.TermNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermVariable.
    def visitTermVariable(self, ctx:fstripsParser.TermVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermTimeStep.
    def visitTermTimeStep(self, ctx:fstripsParser.TermTimeStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TermFunction.
    def visitTermFunction(self, ctx:fstripsParser.TermFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#GenericFunctionTerm.
    def visitGenericFunctionTerm(self, ctx:fstripsParser.GenericFunctionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#BinaryArithmeticFunctionTerm.
    def visitBinaryArithmeticFunctionTerm(self, ctx:fstripsParser.BinaryArithmeticFunctionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UnaryArithmeticFunctionTerm.
    def visitUnaryArithmeticFunctionTerm(self, ctx:fstripsParser.UnaryArithmeticFunctionTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#derivedDef.
    def visitDerivedDef(self, ctx:fstripsParser.DerivedDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ConjunctiveEffectFormula.
    def visitConjunctiveEffectFormula(self, ctx:fstripsParser.ConjunctiveEffectFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SingleEffect.
    def visitSingleEffect(self, ctx:fstripsParser.SingleEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UniversallyQuantifiedEffect.
    def visitUniversallyQuantifiedEffect(self, ctx:fstripsParser.UniversallyQuantifiedEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SingleConditionalEffect.
    def visitSingleConditionalEffect(self, ctx:fstripsParser.SingleConditionalEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#MultipleConditionalEffect.
    def visitMultipleConditionalEffect(self, ctx:fstripsParser.MultipleConditionalEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AtomicEffect.
    def visitAtomicEffect(self, ctx:fstripsParser.AtomicEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AssignConstant.
    def visitAssignConstant(self, ctx:fstripsParser.AssignConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AssignEffect.
    def visitAssignEffect(self, ctx:fstripsParser.AssignEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#DeleteAtomEffect.
    def visitDeleteAtomEffect(self, ctx:fstripsParser.DeleteAtomEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AddAtomEffect.
    def visitAddAtomEffect(self, ctx:fstripsParser.AddAtomEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#builtin_binary_function.
    def visitBuiltin_binary_function(self, ctx:fstripsParser.Builtin_binary_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#builtin_unary_function.
    def visitBuiltin_unary_function(self, ctx:fstripsParser.Builtin_unary_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#builtin_binary_predicate.
    def visitBuiltin_binary_predicate(self, ctx:fstripsParser.Builtin_binary_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#assignOp.
    def visitAssignOp(self, ctx:fstripsParser.AssignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problem.
    def visitProblem(self, ctx:fstripsParser.ProblemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problemMeta.
    def visitProblemMeta(self, ctx:fstripsParser.ProblemMetaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problemDecl.
    def visitProblemDecl(self, ctx:fstripsParser.ProblemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#problemDomain.
    def visitProblemDomain(self, ctx:fstripsParser.ProblemDomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#object_declaration.
    def visitObject_declaration(self, ctx:fstripsParser.Object_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#boundsDecl.
    def visitBoundsDecl(self, ctx:fstripsParser.BoundsDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#typeBoundsDefinition.
    def visitTypeBoundsDefinition(self, ctx:fstripsParser.TypeBoundsDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#init.
    def visitInit(self, ctx:fstripsParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#InitPositiveLiteral.
    def visitInitPositiveLiteral(self, ctx:fstripsParser.InitPositiveLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#InitNegativeLiteral.
    def visitInitNegativeLiteral(self, ctx:fstripsParser.InitNegativeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#InitFunctionAssignment.
    def visitInitFunctionAssignment(self, ctx:fstripsParser.InitFunctionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#flat_term.
    def visitFlat_term(self, ctx:fstripsParser.Flat_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#flat_atom.
    def visitFlat_atom(self, ctx:fstripsParser.Flat_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#symbolic_constant.
    def visitSymbolic_constant(self, ctx:fstripsParser.Symbolic_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#numeric_constant.
    def visitNumeric_constant(self, ctx:fstripsParser.Numeric_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#goal.
    def visitGoal(self, ctx:fstripsParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#probConstraints.
    def visitProbConstraints(self, ctx:fstripsParser.ProbConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ConjunctionOfConstraints.
    def visitConjunctionOfConstraints(self, ctx:fstripsParser.ConjunctionOfConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#UniversallyQuantifiedConstraint.
    def visitUniversallyQuantifiedConstraint(self, ctx:fstripsParser.UniversallyQuantifiedConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#PreferenceConstraint.
    def visitPreferenceConstraint(self, ctx:fstripsParser.PreferenceConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#PlainConstraintList.
    def visitPlainConstraintList(self, ctx:fstripsParser.PlainConstraintListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ProblemMetric.
    def visitProblemMetric(self, ctx:fstripsParser.ProblemMetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#optimization.
    def visitOptimization(self, ctx:fstripsParser.OptimizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#FunctionalExprMetric.
    def visitFunctionalExprMetric(self, ctx:fstripsParser.FunctionalExprMetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#CompositeMetric.
    def visitCompositeMetric(self, ctx:fstripsParser.CompositeMetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#TotalTimeMetric.
    def visitTotalTimeMetric(self, ctx:fstripsParser.TotalTimeMetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#IsViolatedMetric.
    def visitIsViolatedMetric(self, ctx:fstripsParser.IsViolatedMetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#terminalCost.
    def visitTerminalCost(self, ctx:fstripsParser.TerminalCostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#stageCost.
    def visitStageCost(self, ctx:fstripsParser.StageCostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ConjunctiveConstraint.
    def visitConjunctiveConstraint(self, ctx:fstripsParser.ConjunctiveConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#ForallConstraint.
    def visitForallConstraint(self, ctx:fstripsParser.ForallConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AtEndConstraint.
    def visitAtEndConstraint(self, ctx:fstripsParser.AtEndConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AlwaysConstraint.
    def visitAlwaysConstraint(self, ctx:fstripsParser.AlwaysConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SometimeConstraint.
    def visitSometimeConstraint(self, ctx:fstripsParser.SometimeConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#WithinConstraint.
    def visitWithinConstraint(self, ctx:fstripsParser.WithinConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AtMostOnceConstraint.
    def visitAtMostOnceConstraint(self, ctx:fstripsParser.AtMostOnceConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SometimeAfterConstraint.
    def visitSometimeAfterConstraint(self, ctx:fstripsParser.SometimeAfterConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#SometimeBeforeConstraint.
    def visitSometimeBeforeConstraint(self, ctx:fstripsParser.SometimeBeforeConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AlwaysWithinConstraint.
    def visitAlwaysWithinConstraint(self, ctx:fstripsParser.AlwaysWithinConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#HoldDuringConstraint.
    def visitHoldDuringConstraint(self, ctx:fstripsParser.HoldDuringConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#HoldAfterConstraint.
    def visitHoldAfterConstraint(self, ctx:fstripsParser.HoldAfterConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fstripsParser#AlternativeAlwaysConstraint.
    def visitAlternativeAlwaysConstraint(self, ctx:fstripsParser.AlternativeAlwaysConstraintContext):
        return self.visitChildren(ctx)



del fstripsParser