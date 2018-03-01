# Generated from ./grammars/fstrips.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u008d")
        buf.write("\u03a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\3\2\3\2\5\2\u00a3\n\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u00a9\n\3\3\3\5\3\u00ac\n\3\3\3\5\3\u00af\n\3")
        buf.write("\3\3\5\3\u00b2\n\3\3\3\5\3\u00b5\n\3\3\3\7\3\u00b8\n\3")
        buf.write("\f\3\16\3\u00bb\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\6\5\u00c7\n\5\r\5\16\5\u00c8\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\5\7\u00d5\n\7\3\b\3\b\5\b\u00d9")
        buf.write("\n\b\3\t\7\t\u00dc\n\t\f\t\16\t\u00df\13\t\3\n\3\n\6\n")
        buf.write("\u00e3\n\n\r\n\16\n\u00e4\3\n\3\n\5\n\u00e9\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\6\f\u00f3\n\f\r\f\16\f")
        buf.write("\u00f4\3\f\3\f\3\f\5\f\u00fa\n\f\3\r\3\r\5\r\u00fe\n\r")
        buf.write("\3\16\3\16\3\16\7\16\u0103\n\16\f\16\16\16\u0106\13\16")
        buf.write("\3\16\3\16\3\17\3\17\5\17\u010c\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\7\24\u0124\n")
        buf.write("\24\f\24\16\24\u0127\13\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\27\7\27\u0133\n\27\f\27\16\27\u0136")
        buf.write("\13\27\3\27\6\27\u0139\n\27\r\27\16\27\u013a\3\27\7\27")
        buf.write("\u013e\n\27\f\27\16\27\u0141\13\27\5\27\u0143\n\27\3\30")
        buf.write("\6\30\u0146\n\30\r\30\16\30\u0147\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u0152\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\5!\u0181\n!\3\"\3\"\3\"")
        buf.write("\3\"\7\"\u0187\n\"\f\"\16\"\u018a\13\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0190\n\"\f\"\16\"\u0193\13\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01b3")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\7%\u01c4")
        buf.write("\n%\f%\16%\u01c7\13%\3%\3%\3&\3&\3&\3&\3&\5&\u01d0\n&")
        buf.write("\3\'\3\'\3\'\7\'\u01d5\n\'\f\'\16\'\u01d8\13\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01e7")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\7*\u01fb\n*\f*\16*\u01fe\13*\3*\3*\5*\u0202\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\5-\u0213\n")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0224")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u022b\n/\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u0231\n\60\3\61\3\61\3\61\3\61\5\61\u0237\n\61\3\62\3")
        buf.write("\62\3\62\7\62\u023c\n\62\f\62\16\62\u023f\13\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\7\63\u0246\n\63\f\63\16\63\u0249\13")
        buf.write("\63\3\63\3\63\5\63\u024d\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\7\64\u0263\n\64\f\64\16\64\u0266")
        buf.write("\13\64\3\64\3\64\3\64\3\64\5\64\u026c\n\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u0280\n\65\3\66\3\66\3")
        buf.write("\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\3;\5;\u0291\n;")
        buf.write("\3;\5;\u0294\n;\3;\3;\3;\7;\u0299\n;\f;\16;\u029c\13;")
        buf.write("\3;\3;\3<\3<\3<\5<\u02a3\n<\3=\3=\3=\3=\3=\3>\3>\3>\3")
        buf.write(">\3>\3?\3?\3?\3?\3?\3@\3@\3@\6@\u02b7\n@\r@\16@\u02b8")
        buf.write("\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\7B\u02cb")
        buf.write("\nB\fB\16B\u02ce\13B\3B\3B\3C\3C\3C\5C\u02d5\nC\3D\3D")
        buf.write("\3D\7D\u02da\nD\fD\16D\u02dd\13D\3D\3D\3E\3E\3E\3E\3E")
        buf.write("\3E\3E\3E\3E\3E\3E\3E\3E\5E\u02ee\nE\3F\3F\3F\3F\3F\3")
        buf.write("F\5F\u02f6\nF\3G\3G\3G\7G\u02fb\nG\fG\16G\u02fe\13G\3")
        buf.write("G\3G\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3J\3J\3J\7J\u030f\n")
        buf.write("J\fJ\16J\u0312\13J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3")
        buf.write("J\5J\u0320\nJ\3J\3J\3J\3J\6J\u0326\nJ\rJ\16J\u0327\5J")
        buf.write("\u032a\nJ\3K\3K\3K\3K\3K\3K\3L\3L\3M\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3M\3M\5M\u0340\nM\3N\3N\3N\3N\3N\3O\3O\3O\3")
        buf.write("O\3O\3P\3P\3P\6P\u034f\nP\rP\16P\u0350\3P\3P\3P\3P\3P")
        buf.write("\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\6P\u039a\nP\rP\16")
        buf.write("P\u039b\3P\3P\3P\5P\u03a1\nP\3P\2\2Q\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\2\t\3\2RS\5\2\t\t\35\35 $\4\2\t\t%-\4\2\31")
        buf.write("\31.\61\4\2\37\37\62\65\3\2\64\65\3\2AB\2\u03bd\2\u00a2")
        buf.write("\3\2\2\2\4\u00a4\3\2\2\2\6\u00be\3\2\2\2\b\u00c3\3\2\2")
        buf.write("\2\n\u00cc\3\2\2\2\f\u00d4\3\2\2\2\16\u00d8\3\2\2\2\20")
        buf.write("\u00dd\3\2\2\2\22\u00e8\3\2\2\2\24\u00ea\3\2\2\2\26\u00f9")
        buf.write("\3\2\2\2\30\u00fd\3\2\2\2\32\u00ff\3\2\2\2\34\u010b\3")
        buf.write("\2\2\2\36\u010d\3\2\2\2 \u0114\3\2\2\2\"\u0119\3\2\2\2")
        buf.write("$\u011b\3\2\2\2&\u0120\3\2\2\2(\u012a\3\2\2\2*\u012f\3")
        buf.write("\2\2\2,\u0142\3\2\2\2.\u0145\3\2\2\2\60\u0151\3\2\2\2")
        buf.write("\62\u0153\3\2\2\2\64\u015d\3\2\2\2\66\u0168\3\2\2\28\u0172")
        buf.write("\3\2\2\2:\u0174\3\2\2\2<\u0176\3\2\2\2>\u0178\3\2\2\2")
        buf.write("@\u0180\3\2\2\2B\u01b2\3\2\2\2D\u01b4\3\2\2\2F\u01ba\3")
        buf.write("\2\2\2H\u01c0\3\2\2\2J\u01cf\3\2\2\2L\u01e6\3\2\2\2N\u01e8")
        buf.write("\3\2\2\2P\u01f2\3\2\2\2R\u0201\3\2\2\2T\u0203\3\2\2\2")
        buf.write("V\u0209\3\2\2\2X\u0212\3\2\2\2Z\u0223\3\2\2\2\\\u022a")
        buf.write("\3\2\2\2^\u0230\3\2\2\2`\u0236\3\2\2\2b\u0238\3\2\2\2")
        buf.write("d\u024c\3\2\2\2f\u026b\3\2\2\2h\u027f\3\2\2\2j\u0281\3")
        buf.write("\2\2\2l\u0283\3\2\2\2n\u0285\3\2\2\2p\u0287\3\2\2\2r\u0289")
        buf.write("\3\2\2\2t\u028b\3\2\2\2v\u02a2\3\2\2\2x\u02a4\3\2\2\2")
        buf.write("z\u02a9\3\2\2\2|\u02ae\3\2\2\2~\u02b3\3\2\2\2\u0080\u02bc")
        buf.write("\3\2\2\2\u0082\u02c7\3\2\2\2\u0084\u02d4\3\2\2\2\u0086")
        buf.write("\u02d6\3\2\2\2\u0088\u02ed\3\2\2\2\u008a\u02f5\3\2\2\2")
        buf.write("\u008c\u02f7\3\2\2\2\u008e\u0301\3\2\2\2\u0090\u0306\3")
        buf.write("\2\2\2\u0092\u0329\3\2\2\2\u0094\u032b\3\2\2\2\u0096\u0331")
        buf.write("\3\2\2\2\u0098\u033f\3\2\2\2\u009a\u0341\3\2\2\2\u009c")
        buf.write("\u0346\3\2\2\2\u009e\u03a0\3\2\2\2\u00a0\u00a3\5\4\3\2")
        buf.write("\u00a1\u00a3\5t;\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2")
        buf.write("\2\2\u00a3\3\3\2\2\2\u00a4\u00a5\7\3\2\2\u00a5\u00a6\7")
        buf.write("\4\2\2\u00a6\u00a8\5\6\4\2\u00a7\u00a9\5\b\5\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa")
        buf.write("\u00ac\5\n\6\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ae\3\2\2\2\u00ad\u00af\5$\23\2\u00ae\u00ad\3")
        buf.write("\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2")
        buf.write("\5&\24\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00b5\5\32\16\2\u00b4\u00b3\3\2\2")
        buf.write("\2\u00b4\u00b5\3\2\2\2\u00b5\u00b9\3\2\2\2\u00b6\u00b8")
        buf.write("\5\60\31\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bc\u00bd\7\5\2\2\u00bd\5\3\2\2")
        buf.write("\2\u00be\u00bf\7\3\2\2\u00bf\u00c0\7\6\2\2\u00c0\u00c1")
        buf.write("\7R\2\2\u00c1\u00c2\7\5\2\2\u00c2\7\3\2\2\2\u00c3\u00c4")
        buf.write("\7\3\2\2\u00c4\u00c6\7\7\2\2\u00c5\u00c7\7Q\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\7")
        buf.write("\5\2\2\u00cb\t\3\2\2\2\u00cc\u00cd\7\3\2\2\u00cd\u00ce")
        buf.write("\7\b\2\2\u00ce\u00cf\5\22\n\2\u00cf\u00d0\7\5\2\2\u00d0")
        buf.write("\13\3\2\2\2\u00d1\u00d5\7[\2\2\u00d2\u00d5\7\\\2\2\u00d3")
        buf.write("\u00d5\7^\2\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d3\3\2\2\2\u00d5\r\3\2\2\2\u00d6\u00d9\5\f\7")
        buf.write("\2\u00d7\u00d9\7]\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7")
        buf.write("\3\2\2\2\u00d9\17\3\2\2\2\u00da\u00dc\7R\2\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\21\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0")
        buf.write("\u00e9\5\20\t\2\u00e1\u00e3\5\24\13\2\u00e2\u00e1\3\2")
        buf.write("\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\5\20\t\2\u00e7")
        buf.write("\u00e9\3\2\2\2\u00e8\u00e0\3\2\2\2\u00e8\u00e2\3\2\2\2")
        buf.write("\u00e9\23\3\2\2\2\u00ea\u00eb\7R\2\2\u00eb\u00ec\5\20")
        buf.write("\t\2\u00ec\u00ed\7\t\2\2\u00ed\u00ee\5\26\f\2\u00ee\25")
        buf.write("\3\2\2\2\u00ef\u00f0\7\3\2\2\u00f0\u00f2\7\n\2\2\u00f1")
        buf.write("\u00f3\5\30\r\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6\u00f7\7\5\2\2\u00f7\u00fa\3\2\2\2\u00f8")
        buf.write("\u00fa\5\30\r\2\u00f9\u00ef\3\2\2\2\u00f9\u00f8\3\2\2")
        buf.write("\2\u00fa\27\3\2\2\2\u00fb\u00fe\7R\2\2\u00fc\u00fe\5\16")
        buf.write("\b\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\31")
        buf.write("\3\2\2\2\u00ff\u0100\7\3\2\2\u0100\u0104\7\13\2\2\u0101")
        buf.write("\u0103\5\34\17\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2")
        buf.write("\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0107")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7\5\2\2\u0108")
        buf.write("\33\3\2\2\2\u0109\u010c\5\36\20\2\u010a\u010c\5 \21\2")
        buf.write("\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c\35\3\2")
        buf.write("\2\2\u010d\u010e\7\3\2\2\u010e\u010f\5\"\22\2\u010f\u0110")
        buf.write("\5,\27\2\u0110\u0111\7\5\2\2\u0111\u0112\7\t\2\2\u0112")
        buf.write("\u0113\5\30\r\2\u0113\37\3\2\2\2\u0114\u0115\7\3\2\2\u0115")
        buf.write("\u0116\5\"\22\2\u0116\u0117\5,\27\2\u0117\u0118\7\5\2")
        buf.write("\2\u0118!\3\2\2\2\u0119\u011a\t\2\2\2\u011a#\3\2\2\2\u011b")
        buf.write("\u011c\7\3\2\2\u011c\u011d\7\f\2\2\u011d\u011e\5\22\n")
        buf.write("\2\u011e\u011f\7\5\2\2\u011f%\3\2\2\2\u0120\u0121\7\3")
        buf.write("\2\2\u0121\u0125\7\r\2\2\u0122\u0124\5(\25\2\u0123\u0122")
        buf.write("\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0128\u0129\7\5\2\2\u0129\'\3\2\2\2\u012a\u012b\7\3\2")
        buf.write("\2\u012b\u012c\5*\26\2\u012c\u012d\5,\27\2\u012d\u012e")
        buf.write("\7\5\2\2\u012e)\3\2\2\2\u012f\u0130\7R\2\2\u0130+\3\2")
        buf.write("\2\2\u0131\u0133\7T\2\2\u0132\u0131\3\2\2\2\u0133\u0136")
        buf.write("\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0143\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0139\5.\30\2")
        buf.write("\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3")
        buf.write("\2\2\2\u013a\u013b\3\2\2\2\u013b\u013f\3\2\2\2\u013c\u013e")
        buf.write("\7T\2\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2\2\u013f")
        buf.write("\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0143\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0142\u0134\3\2\2\2\u0142\u0138\3")
        buf.write("\2\2\2\u0143-\3\2\2\2\u0144\u0146\7T\2\2\u0145\u0144\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\7\t\2\2\u014a")
        buf.write("\u014b\5\30\r\2\u014b/\3\2\2\2\u014c\u0152\5\62\32\2\u014d")
        buf.write("\u0152\5\66\34\2\u014e\u0152\5V,\2\u014f\u0152\5\64\33")
        buf.write("\2\u0150\u0152\5N(\2\u0151\u014c\3\2\2\2\u0151\u014d\3")
        buf.write("\2\2\2\u0151\u014e\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152\61\3\2\2\2\u0153\u0154\7\3\2\2\u0154\u0155")
        buf.write("\7\16\2\2\u0155\u0156\58\35\2\u0156\u0157\7\17\2\2\u0157")
        buf.write("\u0158\7\3\2\2\u0158\u0159\5,\27\2\u0159\u015a\7\5\2\2")
        buf.write("\u015a\u015b\5> \2\u015b\u015c\7\5\2\2\u015c\63\3\2\2")
        buf.write("\2\u015d\u015e\7\3\2\2\u015e\u015f\7\20\2\2\u015f\u0160")
        buf.write("\5:\36\2\u0160\u0161\7\17\2\2\u0161\u0162\7\3\2\2\u0162")
        buf.write("\u0163\5,\27\2\u0163\u0164\7\5\2\2\u0164\u0165\7\21\2")
        buf.write("\2\u0165\u0166\5B\"\2\u0166\u0167\7\5\2\2\u0167\65\3\2")
        buf.write("\2\2\u0168\u0169\7\3\2\2\u0169\u016a\7\22\2\2\u016a\u016b")
        buf.write("\5<\37\2\u016b\u016c\7\17\2\2\u016c\u016d\7\3\2\2\u016d")
        buf.write("\u016e\5,\27\2\u016e\u016f\7\5\2\2\u016f\u0170\5> \2\u0170")
        buf.write("\u0171\7\5\2\2\u0171\67\3\2\2\2\u0172\u0173\t\2\2\2\u0173")
        buf.write("9\3\2\2\2\u0174\u0175\7R\2\2\u0175;\3\2\2\2\u0176\u0177")
        buf.write("\t\2\2\2\u0177=\3\2\2\2\u0178\u0179\7Y\2\2\u0179\u017a")
        buf.write("\5@!\2\u017a\u017b\7Z\2\2\u017b\u017c\5d\63\2\u017c?\3")
        buf.write("\2\2\2\u017d\u017e\7\3\2\2\u017e\u0181\7\5\2\2\u017f\u0181")
        buf.write("\5B\"\2\u0180\u017d\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("A\3\2\2\2\u0182\u01b3\5H%\2\u0183\u0184\7\3\2\2\u0184")
        buf.write("\u0188\7\23\2\2\u0185\u0187\5B\"\2\u0186\u0185\3\2\2\2")
        buf.write("\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u01b3")
        buf.write("\7\5\2\2\u018c\u018d\7\3\2\2\u018d\u0191\7\24\2\2\u018e")
        buf.write("\u0190\5B\"\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0194\u01b3\7\5\2\2\u0195\u0196")
        buf.write("\7\3\2\2\u0196\u0197\7\25\2\2\u0197\u0198\5B\"\2\u0198")
        buf.write("\u0199\7\5\2\2\u0199\u01b3\3\2\2\2\u019a\u019b\7\3\2\2")
        buf.write("\u019b\u019c\7\26\2\2\u019c\u019d\5B\"\2\u019d\u019e\5")
        buf.write("B\"\2\u019e\u019f\7\5\2\2\u019f\u01b3\3\2\2\2\u01a0\u01a1")
        buf.write("\7\3\2\2\u01a1\u01a2\7\27\2\2\u01a2\u01a3\7\3\2\2\u01a3")
        buf.write("\u01a4\5,\27\2\u01a4\u01a5\7\5\2\2\u01a5\u01a6\5B\"\2")
        buf.write("\u01a6\u01a7\7\5\2\2\u01a7\u01b3\3\2\2\2\u01a8\u01a9\7")
        buf.write("\3\2\2\u01a9\u01aa\7\30\2\2\u01aa\u01ab\7\3\2\2\u01ab")
        buf.write("\u01ac\5,\27\2\u01ac\u01ad\7\5\2\2\u01ad\u01ae\5B\"\2")
        buf.write("\u01ae\u01af\7\5\2\2\u01af\u01b3\3\2\2\2\u01b0\u01b3\5")
        buf.write("F$\2\u01b1\u01b3\5D#\2\u01b2\u0182\3\2\2\2\u01b2\u0183")
        buf.write("\3\2\2\2\u01b2\u018c\3\2\2\2\u01b2\u0195\3\2\2\2\u01b2")
        buf.write("\u019a\3\2\2\2\u01b2\u01a0\3\2\2\2\u01b2\u01a8\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3C\3\2\2")
        buf.write("\2\u01b4\u01b5\7\3\2\2\u01b5\u01b6\7\31\2\2\u01b6\u01b7")
        buf.write("\5J&\2\u01b7\u01b8\5J&\2\u01b8\u01b9\7\5\2\2\u01b9E\3")
        buf.write("\2\2\2\u01ba\u01bb\7\3\2\2\u01bb\u01bc\5n8\2\u01bc\u01bd")
        buf.write("\5X-\2\u01bd\u01be\5X-\2\u01be\u01bf\7\5\2\2\u01bfG\3")
        buf.write("\2\2\2\u01c0\u01c1\7\3\2\2\u01c1\u01c5\5*\26\2\u01c2\u01c4")
        buf.write("\5J&\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c8\u01c9\7\5\2\2\u01c9I\3\2\2\2\u01ca")
        buf.write("\u01d0\7R\2\2\u01cb\u01d0\7U\2\2\u01cc\u01d0\7T\2\2\u01cd")
        buf.write("\u01d0\7\32\2\2\u01ce\u01d0\5L\'\2\u01cf\u01ca\3\2\2\2")
        buf.write("\u01cf\u01cb\3\2\2\2\u01cf\u01cc\3\2\2\2\u01cf\u01cd\3")
        buf.write("\2\2\2\u01cf\u01ce\3\2\2\2\u01d0K\3\2\2\2\u01d1\u01d2")
        buf.write("\7\3\2\2\u01d2\u01d6\5\"\22\2\u01d3\u01d5\5J&\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d9\u01da\7\5\2\2\u01da\u01e7\3\2\2\2\u01db\u01dc")
        buf.write("\7\3\2\2\u01dc\u01dd\5j\66\2\u01dd\u01de\5J&\2\u01de\u01df")
        buf.write("\5J&\2\u01df\u01e0\7\5\2\2\u01e0\u01e7\3\2\2\2\u01e1\u01e2")
        buf.write("\7\3\2\2\u01e2\u01e3\5l\67\2\u01e3\u01e4\5J&\2\u01e4\u01e5")
        buf.write("\7\5\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01d1\3\2\2\2\u01e6")
        buf.write("\u01db\3\2\2\2\u01e6\u01e1\3\2\2\2\u01e7M\3\2\2\2\u01e8")
        buf.write("\u01e9\7\3\2\2\u01e9\u01ea\7\33\2\2\u01ea\u01eb\58\35")
        buf.write("\2\u01eb\u01ec\7\17\2\2\u01ec\u01ed\7\3\2\2\u01ed\u01ee")
        buf.write("\5,\27\2\u01ee\u01ef\7\5\2\2\u01ef\u01f0\5P)\2\u01f0\u01f1")
        buf.write("\7\5\2\2\u01f1O\3\2\2\2\u01f2\u01f3\7Y\2\2\u01f3\u01f4")
        buf.write("\5@!\2\u01f4\u01f5\7Z\2\2\u01f5\u01f6\5R*\2\u01f6Q\3\2")
        buf.write("\2\2\u01f7\u01f8\7\3\2\2\u01f8\u01fc\7\23\2\2\u01f9\u01fb")
        buf.write("\5T+\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01ff\u0202\7\5\2\2\u0200\u0202\5T+\2\u0201")
        buf.write("\u01f7\3\2\2\2\u0201\u0200\3\2\2\2\u0202S\3\2\2\2\u0203")
        buf.write("\u0204\7\3\2\2\u0204\u0205\5r:\2\u0205\u0206\5L\'\2\u0206")
        buf.write("\u0207\5Z.\2\u0207\u0208\7\5\2\2\u0208U\3\2\2\2\u0209")
        buf.write("\u020a\7\3\2\2\u020a\u020b\7\34\2\2\u020b\u020c\5,\27")
        buf.write("\2\u020c\u020d\5B\"\2\u020d\u020e\7\5\2\2\u020eW\3\2\2")
        buf.write("\2\u020f\u0213\5L\'\2\u0210\u0213\7U\2\2\u0211\u0213\7")
        buf.write("T\2\2\u0212\u020f\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0211")
        buf.write("\3\2\2\2\u0213Y\3\2\2\2\u0214\u0215\7\3\2\2\u0215\u0216")
        buf.write("\7\35\2\2\u0216\u0217\5\\/\2\u0217\u0218\7\5\2\2\u0218")
        buf.write("\u0224\3\2\2\2\u0219\u021a\7\3\2\2\u021a\u021b\7\35\2")
        buf.write("\2\u021b\u021c\5^\60\2\u021c\u021d\7\5\2\2\u021d\u0224")
        buf.write("\3\2\2\2\u021e\u021f\7\3\2\2\u021f\u0220\7\35\2\2\u0220")
        buf.write("\u0221\5`\61\2\u0221\u0222\7\5\2\2\u0222\u0224\3\2\2\2")
        buf.write("\u0223\u0214\3\2\2\2\u0223\u0219\3\2\2\2\u0223\u021e\3")
        buf.write("\2\2\2\u0224[\3\2\2\2\u0225\u0226\5L\'\2\u0226\u0227\7")
        buf.write("\32\2\2\u0227\u022b\3\2\2\2\u0228\u0229\7\32\2\2\u0229")
        buf.write("\u022b\5L\'\2\u022a\u0225\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022b]\3\2\2\2\u022c\u022d\7U\2\2\u022d\u0231\7\32\2")
        buf.write("\2\u022e\u022f\7\32\2\2\u022f\u0231\7U\2\2\u0230\u022c")
        buf.write("\3\2\2\2\u0230\u022e\3\2\2\2\u0231_\3\2\2\2\u0232\u0233")
        buf.write("\7T\2\2\u0233\u0237\7\32\2\2\u0234\u0235\7\32\2\2\u0235")
        buf.write("\u0237\7T\2\2\u0236\u0232\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0237a\3\2\2\2\u0238\u0239\7\3\2\2\u0239\u023d\5\"\22")
        buf.write("\2\u023a\u023c\5J&\2\u023b\u023a\3\2\2\2\u023c\u023f\3")
        buf.write("\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0241\7\5\2\2\u0241")
        buf.write("c\3\2\2\2\u0242\u0243\7\3\2\2\u0243\u0247\7\23\2\2\u0244")
        buf.write("\u0246\5f\64\2\u0245\u0244\3\2\2\2\u0246\u0249\3\2\2\2")
        buf.write("\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a\3")
        buf.write("\2\2\2\u0249\u0247\3\2\2\2\u024a\u024d\7\5\2\2\u024b\u024d")
        buf.write("\5f\64\2\u024c\u0242\3\2\2\2\u024c\u024b\3\2\2\2\u024d")
        buf.write("e\3\2\2\2\u024e\u024f\7\3\2\2\u024f\u0250\7\30\2\2\u0250")
        buf.write("\u0251\7\3\2\2\u0251\u0252\5,\27\2\u0252\u0253\7\5\2\2")
        buf.write("\u0253\u0254\5d\63\2\u0254\u0255\7\5\2\2\u0255\u026c\3")
        buf.write("\2\2\2\u0256\u0257\7\3\2\2\u0257\u0258\7\36\2\2\u0258")
        buf.write("\u0259\5B\"\2\u0259\u025a\5h\65\2\u025a\u025b\7\5\2\2")
        buf.write("\u025b\u026c\3\2\2\2\u025c\u025d\7\3\2\2\u025d\u025e\7")
        buf.write("\36\2\2\u025e\u025f\5B\"\2\u025f\u0260\7\3\2\2\u0260\u0264")
        buf.write("\7\23\2\2\u0261\u0263\5h\65\2\u0262\u0261\3\2\2\2\u0263")
        buf.write("\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2")
        buf.write("\u0265\u0267\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0268\7")
        buf.write("\5\2\2\u0268\u0269\7\5\2\2\u0269\u026c\3\2\2\2\u026a\u026c")
        buf.write("\5h\65\2\u026b\u024e\3\2\2\2\u026b\u0256\3\2\2\2\u026b")
        buf.write("\u025c\3\2\2\2\u026b\u026a\3\2\2\2\u026cg\3\2\2\2\u026d")
        buf.write("\u026e\7\3\2\2\u026e\u026f\5p9\2\u026f\u0270\5L\'\2\u0270")
        buf.write("\u0271\5X-\2\u0271\u0272\7\5\2\2\u0272\u0280\3\2\2\2\u0273")
        buf.write("\u0274\7\3\2\2\u0274\u0275\7\25\2\2\u0275\u0276\5H%\2")
        buf.write("\u0276\u0277\7\5\2\2\u0277\u0280\3\2\2\2\u0278\u0280\5")
        buf.write("H%\2\u0279\u027a\7\3\2\2\u027a\u027b\7\37\2\2\u027b\u027c")
        buf.write("\5L\'\2\u027c\u027d\5J&\2\u027d\u027e\7\5\2\2\u027e\u0280")
        buf.write("\3\2\2\2\u027f\u026d\3\2\2\2\u027f\u0273\3\2\2\2\u027f")
        buf.write("\u0278\3\2\2\2\u027f\u0279\3\2\2\2\u0280i\3\2\2\2\u0281")
        buf.write("\u0282\t\3\2\2\u0282k\3\2\2\2\u0283\u0284\t\4\2\2\u0284")
        buf.write("m\3\2\2\2\u0285\u0286\t\5\2\2\u0286o\3\2\2\2\u0287\u0288")
        buf.write("\t\6\2\2\u0288q\3\2\2\2\u0289\u028a\t\7\2\2\u028as\3\2")
        buf.write("\2\2\u028b\u028c\7\3\2\2\u028c\u028d\7\4\2\2\u028d\u028e")
        buf.write("\5x=\2\u028e\u0290\5z>\2\u028f\u0291\5\b\5\2\u0290\u028f")
        buf.write("\3\2\2\2\u0290\u0291\3\2\2\2\u0291\u0293\3\2\2\2\u0292")
        buf.write("\u0294\5|?\2\u0293\u0292\3\2\2\2\u0293\u0294\3\2\2\2\u0294")
        buf.write("\u0295\3\2\2\2\u0295\u0296\5\u0082B\2\u0296\u029a\5\u008e")
        buf.write("H\2\u0297\u0299\5v<\2\u0298\u0297\3\2\2\2\u0299\u029c")
        buf.write("\3\2\2\2\u029a\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b")
        buf.write("\u029d\3\2\2\2\u029c\u029a\3\2\2\2\u029d\u029e\7\5\2\2")
        buf.write("\u029eu\3\2\2\2\u029f\u02a3\5\u0090I\2\u02a0\u02a3\5~")
        buf.write("@\2\u02a1\u02a3\5\u0094K\2\u02a2\u029f\3\2\2\2\u02a2\u02a0")
        buf.write("\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3w\3\2\2\2\u02a4\u02a5")
        buf.write("\7\3\2\2\u02a5\u02a6\7\66\2\2\u02a6\u02a7\7R\2\2\u02a7")
        buf.write("\u02a8\7\5\2\2\u02a8y\3\2\2\2\u02a9\u02aa\7\3\2\2\u02aa")
        buf.write("\u02ab\7\67\2\2\u02ab\u02ac\7R\2\2\u02ac\u02ad\7\5\2\2")
        buf.write("\u02ad{\3\2\2\2\u02ae\u02af\7\3\2\2\u02af\u02b0\78\2\2")
        buf.write("\u02b0\u02b1\5\22\n\2\u02b1\u02b2\7\5\2\2\u02b2}\3\2\2")
        buf.write("\2\u02b3\u02b4\7\3\2\2\u02b4\u02b6\79\2\2\u02b5\u02b7")
        buf.write("\5\u0080A\2\u02b6\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8")
        buf.write("\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02ba\3\2\2\2")
        buf.write("\u02ba\u02bb\7\5\2\2\u02bb\177\3\2\2\2\u02bc\u02bd\7\3")
        buf.write("\2\2\u02bd\u02be\7R\2\2\u02be\u02bf\7\t\2\2\u02bf\u02c0")
        buf.write("\5\f\7\2\u02c0\u02c1\7:\2\2\u02c1\u02c2\7U\2\2\u02c2\u02c3")
        buf.write("\7;\2\2\u02c3\u02c4\7U\2\2\u02c4\u02c5\7<\2\2\u02c5\u02c6")
        buf.write("\7\5\2\2\u02c6\u0081\3\2\2\2\u02c7\u02c8\7\3\2\2\u02c8")
        buf.write("\u02cc\7X\2\2\u02c9\u02cb\5\u0088E\2\u02ca\u02c9\3\2\2")
        buf.write("\2\u02cb\u02ce\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cc\u02cd")
        buf.write("\3\2\2\2\u02cd\u02cf\3\2\2\2\u02ce\u02cc\3\2\2\2\u02cf")
        buf.write("\u02d0\7\5\2\2\u02d0\u0083\3\2\2\2\u02d1\u02d5\7R\2\2")
        buf.write("\u02d2\u02d5\7U\2\2\u02d3\u02d5\5\u0086D\2\u02d4\u02d1")
        buf.write("\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d4\u02d3\3\2\2\2\u02d5")
        buf.write("\u0085\3\2\2\2\u02d6\u02d7\7\3\2\2\u02d7\u02db\5\"\22")
        buf.write("\2\u02d8\u02da\5\u0084C\2\u02d9\u02d8\3\2\2\2\u02da\u02dd")
        buf.write("\3\2\2\2\u02db\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc")
        buf.write("\u02de\3\2\2\2\u02dd\u02db\3\2\2\2\u02de\u02df\7\5\2\2")
        buf.write("\u02df\u0087\3\2\2\2\u02e0\u02ee\5\u008aF\2\u02e1\u02e2")
        buf.write("\7\3\2\2\u02e2\u02e3\7\31\2\2\u02e3\u02e4\5\u0086D\2\u02e4")
        buf.write("\u02e5\7U\2\2\u02e5\u02e6\7\5\2\2\u02e6\u02ee\3\2\2\2")
        buf.write("\u02e7\u02e8\7\3\2\2\u02e8\u02e9\7\31\2\2\u02e9\u02ea")
        buf.write("\5\u0086D\2\u02ea\u02eb\7R\2\2\u02eb\u02ec\7\5\2\2\u02ec")
        buf.write("\u02ee\3\2\2\2\u02ed\u02e0\3\2\2\2\u02ed\u02e1\3\2\2\2")
        buf.write("\u02ed\u02e7\3\2\2\2\u02ee\u0089\3\2\2\2\u02ef\u02f6\5")
        buf.write("\u008cG\2\u02f0\u02f1\7\3\2\2\u02f1\u02f2\7\25\2\2\u02f2")
        buf.write("\u02f3\5\u008cG\2\u02f3\u02f4\7\5\2\2\u02f4\u02f6\3\2")
        buf.write("\2\2\u02f5\u02ef\3\2\2\2\u02f5\u02f0\3\2\2\2\u02f6\u008b")
        buf.write("\3\2\2\2\u02f7\u02f8\7\3\2\2\u02f8\u02fc\5*\26\2\u02f9")
        buf.write("\u02fb\5\u0084C\2\u02fa\u02f9\3\2\2\2\u02fb\u02fe\3\2")
        buf.write("\2\2\u02fc\u02fa\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd\u02ff")
        buf.write("\3\2\2\2\u02fe\u02fc\3\2\2\2\u02ff\u0300\7\5\2\2\u0300")
        buf.write("\u008d\3\2\2\2\u0301\u0302\7\3\2\2\u0302\u0303\7=\2\2")
        buf.write("\u0303\u0304\5B\"\2\u0304\u0305\7\5\2\2\u0305\u008f\3")
        buf.write("\2\2\2\u0306\u0307\7\3\2\2\u0307\u0308\7>\2\2\u0308\u0309")
        buf.write("\5\u0092J\2\u0309\u030a\7\5\2\2\u030a\u0091\3\2\2\2\u030b")
        buf.write("\u030c\7\3\2\2\u030c\u0310\7\23\2\2\u030d\u030f\5\u0092")
        buf.write("J\2\u030e\u030d\3\2\2\2\u030f\u0312\3\2\2\2\u0310\u030e")
        buf.write("\3\2\2\2\u0310\u0311\3\2\2\2\u0311\u0313\3\2\2\2\u0312")
        buf.write("\u0310\3\2\2\2\u0313\u032a\7\5\2\2\u0314\u0315\7\3\2\2")
        buf.write("\u0315\u0316\7\30\2\2\u0316\u0317\7\3\2\2\u0317\u0318")
        buf.write("\5,\27\2\u0318\u0319\7\5\2\2\u0319\u031a\5\u0092J\2\u031a")
        buf.write("\u031b\7\5\2\2\u031b\u032a\3\2\2\2\u031c\u031d\7\3\2\2")
        buf.write("\u031d\u031f\7?\2\2\u031e\u0320\7R\2\2\u031f\u031e\3\2")
        buf.write("\2\2\u031f\u0320\3\2\2\2\u0320\u0321\3\2\2\2\u0321\u0322")
        buf.write("\5\u009eP\2\u0322\u0323\7\5\2\2\u0323\u032a\3\2\2\2\u0324")
        buf.write("\u0326\5\u009eP\2\u0325\u0324\3\2\2\2\u0326\u0327\3\2")
        buf.write("\2\2\u0327\u0325\3\2\2\2\u0327\u0328\3\2\2\2\u0328\u032a")
        buf.write("\3\2\2\2\u0329\u030b\3\2\2\2\u0329\u0314\3\2\2\2\u0329")
        buf.write("\u031c\3\2\2\2\u0329\u0325\3\2\2\2\u032a\u0093\3\2\2\2")
        buf.write("\u032b\u032c\7\3\2\2\u032c\u032d\7@\2\2\u032d\u032e\5")
        buf.write("\u0096L\2\u032e\u032f\5\u0098M\2\u032f\u0330\7\5\2\2\u0330")
        buf.write("\u0095\3\2\2\2\u0331\u0332\t\b\2\2\u0332\u0097\3\2\2\2")
        buf.write("\u0333\u0340\5L\'\2\u0334\u0335\5\u009aN\2\u0335\u0336")
        buf.write("\5\u009cO\2\u0336\u0340\3\2\2\2\u0337\u0338\5\u009cO\2")
        buf.write("\u0338\u0339\5\u009aN\2\u0339\u0340\3\2\2\2\u033a\u0340")
        buf.write("\7C\2\2\u033b\u033c\7\3\2\2\u033c\u033d\7D\2\2\u033d\u033e")
        buf.write("\7R\2\2\u033e\u0340\7\5\2\2\u033f\u0333\3\2\2\2\u033f")
        buf.write("\u0334\3\2\2\2\u033f\u0337\3\2\2\2\u033f\u033a\3\2\2\2")
        buf.write("\u033f\u033b\3\2\2\2\u0340\u0099\3\2\2\2\u0341\u0342\7")
        buf.write("\3\2\2\u0342\u0343\7E\2\2\u0343\u0344\5L\'\2\u0344\u0345")
        buf.write("\7\5\2\2\u0345\u009b\3\2\2\2\u0346\u0347\7\3\2\2\u0347")
        buf.write("\u0348\7F\2\2\u0348\u0349\5L\'\2\u0349\u034a\7\5\2\2\u034a")
        buf.write("\u009d\3\2\2\2\u034b\u034c\7\3\2\2\u034c\u034e\7\23\2")
        buf.write("\2\u034d\u034f\5\u009eP\2\u034e\u034d\3\2\2\2\u034f\u0350")
        buf.write("\3\2\2\2\u0350\u034e\3\2\2\2\u0350\u0351\3\2\2\2\u0351")
        buf.write("\u0352\3\2\2\2\u0352\u0353\7\5\2\2\u0353\u03a1\3\2\2\2")
        buf.write("\u0354\u0355\7\3\2\2\u0355\u0356\7\30\2\2\u0356\u0357")
        buf.write("\7\3\2\2\u0357\u0358\5,\27\2\u0358\u0359\7\5\2\2\u0359")
        buf.write("\u035a\5\u009eP\2\u035a\u035b\7\5\2\2\u035b\u03a1\3\2")
        buf.write("\2\2\u035c\u035d\7\3\2\2\u035d\u035e\7G\2\2\u035e\u035f")
        buf.write("\5B\"\2\u035f\u0360\7\5\2\2\u0360\u03a1\3\2\2\2\u0361")
        buf.write("\u0362\7\3\2\2\u0362\u0363\7H\2\2\u0363\u0364\5B\"\2\u0364")
        buf.write("\u0365\7\5\2\2\u0365\u03a1\3\2\2\2\u0366\u0367\7\3\2\2")
        buf.write("\u0367\u0368\7I\2\2\u0368\u0369\5B\"\2\u0369\u036a\7\5")
        buf.write("\2\2\u036a\u03a1\3\2\2\2\u036b\u036c\7\3\2\2\u036c\u036d")
        buf.write("\7J\2\2\u036d\u036e\7U\2\2\u036e\u036f\5B\"\2\u036f\u0370")
        buf.write("\7\5\2\2\u0370\u03a1\3\2\2\2\u0371\u0372\7\3\2\2\u0372")
        buf.write("\u0373\7K\2\2\u0373\u0374\5B\"\2\u0374\u0375\7\5\2\2\u0375")
        buf.write("\u03a1\3\2\2\2\u0376\u0377\7\3\2\2\u0377\u0378\7L\2\2")
        buf.write("\u0378\u0379\5B\"\2\u0379\u037a\5B\"\2\u037a\u037b\7\5")
        buf.write("\2\2\u037b\u03a1\3\2\2\2\u037c\u037d\7\3\2\2\u037d\u037e")
        buf.write("\7M\2\2\u037e\u037f\5B\"\2\u037f\u0380\5B\"\2\u0380\u0381")
        buf.write("\7\5\2\2\u0381\u03a1\3\2\2\2\u0382\u0383\7\3\2\2\u0383")
        buf.write("\u0384\7N\2\2\u0384\u0385\7U\2\2\u0385\u0386\5B\"\2\u0386")
        buf.write("\u0387\5B\"\2\u0387\u0388\7\5\2\2\u0388\u03a1\3\2\2\2")
        buf.write("\u0389\u038a\7\3\2\2\u038a\u038b\7O\2\2\u038b\u038c\7")
        buf.write("U\2\2\u038c\u038d\7U\2\2\u038d\u038e\5B\"\2\u038e\u038f")
        buf.write("\7\5\2\2\u038f\u03a1\3\2\2\2\u0390\u0391\7\3\2\2\u0391")
        buf.write("\u0392\7P\2\2\u0392\u0393\7U\2\2\u0393\u0394\5B\"\2\u0394")
        buf.write("\u0395\7\5\2\2\u0395\u03a1\3\2\2\2\u0396\u0397\7\3\2\2")
        buf.write("\u0397\u0399\7S\2\2\u0398\u039a\5\u0086D\2\u0399\u0398")
        buf.write("\3\2\2\2\u039a\u039b\3\2\2\2\u039b\u0399\3\2\2\2\u039b")
        buf.write("\u039c\3\2\2\2\u039c\u039d\3\2\2\2\u039d\u039e\7\5\2\2")
        buf.write("\u039e\u03a1\3\2\2\2\u039f\u03a1\5B\"\2\u03a0\u034b\3")
        buf.write("\2\2\2\u03a0\u0354\3\2\2\2\u03a0\u035c\3\2\2\2\u03a0\u0361")
        buf.write("\3\2\2\2\u03a0\u0366\3\2\2\2\u03a0\u036b\3\2\2\2\u03a0")
        buf.write("\u0371\3\2\2\2\u03a0\u0376\3\2\2\2\u03a0\u037c\3\2\2\2")
        buf.write("\u03a0\u0382\3\2\2\2\u03a0\u0389\3\2\2\2\u03a0\u0390\3")
        buf.write("\2\2\2\u03a0\u0396\3\2\2\2\u03a0\u039f\3\2\2\2\u03a1\u009f")
        buf.write("\3\2\2\2C\u00a2\u00a8\u00ab\u00ae\u00b1\u00b4\u00b9\u00c8")
        buf.write("\u00d4\u00d8\u00dd\u00e4\u00e8\u00f4\u00f9\u00fd\u0104")
        buf.write("\u010b\u0125\u0134\u013a\u013f\u0142\u0147\u0151\u0180")
        buf.write("\u0188\u0191\u01b2\u01c5\u01cf\u01d6\u01e6\u01fc\u0201")
        buf.write("\u0212\u0223\u022a\u0230\u0236\u023d\u0247\u024c\u0264")
        buf.write("\u026b\u027f\u0290\u0293\u029a\u02a2\u02b8\u02cc\u02d4")
        buf.write("\u02db\u02ed\u02f5\u02fc\u0310\u031f\u0327\u0329\u033f")
        buf.write("\u0350\u039b\u03a0")
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
    RULE_typesDef = 4
    RULE_numericBuiltinType = 5
    RULE_builtinType = 6
    RULE_nameList = 7
    RULE_typedNameList = 8
    RULE_nameListWithType = 9
    RULE_typename = 10
    RULE_primitive_type = 11
    RULE_function_definition_block = 12
    RULE_single_function_definition = 13
    RULE_typed_function_definition = 14
    RULE_untyped_function_definition = 15
    RULE_logical_symbol_name = 16
    RULE_constantsDef = 17
    RULE_predicate_definition_block = 18
    RULE_single_predicate_definition = 19
    RULE_predicate = 20
    RULE_variableList = 21
    RULE_variableListWithType = 22
    RULE_structureDef = 23
    RULE_actionDef = 24
    RULE_constraintDef = 25
    RULE_eventDef = 26
    RULE_actionName = 27
    RULE_constraintSymbol = 28
    RULE_eventSymbol = 29
    RULE_actionDefBody = 30
    RULE_precondition = 31
    RULE_goalDesc = 32
    RULE_equality = 33
    RULE_fComp = 34
    RULE_atomicTermFormula = 35
    RULE_term = 36
    RULE_functionTerm = 37
    RULE_processDef = 38
    RULE_processDefBody = 39
    RULE_processEffectList = 40
    RULE_processEffect = 41
    RULE_derivedDef = 42
    RULE_fExp = 43
    RULE_processEffectExp = 44
    RULE_processFunctionEff = 45
    RULE_processConstEff = 46
    RULE_processVarEff = 47
    RULE_fHead = 48
    RULE_effect = 49
    RULE_cEffect = 50
    RULE_atomic_effect = 51
    RULE_binaryOp = 52
    RULE_unaryBuiltIn = 53
    RULE_binaryComp = 54
    RULE_assignOp = 55
    RULE_processEffectOp = 56
    RULE_problem = 57
    RULE_problemMeta = 58
    RULE_problemDecl = 59
    RULE_problemDomain = 60
    RULE_object_declaration = 61
    RULE_boundsDecl = 62
    RULE_typeBoundsDefinition = 63
    RULE_init = 64
    RULE_groundTerm = 65
    RULE_groundFunctionTerm = 66
    RULE_initEl = 67
    RULE_nameLiteral = 68
    RULE_groundAtomicFormula = 69
    RULE_goal = 70
    RULE_probConstraints = 71
    RULE_prefConGD = 72
    RULE_metricSpec = 73
    RULE_optimization = 74
    RULE_metricFExp = 75
    RULE_terminalCost = 76
    RULE_stageCost = 77
    RULE_conGD = 78

    ruleNames =  [ "pddlDoc", "domain", "domainName", "requireDef", "typesDef", 
                   "numericBuiltinType", "builtinType", "nameList", "typedNameList", 
                   "nameListWithType", "typename", "primitive_type", "function_definition_block", 
                   "single_function_definition", "typed_function_definition", 
                   "untyped_function_definition", "logical_symbol_name", 
                   "constantsDef", "predicate_definition_block", "single_predicate_definition", 
                   "predicate", "variableList", "variableListWithType", 
                   "structureDef", "actionDef", "constraintDef", "eventDef", 
                   "actionName", "constraintSymbol", "eventSymbol", "actionDefBody", 
                   "precondition", "goalDesc", "equality", "fComp", "atomicTermFormula", 
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
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.domain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
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


        def typesDef(self):
            return self.getTypedRuleContext(fstripsParser.TypesDefContext,0)


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
            self.state = 162
            self.match(fstripsParser.T__0)
            self.state = 163
            self.match(fstripsParser.T__1)
            self.state = 164
            self.domainName()
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 165
                self.requireDef()


            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 168
                self.typesDef()


            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 171
                self.constantsDef()


            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 174
                self.predicate_definition_block()


            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 177
                self.function_definition_block()


            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 180
                self.structureDef()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
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
            self.state = 188
            self.match(fstripsParser.T__0)
            self.state = 189
            self.match(fstripsParser.T__3)
            self.state = 190
            self.match(fstripsParser.NAME)
            self.state = 191
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
            self.state = 193
            self.match(fstripsParser.T__0)
            self.state = 194
            self.match(fstripsParser.T__4)
            self.state = 196 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 195
                self.match(fstripsParser.REQUIRE_KEY)
                self.state = 198 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.REQUIRE_KEY):
                    break

            self.state = 200
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypesDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedNameList(self):
            return self.getTypedRuleContext(fstripsParser.TypedNameListContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_typesDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesDef" ):
                listener.enterTypesDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesDef" ):
                listener.exitTypesDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypesDef" ):
                return visitor.visitTypesDef(self)
            else:
                return visitor.visitChildren(self)




    def typesDef(self):

        localctx = fstripsParser.TypesDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typesDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(fstripsParser.T__0)
            self.state = 203
            self.match(fstripsParser.T__5)
            self.state = 204
            self.typedNameList()
            self.state = 205
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
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.INT_T]:
                localctx = fstripsParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(fstripsParser.INT_T)
                pass
            elif token in [fstripsParser.FLOAT_T]:
                localctx = fstripsParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(fstripsParser.FLOAT_T)
                pass
            elif token in [fstripsParser.NUMBER_T]:
                localctx = fstripsParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 209
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
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.NUMBER_T]:
                localctx = fstripsParser.NumericBuiltinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.numericBuiltinType()
                pass
            elif token in [fstripsParser.OBJECT_T]:
                localctx = fstripsParser.ObjectBuiltinContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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

    class NameListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NAME)
            else:
                return self.getToken(fstripsParser.NAME, i)

        def getRuleIndex(self):
            return fstripsParser.RULE_nameList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameList" ):
                listener.enterNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameList" ):
                listener.exitNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameList" ):
                return visitor.visitNameList(self)
            else:
                return visitor.visitChildren(self)




    def nameList(self):

        localctx = fstripsParser.NameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nameList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.NAME:
                self.state = 216
                self.match(fstripsParser.NAME)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedNameListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_typedNameList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleNameListContext(TypedNameListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TypedNameListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nameList(self):
            return self.getTypedRuleContext(fstripsParser.NameListContext,0)


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


    class ComplexNameListContext(TypedNameListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TypedNameListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nameList(self):
            return self.getTypedRuleContext(fstripsParser.NameListContext,0)

        def nameListWithType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.NameListWithTypeContext)
            else:
                return self.getTypedRuleContext(fstripsParser.NameListWithTypeContext,i)


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



    def typedNameList(self):

        localctx = fstripsParser.TypedNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typedNameList)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.SimpleNameListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.nameList()
                pass

            elif la_ == 2:
                localctx = fstripsParser.ComplexNameListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 224 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 223
                        self.nameListWithType()

                    else:
                        raise NoViableAltException(self)
                    self.state = 226 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 228
                self.nameList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameListWithTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.theType = None # TypenameContext

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def nameList(self):
            return self.getTypedRuleContext(fstripsParser.NameListContext,0)


        def typename(self):
            return self.getTypedRuleContext(fstripsParser.TypenameContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_nameListWithType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameListWithType" ):
                listener.enterNameListWithType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameListWithType" ):
                listener.exitNameListWithType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameListWithType" ):
                return visitor.visitNameListWithType(self)
            else:
                return visitor.visitChildren(self)




    def nameListWithType(self):

        localctx = fstripsParser.NameListWithTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nameListWithType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(fstripsParser.NAME)
            self.state = 233
            self.nameList()
            self.state = 234
            self.match(fstripsParser.T__6)
            self.state = 235
            localctx.theType = self.typename()
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
        self.enterRule(localctx, 20, self.RULE_typename)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(fstripsParser.T__0)
                self.state = 238
                self.match(fstripsParser.T__7)
                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 239
                    self.primitive_type()
                    self.state = 242 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.INT_T - 80)) | (1 << (fstripsParser.FLOAT_T - 80)) | (1 << (fstripsParser.OBJECT_T - 80)) | (1 << (fstripsParser.NUMBER_T - 80)))) != 0)):
                        break

                self.state = 244
                self.match(fstripsParser.T__2)
                pass
            elif token in [fstripsParser.NAME, fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.OBJECT_T, fstripsParser.NUMBER_T]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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
        self.enterRule(localctx, 22, self.RULE_primitive_type)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(fstripsParser.NAME)
                pass
            elif token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.OBJECT_T, fstripsParser.NUMBER_T]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
        self.enterRule(localctx, 24, self.RULE_function_definition_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(fstripsParser.T__0)
            self.state = 254
            self.match(fstripsParser.T__8)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 255
                self.single_function_definition()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 261
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
        self.enterRule(localctx, 26, self.RULE_single_function_definition)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.typed_function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 28, self.RULE_typed_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(fstripsParser.T__0)
            self.state = 268
            self.logical_symbol_name()
            self.state = 269
            self.variableList()
            self.state = 270
            self.match(fstripsParser.T__2)
            self.state = 271
            self.match(fstripsParser.T__6)
            self.state = 272
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 30, self.RULE_untyped_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(fstripsParser.T__0)
            self.state = 275
            self.logical_symbol_name()
            self.state = 276
            self.variableList()
            self.state = 277
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
        self.enterRule(localctx, 32, self.RULE_logical_symbol_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
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

        def typedNameList(self):
            return self.getTypedRuleContext(fstripsParser.TypedNameListContext,0)


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
        self.enterRule(localctx, 34, self.RULE_constantsDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(fstripsParser.T__0)
            self.state = 282
            self.match(fstripsParser.T__9)
            self.state = 283
            self.typedNameList()
            self.state = 284
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
        self.enterRule(localctx, 36, self.RULE_predicate_definition_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(fstripsParser.T__0)
            self.state = 287
            self.match(fstripsParser.T__10)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 288
                self.single_predicate_definition()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 294
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 38, self.RULE_single_predicate_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(fstripsParser.T__0)
            self.state = 297
            self.predicate()
            self.state = 298
            self.variableList()
            self.state = 299
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
        self.enterRule(localctx, 40, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(fstripsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_variableList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UntypedVariableListContext(VariableListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.VariableListContext
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


    class TypedVariableListContext(VariableListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.VariableListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variableListWithType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.VariableListWithTypeContext)
            else:
                return self.getTypedRuleContext(fstripsParser.VariableListWithTypeContext,i)

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



    def variableList(self):

        localctx = fstripsParser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variableList)
        self._la = 0 # Token type
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.UntypedVariableListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.VARIABLE:
                    self.state = 303
                    self.match(fstripsParser.VARIABLE)
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = fstripsParser.TypedVariableListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 310 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 309
                        self.variableListWithType()

                    else:
                        raise NoViableAltException(self)
                    self.state = 312 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.VARIABLE:
                    self.state = 314
                    self.match(fstripsParser.VARIABLE)
                    self.state = 319
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

    class VariableListWithTypeContext(ParserRuleContext):

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
            return fstripsParser.RULE_variableListWithType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableListWithType" ):
                listener.enterVariableListWithType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableListWithType" ):
                listener.exitVariableListWithType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableListWithType" ):
                return visitor.visitVariableListWithType(self)
            else:
                return visitor.visitChildren(self)




    def variableListWithType(self):

        localctx = fstripsParser.VariableListWithTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableListWithType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 322
                self.match(fstripsParser.VARIABLE)
                self.state = 325 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.VARIABLE):
                    break

            self.state = 327
            self.match(fstripsParser.T__6)
            self.state = 328
            self.primitive_type()
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
        self.enterRule(localctx, 46, self.RULE_structureDef)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.actionDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.eventDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.derivedDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 333
                self.constraintDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 334
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 48, self.RULE_actionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(fstripsParser.T__0)
            self.state = 338
            self.match(fstripsParser.T__11)
            self.state = 339
            self.actionName()
            self.state = 340
            self.match(fstripsParser.T__12)
            self.state = 341
            self.match(fstripsParser.T__0)
            self.state = 342
            self.variableList()
            self.state = 343
            self.match(fstripsParser.T__2)
            self.state = 344
            self.actionDefBody()
            self.state = 345
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 50, self.RULE_constraintDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(fstripsParser.T__0)
            self.state = 348
            self.match(fstripsParser.T__13)
            self.state = 349
            self.constraintSymbol()
            self.state = 350
            self.match(fstripsParser.T__12)
            self.state = 351
            self.match(fstripsParser.T__0)
            self.state = 352
            self.variableList()
            self.state = 353
            self.match(fstripsParser.T__2)
            self.state = 354
            self.match(fstripsParser.T__14)
            self.state = 355
            self.goalDesc()
            self.state = 356
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 52, self.RULE_eventDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(fstripsParser.T__0)
            self.state = 359
            self.match(fstripsParser.T__15)
            self.state = 360
            self.eventSymbol()
            self.state = 361
            self.match(fstripsParser.T__12)
            self.state = 362
            self.match(fstripsParser.T__0)
            self.state = 363
            self.variableList()
            self.state = 364
            self.match(fstripsParser.T__2)
            self.state = 365
            self.actionDefBody()
            self.state = 366
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
        self.enterRule(localctx, 54, self.RULE_actionName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 56, self.RULE_constraintSymbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
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
        self.enterRule(localctx, 58, self.RULE_eventSymbol)
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
        self.enterRule(localctx, 60, self.RULE_actionDefBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(fstripsParser.K_PRECONDITION)
            self.state = 375
            self.precondition()
            self.state = 376
            self.match(fstripsParser.K_EFFECT)
            self.state = 377
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
        self.enterRule(localctx, 62, self.RULE_precondition)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.TrivialPreconditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(fstripsParser.T__0)
                self.state = 380
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.RegularPreconditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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

        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)

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

        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)

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
        self.enterRule(localctx, 64, self.RULE_goalDesc)
        self._la = 0 # Token type
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.TermGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.atomicTermFormula()
                pass

            elif la_ == 2:
                localctx = fstripsParser.AndGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.match(fstripsParser.T__0)
                self.state = 386
                self.match(fstripsParser.T__16)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 387
                    self.goalDesc()
                    self.state = 392
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 393
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.OrGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.match(fstripsParser.T__0)
                self.state = 395
                self.match(fstripsParser.T__17)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 396
                    self.goalDesc()
                    self.state = 401
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 402
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.NotGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.match(fstripsParser.T__0)
                self.state = 404
                self.match(fstripsParser.T__18)
                self.state = 405
                self.goalDesc()
                self.state = 406
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 5:
                localctx = fstripsParser.ImplyGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.match(fstripsParser.T__0)
                self.state = 409
                self.match(fstripsParser.T__19)
                self.state = 410
                self.goalDesc()
                self.state = 411
                self.goalDesc()
                self.state = 412
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 6:
                localctx = fstripsParser.ExistentialGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 414
                self.match(fstripsParser.T__0)
                self.state = 415
                self.match(fstripsParser.T__20)
                self.state = 416
                self.match(fstripsParser.T__0)
                self.state = 417
                self.variableList()
                self.state = 418
                self.match(fstripsParser.T__2)
                self.state = 419
                self.goalDesc()
                self.state = 420
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 7:
                localctx = fstripsParser.UniversalGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 422
                self.match(fstripsParser.T__0)
                self.state = 423
                self.match(fstripsParser.T__21)
                self.state = 424
                self.match(fstripsParser.T__0)
                self.state = 425
                self.variableList()
                self.state = 426
                self.match(fstripsParser.T__2)
                self.state = 427
                self.goalDesc()
                self.state = 428
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 8:
                localctx = fstripsParser.ComparisonGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 430
                self.fComp()
                pass

            elif la_ == 9:
                localctx = fstripsParser.EqualityGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 431
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
        self.enterRule(localctx, 66, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(fstripsParser.T__0)
            self.state = 435
            self.match(fstripsParser.T__22)
            self.state = 436
            self.term()
            self.state = 437
            self.term()
            self.state = 438
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
        self.enterRule(localctx, 68, self.RULE_fComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(fstripsParser.T__0)
            self.state = 441
            self.binaryComp()
            self.state = 442
            self.fExp()
            self.state = 443
            self.fExp()
            self.state = 444
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
        self.enterRule(localctx, 70, self.RULE_atomicTermFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(fstripsParser.T__0)
            self.state = 447
            self.predicate()
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.T__23 or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.VARIABLE - 80)) | (1 << (fstripsParser.NUMBER - 80)))) != 0):
                self.state = 448
                self.term()
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 454
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
        self.enterRule(localctx, 72, self.RULE_term)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                localctx = fstripsParser.TermObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(fstripsParser.NAME)
                pass
            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.TermNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(fstripsParser.NUMBER)
                pass
            elif token in [fstripsParser.VARIABLE]:
                localctx = fstripsParser.TermVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.match(fstripsParser.VARIABLE)
                pass
            elif token in [fstripsParser.T__23]:
                localctx = fstripsParser.TermTimeStepContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 459
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__0]:
                localctx = fstripsParser.TermFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 460
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
        self.enterRule(localctx, 74, self.RULE_functionTerm)
        self._la = 0 # Token type
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.GenericFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(fstripsParser.T__0)
                self.state = 464
                self.logical_symbol_name()
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0 or _la==fstripsParser.T__23 or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.VARIABLE - 80)) | (1 << (fstripsParser.NUMBER - 80)))) != 0):
                    self.state = 465
                    self.term()
                    self.state = 470
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 471
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.BinaryArithmeticFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.match(fstripsParser.T__0)
                self.state = 474
                self.binaryOp()
                self.state = 475
                self.term()
                self.state = 476
                self.term()
                self.state = 477
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.UnaryArithmeticFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(fstripsParser.T__0)
                self.state = 480
                self.unaryBuiltIn()
                self.state = 481
                self.term()
                self.state = 482
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


        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 76, self.RULE_processDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(fstripsParser.T__0)
            self.state = 487
            self.match(fstripsParser.T__24)
            self.state = 488
            self.actionName()
            self.state = 489
            self.match(fstripsParser.T__12)
            self.state = 490
            self.match(fstripsParser.T__0)
            self.state = 491
            self.variableList()
            self.state = 492
            self.match(fstripsParser.T__2)
            self.state = 493
            self.processDefBody()
            self.state = 494
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
        self.enterRule(localctx, 78, self.RULE_processDefBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(fstripsParser.K_PRECONDITION)
            self.state = 497
            self.precondition()
            self.state = 498
            self.match(fstripsParser.K_EFFECT)
            self.state = 499
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
        self.enterRule(localctx, 80, self.RULE_processEffectList)
        self._la = 0 # Token type
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ProcessConjunctiveEffectFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(fstripsParser.T__0)
                self.state = 502
                self.match(fstripsParser.T__16)
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 503
                    self.processEffect()
                    self.state = 508
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 509
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ProcessSingleEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 510
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
        self.enterRule(localctx, 82, self.RULE_processEffect)
        try:
            localctx = fstripsParser.ProcessAssignEffectContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(fstripsParser.T__0)
            self.state = 514
            self.processEffectOp()
            self.state = 515
            self.functionTerm()
            self.state = 516
            self.processEffectExp()
            self.state = 517
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

        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)


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
        self.enterRule(localctx, 84, self.RULE_derivedDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(fstripsParser.T__0)
            self.state = 520
            self.match(fstripsParser.T__25)
            self.state = 521
            self.variableList()
            self.state = 522
            self.goalDesc()
            self.state = 523
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
        self.enterRule(localctx, 86, self.RULE_fExp)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                localctx = fstripsParser.FunctionExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.functionTerm()
                pass
            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.NumericConstantExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.match(fstripsParser.NUMBER)
                pass
            elif token in [fstripsParser.VARIABLE]:
                localctx = fstripsParser.VariableExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 527
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
        self.enterRule(localctx, 88, self.RULE_processEffectExp)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.FunctionalProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(fstripsParser.T__0)
                self.state = 531
                self.match(fstripsParser.T__26)
                self.state = 532
                self.processFunctionEff()
                self.state = 533
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ConstProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.match(fstripsParser.T__0)
                self.state = 536
                self.match(fstripsParser.T__26)
                self.state = 537
                self.processConstEff()
                self.state = 538
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.VariableProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.match(fstripsParser.T__0)
                self.state = 541
                self.match(fstripsParser.T__26)
                self.state = 542
                self.processVarEff()
                self.state = 543
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
        self.enterRule(localctx, 90, self.RULE_processFunctionEff)
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.functionTerm()
                self.state = 548
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.match(fstripsParser.T__23)
                self.state = 551
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
        self.enterRule(localctx, 92, self.RULE_processConstEff)
        try:
            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.match(fstripsParser.NUMBER)
                self.state = 555
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.match(fstripsParser.T__23)
                self.state = 557
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
        self.enterRule(localctx, 94, self.RULE_processVarEff)
        try:
            self.state = 564
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.match(fstripsParser.VARIABLE)
                self.state = 561
                self.match(fstripsParser.T__23)
                pass
            elif token in [fstripsParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.match(fstripsParser.T__23)
                self.state = 563
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
        self.enterRule(localctx, 96, self.RULE_fHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(fstripsParser.T__0)
            self.state = 567
            self.logical_symbol_name()
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.T__23 or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (fstripsParser.NAME - 80)) | (1 << (fstripsParser.VARIABLE - 80)) | (1 << (fstripsParser.NUMBER - 80)))) != 0):
                self.state = 568
                self.term()
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 574
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
        self.enterRule(localctx, 98, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctiveEffectFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(fstripsParser.T__0)
                self.state = 577
                self.match(fstripsParser.T__16)
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 578
                    self.cEffect()
                    self.state = 583
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 584
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.SingleEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 585
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

        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)

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
        self.enterRule(localctx, 100, self.RULE_cEffect)
        self._la = 0 # Token type
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.UniversallyQuantifiedEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.match(fstripsParser.T__0)
                self.state = 589
                self.match(fstripsParser.T__21)
                self.state = 590
                self.match(fstripsParser.T__0)
                self.state = 591
                self.variableList()
                self.state = 592
                self.match(fstripsParser.T__2)
                self.state = 593
                self.effect()
                self.state = 594
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.SingleConditionalEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(fstripsParser.T__0)
                self.state = 597
                self.match(fstripsParser.T__27)
                self.state = 598
                self.goalDesc()
                self.state = 599
                self.atomic_effect()
                self.state = 600
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.MultipleConditionalEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 602
                self.match(fstripsParser.T__0)
                self.state = 603
                self.match(fstripsParser.T__27)
                self.state = 604
                self.goalDesc()
                self.state = 605
                self.match(fstripsParser.T__0)
                self.state = 606
                self.match(fstripsParser.T__16)
                self.state = 610
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 607
                    self.atomic_effect()
                    self.state = 612
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 613
                self.match(fstripsParser.T__2)
                self.state = 614
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AtomicEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 616
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
        self.enterRule(localctx, 102, self.RULE_atomic_effect)
        try:
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.AssignEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.match(fstripsParser.T__0)
                self.state = 620
                self.assignOp()
                self.state = 621
                self.functionTerm()
                self.state = 622
                self.fExp()
                self.state = 623
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.DeleteAtomEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.match(fstripsParser.T__0)
                self.state = 626
                self.match(fstripsParser.T__18)
                self.state = 627
                self.atomicTermFormula()
                self.state = 628
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.AddAtomEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 630
                self.atomicTermFormula()
                pass

            elif la_ == 4:
                localctx = fstripsParser.AssignConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 631
                self.match(fstripsParser.T__0)
                self.state = 632
                self.match(fstripsParser.T__28)
                self.state = 633
                self.functionTerm()
                self.state = 634
                self.term()
                self.state = 635
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
        self.enterRule(localctx, 104, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
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
        self.enterRule(localctx, 106, self.RULE_unaryBuiltIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
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
        self.enterRule(localctx, 108, self.RULE_binaryComp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
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
        self.enterRule(localctx, 110, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
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
        self.enterRule(localctx, 112, self.RULE_processEffectOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
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
        self.enterRule(localctx, 114, self.RULE_problem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(fstripsParser.T__0)
            self.state = 650
            self.match(fstripsParser.T__1)
            self.state = 651
            self.problemDecl()
            self.state = 652
            self.problemDomain()
            self.state = 654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 653
                self.requireDef()


            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 656
                self.object_declaration()


            self.state = 659
            self.init()
            self.state = 660
            self.goal()
            self.state = 664
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 661
                self.problemMeta()
                self.state = 666
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 667
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
        self.enterRule(localctx, 116, self.RULE_problemMeta)
        try:
            self.state = 672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 669
                self.probConstraints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                self.boundsDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 671
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
        self.enterRule(localctx, 118, self.RULE_problemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.match(fstripsParser.T__0)
            self.state = 675
            self.match(fstripsParser.T__51)
            self.state = 676
            self.match(fstripsParser.NAME)
            self.state = 677
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
        self.enterRule(localctx, 120, self.RULE_problemDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(fstripsParser.T__0)
            self.state = 680
            self.match(fstripsParser.T__52)
            self.state = 681
            self.match(fstripsParser.NAME)
            self.state = 682
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

        def typedNameList(self):
            return self.getTypedRuleContext(fstripsParser.TypedNameListContext,0)


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
        self.enterRule(localctx, 122, self.RULE_object_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(fstripsParser.T__0)
            self.state = 685
            self.match(fstripsParser.T__53)
            self.state = 686
            self.typedNameList()
            self.state = 687
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
        self.enterRule(localctx, 124, self.RULE_boundsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.match(fstripsParser.T__0)
            self.state = 690
            self.match(fstripsParser.T__54)
            self.state = 692 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 691
                self.typeBoundsDefinition()
                self.state = 694 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.T__0):
                    break

            self.state = 696
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
        self.enterRule(localctx, 126, self.RULE_typeBoundsDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.match(fstripsParser.T__0)
            self.state = 699
            self.match(fstripsParser.NAME)
            self.state = 700
            self.match(fstripsParser.T__6)
            self.state = 701
            self.numericBuiltinType()
            self.state = 702
            self.match(fstripsParser.T__55)
            self.state = 703
            self.match(fstripsParser.NUMBER)
            self.state = 704
            self.match(fstripsParser.T__56)
            self.state = 705
            self.match(fstripsParser.NUMBER)
            self.state = 706
            self.match(fstripsParser.T__57)
            self.state = 707
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
        self.enterRule(localctx, 128, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.match(fstripsParser.T__0)
            self.state = 710
            self.match(fstripsParser.K_INIT)
            self.state = 714
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 711
                self.initEl()
                self.state = 716
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 717
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
        self.enterRule(localctx, 130, self.RULE_groundTerm)
        try:
            self.state = 722
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                localctx = fstripsParser.GroundTermObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 719
                self.match(fstripsParser.NAME)
                pass
            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.GroundTermNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 720
                self.match(fstripsParser.NUMBER)
                pass
            elif token in [fstripsParser.T__0]:
                localctx = fstripsParser.GroundTermFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 721
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
        self.enterRule(localctx, 132, self.RULE_groundFunctionTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(fstripsParser.T__0)
            self.state = 725
            self.logical_symbol_name()
            self.state = 729
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.NAME or _la==fstripsParser.NUMBER:
                self.state = 726
                self.groundTerm()
                self.state = 731
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 732
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
        self.enterRule(localctx, 134, self.RULE_initEl)
        try:
            self.state = 747
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.InitLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 734
                self.nameLiteral()
                pass

            elif la_ == 2:
                localctx = fstripsParser.InitAssignmentNumericContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 735
                self.match(fstripsParser.T__0)
                self.state = 736
                self.match(fstripsParser.T__22)
                self.state = 737
                self.groundFunctionTerm()
                self.state = 738
                self.match(fstripsParser.NUMBER)
                self.state = 739
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.InitAssignmentObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 741
                self.match(fstripsParser.T__0)
                self.state = 742
                self.match(fstripsParser.T__22)
                self.state = 743
                self.groundFunctionTerm()
                self.state = 744
                self.match(fstripsParser.NAME)
                self.state = 745
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
        self.enterRule(localctx, 136, self.RULE_nameLiteral)
        try:
            self.state = 755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.InitPositiveLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 749
                self.groundAtomicFormula()
                pass

            elif la_ == 2:
                localctx = fstripsParser.InitNegativeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 750
                self.match(fstripsParser.T__0)
                self.state = 751
                self.match(fstripsParser.T__18)
                self.state = 752
                self.groundAtomicFormula()
                self.state = 753
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
        self.enterRule(localctx, 138, self.RULE_groundAtomicFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.match(fstripsParser.T__0)
            self.state = 758
            self.predicate()
            self.state = 762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.NAME or _la==fstripsParser.NUMBER:
                self.state = 759
                self.groundTerm()
                self.state = 764
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 765
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
        self.enterRule(localctx, 140, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 767
            self.match(fstripsParser.T__0)
            self.state = 768
            self.match(fstripsParser.T__58)
            self.state = 769
            self.goalDesc()
            self.state = 770
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
        self.enterRule(localctx, 142, self.RULE_probConstraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
            self.match(fstripsParser.T__0)
            self.state = 773
            self.match(fstripsParser.T__59)
            self.state = 774
            self.prefConGD()
            self.state = 775
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

        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)

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
        self.enterRule(localctx, 144, self.RULE_prefConGD)
        self._la = 0 # Token type
        try:
            self.state = 807
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctionOfConstraintsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 777
                self.match(fstripsParser.T__0)
                self.state = 778
                self.match(fstripsParser.T__16)
                self.state = 782
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 779
                    self.prefConGD()
                    self.state = 784
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 785
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.UniversallyQuantifiedConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 786
                self.match(fstripsParser.T__0)
                self.state = 787
                self.match(fstripsParser.T__21)
                self.state = 788
                self.match(fstripsParser.T__0)
                self.state = 789
                self.variableList()
                self.state = 790
                self.match(fstripsParser.T__2)
                self.state = 791
                self.prefConGD()
                self.state = 792
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.PreferenceConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 794
                self.match(fstripsParser.T__0)
                self.state = 795
                self.match(fstripsParser.T__60)
                self.state = 797
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==fstripsParser.NAME:
                    self.state = 796
                    self.match(fstripsParser.NAME)


                self.state = 799
                self.conGD()
                self.state = 800
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.PlainConstraintListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 803 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 802
                        self.conGD()

                    else:
                        raise NoViableAltException(self)
                    self.state = 805 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        self.enterRule(localctx, 146, self.RULE_metricSpec)
        try:
            localctx = fstripsParser.ProblemMetricContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self.match(fstripsParser.T__0)
            self.state = 810
            self.match(fstripsParser.T__61)
            self.state = 811
            self.optimization()
            self.state = 812
            self.metricFExp()
            self.state = 813
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
        self.enterRule(localctx, 148, self.RULE_optimization)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
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
        self.enterRule(localctx, 150, self.RULE_metricFExp)
        try:
            self.state = 829
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.FunctionalExprMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 817
                self.functionTerm()
                pass

            elif la_ == 2:
                localctx = fstripsParser.CompositeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 818
                self.terminalCost()
                self.state = 819
                self.stageCost()
                pass

            elif la_ == 3:
                localctx = fstripsParser.CompositeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 821
                self.stageCost()
                self.state = 822
                self.terminalCost()
                pass

            elif la_ == 4:
                localctx = fstripsParser.TotalTimeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 824
                self.match(fstripsParser.T__64)
                pass

            elif la_ == 5:
                localctx = fstripsParser.IsViolatedMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 825
                self.match(fstripsParser.T__0)
                self.state = 826
                self.match(fstripsParser.T__65)
                self.state = 827
                self.match(fstripsParser.NAME)
                self.state = 828
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
        self.enterRule(localctx, 152, self.RULE_terminalCost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 831
            self.match(fstripsParser.T__0)
            self.state = 832
            self.match(fstripsParser.T__66)
            self.state = 833
            self.functionTerm()
            self.state = 834
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
        self.enterRule(localctx, 154, self.RULE_stageCost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 836
            self.match(fstripsParser.T__0)
            self.state = 837
            self.match(fstripsParser.T__67)
            self.state = 838
            self.functionTerm()
            self.state = 839
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

        def variableList(self):
            return self.getTypedRuleContext(fstripsParser.VariableListContext,0)

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
        self.enterRule(localctx, 156, self.RULE_conGD)
        self._la = 0 # Token type
        try:
            self.state = 926
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctiveConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 841
                self.match(fstripsParser.T__0)
                self.state = 842
                self.match(fstripsParser.T__16)
                self.state = 844 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 843
                    self.conGD()
                    self.state = 846 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==fstripsParser.T__0):
                        break

                self.state = 848
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ForallConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 850
                self.match(fstripsParser.T__0)
                self.state = 851
                self.match(fstripsParser.T__21)
                self.state = 852
                self.match(fstripsParser.T__0)
                self.state = 853
                self.variableList()
                self.state = 854
                self.match(fstripsParser.T__2)
                self.state = 855
                self.conGD()
                self.state = 856
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.AtEndConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 858
                self.match(fstripsParser.T__0)
                self.state = 859
                self.match(fstripsParser.T__68)
                self.state = 860
                self.goalDesc()
                self.state = 861
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AlwaysConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 863
                self.match(fstripsParser.T__0)
                self.state = 864
                self.match(fstripsParser.T__69)
                self.state = 865
                self.goalDesc()
                self.state = 866
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 5:
                localctx = fstripsParser.SometimeConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 868
                self.match(fstripsParser.T__0)
                self.state = 869
                self.match(fstripsParser.T__70)
                self.state = 870
                self.goalDesc()
                self.state = 871
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 6:
                localctx = fstripsParser.WithinConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 873
                self.match(fstripsParser.T__0)
                self.state = 874
                self.match(fstripsParser.T__71)
                self.state = 875
                self.match(fstripsParser.NUMBER)
                self.state = 876
                self.goalDesc()
                self.state = 877
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 7:
                localctx = fstripsParser.AtMostOnceConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 879
                self.match(fstripsParser.T__0)
                self.state = 880
                self.match(fstripsParser.T__72)
                self.state = 881
                self.goalDesc()
                self.state = 882
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 8:
                localctx = fstripsParser.SometimeAfterConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 884
                self.match(fstripsParser.T__0)
                self.state = 885
                self.match(fstripsParser.T__73)
                self.state = 886
                self.goalDesc()
                self.state = 887
                self.goalDesc()
                self.state = 888
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 9:
                localctx = fstripsParser.SometimeBeforeConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 890
                self.match(fstripsParser.T__0)
                self.state = 891
                self.match(fstripsParser.T__74)
                self.state = 892
                self.goalDesc()
                self.state = 893
                self.goalDesc()
                self.state = 894
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 10:
                localctx = fstripsParser.AlwaysWithinConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 896
                self.match(fstripsParser.T__0)
                self.state = 897
                self.match(fstripsParser.T__75)
                self.state = 898
                self.match(fstripsParser.NUMBER)
                self.state = 899
                self.goalDesc()
                self.state = 900
                self.goalDesc()
                self.state = 901
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 11:
                localctx = fstripsParser.HoldDuringConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 903
                self.match(fstripsParser.T__0)
                self.state = 904
                self.match(fstripsParser.T__76)
                self.state = 905
                self.match(fstripsParser.NUMBER)
                self.state = 906
                self.match(fstripsParser.NUMBER)
                self.state = 907
                self.goalDesc()
                self.state = 908
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 12:
                localctx = fstripsParser.HoldAfterConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 910
                self.match(fstripsParser.T__0)
                self.state = 911
                self.match(fstripsParser.T__77)
                self.state = 912
                self.match(fstripsParser.NUMBER)
                self.state = 913
                self.goalDesc()
                self.state = 914
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 13:
                localctx = fstripsParser.ExtensionalConstraintGDContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 916
                self.match(fstripsParser.T__0)
                self.state = 917
                self.match(fstripsParser.EXTNAME)
                self.state = 919 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 918
                    self.groundFunctionTerm()
                    self.state = 921 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==fstripsParser.T__0):
                        break

                self.state = 923
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 14:
                localctx = fstripsParser.AlternativeAlwaysConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 925
                self.goalDesc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





