# -*- coding: utf-8 -*-

from .arithmetic import Addition, Subtraction, Multiplication, Division, Modulo, \
    Power, ArcTangent2, \
    Max, Min, StandardLibFunction

symbols = [
    {},  # 0-ary
    {},  # 1-ary
    # binary:
    {
        '+': Addition,
        '-': Subtraction,
        '*': Multiplication,
        '/': Division,
        '%': Modulo,
        '**': Power,
        '^' : Power,
        'max': Max,
        'min': Min,
        'atan2': ArcTangent2

    }
]


def initialize(lang):
    # register real defined functions
    lang.register_symbol(('sqrt', lang.Real), StandardLibFunction('sqrt', lang, lang.Real))
    lang.register_symbol(('sin', lang.Real), StandardLibFunction('sin', lang, lang.Real))
    lang.register_symbol(('cos', lang.Real), StandardLibFunction('cos', lang, lang.Real))
    lang.register_symbol(('tan', lang.Real), StandardLibFunction('tan', lang, lang.Real))
    lang.register_symbol(('asin', lang.Real), StandardLibFunction('asin', lang, lang.Real))
    lang.register_symbol(('acos', lang.Real), StandardLibFunction('acos', lang, lang.Real))
    lang.register_symbol(('atan', lang.Real), StandardLibFunction('atan', lang, lang.Real))
    lang.register_symbol(('exp', lang.Real), StandardLibFunction('exp', lang, lang.Real))
    lang.register_symbol(('abs', lang.Real), StandardLibFunction('abs', lang, lang.Real))

    # register arithmetic functions
    sorts = [lang.Real, lang.Integer, lang.Natural]

    for sym, klass in symbols[2].items():
        for s in sorts:
            lang.register_symbol((sym, s, s), klass(lang, s, s))
