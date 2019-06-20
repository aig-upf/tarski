# Generated from /home/frances/projects/code/tarski/utils/parsers/grammars/fstrips.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .parser import fstripsParser
else:
    from parser import fstripsParser

# This class defines a complete listener for a parse tree produced by fstripsParser.
class fstripsListener(ParseTreeListener):

    # Enter a parse tree produced by fstripsParser#pddlDoc.
    def enterPddlDoc(self, ctx:fstripsParser.PddlDocContext):
        pass

    # Exit a parse tree produced by fstripsParser#pddlDoc.
    def exitPddlDoc(self, ctx:fstripsParser.PddlDocContext):
        pass


    # Enter a parse tree produced by fstripsParser#domain.
    def enterDomain(self, ctx:fstripsParser.DomainContext):
        pass

    # Exit a parse tree produced by fstripsParser#domain.
    def exitDomain(self, ctx:fstripsParser.DomainContext):
        pass


    # Enter a parse tree produced by fstripsParser#domainName.
    def enterDomainName(self, ctx:fstripsParser.DomainNameContext):
        pass

    # Exit a parse tree produced by fstripsParser#domainName.
    def exitDomainName(self, ctx:fstripsParser.DomainNameContext):
        pass


    # Enter a parse tree produced by fstripsParser#requireDef.
    def enterRequireDef(self, ctx:fstripsParser.RequireDefContext):
        pass

    # Exit a parse tree produced by fstripsParser#requireDef.
    def exitRequireDef(self, ctx:fstripsParser.RequireDefContext):
        pass


    # Enter a parse tree produced by fstripsParser#declaration_of_types.
    def enterDeclaration_of_types(self, ctx:fstripsParser.Declaration_of_typesContext):
        pass

    # Exit a parse tree produced by fstripsParser#declaration_of_types.
    def exitDeclaration_of_types(self, ctx:fstripsParser.Declaration_of_typesContext):
        pass


    # Enter a parse tree produced by fstripsParser#Integer.
    def enterInteger(self, ctx:fstripsParser.IntegerContext):
        pass

    # Exit a parse tree produced by fstripsParser#Integer.
    def exitInteger(self, ctx:fstripsParser.IntegerContext):
        pass


    # Enter a parse tree produced by fstripsParser#Float.
    def enterFloat(self, ctx:fstripsParser.FloatContext):
        pass

    # Exit a parse tree produced by fstripsParser#Float.
    def exitFloat(self, ctx:fstripsParser.FloatContext):
        pass


    # Enter a parse tree produced by fstripsParser#Number.
    def enterNumber(self, ctx:fstripsParser.NumberContext):
        pass

    # Exit a parse tree produced by fstripsParser#Number.
    def exitNumber(self, ctx:fstripsParser.NumberContext):
        pass


    # Enter a parse tree produced by fstripsParser#NumericBuiltin.
    def enterNumericBuiltin(self, ctx:fstripsParser.NumericBuiltinContext):
        pass

    # Exit a parse tree produced by fstripsParser#NumericBuiltin.
    def exitNumericBuiltin(self, ctx:fstripsParser.NumericBuiltinContext):
        pass


    # Enter a parse tree produced by fstripsParser#ObjectBuiltin.
    def enterObjectBuiltin(self, ctx:fstripsParser.ObjectBuiltinContext):
        pass

    # Exit a parse tree produced by fstripsParser#ObjectBuiltin.
    def exitObjectBuiltin(self, ctx:fstripsParser.ObjectBuiltinContext):
        pass


    # Enter a parse tree produced by fstripsParser#SimpleNameList.
    def enterSimpleNameList(self, ctx:fstripsParser.SimpleNameListContext):
        pass

    # Exit a parse tree produced by fstripsParser#SimpleNameList.
    def exitSimpleNameList(self, ctx:fstripsParser.SimpleNameListContext):
        pass


    # Enter a parse tree produced by fstripsParser#ComplexNameList.
    def enterComplexNameList(self, ctx:fstripsParser.ComplexNameListContext):
        pass

    # Exit a parse tree produced by fstripsParser#ComplexNameList.
    def exitComplexNameList(self, ctx:fstripsParser.ComplexNameListContext):
        pass


    # Enter a parse tree produced by fstripsParser#name_list_with_type.
    def enterName_list_with_type(self, ctx:fstripsParser.Name_list_with_typeContext):
        pass

    # Exit a parse tree produced by fstripsParser#name_list_with_type.
    def exitName_list_with_type(self, ctx:fstripsParser.Name_list_with_typeContext):
        pass


    # Enter a parse tree produced by fstripsParser#UntypedTypenameList.
    def enterUntypedTypenameList(self, ctx:fstripsParser.UntypedTypenameListContext):
        pass

    # Exit a parse tree produced by fstripsParser#UntypedTypenameList.
    def exitUntypedTypenameList(self, ctx:fstripsParser.UntypedTypenameListContext):
        pass


    # Enter a parse tree produced by fstripsParser#TypedTypenameList.
    def enterTypedTypenameList(self, ctx:fstripsParser.TypedTypenameListContext):
        pass

    # Exit a parse tree produced by fstripsParser#TypedTypenameList.
    def exitTypedTypenameList(self, ctx:fstripsParser.TypedTypenameListContext):
        pass


    # Enter a parse tree produced by fstripsParser#UntypedVariableList.
    def enterUntypedVariableList(self, ctx:fstripsParser.UntypedVariableListContext):
        pass

    # Exit a parse tree produced by fstripsParser#UntypedVariableList.
    def exitUntypedVariableList(self, ctx:fstripsParser.UntypedVariableListContext):
        pass


    # Enter a parse tree produced by fstripsParser#TypedVariableList.
    def enterTypedVariableList(self, ctx:fstripsParser.TypedVariableListContext):
        pass

    # Exit a parse tree produced by fstripsParser#TypedVariableList.
    def exitTypedVariableList(self, ctx:fstripsParser.TypedVariableListContext):
        pass


    # Enter a parse tree produced by fstripsParser#variable_list_with_type.
    def enterVariable_list_with_type(self, ctx:fstripsParser.Variable_list_with_typeContext):
        pass

    # Exit a parse tree produced by fstripsParser#variable_list_with_type.
    def exitVariable_list_with_type(self, ctx:fstripsParser.Variable_list_with_typeContext):
        pass


    # Enter a parse tree produced by fstripsParser#EitherTypename.
    def enterEitherTypename(self, ctx:fstripsParser.EitherTypenameContext):
        pass

    # Exit a parse tree produced by fstripsParser#EitherTypename.
    def exitEitherTypename(self, ctx:fstripsParser.EitherTypenameContext):
        pass


    # Enter a parse tree produced by fstripsParser#PrimitiveTypename.
    def enterPrimitiveTypename(self, ctx:fstripsParser.PrimitiveTypenameContext):
        pass

    # Exit a parse tree produced by fstripsParser#PrimitiveTypename.
    def exitPrimitiveTypename(self, ctx:fstripsParser.PrimitiveTypenameContext):
        pass


    # Enter a parse tree produced by fstripsParser#primitive_type.
    def enterPrimitive_type(self, ctx:fstripsParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by fstripsParser#primitive_type.
    def exitPrimitive_type(self, ctx:fstripsParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by fstripsParser#function_definition_block.
    def enterFunction_definition_block(self, ctx:fstripsParser.Function_definition_blockContext):
        pass

    # Exit a parse tree produced by fstripsParser#function_definition_block.
    def exitFunction_definition_block(self, ctx:fstripsParser.Function_definition_blockContext):
        pass


    # Enter a parse tree produced by fstripsParser#single_function_definition.
    def enterSingle_function_definition(self, ctx:fstripsParser.Single_function_definitionContext):
        pass

    # Exit a parse tree produced by fstripsParser#single_function_definition.
    def exitSingle_function_definition(self, ctx:fstripsParser.Single_function_definitionContext):
        pass


    # Enter a parse tree produced by fstripsParser#typed_function_definition.
    def enterTyped_function_definition(self, ctx:fstripsParser.Typed_function_definitionContext):
        pass

    # Exit a parse tree produced by fstripsParser#typed_function_definition.
    def exitTyped_function_definition(self, ctx:fstripsParser.Typed_function_definitionContext):
        pass


    # Enter a parse tree produced by fstripsParser#untyped_function_definition.
    def enterUntyped_function_definition(self, ctx:fstripsParser.Untyped_function_definitionContext):
        pass

    # Exit a parse tree produced by fstripsParser#untyped_function_definition.
    def exitUntyped_function_definition(self, ctx:fstripsParser.Untyped_function_definitionContext):
        pass


    # Enter a parse tree produced by fstripsParser#logical_symbol_name.
    def enterLogical_symbol_name(self, ctx:fstripsParser.Logical_symbol_nameContext):
        pass

    # Exit a parse tree produced by fstripsParser#logical_symbol_name.
    def exitLogical_symbol_name(self, ctx:fstripsParser.Logical_symbol_nameContext):
        pass


    # Enter a parse tree produced by fstripsParser#constant_declaration.
    def enterConstant_declaration(self, ctx:fstripsParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by fstripsParser#constant_declaration.
    def exitConstant_declaration(self, ctx:fstripsParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by fstripsParser#predicate_definition_block.
    def enterPredicate_definition_block(self, ctx:fstripsParser.Predicate_definition_blockContext):
        pass

    # Exit a parse tree produced by fstripsParser#predicate_definition_block.
    def exitPredicate_definition_block(self, ctx:fstripsParser.Predicate_definition_blockContext):
        pass


    # Enter a parse tree produced by fstripsParser#single_predicate_definition.
    def enterSingle_predicate_definition(self, ctx:fstripsParser.Single_predicate_definitionContext):
        pass

    # Exit a parse tree produced by fstripsParser#single_predicate_definition.
    def exitSingle_predicate_definition(self, ctx:fstripsParser.Single_predicate_definitionContext):
        pass


    # Enter a parse tree produced by fstripsParser#predicate.
    def enterPredicate(self, ctx:fstripsParser.PredicateContext):
        pass

    # Exit a parse tree produced by fstripsParser#predicate.
    def exitPredicate(self, ctx:fstripsParser.PredicateContext):
        pass


    # Enter a parse tree produced by fstripsParser#function_name.
    def enterFunction_name(self, ctx:fstripsParser.Function_nameContext):
        pass

    # Exit a parse tree produced by fstripsParser#function_name.
    def exitFunction_name(self, ctx:fstripsParser.Function_nameContext):
        pass


    # Enter a parse tree produced by fstripsParser#structureDef.
    def enterStructureDef(self, ctx:fstripsParser.StructureDefContext):
        pass

    # Exit a parse tree produced by fstripsParser#structureDef.
    def exitStructureDef(self, ctx:fstripsParser.StructureDefContext):
        pass


    # Enter a parse tree produced by fstripsParser#actionDef.
    def enterActionDef(self, ctx:fstripsParser.ActionDefContext):
        pass

    # Exit a parse tree produced by fstripsParser#actionDef.
    def exitActionDef(self, ctx:fstripsParser.ActionDefContext):
        pass


    # Enter a parse tree produced by fstripsParser#constraintDef.
    def enterConstraintDef(self, ctx:fstripsParser.ConstraintDefContext):
        pass

    # Exit a parse tree produced by fstripsParser#constraintDef.
    def exitConstraintDef(self, ctx:fstripsParser.ConstraintDefContext):
        pass


    # Enter a parse tree produced by fstripsParser#eventDef.
    def enterEventDef(self, ctx:fstripsParser.EventDefContext):
        pass

    # Exit a parse tree produced by fstripsParser#eventDef.
    def exitEventDef(self, ctx:fstripsParser.EventDefContext):
        pass


    # Enter a parse tree produced by fstripsParser#actionName.
    def enterActionName(self, ctx:fstripsParser.ActionNameContext):
        pass

    # Exit a parse tree produced by fstripsParser#actionName.
    def exitActionName(self, ctx:fstripsParser.ActionNameContext):
        pass


    # Enter a parse tree produced by fstripsParser#constraintSymbol.
    def enterConstraintSymbol(self, ctx:fstripsParser.ConstraintSymbolContext):
        pass

    # Exit a parse tree produced by fstripsParser#constraintSymbol.
    def exitConstraintSymbol(self, ctx:fstripsParser.ConstraintSymbolContext):
        pass


    # Enter a parse tree produced by fstripsParser#eventSymbol.
    def enterEventSymbol(self, ctx:fstripsParser.EventSymbolContext):
        pass

    # Exit a parse tree produced by fstripsParser#eventSymbol.
    def exitEventSymbol(self, ctx:fstripsParser.EventSymbolContext):
        pass


    # Enter a parse tree produced by fstripsParser#actionDefBody.
    def enterActionDefBody(self, ctx:fstripsParser.ActionDefBodyContext):
        pass

    # Exit a parse tree produced by fstripsParser#actionDefBody.
    def exitActionDefBody(self, ctx:fstripsParser.ActionDefBodyContext):
        pass


    # Enter a parse tree produced by fstripsParser#TrivialPrecondition.
    def enterTrivialPrecondition(self, ctx:fstripsParser.TrivialPreconditionContext):
        pass

    # Exit a parse tree produced by fstripsParser#TrivialPrecondition.
    def exitTrivialPrecondition(self, ctx:fstripsParser.TrivialPreconditionContext):
        pass


    # Enter a parse tree produced by fstripsParser#RegularPrecondition.
    def enterRegularPrecondition(self, ctx:fstripsParser.RegularPreconditionContext):
        pass

    # Exit a parse tree produced by fstripsParser#RegularPrecondition.
    def exitRegularPrecondition(self, ctx:fstripsParser.RegularPreconditionContext):
        pass


    # Enter a parse tree produced by fstripsParser#TermGoalDesc.
    def enterTermGoalDesc(self, ctx:fstripsParser.TermGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#TermGoalDesc.
    def exitTermGoalDesc(self, ctx:fstripsParser.TermGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#AndGoalDesc.
    def enterAndGoalDesc(self, ctx:fstripsParser.AndGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#AndGoalDesc.
    def exitAndGoalDesc(self, ctx:fstripsParser.AndGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#OrGoalDesc.
    def enterOrGoalDesc(self, ctx:fstripsParser.OrGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#OrGoalDesc.
    def exitOrGoalDesc(self, ctx:fstripsParser.OrGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#NotGoalDesc.
    def enterNotGoalDesc(self, ctx:fstripsParser.NotGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#NotGoalDesc.
    def exitNotGoalDesc(self, ctx:fstripsParser.NotGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#ImplyGoalDesc.
    def enterImplyGoalDesc(self, ctx:fstripsParser.ImplyGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#ImplyGoalDesc.
    def exitImplyGoalDesc(self, ctx:fstripsParser.ImplyGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#ExistentialGoalDesc.
    def enterExistentialGoalDesc(self, ctx:fstripsParser.ExistentialGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#ExistentialGoalDesc.
    def exitExistentialGoalDesc(self, ctx:fstripsParser.ExistentialGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#UniversalGoalDesc.
    def enterUniversalGoalDesc(self, ctx:fstripsParser.UniversalGoalDescContext):
        pass

    # Exit a parse tree produced by fstripsParser#UniversalGoalDesc.
    def exitUniversalGoalDesc(self, ctx:fstripsParser.UniversalGoalDescContext):
        pass


    # Enter a parse tree produced by fstripsParser#BuiltinBinaryAtom.
    def enterBuiltinBinaryAtom(self, ctx:fstripsParser.BuiltinBinaryAtomContext):
        pass

    # Exit a parse tree produced by fstripsParser#BuiltinBinaryAtom.
    def exitBuiltinBinaryAtom(self, ctx:fstripsParser.BuiltinBinaryAtomContext):
        pass


    # Enter a parse tree produced by fstripsParser#atomicTermFormula.
    def enterAtomicTermFormula(self, ctx:fstripsParser.AtomicTermFormulaContext):
        pass

    # Exit a parse tree produced by fstripsParser#atomicTermFormula.
    def exitAtomicTermFormula(self, ctx:fstripsParser.AtomicTermFormulaContext):
        pass


    # Enter a parse tree produced by fstripsParser#TermObject.
    def enterTermObject(self, ctx:fstripsParser.TermObjectContext):
        pass

    # Exit a parse tree produced by fstripsParser#TermObject.
    def exitTermObject(self, ctx:fstripsParser.TermObjectContext):
        pass


    # Enter a parse tree produced by fstripsParser#TermNumber.
    def enterTermNumber(self, ctx:fstripsParser.TermNumberContext):
        pass

    # Exit a parse tree produced by fstripsParser#TermNumber.
    def exitTermNumber(self, ctx:fstripsParser.TermNumberContext):
        pass


    # Enter a parse tree produced by fstripsParser#TermVariable.
    def enterTermVariable(self, ctx:fstripsParser.TermVariableContext):
        pass

    # Exit a parse tree produced by fstripsParser#TermVariable.
    def exitTermVariable(self, ctx:fstripsParser.TermVariableContext):
        pass


    # Enter a parse tree produced by fstripsParser#TermTimeStep.
    def enterTermTimeStep(self, ctx:fstripsParser.TermTimeStepContext):
        pass

    # Exit a parse tree produced by fstripsParser#TermTimeStep.
    def exitTermTimeStep(self, ctx:fstripsParser.TermTimeStepContext):
        pass


    # Enter a parse tree produced by fstripsParser#TermFunction.
    def enterTermFunction(self, ctx:fstripsParser.TermFunctionContext):
        pass

    # Exit a parse tree produced by fstripsParser#TermFunction.
    def exitTermFunction(self, ctx:fstripsParser.TermFunctionContext):
        pass


    # Enter a parse tree produced by fstripsParser#GenericFunctionTerm.
    def enterGenericFunctionTerm(self, ctx:fstripsParser.GenericFunctionTermContext):
        pass

    # Exit a parse tree produced by fstripsParser#GenericFunctionTerm.
    def exitGenericFunctionTerm(self, ctx:fstripsParser.GenericFunctionTermContext):
        pass


    # Enter a parse tree produced by fstripsParser#BinaryArithmeticFunctionTerm.
    def enterBinaryArithmeticFunctionTerm(self, ctx:fstripsParser.BinaryArithmeticFunctionTermContext):
        pass

    # Exit a parse tree produced by fstripsParser#BinaryArithmeticFunctionTerm.
    def exitBinaryArithmeticFunctionTerm(self, ctx:fstripsParser.BinaryArithmeticFunctionTermContext):
        pass


    # Enter a parse tree produced by fstripsParser#UnaryArithmeticFunctionTerm.
    def enterUnaryArithmeticFunctionTerm(self, ctx:fstripsParser.UnaryArithmeticFunctionTermContext):
        pass

    # Exit a parse tree produced by fstripsParser#UnaryArithmeticFunctionTerm.
    def exitUnaryArithmeticFunctionTerm(self, ctx:fstripsParser.UnaryArithmeticFunctionTermContext):
        pass


    # Enter a parse tree produced by fstripsParser#derivedDef.
    def enterDerivedDef(self, ctx:fstripsParser.DerivedDefContext):
        pass

    # Exit a parse tree produced by fstripsParser#derivedDef.
    def exitDerivedDef(self, ctx:fstripsParser.DerivedDefContext):
        pass


    # Enter a parse tree produced by fstripsParser#ConjunctiveEffectFormula.
    def enterConjunctiveEffectFormula(self, ctx:fstripsParser.ConjunctiveEffectFormulaContext):
        pass

    # Exit a parse tree produced by fstripsParser#ConjunctiveEffectFormula.
    def exitConjunctiveEffectFormula(self, ctx:fstripsParser.ConjunctiveEffectFormulaContext):
        pass


    # Enter a parse tree produced by fstripsParser#SingleEffect.
    def enterSingleEffect(self, ctx:fstripsParser.SingleEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#SingleEffect.
    def exitSingleEffect(self, ctx:fstripsParser.SingleEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#UniversallyQuantifiedEffect.
    def enterUniversallyQuantifiedEffect(self, ctx:fstripsParser.UniversallyQuantifiedEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#UniversallyQuantifiedEffect.
    def exitUniversallyQuantifiedEffect(self, ctx:fstripsParser.UniversallyQuantifiedEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#SingleConditionalEffect.
    def enterSingleConditionalEffect(self, ctx:fstripsParser.SingleConditionalEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#SingleConditionalEffect.
    def exitSingleConditionalEffect(self, ctx:fstripsParser.SingleConditionalEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#MultipleConditionalEffect.
    def enterMultipleConditionalEffect(self, ctx:fstripsParser.MultipleConditionalEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#MultipleConditionalEffect.
    def exitMultipleConditionalEffect(self, ctx:fstripsParser.MultipleConditionalEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#AtomicEffect.
    def enterAtomicEffect(self, ctx:fstripsParser.AtomicEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#AtomicEffect.
    def exitAtomicEffect(self, ctx:fstripsParser.AtomicEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#AssignConstant.
    def enterAssignConstant(self, ctx:fstripsParser.AssignConstantContext):
        pass

    # Exit a parse tree produced by fstripsParser#AssignConstant.
    def exitAssignConstant(self, ctx:fstripsParser.AssignConstantContext):
        pass


    # Enter a parse tree produced by fstripsParser#AssignEffect.
    def enterAssignEffect(self, ctx:fstripsParser.AssignEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#AssignEffect.
    def exitAssignEffect(self, ctx:fstripsParser.AssignEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#DeleteAtomEffect.
    def enterDeleteAtomEffect(self, ctx:fstripsParser.DeleteAtomEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#DeleteAtomEffect.
    def exitDeleteAtomEffect(self, ctx:fstripsParser.DeleteAtomEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#AddAtomEffect.
    def enterAddAtomEffect(self, ctx:fstripsParser.AddAtomEffectContext):
        pass

    # Exit a parse tree produced by fstripsParser#AddAtomEffect.
    def exitAddAtomEffect(self, ctx:fstripsParser.AddAtomEffectContext):
        pass


    # Enter a parse tree produced by fstripsParser#builtin_binary_function.
    def enterBuiltin_binary_function(self, ctx:fstripsParser.Builtin_binary_functionContext):
        pass

    # Exit a parse tree produced by fstripsParser#builtin_binary_function.
    def exitBuiltin_binary_function(self, ctx:fstripsParser.Builtin_binary_functionContext):
        pass


    # Enter a parse tree produced by fstripsParser#builtin_unary_function.
    def enterBuiltin_unary_function(self, ctx:fstripsParser.Builtin_unary_functionContext):
        pass

    # Exit a parse tree produced by fstripsParser#builtin_unary_function.
    def exitBuiltin_unary_function(self, ctx:fstripsParser.Builtin_unary_functionContext):
        pass


    # Enter a parse tree produced by fstripsParser#builtin_binary_predicate.
    def enterBuiltin_binary_predicate(self, ctx:fstripsParser.Builtin_binary_predicateContext):
        pass

    # Exit a parse tree produced by fstripsParser#builtin_binary_predicate.
    def exitBuiltin_binary_predicate(self, ctx:fstripsParser.Builtin_binary_predicateContext):
        pass


    # Enter a parse tree produced by fstripsParser#assignOp.
    def enterAssignOp(self, ctx:fstripsParser.AssignOpContext):
        pass

    # Exit a parse tree produced by fstripsParser#assignOp.
    def exitAssignOp(self, ctx:fstripsParser.AssignOpContext):
        pass


    # Enter a parse tree produced by fstripsParser#problem.
    def enterProblem(self, ctx:fstripsParser.ProblemContext):
        pass

    # Exit a parse tree produced by fstripsParser#problem.
    def exitProblem(self, ctx:fstripsParser.ProblemContext):
        pass


    # Enter a parse tree produced by fstripsParser#problemMeta.
    def enterProblemMeta(self, ctx:fstripsParser.ProblemMetaContext):
        pass

    # Exit a parse tree produced by fstripsParser#problemMeta.
    def exitProblemMeta(self, ctx:fstripsParser.ProblemMetaContext):
        pass


    # Enter a parse tree produced by fstripsParser#problemDecl.
    def enterProblemDecl(self, ctx:fstripsParser.ProblemDeclContext):
        pass

    # Exit a parse tree produced by fstripsParser#problemDecl.
    def exitProblemDecl(self, ctx:fstripsParser.ProblemDeclContext):
        pass


    # Enter a parse tree produced by fstripsParser#problemDomain.
    def enterProblemDomain(self, ctx:fstripsParser.ProblemDomainContext):
        pass

    # Exit a parse tree produced by fstripsParser#problemDomain.
    def exitProblemDomain(self, ctx:fstripsParser.ProblemDomainContext):
        pass


    # Enter a parse tree produced by fstripsParser#object_declaration.
    def enterObject_declaration(self, ctx:fstripsParser.Object_declarationContext):
        pass

    # Exit a parse tree produced by fstripsParser#object_declaration.
    def exitObject_declaration(self, ctx:fstripsParser.Object_declarationContext):
        pass


    # Enter a parse tree produced by fstripsParser#boundsDecl.
    def enterBoundsDecl(self, ctx:fstripsParser.BoundsDeclContext):
        pass

    # Exit a parse tree produced by fstripsParser#boundsDecl.
    def exitBoundsDecl(self, ctx:fstripsParser.BoundsDeclContext):
        pass


    # Enter a parse tree produced by fstripsParser#typeBoundsDefinition.
    def enterTypeBoundsDefinition(self, ctx:fstripsParser.TypeBoundsDefinitionContext):
        pass

    # Exit a parse tree produced by fstripsParser#typeBoundsDefinition.
    def exitTypeBoundsDefinition(self, ctx:fstripsParser.TypeBoundsDefinitionContext):
        pass


    # Enter a parse tree produced by fstripsParser#init.
    def enterInit(self, ctx:fstripsParser.InitContext):
        pass

    # Exit a parse tree produced by fstripsParser#init.
    def exitInit(self, ctx:fstripsParser.InitContext):
        pass


    # Enter a parse tree produced by fstripsParser#InitPositiveLiteral.
    def enterInitPositiveLiteral(self, ctx:fstripsParser.InitPositiveLiteralContext):
        pass

    # Exit a parse tree produced by fstripsParser#InitPositiveLiteral.
    def exitInitPositiveLiteral(self, ctx:fstripsParser.InitPositiveLiteralContext):
        pass


    # Enter a parse tree produced by fstripsParser#InitNegativeLiteral.
    def enterInitNegativeLiteral(self, ctx:fstripsParser.InitNegativeLiteralContext):
        pass

    # Exit a parse tree produced by fstripsParser#InitNegativeLiteral.
    def exitInitNegativeLiteral(self, ctx:fstripsParser.InitNegativeLiteralContext):
        pass


    # Enter a parse tree produced by fstripsParser#InitFunctionAssignment.
    def enterInitFunctionAssignment(self, ctx:fstripsParser.InitFunctionAssignmentContext):
        pass

    # Exit a parse tree produced by fstripsParser#InitFunctionAssignment.
    def exitInitFunctionAssignment(self, ctx:fstripsParser.InitFunctionAssignmentContext):
        pass


    # Enter a parse tree produced by fstripsParser#flat_term.
    def enterFlat_term(self, ctx:fstripsParser.Flat_termContext):
        pass

    # Exit a parse tree produced by fstripsParser#flat_term.
    def exitFlat_term(self, ctx:fstripsParser.Flat_termContext):
        pass


    # Enter a parse tree produced by fstripsParser#flat_atom.
    def enterFlat_atom(self, ctx:fstripsParser.Flat_atomContext):
        pass

    # Exit a parse tree produced by fstripsParser#flat_atom.
    def exitFlat_atom(self, ctx:fstripsParser.Flat_atomContext):
        pass


    # Enter a parse tree produced by fstripsParser#symbolic_constant.
    def enterSymbolic_constant(self, ctx:fstripsParser.Symbolic_constantContext):
        pass

    # Exit a parse tree produced by fstripsParser#symbolic_constant.
    def exitSymbolic_constant(self, ctx:fstripsParser.Symbolic_constantContext):
        pass


    # Enter a parse tree produced by fstripsParser#numeric_constant.
    def enterNumeric_constant(self, ctx:fstripsParser.Numeric_constantContext):
        pass

    # Exit a parse tree produced by fstripsParser#numeric_constant.
    def exitNumeric_constant(self, ctx:fstripsParser.Numeric_constantContext):
        pass


    # Enter a parse tree produced by fstripsParser#goal.
    def enterGoal(self, ctx:fstripsParser.GoalContext):
        pass

    # Exit a parse tree produced by fstripsParser#goal.
    def exitGoal(self, ctx:fstripsParser.GoalContext):
        pass


    # Enter a parse tree produced by fstripsParser#probConstraints.
    def enterProbConstraints(self, ctx:fstripsParser.ProbConstraintsContext):
        pass

    # Exit a parse tree produced by fstripsParser#probConstraints.
    def exitProbConstraints(self, ctx:fstripsParser.ProbConstraintsContext):
        pass


    # Enter a parse tree produced by fstripsParser#ConjunctionOfConstraints.
    def enterConjunctionOfConstraints(self, ctx:fstripsParser.ConjunctionOfConstraintsContext):
        pass

    # Exit a parse tree produced by fstripsParser#ConjunctionOfConstraints.
    def exitConjunctionOfConstraints(self, ctx:fstripsParser.ConjunctionOfConstraintsContext):
        pass


    # Enter a parse tree produced by fstripsParser#UniversallyQuantifiedConstraint.
    def enterUniversallyQuantifiedConstraint(self, ctx:fstripsParser.UniversallyQuantifiedConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#UniversallyQuantifiedConstraint.
    def exitUniversallyQuantifiedConstraint(self, ctx:fstripsParser.UniversallyQuantifiedConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#PreferenceConstraint.
    def enterPreferenceConstraint(self, ctx:fstripsParser.PreferenceConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#PreferenceConstraint.
    def exitPreferenceConstraint(self, ctx:fstripsParser.PreferenceConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#PlainConstraintList.
    def enterPlainConstraintList(self, ctx:fstripsParser.PlainConstraintListContext):
        pass

    # Exit a parse tree produced by fstripsParser#PlainConstraintList.
    def exitPlainConstraintList(self, ctx:fstripsParser.PlainConstraintListContext):
        pass


    # Enter a parse tree produced by fstripsParser#ProblemMetric.
    def enterProblemMetric(self, ctx:fstripsParser.ProblemMetricContext):
        pass

    # Exit a parse tree produced by fstripsParser#ProblemMetric.
    def exitProblemMetric(self, ctx:fstripsParser.ProblemMetricContext):
        pass


    # Enter a parse tree produced by fstripsParser#optimization.
    def enterOptimization(self, ctx:fstripsParser.OptimizationContext):
        pass

    # Exit a parse tree produced by fstripsParser#optimization.
    def exitOptimization(self, ctx:fstripsParser.OptimizationContext):
        pass


    # Enter a parse tree produced by fstripsParser#FunctionalExprMetric.
    def enterFunctionalExprMetric(self, ctx:fstripsParser.FunctionalExprMetricContext):
        pass

    # Exit a parse tree produced by fstripsParser#FunctionalExprMetric.
    def exitFunctionalExprMetric(self, ctx:fstripsParser.FunctionalExprMetricContext):
        pass


    # Enter a parse tree produced by fstripsParser#CompositeMetric.
    def enterCompositeMetric(self, ctx:fstripsParser.CompositeMetricContext):
        pass

    # Exit a parse tree produced by fstripsParser#CompositeMetric.
    def exitCompositeMetric(self, ctx:fstripsParser.CompositeMetricContext):
        pass


    # Enter a parse tree produced by fstripsParser#TotalTimeMetric.
    def enterTotalTimeMetric(self, ctx:fstripsParser.TotalTimeMetricContext):
        pass

    # Exit a parse tree produced by fstripsParser#TotalTimeMetric.
    def exitTotalTimeMetric(self, ctx:fstripsParser.TotalTimeMetricContext):
        pass


    # Enter a parse tree produced by fstripsParser#IsViolatedMetric.
    def enterIsViolatedMetric(self, ctx:fstripsParser.IsViolatedMetricContext):
        pass

    # Exit a parse tree produced by fstripsParser#IsViolatedMetric.
    def exitIsViolatedMetric(self, ctx:fstripsParser.IsViolatedMetricContext):
        pass


    # Enter a parse tree produced by fstripsParser#terminalCost.
    def enterTerminalCost(self, ctx:fstripsParser.TerminalCostContext):
        pass

    # Exit a parse tree produced by fstripsParser#terminalCost.
    def exitTerminalCost(self, ctx:fstripsParser.TerminalCostContext):
        pass


    # Enter a parse tree produced by fstripsParser#stageCost.
    def enterStageCost(self, ctx:fstripsParser.StageCostContext):
        pass

    # Exit a parse tree produced by fstripsParser#stageCost.
    def exitStageCost(self, ctx:fstripsParser.StageCostContext):
        pass


    # Enter a parse tree produced by fstripsParser#ConjunctiveConstraint.
    def enterConjunctiveConstraint(self, ctx:fstripsParser.ConjunctiveConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#ConjunctiveConstraint.
    def exitConjunctiveConstraint(self, ctx:fstripsParser.ConjunctiveConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#ForallConstraint.
    def enterForallConstraint(self, ctx:fstripsParser.ForallConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#ForallConstraint.
    def exitForallConstraint(self, ctx:fstripsParser.ForallConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#AtEndConstraint.
    def enterAtEndConstraint(self, ctx:fstripsParser.AtEndConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#AtEndConstraint.
    def exitAtEndConstraint(self, ctx:fstripsParser.AtEndConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#AlwaysConstraint.
    def enterAlwaysConstraint(self, ctx:fstripsParser.AlwaysConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#AlwaysConstraint.
    def exitAlwaysConstraint(self, ctx:fstripsParser.AlwaysConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#SometimeConstraint.
    def enterSometimeConstraint(self, ctx:fstripsParser.SometimeConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#SometimeConstraint.
    def exitSometimeConstraint(self, ctx:fstripsParser.SometimeConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#WithinConstraint.
    def enterWithinConstraint(self, ctx:fstripsParser.WithinConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#WithinConstraint.
    def exitWithinConstraint(self, ctx:fstripsParser.WithinConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#AtMostOnceConstraint.
    def enterAtMostOnceConstraint(self, ctx:fstripsParser.AtMostOnceConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#AtMostOnceConstraint.
    def exitAtMostOnceConstraint(self, ctx:fstripsParser.AtMostOnceConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#SometimeAfterConstraint.
    def enterSometimeAfterConstraint(self, ctx:fstripsParser.SometimeAfterConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#SometimeAfterConstraint.
    def exitSometimeAfterConstraint(self, ctx:fstripsParser.SometimeAfterConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#SometimeBeforeConstraint.
    def enterSometimeBeforeConstraint(self, ctx:fstripsParser.SometimeBeforeConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#SometimeBeforeConstraint.
    def exitSometimeBeforeConstraint(self, ctx:fstripsParser.SometimeBeforeConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#AlwaysWithinConstraint.
    def enterAlwaysWithinConstraint(self, ctx:fstripsParser.AlwaysWithinConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#AlwaysWithinConstraint.
    def exitAlwaysWithinConstraint(self, ctx:fstripsParser.AlwaysWithinConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#HoldDuringConstraint.
    def enterHoldDuringConstraint(self, ctx:fstripsParser.HoldDuringConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#HoldDuringConstraint.
    def exitHoldDuringConstraint(self, ctx:fstripsParser.HoldDuringConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#HoldAfterConstraint.
    def enterHoldAfterConstraint(self, ctx:fstripsParser.HoldAfterConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#HoldAfterConstraint.
    def exitHoldAfterConstraint(self, ctx:fstripsParser.HoldAfterConstraintContext):
        pass


    # Enter a parse tree produced by fstripsParser#AlternativeAlwaysConstraint.
    def enterAlternativeAlwaysConstraint(self, ctx:fstripsParser.AlternativeAlwaysConstraintContext):
        pass

    # Exit a parse tree produced by fstripsParser#AlternativeAlwaysConstraint.
    def exitAlternativeAlwaysConstraint(self, ctx:fstripsParser.AlternativeAlwaysConstraintContext):
        pass


