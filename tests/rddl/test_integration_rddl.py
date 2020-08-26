import pytest
import tarski
from tarski.syntax import *
from tarski.theories import Theory


def test_bool_arithmetic_atom():
    lang = tarski.language(theories=[Theory.ARITHMETIC])
    f = lang.predicate('f')
    phi = lang.constant(1, lang.Integer) * f()
    assert isinstance(phi, Term), "phi should be a Term"

def test_bool_arithmetic_compoundterm():
    lang = tarski.language(theories=[Theory.ARITHMETIC])
    f = lang.predicate('f')
    phi = lang.constant(1, lang.Integer) * (lang.constant(0, lang.Integer) > lang.constant(1, lang.Integer))
    assert isinstance(phi, Term), "phi should be a Term"

def test_bool_constants():
    lang = tarski.language(theories=[Theory.ARITHMETIC])
    true = lang.constant(1, lang.Boolean)
    assert isinstance(true, Constant), "Boolean constants should be declarable"

def test_complex_mixed_type_formula():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.EQUALITY])
    x = lang.predicate("x")
    y = lang.predicate("y")
    f = ((x == y) + lang.constant(1, lang.Integer))
    assert isinstance(f, CompoundTerm) , "should construct a correct CompoundTerm with mixed Bool and Int"
    z = lang.predicate("z")
    g = ((x() == y()) & z())
    assert isinstance(g, CompoundFormula), "should construct a compoundformula when allowed"

    a = lang.predicate("a")
    b = lang.predicate("b")
    g = ((x == y) + (a() & b()))

    assert isinstance(g, CompoundTerm), "should construct a correct CompoundTerm with mixed Bool and Int"

def test_equiv_simple():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.EQUALITY])
    c1 = lang.constant(1, lang.Boolean)
    c2 = lang.constant(1, lang.Boolean)
    
    v = lang.variable('v', lang.Boolean)

    a = (v == c1)
    b = (v == c2)

    assert a.is_syntactically_equal(b)

def test_equiv_mixed_type():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.EQUALITY])
    c1 = lang.constant(True, lang.Boolean)
    c2 = lang.constant(True, lang.Boolean)
    
    v = lang.variable('v', lang.Boolean)
    x = lang.variable('x', lang.Integer)
    y = lang.variable('y', lang.Integer)

    a = (x < y) | (c1 & v)
    b = (x > y) | (c1 & v)
    assert not a.is_syntactically_equal(b)

#def test_land_fails_if_improper_numeric_type():
#    #todo:this
#    pass
#

def test_quantified_over_bool_functions():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.BOOLEAN, Theory.EQUALITY])

    c1 = lang.constant(True, lang.Boolean)
    v = lang.variable('v', lang.Boolean)
    x = lang.variable('x', lang.Integer)
    y = lang.variable('y', lang.Integer)
    b = (x > y) | (c1 & v)

    qf = tarski.syntax.formulas.forall(v,x,y, (b == 1))
    assert isinstance(qf, QuantifiedFormula), "should have built a quantified formula"
    #todo: better test
    with pytest.raises(Exception):
        qf = tarski.syntax.formulas.forall(v,x,y, b + 5) #should raise an exception if top level type is not boolean


def test_if_then_else_boolean_codomain():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.BOOLEAN, Theory.EQUALITY])

    v = lang.predicate('v')
    x = lang.variable('x', lang.Integer)
    y = lang.variable('y', lang.Integer)

    ite = tarski.syntax.ite(x < y, v(), lang.constant(0, lang.Boolean))
    assert isinstance(ite, Term), "if then else should be a term"
    assert ite.sort == lang.Boolean, "if then else term should have boolean codomain"

def test_if_then_else_numeric_codomain():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.BOOLEAN, Theory.EQUALITY])

    v = lang.predicate('v')
    x = lang.variable('x', lang.Integer)
    y = lang.variable('y', lang.Integer)

    ite = tarski.syntax.ite(x < y, (x + 1), lang.constant(3, lang.Integer))
    assert isinstance(ite, Term), "if then else should be a term"
    assert ite.sort == lang.Real, "if then else term should have numeric codomain" #todo: actually might need to be integer


def test_if_then_else_fails_on_conflicting_codomain():
    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.BOOLEAN, Theory.EQUALITY])

    v = lang.variable('v', lang.Boolean)
    x = lang.variable('x', lang.Integer)
    y = lang.variable('y', lang.Integer)

    ite = tarski.syntax.ite(x < y, (x + 1), lang.constant(3, lang.Integer))

    with pytest.raises(Exception):
        ite = tarski.syntax.ite(x < y, lang.constant(True, lang.Boolean), lang.constant(3, lang.Integer))

def test_sum_operates_over_predicates():
    from tarski.syntax.arithmetic import sumterm

    lang = tarski.language(theories=[Theory.ARITHMETIC, Theory.EQUALITY])
    box_t = lang.sort("box")
    v = lang.variable('v', box_t)
    boxes = [lang.constant(f"b{k}", box_t) for k in range(5)]
    
    visible = lang.predicate('visible', box_t)
    s = (sumterm(v, visible(v)) >= lang.constant(3, lang.Integer))
    assert isinstance(s, Formula), "after summing and making a logical comparison, we should have a formula"
