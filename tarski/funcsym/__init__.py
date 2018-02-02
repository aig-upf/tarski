# -*- coding: utf-8 -*-

from ._arithmetic import Addition, Subtraction, Multiplication, Division, Modulo, \
    Power, ArcTangent2, \
    Max, Min, StandardLibFunction

symbols = [
    # 0-ary
    {}, \
    # 1-ary
    { }, \
    # binary
    {
        '+' : Addition,
        '-' : Subtraction,
        '*' : Multiplication,
        '/' : Division,
        '**' : Power,
        'max' : Max,
        'min' : Min,
        'atan2' : ArcTangent2

    }
]

def initialize( L  ) :

    # register real defined functions
    L.register_symbol( ('sqrt', L.Real), StandardLibFunction( 'sqrt', L, L.Real) )
    L.register_symbol( ('sin', L.Real), StandardLibFunction( 'sin', L, L.Real) )
    L.register_symbol( ('cos', L.Real), StandardLibFunction( 'cos', L, L.Real) )
    L.register_symbol( ('tan', L.Real), StandardLibFunction( 'tan', L, L.Real) )
    L.register_symbol( ('asin', L.Real), StandardLibFunction( 'asin', L, L.Real) )
    L.register_symbol( ('acos', L.Real), StandardLibFunction( 'acos', L, L.Real) )
    L.register_symbol( ('atan', L.Real), StandardLibFunction( 'atan', L, L.Real) )
    L.register_symbol( ('exp', L.Real), StandardLibFunction( 'exp', L, L.Real) )
    L.register_symbol( ('abs', L.Real), StandardLibFunction( 'abs', L, L.Real) )

    # register arithmetic functions
    sorts = [ L.Real, L.Integer, L.Natural ]

    for sym, klass in symbols[2].items() :
        for s in sorts :
            L.register_symbol( (sym, s, s), klass(L,s,s))
