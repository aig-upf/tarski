# Generated from ./grammars/fstrips.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u008d")
        buf.write("\u03a7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\3\2\3\2\5\2\u00a1\n\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u00a7\n\3\3\3\5\3\u00aa\n\3\3\3\5\3\u00ad\n\3\3\3\5")
        buf.write("\3\u00b0\n\3\3\3\5\3\u00b3\n\3\3\3\7\3\u00b6\n\3\f\3\16")
        buf.write("\3\u00b9\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\6\5\u00c5\n\5\r\5\16\5\u00c6\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\5\7\u00d3\n\7\3\b\3\b\5\b\u00d7\n\b\3")
        buf.write("\t\7\t\u00da\n\t\f\t\16\t\u00dd\13\t\3\t\6\t\u00e0\n\t")
        buf.write("\r\t\16\t\u00e1\3\t\7\t\u00e5\n\t\f\t\16\t\u00e8\13\t")
        buf.write("\5\t\u00ea\n\t\3\n\6\n\u00ed\n\n\r\n\16\n\u00ee\3\n\3")
        buf.write("\n\3\n\3\13\7\13\u00f5\n\13\f\13\16\13\u00f8\13\13\3\13")
        buf.write("\6\13\u00fb\n\13\r\13\16\13\u00fc\3\13\7\13\u0100\n\13")
        buf.write("\f\13\16\13\u0103\13\13\5\13\u0105\n\13\3\f\6\f\u0108")
        buf.write("\n\f\r\f\16\f\u0109\3\f\3\f\3\f\3\r\3\r\3\r\6\r\u0112")
        buf.write("\n\r\r\r\16\r\u0113\3\r\3\r\3\r\5\r\u0119\n\r\3\16\3\16")
        buf.write("\5\16\u011d\n\16\3\17\3\17\3\17\7\17\u0122\n\17\f\17\16")
        buf.write("\17\u0125\13\17\3\17\3\17\3\20\3\20\5\20\u012b\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\7\25\u0143\n\25\f\25\16\25\u0146\13\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0156\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \5 \u0185\n \3!\3!\3!\3!\7!\u018b\n")
        buf.write("!\f!\16!\u018e\13!\3!\3!\3!\3!\7!\u0194\n!\f!\16!\u0197")
        buf.write("\13!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01b7\n!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\7$\u01c8")
        buf.write("\n$\f$\16$\u01cb\13$\3$\3$\3%\3%\3%\3%\3%\5%\u01d4\n%")
        buf.write("\3&\3&\3&\7&\u01d9\n&\f&\16&\u01dc\13&\3&\3&\3&\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01eb\n&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\7)\u01ff")
        buf.write("\n)\f)\16)\u0202\13)\3)\3)\5)\u0206\n)\3*\3*\3*\3*\3*")
        buf.write("\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\5,\u0217\n,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0228\n-\3.\3.\3")
        buf.write(".\3.\3.\5.\u022f\n.\3/\3/\3/\3/\5/\u0235\n/\3\60\3\60")
        buf.write("\3\60\3\60\5\60\u023b\n\60\3\61\3\61\3\61\7\61\u0240\n")
        buf.write("\61\f\61\16\61\u0243\13\61\3\61\3\61\3\62\3\62\3\62\7")
        buf.write("\62\u024a\n\62\f\62\16\62\u024d\13\62\3\62\3\62\5\62\u0251")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\7\63")
        buf.write("\u0267\n\63\f\63\16\63\u026a\13\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u0270\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u0284\n\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3:\3:\3:\5:\u0295\n:\3:\5:\u0298\n:\3:\3:\3")
        buf.write(":\7:\u029d\n:\f:\16:\u02a0\13:\3:\3:\3;\3;\3;\5;\u02a7")
        buf.write("\n;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3")
        buf.write("?\3?\6?\u02bb\n?\r?\16?\u02bc\3?\3?\3@\3@\3@\3@\3@\3@")
        buf.write("\3@\3@\3@\3@\3@\3A\3A\3A\7A\u02cf\nA\fA\16A\u02d2\13A")
        buf.write("\3A\3A\3B\3B\3B\5B\u02d9\nB\3C\3C\3C\7C\u02de\nC\fC\16")
        buf.write("C\u02e1\13C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D")
        buf.write("\3D\5D\u02f2\nD\3E\3E\3E\3E\3E\3E\5E\u02fa\nE\3F\3F\3")
        buf.write("F\7F\u02ff\nF\fF\16F\u0302\13F\3F\3F\3G\3G\3G\3G\3G\3")
        buf.write("H\3H\3H\3H\3H\3I\3I\3I\7I\u0313\nI\fI\16I\u0316\13I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u0324\nI\3I\3I\3")
        buf.write("I\3I\6I\u032a\nI\rI\16I\u032b\5I\u032e\nI\3J\3J\3J\3J")
        buf.write("\3J\3J\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u0344")
        buf.write("\nL\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3O\3O\3O\6O\u0353\n")
        buf.write("O\rO\16O\u0354\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O")
        buf.write("\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\3O\6O\u039e\nO\rO\16O\u039f\3O\3O\3O\5O\u03a5")
        buf.write("\nO\3O\2\2P\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\2\t\3\2RS\5\2\t\t")
        buf.write("\35\35 $\4\2\t\t%-\4\2\31\31.\61\4\2\37\37\62\65\3\2\64")
        buf.write("\65\3\2AB\2\u03c4\2\u00a0\3\2\2\2\4\u00a2\3\2\2\2\6\u00bc")
        buf.write("\3\2\2\2\b\u00c1\3\2\2\2\n\u00ca\3\2\2\2\f\u00d2\3\2\2")
        buf.write("\2\16\u00d6\3\2\2\2\20\u00e9\3\2\2\2\22\u00ec\3\2\2\2")
        buf.write("\24\u0104\3\2\2\2\26\u0107\3\2\2\2\30\u0118\3\2\2\2\32")
        buf.write("\u011c\3\2\2\2\34\u011e\3\2\2\2\36\u012a\3\2\2\2 \u012c")
        buf.write("\3\2\2\2\"\u0133\3\2\2\2$\u0138\3\2\2\2&\u013a\3\2\2\2")
        buf.write("(\u013f\3\2\2\2*\u0149\3\2\2\2,\u014e\3\2\2\2.\u0155\3")
        buf.write("\2\2\2\60\u0157\3\2\2\2\62\u0161\3\2\2\2\64\u016c\3\2")
        buf.write("\2\2\66\u0176\3\2\2\28\u0178\3\2\2\2:\u017a\3\2\2\2<\u017c")
        buf.write("\3\2\2\2>\u0184\3\2\2\2@\u01b6\3\2\2\2B\u01b8\3\2\2\2")
        buf.write("D\u01be\3\2\2\2F\u01c4\3\2\2\2H\u01d3\3\2\2\2J\u01ea\3")
        buf.write("\2\2\2L\u01ec\3\2\2\2N\u01f6\3\2\2\2P\u0205\3\2\2\2R\u0207")
        buf.write("\3\2\2\2T\u020d\3\2\2\2V\u0216\3\2\2\2X\u0227\3\2\2\2")
        buf.write("Z\u022e\3\2\2\2\\\u0234\3\2\2\2^\u023a\3\2\2\2`\u023c")
        buf.write("\3\2\2\2b\u0250\3\2\2\2d\u026f\3\2\2\2f\u0283\3\2\2\2")
        buf.write("h\u0285\3\2\2\2j\u0287\3\2\2\2l\u0289\3\2\2\2n\u028b\3")
        buf.write("\2\2\2p\u028d\3\2\2\2r\u028f\3\2\2\2t\u02a6\3\2\2\2v\u02a8")
        buf.write("\3\2\2\2x\u02ad\3\2\2\2z\u02b2\3\2\2\2|\u02b7\3\2\2\2")
        buf.write("~\u02c0\3\2\2\2\u0080\u02cb\3\2\2\2\u0082\u02d8\3\2\2")
        buf.write("\2\u0084\u02da\3\2\2\2\u0086\u02f1\3\2\2\2\u0088\u02f9")
        buf.write("\3\2\2\2\u008a\u02fb\3\2\2\2\u008c\u0305\3\2\2\2\u008e")
        buf.write("\u030a\3\2\2\2\u0090\u032d\3\2\2\2\u0092\u032f\3\2\2\2")
        buf.write("\u0094\u0335\3\2\2\2\u0096\u0343\3\2\2\2\u0098\u0345\3")
        buf.write("\2\2\2\u009a\u034a\3\2\2\2\u009c\u03a4\3\2\2\2\u009e\u00a1")
        buf.write("\5\4\3\2\u009f\u00a1\5r:\2\u00a0\u009e\3\2\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a1\3\3\2\2\2\u00a2\u00a3\7\3\2\2\u00a3\u00a4")
        buf.write("\7\4\2\2\u00a4\u00a6\5\6\4\2\u00a5\u00a7\5\b\5\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2")
        buf.write("\u00a8\u00aa\5\n\6\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00ad\5&\24\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae")
        buf.write("\u00b0\5(\25\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00b2\3\2\2\2\u00b1\u00b3\5\34\17\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b7\3\2\2\2\u00b4")
        buf.write("\u00b6\5.\30\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3")
        buf.write("\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb\7\5\2\2\u00bb\5")
        buf.write("\3\2\2\2\u00bc\u00bd\7\3\2\2\u00bd\u00be\7\6\2\2\u00be")
        buf.write("\u00bf\7R\2\2\u00bf\u00c0\7\5\2\2\u00c0\7\3\2\2\2\u00c1")
        buf.write("\u00c2\7\3\2\2\u00c2\u00c4\7\7\2\2\u00c3\u00c5\7Q\2\2")
        buf.write("\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3")
        buf.write("\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9")
        buf.write("\7\5\2\2\u00c9\t\3\2\2\2\u00ca\u00cb\7\3\2\2\u00cb\u00cc")
        buf.write("\7\b\2\2\u00cc\u00cd\5\20\t\2\u00cd\u00ce\7\5\2\2\u00ce")
        buf.write("\13\3\2\2\2\u00cf\u00d3\7[\2\2\u00d0\u00d3\7\\\2\2\u00d1")
        buf.write("\u00d3\7^\2\2\u00d2\u00cf\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\r\3\2\2\2\u00d4\u00d7\5\f\7")
        buf.write("\2\u00d5\u00d7\7]\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\17\3\2\2\2\u00d8\u00da\7R\2\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00ea\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00de\u00e0\5\22\n\2\u00df\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e6\3\2\2\2\u00e3\u00e5\7R\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00db")
        buf.write("\3\2\2\2\u00e9\u00df\3\2\2\2\u00ea\21\3\2\2\2\u00eb\u00ed")
        buf.write("\7R\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f1\7\t\2\2\u00f1\u00f2\5\30\r\2\u00f2\23\3\2")
        buf.write("\2\2\u00f3\u00f5\7T\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u0105\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fb\5\26\f")
        buf.write("\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u0101\3\2\2\2\u00fe")
        buf.write("\u0100\7T\2\2\u00ff\u00fe\3\2\2\2\u0100\u0103\3\2\2\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0105\3")
        buf.write("\2\2\2\u0103\u0101\3\2\2\2\u0104\u00f6\3\2\2\2\u0104\u00fa")
        buf.write("\3\2\2\2\u0105\25\3\2\2\2\u0106\u0108\7T\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\7\t\2\2")
        buf.write("\u010c\u010d\5\32\16\2\u010d\27\3\2\2\2\u010e\u010f\7")
        buf.write("\3\2\2\u010f\u0111\7\n\2\2\u0110\u0112\5\32\16\2\u0111")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0111\3\2\2\2")
        buf.write("\u0113\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\7")
        buf.write("\5\2\2\u0116\u0119\3\2\2\2\u0117\u0119\5\32\16\2\u0118")
        buf.write("\u010e\3\2\2\2\u0118\u0117\3\2\2\2\u0119\31\3\2\2\2\u011a")
        buf.write("\u011d\7R\2\2\u011b\u011d\5\16\b\2\u011c\u011a\3\2\2\2")
        buf.write("\u011c\u011b\3\2\2\2\u011d\33\3\2\2\2\u011e\u011f\7\3")
        buf.write("\2\2\u011f\u0123\7\13\2\2\u0120\u0122\5\36\20\2\u0121")
        buf.write("\u0120\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0126\u0127\7\5\2\2\u0127\35\3\2\2\2\u0128\u012b")
        buf.write("\5 \21\2\u0129\u012b\5\"\22\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\37\3\2\2\2\u012c\u012d\7\3\2\2\u012d")
        buf.write("\u012e\5$\23\2\u012e\u012f\5\24\13\2\u012f\u0130\7\5\2")
        buf.write("\2\u0130\u0131\7\t\2\2\u0131\u0132\5\32\16\2\u0132!\3")
        buf.write("\2\2\2\u0133\u0134\7\3\2\2\u0134\u0135\5$\23\2\u0135\u0136")
        buf.write("\5\24\13\2\u0136\u0137\7\5\2\2\u0137#\3\2\2\2\u0138\u0139")
        buf.write("\t\2\2\2\u0139%\3\2\2\2\u013a\u013b\7\3\2\2\u013b\u013c")
        buf.write("\7\f\2\2\u013c\u013d\5\20\t\2\u013d\u013e\7\5\2\2\u013e")
        buf.write("\'\3\2\2\2\u013f\u0140\7\3\2\2\u0140\u0144\7\r\2\2\u0141")
        buf.write("\u0143\5*\26\2\u0142\u0141\3\2\2\2\u0143\u0146\3\2\2\2")
        buf.write("\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0147\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7\5\2\2\u0148)")
        buf.write("\3\2\2\2\u0149\u014a\7\3\2\2\u014a\u014b\5,\27\2\u014b")
        buf.write("\u014c\5\24\13\2\u014c\u014d\7\5\2\2\u014d+\3\2\2\2\u014e")
        buf.write("\u014f\7R\2\2\u014f-\3\2\2\2\u0150\u0156\5\60\31\2\u0151")
        buf.write("\u0156\5\64\33\2\u0152\u0156\5T+\2\u0153\u0156\5\62\32")
        buf.write("\2\u0154\u0156\5L\'\2\u0155\u0150\3\2\2\2\u0155\u0151")
        buf.write("\3\2\2\2\u0155\u0152\3\2\2\2\u0155\u0153\3\2\2\2\u0155")
        buf.write("\u0154\3\2\2\2\u0156/\3\2\2\2\u0157\u0158\7\3\2\2\u0158")
        buf.write("\u0159\7\16\2\2\u0159\u015a\5\66\34\2\u015a\u015b\7\17")
        buf.write("\2\2\u015b\u015c\7\3\2\2\u015c\u015d\5\24\13\2\u015d\u015e")
        buf.write("\7\5\2\2\u015e\u015f\5<\37\2\u015f\u0160\7\5\2\2\u0160")
        buf.write("\61\3\2\2\2\u0161\u0162\7\3\2\2\u0162\u0163\7\20\2\2\u0163")
        buf.write("\u0164\58\35\2\u0164\u0165\7\17\2\2\u0165\u0166\7\3\2")
        buf.write("\2\u0166\u0167\5\24\13\2\u0167\u0168\7\5\2\2\u0168\u0169")
        buf.write("\7\21\2\2\u0169\u016a\5@!\2\u016a\u016b\7\5\2\2\u016b")
        buf.write("\63\3\2\2\2\u016c\u016d\7\3\2\2\u016d\u016e\7\22\2\2\u016e")
        buf.write("\u016f\5:\36\2\u016f\u0170\7\17\2\2\u0170\u0171\7\3\2")
        buf.write("\2\u0171\u0172\5\24\13\2\u0172\u0173\7\5\2\2\u0173\u0174")
        buf.write("\5<\37\2\u0174\u0175\7\5\2\2\u0175\65\3\2\2\2\u0176\u0177")
        buf.write("\t\2\2\2\u0177\67\3\2\2\2\u0178\u0179\7R\2\2\u01799\3")
        buf.write("\2\2\2\u017a\u017b\t\2\2\2\u017b;\3\2\2\2\u017c\u017d")
        buf.write("\7Y\2\2\u017d\u017e\5> \2\u017e\u017f\7Z\2\2\u017f\u0180")
        buf.write("\5b\62\2\u0180=\3\2\2\2\u0181\u0182\7\3\2\2\u0182\u0185")
        buf.write("\7\5\2\2\u0183\u0185\5@!\2\u0184\u0181\3\2\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185?\3\2\2\2\u0186\u01b7\5F$\2\u0187\u0188")
        buf.write("\7\3\2\2\u0188\u018c\7\23\2\2\u0189\u018b\5@!\2\u018a")
        buf.write("\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u018c\3")
        buf.write("\2\2\2\u018f\u01b7\7\5\2\2\u0190\u0191\7\3\2\2\u0191\u0195")
        buf.write("\7\24\2\2\u0192\u0194\5@!\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u01b7\7")
        buf.write("\5\2\2\u0199\u019a\7\3\2\2\u019a\u019b\7\25\2\2\u019b")
        buf.write("\u019c\5@!\2\u019c\u019d\7\5\2\2\u019d\u01b7\3\2\2\2\u019e")
        buf.write("\u019f\7\3\2\2\u019f\u01a0\7\26\2\2\u01a0\u01a1\5@!\2")
        buf.write("\u01a1\u01a2\5@!\2\u01a2\u01a3\7\5\2\2\u01a3\u01b7\3\2")
        buf.write("\2\2\u01a4\u01a5\7\3\2\2\u01a5\u01a6\7\27\2\2\u01a6\u01a7")
        buf.write("\7\3\2\2\u01a7\u01a8\5\24\13\2\u01a8\u01a9\7\5\2\2\u01a9")
        buf.write("\u01aa\5@!\2\u01aa\u01ab\7\5\2\2\u01ab\u01b7\3\2\2\2\u01ac")
        buf.write("\u01ad\7\3\2\2\u01ad\u01ae\7\30\2\2\u01ae\u01af\7\3\2")
        buf.write("\2\u01af\u01b0\5\24\13\2\u01b0\u01b1\7\5\2\2\u01b1\u01b2")
        buf.write("\5@!\2\u01b2\u01b3\7\5\2\2\u01b3\u01b7\3\2\2\2\u01b4\u01b7")
        buf.write("\5D#\2\u01b5\u01b7\5B\"\2\u01b6\u0186\3\2\2\2\u01b6\u0187")
        buf.write("\3\2\2\2\u01b6\u0190\3\2\2\2\u01b6\u0199\3\2\2\2\u01b6")
        buf.write("\u019e\3\2\2\2\u01b6\u01a4\3\2\2\2\u01b6\u01ac\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7A\3\2\2")
        buf.write("\2\u01b8\u01b9\7\3\2\2\u01b9\u01ba\7\31\2\2\u01ba\u01bb")
        buf.write("\5H%\2\u01bb\u01bc\5H%\2\u01bc\u01bd\7\5\2\2\u01bdC\3")
        buf.write("\2\2\2\u01be\u01bf\7\3\2\2\u01bf\u01c0\5l\67\2\u01c0\u01c1")
        buf.write("\5V,\2\u01c1\u01c2\5V,\2\u01c2\u01c3\7\5\2\2\u01c3E\3")
        buf.write("\2\2\2\u01c4\u01c5\7\3\2\2\u01c5\u01c9\5,\27\2\u01c6\u01c8")
        buf.write("\5H%\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cc\u01cd\7\5\2\2\u01cdG\3\2\2\2\u01ce")
        buf.write("\u01d4\7R\2\2\u01cf\u01d4\7U\2\2\u01d0\u01d4\7T\2\2\u01d1")
        buf.write("\u01d4\7\32\2\2\u01d2\u01d4\5J&\2\u01d3\u01ce\3\2\2\2")
        buf.write("\u01d3\u01cf\3\2\2\2\u01d3\u01d0\3\2\2\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d3\u01d2\3\2\2\2\u01d4I\3\2\2\2\u01d5\u01d6")
        buf.write("\7\3\2\2\u01d6\u01da\5$\23\2\u01d7\u01d9\5H%\2\u01d8\u01d7")
        buf.write("\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dd\u01de\7\5\2\2\u01de\u01eb\3\2\2\2\u01df\u01e0\7")
        buf.write("\3\2\2\u01e0\u01e1\5h\65\2\u01e1\u01e2\5H%\2\u01e2\u01e3")
        buf.write("\5H%\2\u01e3\u01e4\7\5\2\2\u01e4\u01eb\3\2\2\2\u01e5\u01e6")
        buf.write("\7\3\2\2\u01e6\u01e7\5j\66\2\u01e7\u01e8\5H%\2\u01e8\u01e9")
        buf.write("\7\5\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01d5\3\2\2\2\u01ea")
        buf.write("\u01df\3\2\2\2\u01ea\u01e5\3\2\2\2\u01ebK\3\2\2\2\u01ec")
        buf.write("\u01ed\7\3\2\2\u01ed\u01ee\7\33\2\2\u01ee\u01ef\5\66\34")
        buf.write("\2\u01ef\u01f0\7\17\2\2\u01f0\u01f1\7\3\2\2\u01f1\u01f2")
        buf.write("\5\24\13\2\u01f2\u01f3\7\5\2\2\u01f3\u01f4\5N(\2\u01f4")
        buf.write("\u01f5\7\5\2\2\u01f5M\3\2\2\2\u01f6\u01f7\7Y\2\2\u01f7")
        buf.write("\u01f8\5> \2\u01f8\u01f9\7Z\2\2\u01f9\u01fa\5P)\2\u01fa")
        buf.write("O\3\2\2\2\u01fb\u01fc\7\3\2\2\u01fc\u0200\7\23\2\2\u01fd")
        buf.write("\u01ff\5R*\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2\2")
        buf.write("\u0202\u0200\3\2\2\2\u0203\u0206\7\5\2\2\u0204\u0206\5")
        buf.write("R*\2\u0205\u01fb\3\2\2\2\u0205\u0204\3\2\2\2\u0206Q\3")
        buf.write("\2\2\2\u0207\u0208\7\3\2\2\u0208\u0209\5p9\2\u0209\u020a")
        buf.write("\5J&\2\u020a\u020b\5X-\2\u020b\u020c\7\5\2\2\u020cS\3")
        buf.write("\2\2\2\u020d\u020e\7\3\2\2\u020e\u020f\7\34\2\2\u020f")
        buf.write("\u0210\5\24\13\2\u0210\u0211\5@!\2\u0211\u0212\7\5\2\2")
        buf.write("\u0212U\3\2\2\2\u0213\u0217\5J&\2\u0214\u0217\7U\2\2\u0215")
        buf.write("\u0217\7T\2\2\u0216\u0213\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0216\u0215\3\2\2\2\u0217W\3\2\2\2\u0218\u0219\7\3\2")
        buf.write("\2\u0219\u021a\7\35\2\2\u021a\u021b\5Z.\2\u021b\u021c")
        buf.write("\7\5\2\2\u021c\u0228\3\2\2\2\u021d\u021e\7\3\2\2\u021e")
        buf.write("\u021f\7\35\2\2\u021f\u0220\5\\/\2\u0220\u0221\7\5\2\2")
        buf.write("\u0221\u0228\3\2\2\2\u0222\u0223\7\3\2\2\u0223\u0224\7")
        buf.write("\35\2\2\u0224\u0225\5^\60\2\u0225\u0226\7\5\2\2\u0226")
        buf.write("\u0228\3\2\2\2\u0227\u0218\3\2\2\2\u0227\u021d\3\2\2\2")
        buf.write("\u0227\u0222\3\2\2\2\u0228Y\3\2\2\2\u0229\u022a\5J&\2")
        buf.write("\u022a\u022b\7\32\2\2\u022b\u022f\3\2\2\2\u022c\u022d")
        buf.write("\7\32\2\2\u022d\u022f\5J&\2\u022e\u0229\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022f[\3\2\2\2\u0230\u0231\7U\2\2\u0231")
        buf.write("\u0235\7\32\2\2\u0232\u0233\7\32\2\2\u0233\u0235\7U\2")
        buf.write("\2\u0234\u0230\3\2\2\2\u0234\u0232\3\2\2\2\u0235]\3\2")
        buf.write("\2\2\u0236\u0237\7T\2\2\u0237\u023b\7\32\2\2\u0238\u0239")
        buf.write("\7\32\2\2\u0239\u023b\7T\2\2\u023a\u0236\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023b_\3\2\2\2\u023c\u023d\7\3\2\2\u023d")
        buf.write("\u0241\5$\23\2\u023e\u0240\5H%\2\u023f\u023e\3\2\2\2\u0240")
        buf.write("\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2")
        buf.write("\u0242\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0245\7")
        buf.write("\5\2\2\u0245a\3\2\2\2\u0246\u0247\7\3\2\2\u0247\u024b")
        buf.write("\7\23\2\2\u0248\u024a\5d\63\2\u0249\u0248\3\2\2\2\u024a")
        buf.write("\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c\3\2\2\2")
        buf.write("\u024c\u024e\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0251\7")
        buf.write("\5\2\2\u024f\u0251\5d\63\2\u0250\u0246\3\2\2\2\u0250\u024f")
        buf.write("\3\2\2\2\u0251c\3\2\2\2\u0252\u0253\7\3\2\2\u0253\u0254")
        buf.write("\7\30\2\2\u0254\u0255\7\3\2\2\u0255\u0256\5\24\13\2\u0256")
        buf.write("\u0257\7\5\2\2\u0257\u0258\5b\62\2\u0258\u0259\7\5\2\2")
        buf.write("\u0259\u0270\3\2\2\2\u025a\u025b\7\3\2\2\u025b\u025c\7")
        buf.write("\36\2\2\u025c\u025d\5@!\2\u025d\u025e\5f\64\2\u025e\u025f")
        buf.write("\7\5\2\2\u025f\u0270\3\2\2\2\u0260\u0261\7\3\2\2\u0261")
        buf.write("\u0262\7\36\2\2\u0262\u0263\5@!\2\u0263\u0264\7\3\2\2")
        buf.write("\u0264\u0268\7\23\2\2\u0265\u0267\5f\64\2\u0266\u0265")
        buf.write("\3\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0268")
        buf.write("\u0269\3\2\2\2\u0269\u026b\3\2\2\2\u026a\u0268\3\2\2\2")
        buf.write("\u026b\u026c\7\5\2\2\u026c\u026d\7\5\2\2\u026d\u0270\3")
        buf.write("\2\2\2\u026e\u0270\5f\64\2\u026f\u0252\3\2\2\2\u026f\u025a")
        buf.write("\3\2\2\2\u026f\u0260\3\2\2\2\u026f\u026e\3\2\2\2\u0270")
        buf.write("e\3\2\2\2\u0271\u0272\7\3\2\2\u0272\u0273\5n8\2\u0273")
        buf.write("\u0274\5J&\2\u0274\u0275\5V,\2\u0275\u0276\7\5\2\2\u0276")
        buf.write("\u0284\3\2\2\2\u0277\u0278\7\3\2\2\u0278\u0279\7\25\2")
        buf.write("\2\u0279\u027a\5F$\2\u027a\u027b\7\5\2\2\u027b\u0284\3")
        buf.write("\2\2\2\u027c\u0284\5F$\2\u027d\u027e\7\3\2\2\u027e\u027f")
        buf.write("\7\37\2\2\u027f\u0280\5J&\2\u0280\u0281\5H%\2\u0281\u0282")
        buf.write("\7\5\2\2\u0282\u0284\3\2\2\2\u0283\u0271\3\2\2\2\u0283")
        buf.write("\u0277\3\2\2\2\u0283\u027c\3\2\2\2\u0283\u027d\3\2\2\2")
        buf.write("\u0284g\3\2\2\2\u0285\u0286\t\3\2\2\u0286i\3\2\2\2\u0287")
        buf.write("\u0288\t\4\2\2\u0288k\3\2\2\2\u0289\u028a\t\5\2\2\u028a")
        buf.write("m\3\2\2\2\u028b\u028c\t\6\2\2\u028co\3\2\2\2\u028d\u028e")
        buf.write("\t\7\2\2\u028eq\3\2\2\2\u028f\u0290\7\3\2\2\u0290\u0291")
        buf.write("\7\4\2\2\u0291\u0292\5v<\2\u0292\u0294\5x=\2\u0293\u0295")
        buf.write("\5\b\5\2\u0294\u0293\3\2\2\2\u0294\u0295\3\2\2\2\u0295")
        buf.write("\u0297\3\2\2\2\u0296\u0298\5z>\2\u0297\u0296\3\2\2\2\u0297")
        buf.write("\u0298\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u029a\5\u0080")
        buf.write("A\2\u029a\u029e\5\u008cG\2\u029b\u029d\5t;\2\u029c\u029b")
        buf.write("\3\2\2\2\u029d\u02a0\3\2\2\2\u029e\u029c\3\2\2\2\u029e")
        buf.write("\u029f\3\2\2\2\u029f\u02a1\3\2\2\2\u02a0\u029e\3\2\2\2")
        buf.write("\u02a1\u02a2\7\5\2\2\u02a2s\3\2\2\2\u02a3\u02a7\5\u008e")
        buf.write("H\2\u02a4\u02a7\5|?\2\u02a5\u02a7\5\u0092J\2\u02a6\u02a3")
        buf.write("\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a6\u02a5\3\2\2\2\u02a7")
        buf.write("u\3\2\2\2\u02a8\u02a9\7\3\2\2\u02a9\u02aa\7\66\2\2\u02aa")
        buf.write("\u02ab\7R\2\2\u02ab\u02ac\7\5\2\2\u02acw\3\2\2\2\u02ad")
        buf.write("\u02ae\7\3\2\2\u02ae\u02af\7\67\2\2\u02af\u02b0\7R\2\2")
        buf.write("\u02b0\u02b1\7\5\2\2\u02b1y\3\2\2\2\u02b2\u02b3\7\3\2")
        buf.write("\2\u02b3\u02b4\78\2\2\u02b4\u02b5\5\20\t\2\u02b5\u02b6")
        buf.write("\7\5\2\2\u02b6{\3\2\2\2\u02b7\u02b8\7\3\2\2\u02b8\u02ba")
        buf.write("\79\2\2\u02b9\u02bb\5~@\2\u02ba\u02b9\3\2\2\2\u02bb\u02bc")
        buf.write("\3\2\2\2\u02bc\u02ba\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd")
        buf.write("\u02be\3\2\2\2\u02be\u02bf\7\5\2\2\u02bf}\3\2\2\2\u02c0")
        buf.write("\u02c1\7\3\2\2\u02c1\u02c2\7R\2\2\u02c2\u02c3\7\t\2\2")
        buf.write("\u02c3\u02c4\5\f\7\2\u02c4\u02c5\7:\2\2\u02c5\u02c6\7")
        buf.write("U\2\2\u02c6\u02c7\7;\2\2\u02c7\u02c8\7U\2\2\u02c8\u02c9")
        buf.write("\7<\2\2\u02c9\u02ca\7\5\2\2\u02ca\177\3\2\2\2\u02cb\u02cc")
        buf.write("\7\3\2\2\u02cc\u02d0\7X\2\2\u02cd\u02cf\5\u0086D\2\u02ce")
        buf.write("\u02cd\3\2\2\2\u02cf\u02d2\3\2\2\2\u02d0\u02ce\3\2\2\2")
        buf.write("\u02d0\u02d1\3\2\2\2\u02d1\u02d3\3\2\2\2\u02d2\u02d0\3")
        buf.write("\2\2\2\u02d3\u02d4\7\5\2\2\u02d4\u0081\3\2\2\2\u02d5\u02d9")
        buf.write("\7R\2\2\u02d6\u02d9\7U\2\2\u02d7\u02d9\5\u0084C\2\u02d8")
        buf.write("\u02d5\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d8\u02d7\3\2\2\2")
        buf.write("\u02d9\u0083\3\2\2\2\u02da\u02db\7\3\2\2\u02db\u02df\5")
        buf.write("$\23\2\u02dc\u02de\5\u0082B\2\u02dd\u02dc\3\2\2\2\u02de")
        buf.write("\u02e1\3\2\2\2\u02df\u02dd\3\2\2\2\u02df\u02e0\3\2\2\2")
        buf.write("\u02e0\u02e2\3\2\2\2\u02e1\u02df\3\2\2\2\u02e2\u02e3\7")
        buf.write("\5\2\2\u02e3\u0085\3\2\2\2\u02e4\u02f2\5\u0088E\2\u02e5")
        buf.write("\u02e6\7\3\2\2\u02e6\u02e7\7\31\2\2\u02e7\u02e8\5\u0084")
        buf.write("C\2\u02e8\u02e9\7U\2\2\u02e9\u02ea\7\5\2\2\u02ea\u02f2")
        buf.write("\3\2\2\2\u02eb\u02ec\7\3\2\2\u02ec\u02ed\7\31\2\2\u02ed")
        buf.write("\u02ee\5\u0084C\2\u02ee\u02ef\7R\2\2\u02ef\u02f0\7\5\2")
        buf.write("\2\u02f0\u02f2\3\2\2\2\u02f1\u02e4\3\2\2\2\u02f1\u02e5")
        buf.write("\3\2\2\2\u02f1\u02eb\3\2\2\2\u02f2\u0087\3\2\2\2\u02f3")
        buf.write("\u02fa\5\u008aF\2\u02f4\u02f5\7\3\2\2\u02f5\u02f6\7\25")
        buf.write("\2\2\u02f6\u02f7\5\u008aF\2\u02f7\u02f8\7\5\2\2\u02f8")
        buf.write("\u02fa\3\2\2\2\u02f9\u02f3\3\2\2\2\u02f9\u02f4\3\2\2\2")
        buf.write("\u02fa\u0089\3\2\2\2\u02fb\u02fc\7\3\2\2\u02fc\u0300\5")
        buf.write(",\27\2\u02fd\u02ff\5\u0082B\2\u02fe\u02fd\3\2\2\2\u02ff")
        buf.write("\u0302\3\2\2\2\u0300\u02fe\3\2\2\2\u0300\u0301\3\2\2\2")
        buf.write("\u0301\u0303\3\2\2\2\u0302\u0300\3\2\2\2\u0303\u0304\7")
        buf.write("\5\2\2\u0304\u008b\3\2\2\2\u0305\u0306\7\3\2\2\u0306\u0307")
        buf.write("\7=\2\2\u0307\u0308\5@!\2\u0308\u0309\7\5\2\2\u0309\u008d")
        buf.write("\3\2\2\2\u030a\u030b\7\3\2\2\u030b\u030c\7>\2\2\u030c")
        buf.write("\u030d\5\u0090I\2\u030d\u030e\7\5\2\2\u030e\u008f\3\2")
        buf.write("\2\2\u030f\u0310\7\3\2\2\u0310\u0314\7\23\2\2\u0311\u0313")
        buf.write("\5\u0090I\2\u0312\u0311\3\2\2\2\u0313\u0316\3\2\2\2\u0314")
        buf.write("\u0312\3\2\2\2\u0314\u0315\3\2\2\2\u0315\u0317\3\2\2\2")
        buf.write("\u0316\u0314\3\2\2\2\u0317\u032e\7\5\2\2\u0318\u0319\7")
        buf.write("\3\2\2\u0319\u031a\7\30\2\2\u031a\u031b\7\3\2\2\u031b")
        buf.write("\u031c\5\24\13\2\u031c\u031d\7\5\2\2\u031d\u031e\5\u0090")
        buf.write("I\2\u031e\u031f\7\5\2\2\u031f\u032e\3\2\2\2\u0320\u0321")
        buf.write("\7\3\2\2\u0321\u0323\7?\2\2\u0322\u0324\7R\2\2\u0323\u0322")
        buf.write("\3\2\2\2\u0323\u0324\3\2\2\2\u0324\u0325\3\2\2\2\u0325")
        buf.write("\u0326\5\u009cO\2\u0326\u0327\7\5\2\2\u0327\u032e\3\2")
        buf.write("\2\2\u0328\u032a\5\u009cO\2\u0329\u0328\3\2\2\2\u032a")
        buf.write("\u032b\3\2\2\2\u032b\u0329\3\2\2\2\u032b\u032c\3\2\2\2")
        buf.write("\u032c\u032e\3\2\2\2\u032d\u030f\3\2\2\2\u032d\u0318\3")
        buf.write("\2\2\2\u032d\u0320\3\2\2\2\u032d\u0329\3\2\2\2\u032e\u0091")
        buf.write("\3\2\2\2\u032f\u0330\7\3\2\2\u0330\u0331\7@\2\2\u0331")
        buf.write("\u0332\5\u0094K\2\u0332\u0333\5\u0096L\2\u0333\u0334\7")
        buf.write("\5\2\2\u0334\u0093\3\2\2\2\u0335\u0336\t\b\2\2\u0336\u0095")
        buf.write("\3\2\2\2\u0337\u0344\5J&\2\u0338\u0339\5\u0098M\2\u0339")
        buf.write("\u033a\5\u009aN\2\u033a\u0344\3\2\2\2\u033b\u033c\5\u009a")
        buf.write("N\2\u033c\u033d\5\u0098M\2\u033d\u0344\3\2\2\2\u033e\u0344")
        buf.write("\7C\2\2\u033f\u0340\7\3\2\2\u0340\u0341\7D\2\2\u0341\u0342")
        buf.write("\7R\2\2\u0342\u0344\7\5\2\2\u0343\u0337\3\2\2\2\u0343")
        buf.write("\u0338\3\2\2\2\u0343\u033b\3\2\2\2\u0343\u033e\3\2\2\2")
        buf.write("\u0343\u033f\3\2\2\2\u0344\u0097\3\2\2\2\u0345\u0346\7")
        buf.write("\3\2\2\u0346\u0347\7E\2\2\u0347\u0348\5J&\2\u0348\u0349")
        buf.write("\7\5\2\2\u0349\u0099\3\2\2\2\u034a\u034b\7\3\2\2\u034b")
        buf.write("\u034c\7F\2\2\u034c\u034d\5J&\2\u034d\u034e\7\5\2\2\u034e")
        buf.write("\u009b\3\2\2\2\u034f\u0350\7\3\2\2\u0350\u0352\7\23\2")
        buf.write("\2\u0351\u0353\5\u009cO\2\u0352\u0351\3\2\2\2\u0353\u0354")
        buf.write("\3\2\2\2\u0354\u0352\3\2\2\2\u0354\u0355\3\2\2\2\u0355")
        buf.write("\u0356\3\2\2\2\u0356\u0357\7\5\2\2\u0357\u03a5\3\2\2\2")
        buf.write("\u0358\u0359\7\3\2\2\u0359\u035a\7\30\2\2\u035a\u035b")
        buf.write("\7\3\2\2\u035b\u035c\5\24\13\2\u035c\u035d\7\5\2\2\u035d")
        buf.write("\u035e\5\u009cO\2\u035e\u035f\7\5\2\2\u035f\u03a5\3\2")
        buf.write("\2\2\u0360\u0361\7\3\2\2\u0361\u0362\7G\2\2\u0362\u0363")
        buf.write("\5@!\2\u0363\u0364\7\5\2\2\u0364\u03a5\3\2\2\2\u0365\u0366")
        buf.write("\7\3\2\2\u0366\u0367\7H\2\2\u0367\u0368\5@!\2\u0368\u0369")
        buf.write("\7\5\2\2\u0369\u03a5\3\2\2\2\u036a\u036b\7\3\2\2\u036b")
        buf.write("\u036c\7I\2\2\u036c\u036d\5@!\2\u036d\u036e\7\5\2\2\u036e")
        buf.write("\u03a5\3\2\2\2\u036f\u0370\7\3\2\2\u0370\u0371\7J\2\2")
        buf.write("\u0371\u0372\7U\2\2\u0372\u0373\5@!\2\u0373\u0374\7\5")
        buf.write("\2\2\u0374\u03a5\3\2\2\2\u0375\u0376\7\3\2\2\u0376\u0377")
        buf.write("\7K\2\2\u0377\u0378\5@!\2\u0378\u0379\7\5\2\2\u0379\u03a5")
        buf.write("\3\2\2\2\u037a\u037b\7\3\2\2\u037b\u037c\7L\2\2\u037c")
        buf.write("\u037d\5@!\2\u037d\u037e\5@!\2\u037e\u037f\7\5\2\2\u037f")
        buf.write("\u03a5\3\2\2\2\u0380\u0381\7\3\2\2\u0381\u0382\7M\2\2")
        buf.write("\u0382\u0383\5@!\2\u0383\u0384\5@!\2\u0384\u0385\7\5\2")
        buf.write("\2\u0385\u03a5\3\2\2\2\u0386\u0387\7\3\2\2\u0387\u0388")
        buf.write("\7N\2\2\u0388\u0389\7U\2\2\u0389\u038a\5@!\2\u038a\u038b")
        buf.write("\5@!\2\u038b\u038c\7\5\2\2\u038c\u03a5\3\2\2\2\u038d\u038e")
        buf.write("\7\3\2\2\u038e\u038f\7O\2\2\u038f\u0390\7U\2\2\u0390\u0391")
        buf.write("\7U\2\2\u0391\u0392\5@!\2\u0392\u0393\7\5\2\2\u0393\u03a5")
        buf.write("\3\2\2\2\u0394\u0395\7\3\2\2\u0395\u0396\7P\2\2\u0396")
        buf.write("\u0397\7U\2\2\u0397\u0398\5@!\2\u0398\u0399\7\5\2\2\u0399")
        buf.write("\u03a5\3\2\2\2\u039a\u039b\7\3\2\2\u039b\u039d\7S\2\2")
        buf.write("\u039c\u039e\5\u0084C\2\u039d\u039c\3\2\2\2\u039e\u039f")
        buf.write("\3\2\2\2\u039f\u039d\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0")
        buf.write("\u03a1\3\2\2\2\u03a1\u03a2\7\5\2\2\u03a2\u03a5\3\2\2\2")
        buf.write("\u03a3\u03a5\5@!\2\u03a4\u034f\3\2\2\2\u03a4\u0358\3\2")
        buf.write("\2\2\u03a4\u0360\3\2\2\2\u03a4\u0365\3\2\2\2\u03a4\u036a")
        buf.write("\3\2\2\2\u03a4\u036f\3\2\2\2\u03a4\u0375\3\2\2\2\u03a4")
        buf.write("\u037a\3\2\2\2\u03a4\u0380\3\2\2\2\u03a4\u0386\3\2\2\2")
        buf.write("\u03a4\u038d\3\2\2\2\u03a4\u0394\3\2\2\2\u03a4\u039a\3")
        buf.write("\2\2\2\u03a4\u03a3\3\2\2\2\u03a5\u009d\3\2\2\2E\u00a0")
        buf.write("\u00a6\u00a9\u00ac\u00af\u00b2\u00b7\u00c6\u00d2\u00d6")
        buf.write("\u00db\u00e1\u00e6\u00e9\u00ee\u00f6\u00fc\u0101\u0104")
        buf.write("\u0109\u0113\u0118\u011c\u0123\u012a\u0144\u0155\u0184")
        buf.write("\u018c\u0195\u01b6\u01c9\u01d3\u01da\u01ea\u0200\u0205")
        buf.write("\u0216\u0227\u022e\u0234\u023a\u0241\u024b\u0250\u0268")
        buf.write("\u026f\u0283\u0294\u0297\u029e\u02a6\u02bc\u02d0\u02d8")
        buf.write("\u02df\u02f1\u02f9\u0300\u0314\u0323\u032b\u032d\u0343")
        buf.write("\u0354\u039f\u03a4")
        return buf.getvalue()


class fstripsParser ( Parser ):

    grammarFileName = "fstrips.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "'define'", "')'", "'domain'", 
                     "':requirements'", "':types'", "'-'", "'either'", "':functions'", 
                     "':constants'", "':predicates'", "':action'", "':parameters'", 
                     "':constraint'", "':condition'", "':event'", "'and'", 
                     "'or'", "'not'", "'imply'", "'exists'", "'forall'", 
                     "'='", "'#t'", "':process'", "':derived'", "'*'", "'when'", 
                     "'assign'", "'+'", "'/'", "'^'", "'max'", "'min'", 
                     "'sin'", "'cos'", "'sqrt'", "'tan'", "'acos'", "'asin'", 
                     "'atan'", "'exp'", "'abs'", "'>'", "'<'", "'>='", "'<='", 
                     "'scale-up'", "'scale-down'", "'increase'", "'decrease'", 
                     "'problem'", "':domain'", "':objects'", "':bounds'", 
                     "'['", "'..'", "']'", "':goal'", "':constraints'", 
                     "'preference'", "':metric'", "'minimize'", "'maximize'", 
                     "'(total-time)'", "'is-violated'", "':terminal'", "':stage'", 
                     "'at-end'", "'always'", "'sometime'", "'within'", "'at-most-once'", 
                     "'sometime-after'", "'sometime-before'", "'always-within'", 
                     "'hold-during'", "'hold-after'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':effect'", 
                     "'int'", "'float'", "'object'", "'number'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "REQUIRE_KEY", 
                      "NAME", "EXTNAME", "VARIABLE", "NUMBER", "LINE_COMMENT", 
                      "WHITESPACE", "K_INIT", "K_PRECONDITION", "K_EFFECT", 
                      "INT_T", "FLOAT_T", "OBJECT_T", "NUMBER_T", "DOMAIN", 
                      "DOMAIN_NAME", "REQUIREMENTS", "TYPES", "EITHER_TYPE", 
                      "CONSTANTS", "FUNCTIONS", "FREE_FUNCTIONS", "PREDICATES", 
                      "ACTION", "CONSTRAINT", "EVENT", "GLOBAL_CONSTRAINT", 
                      "DURATIVE_ACTION", "PROBLEM", "PROBLEM_NAME", "PROBLEM_DOMAIN", 
                      "OBJECTS", "INIT", "FUNC_HEAD", "PRECONDITION", "EFFECT", 
                      "AND_GD", "OR_GD", "NOT_GD", "IMPLY_GD", "EXISTS_GD", 
                      "FORALL_GD", "COMPARISON_GD", "AND_EFFECT", "FORALL_EFFECT", 
                      "WHEN_EFFECT", "ASSIGN_EFFECT", "NOT_EFFECT", "PRED_HEAD", 
                      "GOAL", "BINARY_OP", "EQUALITY_CON", "MULTI_OP", "MINUS_OP", 
                      "UNARY_MINUS", "INIT_EQ", "INIT_AT", "NOT_PRED_INIT", 
                      "PRED_INST", "PROBLEM_CONSTRAINT", "PROBLEM_METRIC" ]

    RULE_pddlDoc = 0
    RULE_domain = 1
    RULE_domainName = 2
    RULE_requireDef = 3
    RULE_declaration_of_types = 4
    RULE_numericBuiltinType = 5
    RULE_builtinType = 6
    RULE_possibly_typed_name_list = 7
    RULE_name_list_with_type = 8
    RULE_possibly_typed_variable_list = 9
    RULE_variable_list_with_type = 10
    RULE_typename = 11
    RULE_primitive_type = 12
    RULE_function_definition_block = 13
    RULE_single_function_definition = 14
    RULE_typed_function_definition = 15
    RULE_untyped_function_definition = 16
    RULE_logical_symbol_name = 17
    RULE_constantsDef = 18
    RULE_predicate_definition_block = 19
    RULE_single_predicate_definition = 20
    RULE_predicate = 21
    RULE_structureDef = 22
    RULE_actionDef = 23
    RULE_constraintDef = 24
    RULE_eventDef = 25
    RULE_actionName = 26
    RULE_constraintSymbol = 27
    RULE_eventSymbol = 28
    RULE_actionDefBody = 29
    RULE_precondition = 30
    RULE_goalDesc = 31
    RULE_equality = 32
    RULE_fComp = 33
    RULE_atomicTermFormula = 34
    RULE_term = 35
    RULE_functionTerm = 36
    RULE_processDef = 37
    RULE_processDefBody = 38
    RULE_processEffectList = 39
    RULE_processEffect = 40
    RULE_derivedDef = 41
    RULE_fExp = 42
    RULE_processEffectExp = 43
    RULE_processFunctionEff = 44
    RULE_processConstEff = 45
    RULE_processVarEff = 46
    RULE_fHead = 47
    RULE_effect = 48
    RULE_cEffect = 49
    RULE_atomic_effect = 50
    RULE_binaryOp = 51
    RULE_unaryBuiltIn = 52
    RULE_binaryComp = 53
    RULE_assignOp = 54
    RULE_processEffectOp = 55
    RULE_problem = 56
    RULE_problemMeta = 57
    RULE_problemDecl = 58
    RULE_problemDomain = 59
    RULE_object_declaration = 60
    RULE_boundsDecl = 61
    RULE_typeBoundsDefinition = 62
    RULE_init = 63
    RULE_groundTerm = 64
    RULE_groundFunctionTerm = 65
    RULE_initEl = 66
    RULE_nameLiteral = 67
    RULE_groundAtomicFormula = 68
    RULE_goal = 69
    RULE_probConstraints = 70
    RULE_prefConGD = 71
    RULE_metricSpec = 72
    RULE_optimization = 73
    RULE_metricFExp = 74
    RULE_terminalCost = 75
    RULE_stageCost = 76
    RULE_conGD = 77

    ruleNames =  [ "pddlDoc", "domain", "domainName", "requireDef", "declaration_of_types", 
                   "numericBuiltinType", "builtinType", "possibly_typed_name_list", 
                   "name_list_with_type", "possibly_typed_variable_list", 
                   "variable_list_with_type", "typename", "primitive_type", 
                   "function_definition_block", "single_function_definition", 
                   "typed_function_definition", "untyped_function_definition", 
                   "logical_symbol_name", "constantsDef", "predicate_definition_block", 
                   "single_predicate_definition", "predicate", "structureDef", 
                   "actionDef", "constraintDef", "eventDef", "actionName", 
                   "constraintSymbol", "eventSymbol", "actionDefBody", "precondition", 
                   "goalDesc", "equality", "fComp", "atomicTermFormula", 
                   "term", "functionTerm", "processDef", "processDefBody", 
                   "processEffectList", "processEffect", "derivedDef", "fExp", 
                   "processEffectExp", "processFunctionEff", "processConstEff", 
                   "processVarEff", "fHead", "effect", "cEffect", "atomic_effect", 
                   "binaryOp", "unaryBuiltIn", "binaryComp", "assignOp", 
                   "processEffectOp", "problem", "problemMeta", "problemDecl", 
                   "problemDomain", "object_declaration", "boundsDecl", 
                   "typeBoundsDefinition", "init", "groundTerm", "groundFunctionTerm", 
                   "initEl", "nameLiteral", "groundAtomicFormula", "goal", 
                   "probConstraints", "prefConGD", "metricSpec", "optimization", 
                   "metricFExp", "terminalCost", "stageCost", "conGD" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    REQUIRE_KEY=79
    NAME=80
    EXTNAME=81
    VARIABLE=82
    NUMBER=83
    LINE_COMMENT=84
    WHITESPACE=85
    K_INIT=86
    K_PRECONDITION=87
    K_EFFECT=88
    INT_T=89
    FLOAT_T=90
    OBJECT_T=91
    NUMBER_T=92
    DOMAIN=93
    DOMAIN_NAME=94
    REQUIREMENTS=95
    TYPES=96
    EITHER_TYPE=97
    CONSTANTS=98
    FUNCTIONS=99
    FREE_FUNCTIONS=100
    PREDICATES=101
    ACTION=102
    CONSTRAINT=103
    EVENT=104
    GLOBAL_CONSTRAINT=105
    DURATIVE_ACTION=106
    PROBLEM=107
    PROBLEM_NAME=108
    PROBLEM_DOMAIN=109
    OBJECTS=110
    INIT=111
    FUNC_HEAD=112
    PRECONDITION=113
    EFFECT=114
    AND_GD=115
    OR_GD=116
    NOT_GD=117
    IMPLY_GD=118
    EXISTS_GD=119
    FORALL_GD=120
    COMPARISON_GD=121
    AND_EFFECT=122
    FORALL_EFFECT=123
    WHEN_EFFECT=124
    ASSIGN_EFFECT=125
    NOT_EFFECT=126
    PRED_HEAD=127
    GOAL=128
    BINARY_OP=129
    EQUALITY_CON=130
    MULTI_OP=131
    MINUS_OP=132
    UNARY_MINUS=133
    INIT_EQ=134
    INIT_AT=135
    NOT_PRED_INIT=136
    PRED_INST=137
    PROBLEM_CONSTRAINT=138
    PROBLEM_METRIC=139

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class PddlDocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(fstripsParser.DomainContext,0)


        def problem(self):
            return self.getTypedRuleContext(fstripsParser.ProblemContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_pddlDoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPddlDoc" ):
                listener.enterPddlDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPddlDoc" ):
                listener.exitPddlDoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPddlDoc" ):
                return visitor.visitPddlDoc(self)
            else:
                return visitor.visitChildren(self)




    def pddlDoc(self):

        localctx = fstripsParser.PddlDocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pddlDoc)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.domain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.problem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DomainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domainName(self):
            return self.getTypedRuleContext(fstripsParser.DomainNameContext,0)


        def requireDef(self):
            return self.getTypedRuleContext(fstripsParser.RequireDefContext,0)


        def declaration_of_types(self):
            return self.getTypedRuleContext(fstripsParser.Declaration_of_typesContext,0)


        def constantsDef(self):
            return self.getTypedRuleContext(fstripsParser.ConstantsDefContext,0)


        def predicate_definition_block(self):
            return self.getTypedRuleContext(fstripsParser.Predicate_definition_blockContext,0)


        def function_definition_block(self):
            return self.getTypedRuleContext(fstripsParser.Function_definition_blockContext,0)


        def structureDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.StructureDefContext)
            else:
                return self.getTypedRuleContext(fstripsParser.StructureDefContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomain" ):
                return visitor.visitDomain(self)
            else:
                return visitor.visitChildren(self)




    def domain(self):

        localctx = fstripsParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(fstripsParser.T__0)
            self.state = 161
            self.match(fstripsParser.T__1)
            self.state = 162
            self.domainName()
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 163
                self.requireDef()


            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 166
                self.declaration_of_types()


            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 169
                self.constantsDef()


            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 172
                self.predicate_definition_block()


            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 175
                self.function_definition_block()


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 178
                self.structureDef()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DomainNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_domainName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomainName" ):
                listener.enterDomainName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomainName" ):
                listener.exitDomainName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomainName" ):
                return visitor.visitDomainName(self)
            else:
                return visitor.visitChildren(self)




    def domainName(self):

        localctx = fstripsParser.DomainNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_domainName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(fstripsParser.T__0)
            self.state = 187
            self.match(fstripsParser.T__3)
            self.state = 188
            self.match(fstripsParser.NAME)
            self.state = 189
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RequireDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIRE_KEY(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.REQUIRE_KEY)
            else:
                return self.getToken(fstripsParser.REQUIRE_KEY, i)

        def getRuleIndex(self):
            return fstripsParser.RULE_requireDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireDef" ):
                listener.enterRequireDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireDef" ):
                listener.exitRequireDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequireDef" ):
                return visitor.visitRequireDef(self)
            else:
                return visitor.visitChildren(self)




    def requireDef(self):

        localctx = fstripsParser.RequireDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_requireDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(fstripsParser.T__0)
            self.state = 192
            self.match(fstripsParser.T__4)
            self.state = 194 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 193
                self.match(fstripsParser.REQUIRE_KEY)
                self.state = 196 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.REQUIRE_KEY):
                    break

            self.state = 198
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_of_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possibly_typed_name_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_name_listContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_declaration_of_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_of_types" ):
                listener.enterDeclaration_of_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_of_types" ):
                listener.exitDeclaration_of_types(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_of_types" ):
                return visitor.visitDeclaration_of_types(self)
            else:
                return visitor.visitChildren(self)




    def declaration_of_types(self):

        localctx = fstripsParser.Declaration_of_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration_of_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(fstripsParser.T__0)
            self.state = 201
            self.match(fstripsParser.T__5)
            self.state = 202
            self.possibly_typed_name_list()
            self.state = 203
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericBuiltinTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_numericBuiltinType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(NumericBuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NumericBuiltinTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_T(self):
            return self.getToken(fstripsParser.INT_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(NumericBuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NumericBuiltinTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_T(self):
            return self.getToken(fstripsParser.FLOAT_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(NumericBuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NumericBuiltinTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_T(self):
            return self.getToken(fstripsParser.NUMBER_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)



    def numericBuiltinType(self):

        localctx = fstripsParser.NumericBuiltinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numericBuiltinType)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.INT_T]:
                localctx = fstripsParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(fstripsParser.INT_T)
                pass
            elif token in [fstripsParser.FLOAT_T]:
                localctx = fstripsParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(fstripsParser.FLOAT_T)
                pass
            elif token in [fstripsParser.NUMBER_T]:
                localctx = fstripsParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(fstripsParser.NUMBER_T)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BuiltinTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_builtinType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ObjectBuiltinContext(BuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.BuiltinTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_T(self):
            return self.getToken(fstripsParser.OBJECT_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectBuiltin" ):
                listener.enterObjectBuiltin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectBuiltin" ):
                listener.exitObjectBuiltin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectBuiltin" ):
                return visitor.visitObjectBuiltin(self)
            else:
                return visitor.visitChildren(self)


    class NumericBuiltinContext(BuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.BuiltinTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numericBuiltinType(self):
            return self.getTypedRuleContext(fstripsParser.NumericBuiltinTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericBuiltin" ):
                listener.enterNumericBuiltin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericBuiltin" ):
                listener.exitNumericBuiltin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericBuiltin" ):
                return visitor.visitNumericBuiltin(self)
            else:
                return visitor.visitChildren(self)



    def builtinType(self):

        localctx = fstripsParser.BuiltinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_builtinType)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.NUMBER_T]:
                localctx = fstripsParser.NumericBuiltinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.numericBuiltinType()
                pass
            elif token in [fstripsParser.OBJECT_T]:
                localctx = fstripsParser.ObjectBuiltinContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(fstripsParser.OBJECT_T)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Possibly_typed_name_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_possibly_typed_name_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleNameListContext(Possibly_typed_name_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_name_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NAME)
            else:
                return self.getToken(fstripsParser.NAME, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleNameList" ):
                listener.enterSimpleNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleNameList" ):
                listener.exitSimpleNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleNameList" ):
                return visitor.visitSimpleNameList(self)
            else:
                return visitor.visitChildren(self)


    class ComplexNameListContext(Possibly_typed_name_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_name_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def name_list_with_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Name_list_with_typeContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Name_list_with_typeContext,i)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NAME)
            else:
                return self.getToken(fstripsParser.NAME, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexNameList" ):
                listener.enterComplexNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexNameList" ):
                listener.exitComplexNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexNameList" ):
                return visitor.visitComplexNameList(self)
            else:
                return visitor.visitChildren(self)



    def possibly_typed_name_list(self):

        localctx = fstripsParser.Possibly_typed_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_possibly_typed_name_list)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.SimpleNameListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.NAME:
                    self.state = 214
                    self.match(fstripsParser.NAME)
                    self.state = 219
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = fstripsParser.ComplexNameListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 221 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 220
                        self.name_list_with_type()

                    else:
                        raise NoViableAltException(self)
                    self.state = 223 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.NAME:
                    self.state = 225
                    self.match(fstripsParser.NAME)
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Name_list_with_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(fstripsParser.TypenameContext,0)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NAME)
            else:
                return self.getToken(fstripsParser.NAME, i)

        def getRuleIndex(self):
            return fstripsParser.RULE_name_list_with_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_list_with_type" ):
                listener.enterName_list_with_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_list_with_type" ):
                listener.exitName_list_with_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_list_with_type" ):
                return visitor.visitName_list_with_type(self)
            else:
                return visitor.visitChildren(self)




    def name_list_with_type(self):

        localctx = fstripsParser.Name_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_name_list_with_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 233
                self.match(fstripsParser.NAME)
                self.state = 236 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.NAME):
                    break

            self.state = 238
            self.match(fstripsParser.T__6)
            self.state = 239
            self.typename()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Possibly_typed_variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_possibly_typed_variable_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UntypedVariableListContext(Possibly_typed_variable_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_variable_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.VARIABLE)
            else:
                return self.getToken(fstripsParser.VARIABLE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntypedVariableList" ):
                listener.enterUntypedVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntypedVariableList" ):
                listener.exitUntypedVariableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntypedVariableList" ):
                return visitor.visitUntypedVariableList(self)
            else:
                return visitor.visitChildren(self)


    class TypedVariableListContext(Possibly_typed_variable_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_variable_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable_list_with_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Variable_list_with_typeContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Variable_list_with_typeContext,i)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.VARIABLE)
            else:
                return self.getToken(fstripsParser.VARIABLE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedVariableList" ):
                listener.enterTypedVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedVariableList" ):
                listener.exitTypedVariableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedVariableList" ):
                return visitor.visitTypedVariableList(self)
            else:
                return visitor.visitChildren(self)



    def possibly_typed_variable_list(self):

        localctx = fstripsParser.Possibly_typed_variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_possibly_typed_variable_list)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.UntypedVariableListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.VARIABLE:
                    self.state = 241
                    self.match(fstripsParser.VARIABLE)
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = fstripsParser.TypedVariableListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 248 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 247
                        self.variable_list_with_type()

                    else:
                        raise NoViableAltException(self)
                    self.state = 250 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.VARIABLE:
                    self.state = 252
                    self.match(fstripsParser.VARIABLE)
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_list_with_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(fstripsParser.Primitive_typeContext,0)


        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.VARIABLE)
            else:
                return self.getToken(fstripsParser.VARIABLE, i)

        def getRuleIndex(self):
            return fstripsParser.RULE_variable_list_with_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_list_with_type" ):
                listener.enterVariable_list_with_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_list_with_type" ):
                listener.exitVariable_list_with_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list_with_type" ):
                return visitor.visitVariable_list_with_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_list_with_type(self):

        localctx = fstripsParser.Variable_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_list_with_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 260
                self.match(fstripsParser.VARIABLE)
                self.state = 263 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.VARIABLE):
                    break

            self.state = 265
            self.match(fstripsParser.T__6)
            self.state = 266
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Primitive_typeContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Primitive_typeContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_typename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypename" ):
                listener.enterTypename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypename" ):
                listener.exitTypename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypename" ):
                return visitor.visitTypename(self)
            else:
                return visitor.visitChildren(self)




    def typename(self):

        localctx = fstripsParser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typename)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(fstripsParser.T__0)
                self.state = 269
                self.match(fstripsParser.T__7)
                self.state = 271 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 270
                    self.primitive_type()
                    self.state = 273 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.INT_T - 80)) | (1 << (fstripsParser.FLOAT_T - 80)) | (1 << (fstripsParser.OBJECT_T - 80)) | (1 << (fstripsParser.NUMBER_T - 80)))) != 0)):
                        break

                self.state = 275
                self.match(fstripsParser.T__2)
                pass
            elif token in [fstripsParser.NAME, fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.OBJECT_T, fstripsParser.NUMBER_T]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.primitive_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def builtinType(self):
            return self.getTypedRuleContext(fstripsParser.BuiltinTypeContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_primitive_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_type" ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_type" ):
                listener.exitPrimitive_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = fstripsParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primitive_type)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(fstripsParser.NAME)
                pass
            elif token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.OBJECT_T, fstripsParser.NUMBER_T]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.builtinType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_definition_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_function_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Single_function_definitionContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Single_function_definitionContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_function_definition_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition_block" ):
                listener.enterFunction_definition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition_block" ):
                listener.exitFunction_definition_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition_block" ):
                return visitor.visitFunction_definition_block(self)
            else:
                return visitor.visitChildren(self)




    def function_definition_block(self):

        localctx = fstripsParser.Function_definition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_definition_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(fstripsParser.T__0)
            self.state = 285
            self.match(fstripsParser.T__8)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 286
                self.single_function_definition()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 292
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_function_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typed_function_definition(self):
            return self.getTypedRuleContext(fstripsParser.Typed_function_definitionContext,0)


        def untyped_function_definition(self):
            return self.getTypedRuleContext(fstripsParser.Untyped_function_definitionContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_single_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_function_definition" ):
                listener.enterSingle_function_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_function_definition" ):
                listener.exitSingle_function_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_function_definition" ):
                return visitor.visitSingle_function_definition(self)
            else:
                return visitor.visitChildren(self)




    def single_function_definition(self):

        localctx = fstripsParser.Single_function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_single_function_definition)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.typed_function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.untyped_function_definition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_function_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_symbol_name(self):
            return self.getTypedRuleContext(fstripsParser.Logical_symbol_nameContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(fstripsParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_typed_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyped_function_definition" ):
                listener.enterTyped_function_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyped_function_definition" ):
                listener.exitTyped_function_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyped_function_definition" ):
                return visitor.visitTyped_function_definition(self)
            else:
                return visitor.visitChildren(self)




    def typed_function_definition(self):

        localctx = fstripsParser.Typed_function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typed_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(fstripsParser.T__0)
            self.state = 299
            self.logical_symbol_name()
            self.state = 300
            self.possibly_typed_variable_list()
            self.state = 301
            self.match(fstripsParser.T__2)
            self.state = 302
            self.match(fstripsParser.T__6)
            self.state = 303
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Untyped_function_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_symbol_name(self):
            return self.getTypedRuleContext(fstripsParser.Logical_symbol_nameContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_untyped_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntyped_function_definition" ):
                listener.enterUntyped_function_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntyped_function_definition" ):
                listener.exitUntyped_function_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntyped_function_definition" ):
                return visitor.visitUntyped_function_definition(self)
            else:
                return visitor.visitChildren(self)




    def untyped_function_definition(self):

        localctx = fstripsParser.Untyped_function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_untyped_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(fstripsParser.T__0)
            self.state = 306
            self.logical_symbol_name()
            self.state = 307
            self.possibly_typed_variable_list()
            self.state = 308
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Logical_symbol_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def EXTNAME(self):
            return self.getToken(fstripsParser.EXTNAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_logical_symbol_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_symbol_name" ):
                listener.enterLogical_symbol_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_symbol_name" ):
                listener.exitLogical_symbol_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_symbol_name" ):
                return visitor.visitLogical_symbol_name(self)
            else:
                return visitor.visitChildren(self)




    def logical_symbol_name(self):

        localctx = fstripsParser.Logical_symbol_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logical_symbol_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            _la = self._input.LA(1)
            if not(_la==fstripsParser.NAME or _la==fstripsParser.EXTNAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantsDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possibly_typed_name_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_name_listContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_constantsDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantsDef" ):
                listener.enterConstantsDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantsDef" ):
                listener.exitConstantsDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantsDef" ):
                return visitor.visitConstantsDef(self)
            else:
                return visitor.visitChildren(self)




    def constantsDef(self):

        localctx = fstripsParser.ConstantsDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constantsDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(fstripsParser.T__0)
            self.state = 313
            self.match(fstripsParser.T__9)
            self.state = 314
            self.possibly_typed_name_list()
            self.state = 315
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Predicate_definition_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_predicate_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Single_predicate_definitionContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Single_predicate_definitionContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_predicate_definition_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate_definition_block" ):
                listener.enterPredicate_definition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate_definition_block" ):
                listener.exitPredicate_definition_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_definition_block" ):
                return visitor.visitPredicate_definition_block(self)
            else:
                return visitor.visitChildren(self)




    def predicate_definition_block(self):

        localctx = fstripsParser.Predicate_definition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_predicate_definition_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(fstripsParser.T__0)
            self.state = 318
            self.match(fstripsParser.T__10)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 319
                self.single_predicate_definition()
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 325
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_predicate_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(fstripsParser.PredicateContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_single_predicate_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_predicate_definition" ):
                listener.enterSingle_predicate_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_predicate_definition" ):
                listener.exitSingle_predicate_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_predicate_definition" ):
                return visitor.visitSingle_predicate_definition(self)
            else:
                return visitor.visitChildren(self)




    def single_predicate_definition(self):

        localctx = fstripsParser.Single_predicate_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_single_predicate_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(fstripsParser.T__0)
            self.state = 328
            self.predicate()
            self.state = 329
            self.possibly_typed_variable_list()
            self.state = 330
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = fstripsParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(fstripsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructureDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionDef(self):
            return self.getTypedRuleContext(fstripsParser.ActionDefContext,0)


        def eventDef(self):
            return self.getTypedRuleContext(fstripsParser.EventDefContext,0)


        def derivedDef(self):
            return self.getTypedRuleContext(fstripsParser.DerivedDefContext,0)


        def constraintDef(self):
            return self.getTypedRuleContext(fstripsParser.ConstraintDefContext,0)


        def processDef(self):
            return self.getTypedRuleContext(fstripsParser.ProcessDefContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_structureDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructureDef" ):
                listener.enterStructureDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructureDef" ):
                listener.exitStructureDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructureDef" ):
                return visitor.visitStructureDef(self)
            else:
                return visitor.visitChildren(self)




    def structureDef(self):

        localctx = fstripsParser.StructureDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_structureDef)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.actionDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.eventDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.derivedDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.constraintDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.processDef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionName(self):
            return self.getTypedRuleContext(fstripsParser.ActionNameContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def actionDefBody(self):
            return self.getTypedRuleContext(fstripsParser.ActionDefBodyContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_actionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionDef" ):
                listener.enterActionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionDef" ):
                listener.exitActionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionDef" ):
                return visitor.visitActionDef(self)
            else:
                return visitor.visitChildren(self)




    def actionDef(self):

        localctx = fstripsParser.ActionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_actionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(fstripsParser.T__0)
            self.state = 342
            self.match(fstripsParser.T__11)
            self.state = 343
            self.actionName()
            self.state = 344
            self.match(fstripsParser.T__12)
            self.state = 345
            self.match(fstripsParser.T__0)
            self.state = 346
            self.possibly_typed_variable_list()
            self.state = 347
            self.match(fstripsParser.T__2)
            self.state = 348
            self.actionDefBody()
            self.state = 349
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstraintDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraintSymbol(self):
            return self.getTypedRuleContext(fstripsParser.ConstraintSymbolContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_constraintDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintDef" ):
                listener.enterConstraintDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintDef" ):
                listener.exitConstraintDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraintDef" ):
                return visitor.visitConstraintDef(self)
            else:
                return visitor.visitChildren(self)




    def constraintDef(self):

        localctx = fstripsParser.ConstraintDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_constraintDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(fstripsParser.T__0)
            self.state = 352
            self.match(fstripsParser.T__13)
            self.state = 353
            self.constraintSymbol()
            self.state = 354
            self.match(fstripsParser.T__12)
            self.state = 355
            self.match(fstripsParser.T__0)
            self.state = 356
            self.possibly_typed_variable_list()
            self.state = 357
            self.match(fstripsParser.T__2)
            self.state = 358
            self.match(fstripsParser.T__14)
            self.state = 359
            self.goalDesc()
            self.state = 360
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eventSymbol(self):
            return self.getTypedRuleContext(fstripsParser.EventSymbolContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def actionDefBody(self):
            return self.getTypedRuleContext(fstripsParser.ActionDefBodyContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_eventDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventDef" ):
                listener.enterEventDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventDef" ):
                listener.exitEventDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventDef" ):
                return visitor.visitEventDef(self)
            else:
                return visitor.visitChildren(self)




    def eventDef(self):

        localctx = fstripsParser.EventDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_eventDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(fstripsParser.T__0)
            self.state = 363
            self.match(fstripsParser.T__15)
            self.state = 364
            self.eventSymbol()
            self.state = 365
            self.match(fstripsParser.T__12)
            self.state = 366
            self.match(fstripsParser.T__0)
            self.state = 367
            self.possibly_typed_variable_list()
            self.state = 368
            self.match(fstripsParser.T__2)
            self.state = 369
            self.actionDefBody()
            self.state = 370
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def EXTNAME(self):
            return self.getToken(fstripsParser.EXTNAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_actionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionName" ):
                listener.enterActionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionName" ):
                listener.exitActionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionName" ):
                return visitor.visitActionName(self)
            else:
                return visitor.visitChildren(self)




    def actionName(self):

        localctx = fstripsParser.ActionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_actionName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            _la = self._input.LA(1)
            if not(_la==fstripsParser.NAME or _la==fstripsParser.EXTNAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstraintSymbolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_constraintSymbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintSymbol" ):
                listener.enterConstraintSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintSymbol" ):
                listener.exitConstraintSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraintSymbol" ):
                return visitor.visitConstraintSymbol(self)
            else:
                return visitor.visitChildren(self)




    def constraintSymbol(self):

        localctx = fstripsParser.ConstraintSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_constraintSymbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(fstripsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventSymbolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def EXTNAME(self):
            return self.getToken(fstripsParser.EXTNAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_eventSymbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventSymbol" ):
                listener.enterEventSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventSymbol" ):
                listener.exitEventSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventSymbol" ):
                return visitor.visitEventSymbol(self)
            else:
                return visitor.visitChildren(self)




    def eventSymbol(self):

        localctx = fstripsParser.EventSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_eventSymbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if not(_la==fstripsParser.NAME or _la==fstripsParser.EXTNAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionDefBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_PRECONDITION(self):
            return self.getToken(fstripsParser.K_PRECONDITION, 0)

        def precondition(self):
            return self.getTypedRuleContext(fstripsParser.PreconditionContext,0)


        def K_EFFECT(self):
            return self.getToken(fstripsParser.K_EFFECT, 0)

        def effect(self):
            return self.getTypedRuleContext(fstripsParser.EffectContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_actionDefBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionDefBody" ):
                listener.enterActionDefBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionDefBody" ):
                listener.exitActionDefBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionDefBody" ):
                return visitor.visitActionDefBody(self)
            else:
                return visitor.visitChildren(self)




    def actionDefBody(self):

        localctx = fstripsParser.ActionDefBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_actionDefBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(fstripsParser.K_PRECONDITION)
            self.state = 379
            self.precondition()
            self.state = 380
            self.match(fstripsParser.K_EFFECT)
            self.state = 381
            self.effect()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreconditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_precondition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RegularPreconditionContext(PreconditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PreconditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegularPrecondition" ):
                listener.enterRegularPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegularPrecondition" ):
                listener.exitRegularPrecondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegularPrecondition" ):
                return visitor.visitRegularPrecondition(self)
            else:
                return visitor.visitChildren(self)


    class TrivialPreconditionContext(PreconditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PreconditionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrivialPrecondition" ):
                listener.enterTrivialPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrivialPrecondition" ):
                listener.exitTrivialPrecondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrivialPrecondition" ):
                return visitor.visitTrivialPrecondition(self)
            else:
                return visitor.visitChildren(self)



    def precondition(self):

        localctx = fstripsParser.PreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_precondition)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.TrivialPreconditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.match(fstripsParser.T__0)
                self.state = 384
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.RegularPreconditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.goalDesc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GoalDescContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_goalDesc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AndGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndGoalDesc" ):
                listener.enterAndGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndGoalDesc" ):
                listener.exitAndGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndGoalDesc" ):
                return visitor.visitAndGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class OrGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrGoalDesc" ):
                listener.enterOrGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrGoalDesc" ):
                listener.exitOrGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrGoalDesc" ):
                return visitor.visitOrGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class EqualityGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def equality(self):
            return self.getTypedRuleContext(fstripsParser.EqualityContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityGoalDesc" ):
                listener.enterEqualityGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityGoalDesc" ):
                listener.exitEqualityGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityGoalDesc" ):
                return visitor.visitEqualityGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class UniversalGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniversalGoalDesc" ):
                listener.enterUniversalGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniversalGoalDesc" ):
                listener.exitUniversalGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniversalGoalDesc" ):
                return visitor.visitUniversalGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fComp(self):
            return self.getTypedRuleContext(fstripsParser.FCompContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonGoalDesc" ):
                listener.enterComparisonGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonGoalDesc" ):
                listener.exitComparisonGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonGoalDesc" ):
                return visitor.visitComparisonGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class TermGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicTermFormula(self):
            return self.getTypedRuleContext(fstripsParser.AtomicTermFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermGoalDesc" ):
                listener.enterTermGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermGoalDesc" ):
                listener.exitTermGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermGoalDesc" ):
                return visitor.visitTermGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class ExistentialGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExistentialGoalDesc" ):
                listener.enterExistentialGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExistentialGoalDesc" ):
                listener.exitExistentialGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExistentialGoalDesc" ):
                return visitor.visitExistentialGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class NotGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotGoalDesc" ):
                listener.enterNotGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotGoalDesc" ):
                listener.exitNotGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotGoalDesc" ):
                return visitor.visitNotGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class ImplyGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplyGoalDesc" ):
                listener.enterImplyGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplyGoalDesc" ):
                listener.exitImplyGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplyGoalDesc" ):
                return visitor.visitImplyGoalDesc(self)
            else:
                return visitor.visitChildren(self)



    def goalDesc(self):

        localctx = fstripsParser.GoalDescContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_goalDesc)
        self._la = 0 # Token type
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.TermGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.atomicTermFormula()
                pass

            elif la_ == 2:
                localctx = fstripsParser.AndGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(fstripsParser.T__0)
                self.state = 390
                self.match(fstripsParser.T__16)
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 391
                    self.goalDesc()
                    self.state = 396
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 397
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.OrGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.match(fstripsParser.T__0)
                self.state = 399
                self.match(fstripsParser.T__17)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 400
                    self.goalDesc()
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 406
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.NotGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.match(fstripsParser.T__0)
                self.state = 408
                self.match(fstripsParser.T__18)
                self.state = 409
                self.goalDesc()
                self.state = 410
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 5:
                localctx = fstripsParser.ImplyGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 412
                self.match(fstripsParser.T__0)
                self.state = 413
                self.match(fstripsParser.T__19)
                self.state = 414
                self.goalDesc()
                self.state = 415
                self.goalDesc()
                self.state = 416
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 6:
                localctx = fstripsParser.ExistentialGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 418
                self.match(fstripsParser.T__0)
                self.state = 419
                self.match(fstripsParser.T__20)
                self.state = 420
                self.match(fstripsParser.T__0)
                self.state = 421
                self.possibly_typed_variable_list()
                self.state = 422
                self.match(fstripsParser.T__2)
                self.state = 423
                self.goalDesc()
                self.state = 424
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 7:
                localctx = fstripsParser.UniversalGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 426
                self.match(fstripsParser.T__0)
                self.state = 427
                self.match(fstripsParser.T__21)
                self.state = 428
                self.match(fstripsParser.T__0)
                self.state = 429
                self.possibly_typed_variable_list()
                self.state = 430
                self.match(fstripsParser.T__2)
                self.state = 431
                self.goalDesc()
                self.state = 432
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 8:
                localctx = fstripsParser.ComparisonGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 434
                self.fComp()
                pass

            elif la_ == 9:
                localctx = fstripsParser.EqualityGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 435
                self.equality()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EqualityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = fstripsParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(fstripsParser.T__0)
            self.state = 439
            self.match(fstripsParser.T__22)
            self.state = 440
            self.term()
            self.state = 441
            self.term()
            self.state = 442
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FCompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binaryComp(self):
            return self.getTypedRuleContext(fstripsParser.BinaryCompContext,0)


        def fExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.FExpContext)
            else:
                return self.getTypedRuleContext(fstripsParser.FExpContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_fComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFComp" ):
                listener.enterFComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFComp" ):
                listener.exitFComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFComp" ):
                return visitor.visitFComp(self)
            else:
                return visitor.visitChildren(self)




    def fComp(self):

        localctx = fstripsParser.FCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_fComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(fstripsParser.T__0)
            self.state = 445
            self.binaryComp()
            self.state = 446
            self.fExp()
            self.state = 447
            self.fExp()
            self.state = 448
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomicTermFormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(fstripsParser.PredicateContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_atomicTermFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicTermFormula" ):
                listener.enterAtomicTermFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicTermFormula" ):
                listener.exitAtomicTermFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicTermFormula" ):
                return visitor.visitAtomicTermFormula(self)
            else:
                return visitor.visitChildren(self)




    def atomicTermFormula(self):

        localctx = fstripsParser.AtomicTermFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_atomicTermFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(fstripsParser.T__0)
            self.state = 451
            self.predicate()
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.T__23 or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.VARIABLE - 80)) | (1 << (fstripsParser.NUMBER - 80)))) != 0):
                self.state = 452
                self.term()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 458
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermObjectContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermObject" ):
                listener.enterTermObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermObject" ):
                listener.exitTermObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermObject" ):
                return visitor.visitTermObject(self)
            else:
                return visitor.visitChildren(self)


    class TermTimeStepContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermTimeStep" ):
                listener.enterTermTimeStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermTimeStep" ):
                listener.exitTermTimeStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermTimeStep" ):
                return visitor.visitTermTimeStep(self)
            else:
                return visitor.visitChildren(self)


    class TermFunctionContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermFunction" ):
                listener.enterTermFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermFunction" ):
                listener.exitTermFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermFunction" ):
                return visitor.visitTermFunction(self)
            else:
                return visitor.visitChildren(self)


    class TermVariableContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(fstripsParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermVariable" ):
                listener.enterTermVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermVariable" ):
                listener.exitTermVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermVariable" ):
                return visitor.visitTermVariable(self)
            else:
                return visitor.visitChildren(self)


    class TermNumberContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermNumber" ):
                listener.enterTermNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermNumber" ):
                listener.exitTermNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermNumber" ):
                return visitor.visitTermNumber(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = fstripsParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_term)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                localctx = fstripsParser.TermObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(fstripsParser.NAME)
                pass
            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.TermNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(fstripsParser.NUMBER)
                pass
            elif token in [fstripsParser.VARIABLE]:
                localctx = fstripsParser.TermVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.match(fstripsParser.VARIABLE)
                pass
            elif token in [fstripsParser.T__23]:
                localctx = fstripsParser.TermTimeStepContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 463
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__0]:
                localctx = fstripsParser.TermFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 464
                self.functionTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_functionTerm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnaryArithmeticFunctionTermContext(FunctionTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FunctionTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryBuiltIn(self):
            return self.getTypedRuleContext(fstripsParser.UnaryBuiltInContext,0)

        def term(self):
            return self.getTypedRuleContext(fstripsParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryArithmeticFunctionTerm" ):
                listener.enterUnaryArithmeticFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryArithmeticFunctionTerm" ):
                listener.exitUnaryArithmeticFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryArithmeticFunctionTerm" ):
                return visitor.visitUnaryArithmeticFunctionTerm(self)
            else:
                return visitor.visitChildren(self)


    class BinaryArithmeticFunctionTermContext(FunctionTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FunctionTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def binaryOp(self):
            return self.getTypedRuleContext(fstripsParser.BinaryOpContext,0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryArithmeticFunctionTerm" ):
                listener.enterBinaryArithmeticFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryArithmeticFunctionTerm" ):
                listener.exitBinaryArithmeticFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryArithmeticFunctionTerm" ):
                return visitor.visitBinaryArithmeticFunctionTerm(self)
            else:
                return visitor.visitChildren(self)


    class GenericFunctionTermContext(FunctionTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FunctionTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logical_symbol_name(self):
            return self.getTypedRuleContext(fstripsParser.Logical_symbol_nameContext,0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericFunctionTerm" ):
                listener.enterGenericFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericFunctionTerm" ):
                listener.exitGenericFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericFunctionTerm" ):
                return visitor.visitGenericFunctionTerm(self)
            else:
                return visitor.visitChildren(self)



    def functionTerm(self):

        localctx = fstripsParser.FunctionTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_functionTerm)
        self._la = 0 # Token type
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.GenericFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(fstripsParser.T__0)
                self.state = 468
                self.logical_symbol_name()
                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0 or _la==fstripsParser.T__23 or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.VARIABLE - 80)) | (1 << (fstripsParser.NUMBER - 80)))) != 0):
                    self.state = 469
                    self.term()
                    self.state = 474
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 475
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.BinaryArithmeticFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.match(fstripsParser.T__0)
                self.state = 478
                self.binaryOp()
                self.state = 479
                self.term()
                self.state = 480
                self.term()
                self.state = 481
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.UnaryArithmeticFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(fstripsParser.T__0)
                self.state = 484
                self.unaryBuiltIn()
                self.state = 485
                self.term()
                self.state = 486
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionName(self):
            return self.getTypedRuleContext(fstripsParser.ActionNameContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def processDefBody(self):
            return self.getTypedRuleContext(fstripsParser.ProcessDefBodyContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_processDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessDef" ):
                listener.enterProcessDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessDef" ):
                listener.exitProcessDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessDef" ):
                return visitor.visitProcessDef(self)
            else:
                return visitor.visitChildren(self)




    def processDef(self):

        localctx = fstripsParser.ProcessDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_processDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(fstripsParser.T__0)
            self.state = 491
            self.match(fstripsParser.T__24)
            self.state = 492
            self.actionName()
            self.state = 493
            self.match(fstripsParser.T__12)
            self.state = 494
            self.match(fstripsParser.T__0)
            self.state = 495
            self.possibly_typed_variable_list()
            self.state = 496
            self.match(fstripsParser.T__2)
            self.state = 497
            self.processDefBody()
            self.state = 498
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessDefBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_PRECONDITION(self):
            return self.getToken(fstripsParser.K_PRECONDITION, 0)

        def precondition(self):
            return self.getTypedRuleContext(fstripsParser.PreconditionContext,0)


        def K_EFFECT(self):
            return self.getToken(fstripsParser.K_EFFECT, 0)

        def processEffectList(self):
            return self.getTypedRuleContext(fstripsParser.ProcessEffectListContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_processDefBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessDefBody" ):
                listener.enterProcessDefBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessDefBody" ):
                listener.exitProcessDefBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessDefBody" ):
                return visitor.visitProcessDefBody(self)
            else:
                return visitor.visitChildren(self)




    def processDefBody(self):

        localctx = fstripsParser.ProcessDefBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_processDefBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(fstripsParser.K_PRECONDITION)
            self.state = 501
            self.precondition()
            self.state = 502
            self.match(fstripsParser.K_EFFECT)
            self.state = 503
            self.processEffectList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessEffectListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_processEffectList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProcessSingleEffectContext(ProcessEffectListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processEffect(self):
            return self.getTypedRuleContext(fstripsParser.ProcessEffectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessSingleEffect" ):
                listener.enterProcessSingleEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessSingleEffect" ):
                listener.exitProcessSingleEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessSingleEffect" ):
                return visitor.visitProcessSingleEffect(self)
            else:
                return visitor.visitChildren(self)


    class ProcessConjunctiveEffectFormulaContext(ProcessEffectListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processEffect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.ProcessEffectContext)
            else:
                return self.getTypedRuleContext(fstripsParser.ProcessEffectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessConjunctiveEffectFormula" ):
                listener.enterProcessConjunctiveEffectFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessConjunctiveEffectFormula" ):
                listener.exitProcessConjunctiveEffectFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessConjunctiveEffectFormula" ):
                return visitor.visitProcessConjunctiveEffectFormula(self)
            else:
                return visitor.visitChildren(self)



    def processEffectList(self):

        localctx = fstripsParser.ProcessEffectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_processEffectList)
        self._la = 0 # Token type
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ProcessConjunctiveEffectFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(fstripsParser.T__0)
                self.state = 506
                self.match(fstripsParser.T__16)
                self.state = 510
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 507
                    self.processEffect()
                    self.state = 512
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 513
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ProcessSingleEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.processEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessEffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_processEffect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProcessAssignEffectContext(ProcessEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processEffectOp(self):
            return self.getTypedRuleContext(fstripsParser.ProcessEffectOpContext,0)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)

        def processEffectExp(self):
            return self.getTypedRuleContext(fstripsParser.ProcessEffectExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessAssignEffect" ):
                listener.enterProcessAssignEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessAssignEffect" ):
                listener.exitProcessAssignEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessAssignEffect" ):
                return visitor.visitProcessAssignEffect(self)
            else:
                return visitor.visitChildren(self)



    def processEffect(self):

        localctx = fstripsParser.ProcessEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_processEffect)
        try:
            localctx = fstripsParser.ProcessAssignEffectContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(fstripsParser.T__0)
            self.state = 518
            self.processEffectOp()
            self.state = 519
            self.functionTerm()
            self.state = 520
            self.processEffectExp()
            self.state = 521
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DerivedDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_derivedDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDerivedDef" ):
                listener.enterDerivedDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDerivedDef" ):
                listener.exitDerivedDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDerivedDef" ):
                return visitor.visitDerivedDef(self)
            else:
                return visitor.visitChildren(self)




    def derivedDef(self):

        localctx = fstripsParser.DerivedDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_derivedDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(fstripsParser.T__0)
            self.state = 524
            self.match(fstripsParser.T__25)
            self.state = 525
            self.possibly_typed_variable_list()
            self.state = 526
            self.goalDesc()
            self.state = 527
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_fExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionExprContext(FExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpr" ):
                return visitor.visitFunctionExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumericConstantExprContext(FExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericConstantExpr" ):
                listener.enterNumericConstantExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericConstantExpr" ):
                listener.exitNumericConstantExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericConstantExpr" ):
                return visitor.visitNumericConstantExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(FExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(fstripsParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)



    def fExp(self):

        localctx = fstripsParser.FExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_fExp)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                localctx = fstripsParser.FunctionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.functionTerm()
                pass
            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.NumericConstantExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.match(fstripsParser.NUMBER)
                pass
            elif token in [fstripsParser.VARIABLE]:
                localctx = fstripsParser.VariableExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 531
                self.match(fstripsParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessEffectExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_processEffectExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionalProcessEffectExprContext(ProcessEffectExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processFunctionEff(self):
            return self.getTypedRuleContext(fstripsParser.ProcessFunctionEffContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionalProcessEffectExpr" ):
                listener.enterFunctionalProcessEffectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionalProcessEffectExpr" ):
                listener.exitFunctionalProcessEffectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionalProcessEffectExpr" ):
                return visitor.visitFunctionalProcessEffectExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConstProcessEffectExprContext(ProcessEffectExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processConstEff(self):
            return self.getTypedRuleContext(fstripsParser.ProcessConstEffContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstProcessEffectExpr" ):
                listener.enterConstProcessEffectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstProcessEffectExpr" ):
                listener.exitConstProcessEffectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstProcessEffectExpr" ):
                return visitor.visitConstProcessEffectExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableProcessEffectExprContext(ProcessEffectExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def processVarEff(self):
            return self.getTypedRuleContext(fstripsParser.ProcessVarEffContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableProcessEffectExpr" ):
                listener.enterVariableProcessEffectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableProcessEffectExpr" ):
                listener.exitVariableProcessEffectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableProcessEffectExpr" ):
                return visitor.visitVariableProcessEffectExpr(self)
            else:
                return visitor.visitChildren(self)



    def processEffectExp(self):

        localctx = fstripsParser.ProcessEffectExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_processEffectExp)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.FunctionalProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(fstripsParser.T__0)
                self.state = 535
                self.match(fstripsParser.T__26)
                self.state = 536
                self.processFunctionEff()
                self.state = 537
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ConstProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.match(fstripsParser.T__0)
                self.state = 540
                self.match(fstripsParser.T__26)
                self.state = 541
                self.processConstEff()
                self.state = 542
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.VariableProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 544
                self.match(fstripsParser.T__0)
                self.state = 545
                self.match(fstripsParser.T__26)
                self.state = 546
                self.processVarEff()
                self.state = 547
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessFunctionEffContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_processFunctionEff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessFunctionEff" ):
                listener.enterProcessFunctionEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessFunctionEff" ):
                listener.exitProcessFunctionEff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessFunctionEff" ):
                return visitor.visitProcessFunctionEff(self)
            else:
                return visitor.visitChildren(self)




    def processFunctionEff(self):

        localctx = fstripsParser.ProcessFunctionEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_processFunctionEff)
        try:
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.functionTerm()
                self.state = 552
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.match(fstripsParser.T__23)
                self.state = 555
                self.functionTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessConstEffContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_processConstEff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessConstEff" ):
                listener.enterProcessConstEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessConstEff" ):
                listener.exitProcessConstEff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessConstEff" ):
                return visitor.visitProcessConstEff(self)
            else:
                return visitor.visitChildren(self)




    def processConstEff(self):

        localctx = fstripsParser.ProcessConstEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_processConstEff)
        try:
            self.state = 562
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.match(fstripsParser.NUMBER)
                self.state = 559
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                self.match(fstripsParser.T__23)
                self.state = 561
                self.match(fstripsParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessVarEffContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(fstripsParser.VARIABLE, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_processVarEff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessVarEff" ):
                listener.enterProcessVarEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessVarEff" ):
                listener.exitProcessVarEff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessVarEff" ):
                return visitor.visitProcessVarEff(self)
            else:
                return visitor.visitChildren(self)




    def processVarEff(self):

        localctx = fstripsParser.ProcessVarEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_processVarEff)
        try:
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(fstripsParser.VARIABLE)
                self.state = 565
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(fstripsParser.T__23)
                self.state = 567
                self.match(fstripsParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FHeadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_symbol_name(self):
            return self.getTypedRuleContext(fstripsParser.Logical_symbol_nameContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_fHead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFHead" ):
                listener.enterFHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFHead" ):
                listener.exitFHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFHead" ):
                return visitor.visitFHead(self)
            else:
                return visitor.visitChildren(self)




    def fHead(self):

        localctx = fstripsParser.FHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_fHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(fstripsParser.T__0)
            self.state = 571
            self.logical_symbol_name()
            self.state = 575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.T__23 or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.VARIABLE - 80)) | (1 << (fstripsParser.NUMBER - 80)))) != 0):
                self.state = 572
                self.term()
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 578
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_effect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleEffectContext(EffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.EffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cEffect(self):
            return self.getTypedRuleContext(fstripsParser.CEffectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleEffect" ):
                listener.enterSingleEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleEffect" ):
                listener.exitSingleEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleEffect" ):
                return visitor.visitSingleEffect(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctiveEffectFormulaContext(EffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.EffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cEffect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.CEffectContext)
            else:
                return self.getTypedRuleContext(fstripsParser.CEffectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctiveEffectFormula" ):
                listener.enterConjunctiveEffectFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctiveEffectFormula" ):
                listener.exitConjunctiveEffectFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunctiveEffectFormula" ):
                return visitor.visitConjunctiveEffectFormula(self)
            else:
                return visitor.visitChildren(self)



    def effect(self):

        localctx = fstripsParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctiveEffectFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.match(fstripsParser.T__0)
                self.state = 581
                self.match(fstripsParser.T__16)
                self.state = 585
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 582
                    self.cEffect()
                    self.state = 587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 588
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.SingleEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 589
                self.cEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CEffectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_cEffect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleConditionalEffectContext(CEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.CEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)

        def atomic_effect(self):
            return self.getTypedRuleContext(fstripsParser.Atomic_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleConditionalEffect" ):
                listener.enterSingleConditionalEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleConditionalEffect" ):
                listener.exitSingleConditionalEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleConditionalEffect" ):
                return visitor.visitSingleConditionalEffect(self)
            else:
                return visitor.visitChildren(self)


    class MultipleConditionalEffectContext(CEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.CEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)

        def atomic_effect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Atomic_effectContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Atomic_effectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultipleConditionalEffect" ):
                listener.enterMultipleConditionalEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultipleConditionalEffect" ):
                listener.exitMultipleConditionalEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultipleConditionalEffect" ):
                return visitor.visitMultipleConditionalEffect(self)
            else:
                return visitor.visitChildren(self)


    class UniversallyQuantifiedEffectContext(CEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.CEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def effect(self):
            return self.getTypedRuleContext(fstripsParser.EffectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniversallyQuantifiedEffect" ):
                listener.enterUniversallyQuantifiedEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniversallyQuantifiedEffect" ):
                listener.exitUniversallyQuantifiedEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniversallyQuantifiedEffect" ):
                return visitor.visitUniversallyQuantifiedEffect(self)
            else:
                return visitor.visitChildren(self)


    class AtomicEffectContext(CEffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.CEffectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_effect(self):
            return self.getTypedRuleContext(fstripsParser.Atomic_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicEffect" ):
                listener.enterAtomicEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicEffect" ):
                listener.exitAtomicEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicEffect" ):
                return visitor.visitAtomicEffect(self)
            else:
                return visitor.visitChildren(self)



    def cEffect(self):

        localctx = fstripsParser.CEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_cEffect)
        self._la = 0 # Token type
        try:
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.UniversallyQuantifiedEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 592
                self.match(fstripsParser.T__0)
                self.state = 593
                self.match(fstripsParser.T__21)
                self.state = 594
                self.match(fstripsParser.T__0)
                self.state = 595
                self.possibly_typed_variable_list()
                self.state = 596
                self.match(fstripsParser.T__2)
                self.state = 597
                self.effect()
                self.state = 598
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.SingleConditionalEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.match(fstripsParser.T__0)
                self.state = 601
                self.match(fstripsParser.T__27)
                self.state = 602
                self.goalDesc()
                self.state = 603
                self.atomic_effect()
                self.state = 604
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.MultipleConditionalEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 606
                self.match(fstripsParser.T__0)
                self.state = 607
                self.match(fstripsParser.T__27)
                self.state = 608
                self.goalDesc()
                self.state = 609
                self.match(fstripsParser.T__0)
                self.state = 610
                self.match(fstripsParser.T__16)
                self.state = 614
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 611
                    self.atomic_effect()
                    self.state = 616
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 617
                self.match(fstripsParser.T__2)
                self.state = 618
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AtomicEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 620
                self.atomic_effect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atomic_effectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_atomic_effect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeleteAtomEffectContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicTermFormula(self):
            return self.getTypedRuleContext(fstripsParser.AtomicTermFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteAtomEffect" ):
                listener.enterDeleteAtomEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteAtomEffect" ):
                listener.exitDeleteAtomEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteAtomEffect" ):
                return visitor.visitDeleteAtomEffect(self)
            else:
                return visitor.visitChildren(self)


    class AssignEffectContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignOp(self):
            return self.getTypedRuleContext(fstripsParser.AssignOpContext,0)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)

        def fExp(self):
            return self.getTypedRuleContext(fstripsParser.FExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignEffect" ):
                listener.enterAssignEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignEffect" ):
                listener.exitAssignEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignEffect" ):
                return visitor.visitAssignEffect(self)
            else:
                return visitor.visitChildren(self)


    class AssignConstantContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)

        def term(self):
            return self.getTypedRuleContext(fstripsParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignConstant" ):
                listener.enterAssignConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignConstant" ):
                listener.exitAssignConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignConstant" ):
                return visitor.visitAssignConstant(self)
            else:
                return visitor.visitChildren(self)


    class AddAtomEffectContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicTermFormula(self):
            return self.getTypedRuleContext(fstripsParser.AtomicTermFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddAtomEffect" ):
                listener.enterAddAtomEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddAtomEffect" ):
                listener.exitAddAtomEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddAtomEffect" ):
                return visitor.visitAddAtomEffect(self)
            else:
                return visitor.visitChildren(self)



    def atomic_effect(self):

        localctx = fstripsParser.Atomic_effectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_atomic_effect)
        try:
            self.state = 641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.AssignEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 623
                self.match(fstripsParser.T__0)
                self.state = 624
                self.assignOp()
                self.state = 625
                self.functionTerm()
                self.state = 626
                self.fExp()
                self.state = 627
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.DeleteAtomEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 629
                self.match(fstripsParser.T__0)
                self.state = 630
                self.match(fstripsParser.T__18)
                self.state = 631
                self.atomicTermFormula()
                self.state = 632
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.AddAtomEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 634
                self.atomicTermFormula()
                pass

            elif la_ == 4:
                localctx = fstripsParser.AssignConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 635
                self.match(fstripsParser.T__0)
                self.state = 636
                self.match(fstripsParser.T__28)
                self.state = 637
                self.functionTerm()
                self.state = 638
                self.term()
                self.state = 639
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BinaryOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = fstripsParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__6) | (1 << fstripsParser.T__26) | (1 << fstripsParser.T__29) | (1 << fstripsParser.T__30) | (1 << fstripsParser.T__31) | (1 << fstripsParser.T__32) | (1 << fstripsParser.T__33))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryBuiltInContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_unaryBuiltIn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryBuiltIn" ):
                listener.enterUnaryBuiltIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryBuiltIn" ):
                listener.exitUnaryBuiltIn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryBuiltIn" ):
                return visitor.visitUnaryBuiltIn(self)
            else:
                return visitor.visitChildren(self)




    def unaryBuiltIn(self):

        localctx = fstripsParser.UnaryBuiltInContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_unaryBuiltIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__6) | (1 << fstripsParser.T__34) | (1 << fstripsParser.T__35) | (1 << fstripsParser.T__36) | (1 << fstripsParser.T__37) | (1 << fstripsParser.T__38) | (1 << fstripsParser.T__39) | (1 << fstripsParser.T__40) | (1 << fstripsParser.T__41) | (1 << fstripsParser.T__42))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BinaryCompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_binaryComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryComp" ):
                listener.enterBinaryComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryComp" ):
                listener.exitBinaryComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryComp" ):
                return visitor.visitBinaryComp(self)
            else:
                return visitor.visitChildren(self)




    def binaryComp(self):

        localctx = fstripsParser.BinaryCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_binaryComp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__22) | (1 << fstripsParser.T__43) | (1 << fstripsParser.T__44) | (1 << fstripsParser.T__45) | (1 << fstripsParser.T__46))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_assignOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignOp" ):
                listener.enterAssignOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignOp" ):
                listener.exitAssignOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOp" ):
                return visitor.visitAssignOp(self)
            else:
                return visitor.visitChildren(self)




    def assignOp(self):

        localctx = fstripsParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__28) | (1 << fstripsParser.T__47) | (1 << fstripsParser.T__48) | (1 << fstripsParser.T__49) | (1 << fstripsParser.T__50))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessEffectOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_processEffectOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessEffectOp" ):
                listener.enterProcessEffectOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessEffectOp" ):
                listener.exitProcessEffectOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessEffectOp" ):
                return visitor.visitProcessEffectOp(self)
            else:
                return visitor.visitChildren(self)




    def processEffectOp(self):

        localctx = fstripsParser.ProcessEffectOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_processEffectOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            _la = self._input.LA(1)
            if not(_la==fstripsParser.T__49 or _la==fstripsParser.T__50):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProblemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def problemDecl(self):
            return self.getTypedRuleContext(fstripsParser.ProblemDeclContext,0)


        def problemDomain(self):
            return self.getTypedRuleContext(fstripsParser.ProblemDomainContext,0)


        def init(self):
            return self.getTypedRuleContext(fstripsParser.InitContext,0)


        def goal(self):
            return self.getTypedRuleContext(fstripsParser.GoalContext,0)


        def requireDef(self):
            return self.getTypedRuleContext(fstripsParser.RequireDefContext,0)


        def object_declaration(self):
            return self.getTypedRuleContext(fstripsParser.Object_declarationContext,0)


        def problemMeta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.ProblemMetaContext)
            else:
                return self.getTypedRuleContext(fstripsParser.ProblemMetaContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_problem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblem" ):
                listener.enterProblem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblem" ):
                listener.exitProblem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProblem" ):
                return visitor.visitProblem(self)
            else:
                return visitor.visitChildren(self)




    def problem(self):

        localctx = fstripsParser.ProblemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_problem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(fstripsParser.T__0)
            self.state = 654
            self.match(fstripsParser.T__1)
            self.state = 655
            self.problemDecl()
            self.state = 656
            self.problemDomain()
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 657
                self.requireDef()


            self.state = 661
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 660
                self.object_declaration()


            self.state = 663
            self.init()
            self.state = 664
            self.goal()
            self.state = 668
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 665
                self.problemMeta()
                self.state = 670
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 671
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProblemMetaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def probConstraints(self):
            return self.getTypedRuleContext(fstripsParser.ProbConstraintsContext,0)


        def boundsDecl(self):
            return self.getTypedRuleContext(fstripsParser.BoundsDeclContext,0)


        def metricSpec(self):
            return self.getTypedRuleContext(fstripsParser.MetricSpecContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_problemMeta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemMeta" ):
                listener.enterProblemMeta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemMeta" ):
                listener.exitProblemMeta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProblemMeta" ):
                return visitor.visitProblemMeta(self)
            else:
                return visitor.visitChildren(self)




    def problemMeta(self):

        localctx = fstripsParser.ProblemMetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_problemMeta)
        try:
            self.state = 676
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.probConstraints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 674
                self.boundsDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 675
                self.metricSpec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProblemDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_problemDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemDecl" ):
                listener.enterProblemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemDecl" ):
                listener.exitProblemDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProblemDecl" ):
                return visitor.visitProblemDecl(self)
            else:
                return visitor.visitChildren(self)




    def problemDecl(self):

        localctx = fstripsParser.ProblemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_problemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.match(fstripsParser.T__0)
            self.state = 679
            self.match(fstripsParser.T__51)
            self.state = 680
            self.match(fstripsParser.NAME)
            self.state = 681
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProblemDomainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_problemDomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemDomain" ):
                listener.enterProblemDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemDomain" ):
                listener.exitProblemDomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProblemDomain" ):
                return visitor.visitProblemDomain(self)
            else:
                return visitor.visitChildren(self)




    def problemDomain(self):

        localctx = fstripsParser.ProblemDomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_problemDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self.match(fstripsParser.T__0)
            self.state = 684
            self.match(fstripsParser.T__52)
            self.state = 685
            self.match(fstripsParser.NAME)
            self.state = 686
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Object_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possibly_typed_name_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_name_listContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_object_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_declaration" ):
                listener.enterObject_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_declaration" ):
                listener.exitObject_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_declaration" ):
                return visitor.visitObject_declaration(self)
            else:
                return visitor.visitChildren(self)




    def object_declaration(self):

        localctx = fstripsParser.Object_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_object_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(fstripsParser.T__0)
            self.state = 689
            self.match(fstripsParser.T__53)
            self.state = 690
            self.possibly_typed_name_list()
            self.state = 691
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoundsDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeBoundsDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TypeBoundsDefinitionContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TypeBoundsDefinitionContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_boundsDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoundsDecl" ):
                listener.enterBoundsDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoundsDecl" ):
                listener.exitBoundsDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoundsDecl" ):
                return visitor.visitBoundsDecl(self)
            else:
                return visitor.visitChildren(self)




    def boundsDecl(self):

        localctx = fstripsParser.BoundsDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_boundsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            self.match(fstripsParser.T__0)
            self.state = 694
            self.match(fstripsParser.T__54)
            self.state = 696 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 695
                self.typeBoundsDefinition()
                self.state = 698 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.T__0):
                    break

            self.state = 700
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeBoundsDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def numericBuiltinType(self):
            return self.getTypedRuleContext(fstripsParser.NumericBuiltinTypeContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NUMBER)
            else:
                return self.getToken(fstripsParser.NUMBER, i)

        def getRuleIndex(self):
            return fstripsParser.RULE_typeBoundsDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBoundsDefinition" ):
                listener.enterTypeBoundsDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBoundsDefinition" ):
                listener.exitTypeBoundsDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBoundsDefinition" ):
                return visitor.visitTypeBoundsDefinition(self)
            else:
                return visitor.visitChildren(self)




    def typeBoundsDefinition(self):

        localctx = fstripsParser.TypeBoundsDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_typeBoundsDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.match(fstripsParser.T__0)
            self.state = 703
            self.match(fstripsParser.NAME)
            self.state = 704
            self.match(fstripsParser.T__6)
            self.state = 705
            self.numericBuiltinType()
            self.state = 706
            self.match(fstripsParser.T__55)
            self.state = 707
            self.match(fstripsParser.NUMBER)
            self.state = 708
            self.match(fstripsParser.T__56)
            self.state = 709
            self.match(fstripsParser.NUMBER)
            self.state = 710
            self.match(fstripsParser.T__57)
            self.state = 711
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_INIT(self):
            return self.getToken(fstripsParser.K_INIT, 0)

        def initEl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.InitElContext)
            else:
                return self.getTypedRuleContext(fstripsParser.InitElContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = fstripsParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            self.match(fstripsParser.T__0)
            self.state = 714
            self.match(fstripsParser.K_INIT)
            self.state = 718
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 715
                self.initEl()
                self.state = 720
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 721
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroundTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_groundTerm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GroundTermNumberContext(GroundTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GroundTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundTermNumber" ):
                listener.enterGroundTermNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundTermNumber" ):
                listener.exitGroundTermNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroundTermNumber" ):
                return visitor.visitGroundTermNumber(self)
            else:
                return visitor.visitChildren(self)


    class GroundTermFunctionContext(GroundTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GroundTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def groundFunctionTerm(self):
            return self.getTypedRuleContext(fstripsParser.GroundFunctionTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundTermFunction" ):
                listener.enterGroundTermFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundTermFunction" ):
                listener.exitGroundTermFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroundTermFunction" ):
                return visitor.visitGroundTermFunction(self)
            else:
                return visitor.visitChildren(self)


    class GroundTermObjectContext(GroundTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GroundTermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundTermObject" ):
                listener.enterGroundTermObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundTermObject" ):
                listener.exitGroundTermObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroundTermObject" ):
                return visitor.visitGroundTermObject(self)
            else:
                return visitor.visitChildren(self)



    def groundTerm(self):

        localctx = fstripsParser.GroundTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_groundTerm)
        try:
            self.state = 726
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                localctx = fstripsParser.GroundTermObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 723
                self.match(fstripsParser.NAME)
                pass
            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.GroundTermNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 724
                self.match(fstripsParser.NUMBER)
                pass
            elif token in [fstripsParser.T__0]:
                localctx = fstripsParser.GroundTermFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 725
                self.groundFunctionTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroundFunctionTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_symbol_name(self):
            return self.getTypedRuleContext(fstripsParser.Logical_symbol_nameContext,0)


        def groundTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GroundTermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GroundTermContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_groundFunctionTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundFunctionTerm" ):
                listener.enterGroundFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundFunctionTerm" ):
                listener.exitGroundFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroundFunctionTerm" ):
                return visitor.visitGroundFunctionTerm(self)
            else:
                return visitor.visitChildren(self)




    def groundFunctionTerm(self):

        localctx = fstripsParser.GroundFunctionTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_groundFunctionTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 728
            self.match(fstripsParser.T__0)
            self.state = 729
            self.logical_symbol_name()
            self.state = 733
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.NAME or _la==fstripsParser.NUMBER:
                self.state = 730
                self.groundTerm()
                self.state = 735
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 736
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitElContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_initEl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InitLiteralContext(InitElContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.InitElContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nameLiteral(self):
            return self.getTypedRuleContext(fstripsParser.NameLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitLiteral" ):
                listener.enterInitLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitLiteral" ):
                listener.exitInitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitLiteral" ):
                return visitor.visitInitLiteral(self)
            else:
                return visitor.visitChildren(self)


    class InitAssignmentNumericContext(InitElContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.InitElContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def groundFunctionTerm(self):
            return self.getTypedRuleContext(fstripsParser.GroundFunctionTermContext,0)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitAssignmentNumeric" ):
                listener.enterInitAssignmentNumeric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitAssignmentNumeric" ):
                listener.exitInitAssignmentNumeric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitAssignmentNumeric" ):
                return visitor.visitInitAssignmentNumeric(self)
            else:
                return visitor.visitChildren(self)


    class InitAssignmentObjectContext(InitElContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.InitElContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def groundFunctionTerm(self):
            return self.getTypedRuleContext(fstripsParser.GroundFunctionTermContext,0)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitAssignmentObject" ):
                listener.enterInitAssignmentObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitAssignmentObject" ):
                listener.exitInitAssignmentObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitAssignmentObject" ):
                return visitor.visitInitAssignmentObject(self)
            else:
                return visitor.visitChildren(self)



    def initEl(self):

        localctx = fstripsParser.InitElContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_initEl)
        try:
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.InitLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 738
                self.nameLiteral()
                pass

            elif la_ == 2:
                localctx = fstripsParser.InitAssignmentNumericContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 739
                self.match(fstripsParser.T__0)
                self.state = 740
                self.match(fstripsParser.T__22)
                self.state = 741
                self.groundFunctionTerm()
                self.state = 742
                self.match(fstripsParser.NUMBER)
                self.state = 743
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.InitAssignmentObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 745
                self.match(fstripsParser.T__0)
                self.state = 746
                self.match(fstripsParser.T__22)
                self.state = 747
                self.groundFunctionTerm()
                self.state = 748
                self.match(fstripsParser.NAME)
                self.state = 749
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_nameLiteral

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InitNegativeLiteralContext(NameLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NameLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def groundAtomicFormula(self):
            return self.getTypedRuleContext(fstripsParser.GroundAtomicFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitNegativeLiteral" ):
                listener.enterInitNegativeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitNegativeLiteral" ):
                listener.exitInitNegativeLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitNegativeLiteral" ):
                return visitor.visitInitNegativeLiteral(self)
            else:
                return visitor.visitChildren(self)


    class InitPositiveLiteralContext(NameLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NameLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def groundAtomicFormula(self):
            return self.getTypedRuleContext(fstripsParser.GroundAtomicFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitPositiveLiteral" ):
                listener.enterInitPositiveLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitPositiveLiteral" ):
                listener.exitInitPositiveLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitPositiveLiteral" ):
                return visitor.visitInitPositiveLiteral(self)
            else:
                return visitor.visitChildren(self)



    def nameLiteral(self):

        localctx = fstripsParser.NameLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_nameLiteral)
        try:
            self.state = 759
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.InitPositiveLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 753
                self.groundAtomicFormula()
                pass

            elif la_ == 2:
                localctx = fstripsParser.InitNegativeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 754
                self.match(fstripsParser.T__0)
                self.state = 755
                self.match(fstripsParser.T__18)
                self.state = 756
                self.groundAtomicFormula()
                self.state = 757
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroundAtomicFormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(fstripsParser.PredicateContext,0)


        def groundTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GroundTermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GroundTermContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_groundAtomicFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundAtomicFormula" ):
                listener.enterGroundAtomicFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundAtomicFormula" ):
                listener.exitGroundAtomicFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroundAtomicFormula" ):
                return visitor.visitGroundAtomicFormula(self)
            else:
                return visitor.visitChildren(self)




    def groundAtomicFormula(self):

        localctx = fstripsParser.GroundAtomicFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_groundAtomicFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
            self.match(fstripsParser.T__0)
            self.state = 762
            self.predicate()
            self.state = 766
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.NAME or _la==fstripsParser.NUMBER:
                self.state = 763
                self.groundTerm()
                self.state = 768
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 769
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GoalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal" ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal" ):
                listener.exitGoal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoal" ):
                return visitor.visitGoal(self)
            else:
                return visitor.visitChildren(self)




    def goal(self):

        localctx = fstripsParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 771
            self.match(fstripsParser.T__0)
            self.state = 772
            self.match(fstripsParser.T__58)
            self.state = 773
            self.goalDesc()
            self.state = 774
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProbConstraintsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefConGD(self):
            return self.getTypedRuleContext(fstripsParser.PrefConGDContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_probConstraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbConstraints" ):
                listener.enterProbConstraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbConstraints" ):
                listener.exitProbConstraints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProbConstraints" ):
                return visitor.visitProbConstraints(self)
            else:
                return visitor.visitChildren(self)




    def probConstraints(self):

        localctx = fstripsParser.ProbConstraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_probConstraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            self.match(fstripsParser.T__0)
            self.state = 777
            self.match(fstripsParser.T__59)
            self.state = 778
            self.prefConGD()
            self.state = 779
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefConGDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_prefConGD

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UniversallyQuantifiedConstraintContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def prefConGD(self):
            return self.getTypedRuleContext(fstripsParser.PrefConGDContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniversallyQuantifiedConstraint" ):
                listener.enterUniversallyQuantifiedConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniversallyQuantifiedConstraint" ):
                listener.exitUniversallyQuantifiedConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniversallyQuantifiedConstraint" ):
                return visitor.visitUniversallyQuantifiedConstraint(self)
            else:
                return visitor.visitChildren(self)


    class PlainConstraintListContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conGD(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.ConGDContext)
            else:
                return self.getTypedRuleContext(fstripsParser.ConGDContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlainConstraintList" ):
                listener.enterPlainConstraintList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlainConstraintList" ):
                listener.exitPlainConstraintList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlainConstraintList" ):
                return visitor.visitPlainConstraintList(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionOfConstraintsContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prefConGD(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.PrefConGDContext)
            else:
                return self.getTypedRuleContext(fstripsParser.PrefConGDContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctionOfConstraints" ):
                listener.enterConjunctionOfConstraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctionOfConstraints" ):
                listener.exitConjunctionOfConstraints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunctionOfConstraints" ):
                return visitor.visitConjunctionOfConstraints(self)
            else:
                return visitor.visitChildren(self)


    class PreferenceConstraintContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conGD(self):
            return self.getTypedRuleContext(fstripsParser.ConGDContext,0)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreferenceConstraint" ):
                listener.enterPreferenceConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreferenceConstraint" ):
                listener.exitPreferenceConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreferenceConstraint" ):
                return visitor.visitPreferenceConstraint(self)
            else:
                return visitor.visitChildren(self)



    def prefConGD(self):

        localctx = fstripsParser.PrefConGDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_prefConGD)
        self._la = 0 # Token type
        try:
            self.state = 811
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctionOfConstraintsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 781
                self.match(fstripsParser.T__0)
                self.state = 782
                self.match(fstripsParser.T__16)
                self.state = 786
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 783
                    self.prefConGD()
                    self.state = 788
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 789
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.UniversallyQuantifiedConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 790
                self.match(fstripsParser.T__0)
                self.state = 791
                self.match(fstripsParser.T__21)
                self.state = 792
                self.match(fstripsParser.T__0)
                self.state = 793
                self.possibly_typed_variable_list()
                self.state = 794
                self.match(fstripsParser.T__2)
                self.state = 795
                self.prefConGD()
                self.state = 796
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.PreferenceConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 798
                self.match(fstripsParser.T__0)
                self.state = 799
                self.match(fstripsParser.T__60)
                self.state = 801
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fstripsParser.NAME:
                    self.state = 800
                    self.match(fstripsParser.NAME)


                self.state = 803
                self.conGD()
                self.state = 804
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.PlainConstraintListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 807 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 806
                        self.conGD()

                    else:
                        raise NoViableAltException(self)
                    self.state = 809 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetricSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_metricSpec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProblemMetricContext(MetricSpecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricSpecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def optimization(self):
            return self.getTypedRuleContext(fstripsParser.OptimizationContext,0)

        def metricFExp(self):
            return self.getTypedRuleContext(fstripsParser.MetricFExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemMetric" ):
                listener.enterProblemMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemMetric" ):
                listener.exitProblemMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProblemMetric" ):
                return visitor.visitProblemMetric(self)
            else:
                return visitor.visitChildren(self)



    def metricSpec(self):

        localctx = fstripsParser.MetricSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_metricSpec)
        try:
            localctx = fstripsParser.ProblemMetricContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 813
            self.match(fstripsParser.T__0)
            self.state = 814
            self.match(fstripsParser.T__61)
            self.state = 815
            self.optimization()
            self.state = 816
            self.metricFExp()
            self.state = 817
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptimizationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_optimization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimization" ):
                listener.enterOptimization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimization" ):
                listener.exitOptimization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptimization" ):
                return visitor.visitOptimization(self)
            else:
                return visitor.visitChildren(self)




    def optimization(self):

        localctx = fstripsParser.OptimizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_optimization)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 819
            _la = self._input.LA(1)
            if not(_la==fstripsParser.T__62 or _la==fstripsParser.T__63):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetricFExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_metricFExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionalExprMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionalExprMetric" ):
                listener.enterFunctionalExprMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionalExprMetric" ):
                listener.exitFunctionalExprMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionalExprMetric" ):
                return visitor.visitFunctionalExprMetric(self)
            else:
                return visitor.visitChildren(self)


    class CompositeMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terminalCost(self):
            return self.getTypedRuleContext(fstripsParser.TerminalCostContext,0)

        def stageCost(self):
            return self.getTypedRuleContext(fstripsParser.StageCostContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompositeMetric" ):
                listener.enterCompositeMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompositeMetric" ):
                listener.exitCompositeMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeMetric" ):
                return visitor.visitCompositeMetric(self)
            else:
                return visitor.visitChildren(self)


    class IsViolatedMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsViolatedMetric" ):
                listener.enterIsViolatedMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsViolatedMetric" ):
                listener.exitIsViolatedMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsViolatedMetric" ):
                return visitor.visitIsViolatedMetric(self)
            else:
                return visitor.visitChildren(self)


    class TotalTimeMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTotalTimeMetric" ):
                listener.enterTotalTimeMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTotalTimeMetric" ):
                listener.exitTotalTimeMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTotalTimeMetric" ):
                return visitor.visitTotalTimeMetric(self)
            else:
                return visitor.visitChildren(self)



    def metricFExp(self):

        localctx = fstripsParser.MetricFExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_metricFExp)
        try:
            self.state = 833
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.FunctionalExprMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 821
                self.functionTerm()
                pass

            elif la_ == 2:
                localctx = fstripsParser.CompositeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 822
                self.terminalCost()
                self.state = 823
                self.stageCost()
                pass

            elif la_ == 3:
                localctx = fstripsParser.CompositeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 825
                self.stageCost()
                self.state = 826
                self.terminalCost()
                pass

            elif la_ == 4:
                localctx = fstripsParser.TotalTimeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 828
                self.match(fstripsParser.T__64)
                pass

            elif la_ == 5:
                localctx = fstripsParser.IsViolatedMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 829
                self.match(fstripsParser.T__0)
                self.state = 830
                self.match(fstripsParser.T__65)
                self.state = 831
                self.match(fstripsParser.NAME)
                self.state = 832
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminalCostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_terminalCost

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminalCost" ):
                listener.enterTerminalCost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminalCost" ):
                listener.exitTerminalCost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminalCost" ):
                return visitor.visitTerminalCost(self)
            else:
                return visitor.visitChildren(self)




    def terminalCost(self):

        localctx = fstripsParser.TerminalCostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_terminalCost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 835
            self.match(fstripsParser.T__0)
            self.state = 836
            self.match(fstripsParser.T__66)
            self.state = 837
            self.functionTerm()
            self.state = 838
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StageCostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_stageCost

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStageCost" ):
                listener.enterStageCost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStageCost" ):
                listener.exitStageCost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStageCost" ):
                return visitor.visitStageCost(self)
            else:
                return visitor.visitChildren(self)




    def stageCost(self):

        localctx = fstripsParser.StageCostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_stageCost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 840
            self.match(fstripsParser.T__0)
            self.state = 841
            self.match(fstripsParser.T__67)
            self.state = 842
            self.functionTerm()
            self.state = 843
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConGDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_conGD

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForallConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def conGD(self):
            return self.getTypedRuleContext(fstripsParser.ConGDContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForallConstraint" ):
                listener.enterForallConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForallConstraint" ):
                listener.exitForallConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForallConstraint" ):
                return visitor.visitForallConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlwaysConstraint" ):
                listener.enterAlwaysConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlwaysConstraint" ):
                listener.exitAlwaysConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlwaysConstraint" ):
                return visitor.visitAlwaysConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AtEndConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtEndConstraint" ):
                listener.enterAtEndConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtEndConstraint" ):
                listener.exitAtEndConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtEndConstraint" ):
                return visitor.visitAtEndConstraint(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctiveConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conGD(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.ConGDContext)
            else:
                return self.getTypedRuleContext(fstripsParser.ConGDContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctiveConstraint" ):
                listener.enterConjunctiveConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctiveConstraint" ):
                listener.exitConjunctiveConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunctiveConstraint" ):
                return visitor.visitConjunctiveConstraint(self)
            else:
                return visitor.visitChildren(self)


    class SometimeConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSometimeConstraint" ):
                listener.enterSometimeConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSometimeConstraint" ):
                listener.exitSometimeConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSometimeConstraint" ):
                return visitor.visitSometimeConstraint(self)
            else:
                return visitor.visitChildren(self)


    class WithinConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithinConstraint" ):
                listener.enterWithinConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithinConstraint" ):
                listener.exitWithinConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithinConstraint" ):
                return visitor.visitWithinConstraint(self)
            else:
                return visitor.visitChildren(self)


    class HoldAfterConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHoldAfterConstraint" ):
                listener.enterHoldAfterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHoldAfterConstraint" ):
                listener.exitHoldAfterConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHoldAfterConstraint" ):
                return visitor.visitHoldAfterConstraint(self)
            else:
                return visitor.visitChildren(self)


    class SometimeBeforeConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSometimeBeforeConstraint" ):
                listener.enterSometimeBeforeConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSometimeBeforeConstraint" ):
                listener.exitSometimeBeforeConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSometimeBeforeConstraint" ):
                return visitor.visitSometimeBeforeConstraint(self)
            else:
                return visitor.visitChildren(self)


    class SometimeAfterConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSometimeAfterConstraint" ):
                listener.enterSometimeAfterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSometimeAfterConstraint" ):
                listener.exitSometimeAfterConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSometimeAfterConstraint" ):
                return visitor.visitSometimeAfterConstraint(self)
            else:
                return visitor.visitChildren(self)


    class ExtensionalConstraintGDContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXTNAME(self):
            return self.getToken(fstripsParser.EXTNAME, 0)
        def groundFunctionTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GroundFunctionTermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GroundFunctionTermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtensionalConstraintGD" ):
                listener.enterExtensionalConstraintGD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtensionalConstraintGD" ):
                listener.exitExtensionalConstraintGD(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtensionalConstraintGD" ):
                return visitor.visitExtensionalConstraintGD(self)
            else:
                return visitor.visitChildren(self)


    class HoldDuringConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NUMBER)
            else:
                return self.getToken(fstripsParser.NUMBER, i)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHoldDuringConstraint" ):
                listener.enterHoldDuringConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHoldDuringConstraint" ):
                listener.exitHoldDuringConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHoldDuringConstraint" ):
                return visitor.visitHoldDuringConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysWithinConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)
        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlwaysWithinConstraint" ):
                listener.enterAlwaysWithinConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlwaysWithinConstraint" ):
                listener.exitAlwaysWithinConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlwaysWithinConstraint" ):
                return visitor.visitAlwaysWithinConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AlternativeAlwaysConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternativeAlwaysConstraint" ):
                listener.enterAlternativeAlwaysConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternativeAlwaysConstraint" ):
                listener.exitAlternativeAlwaysConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternativeAlwaysConstraint" ):
                return visitor.visitAlternativeAlwaysConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AtMostOnceConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtMostOnceConstraint" ):
                listener.enterAtMostOnceConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtMostOnceConstraint" ):
                listener.exitAtMostOnceConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtMostOnceConstraint" ):
                return visitor.visitAtMostOnceConstraint(self)
            else:
                return visitor.visitChildren(self)



    def conGD(self):

        localctx = fstripsParser.ConGDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_conGD)
        self._la = 0 # Token type
        try:
            self.state = 930
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctiveConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 845
                self.match(fstripsParser.T__0)
                self.state = 846
                self.match(fstripsParser.T__16)
                self.state = 848 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 847
                    self.conGD()
                    self.state = 850 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==fstripsParser.T__0):
                        break

                self.state = 852
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ForallConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 854
                self.match(fstripsParser.T__0)
                self.state = 855
                self.match(fstripsParser.T__21)
                self.state = 856
                self.match(fstripsParser.T__0)
                self.state = 857
                self.possibly_typed_variable_list()
                self.state = 858
                self.match(fstripsParser.T__2)
                self.state = 859
                self.conGD()
                self.state = 860
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.AtEndConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 862
                self.match(fstripsParser.T__0)
                self.state = 863
                self.match(fstripsParser.T__68)
                self.state = 864
                self.goalDesc()
                self.state = 865
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AlwaysConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 867
                self.match(fstripsParser.T__0)
                self.state = 868
                self.match(fstripsParser.T__69)
                self.state = 869
                self.goalDesc()
                self.state = 870
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 5:
                localctx = fstripsParser.SometimeConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 872
                self.match(fstripsParser.T__0)
                self.state = 873
                self.match(fstripsParser.T__70)
                self.state = 874
                self.goalDesc()
                self.state = 875
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 6:
                localctx = fstripsParser.WithinConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 877
                self.match(fstripsParser.T__0)
                self.state = 878
                self.match(fstripsParser.T__71)
                self.state = 879
                self.match(fstripsParser.NUMBER)
                self.state = 880
                self.goalDesc()
                self.state = 881
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 7:
                localctx = fstripsParser.AtMostOnceConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 883
                self.match(fstripsParser.T__0)
                self.state = 884
                self.match(fstripsParser.T__72)
                self.state = 885
                self.goalDesc()
                self.state = 886
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 8:
                localctx = fstripsParser.SometimeAfterConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 888
                self.match(fstripsParser.T__0)
                self.state = 889
                self.match(fstripsParser.T__73)
                self.state = 890
                self.goalDesc()
                self.state = 891
                self.goalDesc()
                self.state = 892
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 9:
                localctx = fstripsParser.SometimeBeforeConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 894
                self.match(fstripsParser.T__0)
                self.state = 895
                self.match(fstripsParser.T__74)
                self.state = 896
                self.goalDesc()
                self.state = 897
                self.goalDesc()
                self.state = 898
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 10:
                localctx = fstripsParser.AlwaysWithinConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 900
                self.match(fstripsParser.T__0)
                self.state = 901
                self.match(fstripsParser.T__75)
                self.state = 902
                self.match(fstripsParser.NUMBER)
                self.state = 903
                self.goalDesc()
                self.state = 904
                self.goalDesc()
                self.state = 905
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 11:
                localctx = fstripsParser.HoldDuringConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 907
                self.match(fstripsParser.T__0)
                self.state = 908
                self.match(fstripsParser.T__76)
                self.state = 909
                self.match(fstripsParser.NUMBER)
                self.state = 910
                self.match(fstripsParser.NUMBER)
                self.state = 911
                self.goalDesc()
                self.state = 912
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 12:
                localctx = fstripsParser.HoldAfterConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 914
                self.match(fstripsParser.T__0)
                self.state = 915
                self.match(fstripsParser.T__77)
                self.state = 916
                self.match(fstripsParser.NUMBER)
                self.state = 917
                self.goalDesc()
                self.state = 918
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 13:
                localctx = fstripsParser.ExtensionalConstraintGDContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 920
                self.match(fstripsParser.T__0)
                self.state = 921
                self.match(fstripsParser.EXTNAME)
                self.state = 923 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 922
                    self.groundFunctionTerm()
                    self.state = 925 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==fstripsParser.T__0):
                        break

                self.state = 927
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 14:
                localctx = fstripsParser.AlternativeAlwaysConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 929
                self.goalDesc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





