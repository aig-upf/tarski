# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .listener import fstripsListener
    from .visitor import fstripsVisitor
else:
    from listener import fstripsListener
    from visitor import fstripsVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u008c")
        buf.write("\u0349\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\3\2\5\2\u008f\n\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u0095\n\3\3\3\5\3\u0098\n\3\3\3\5\3\u009b\n\3\3\3\5")
        buf.write("\3\u009e\n\3\3\3\5\3\u00a1\n\3\3\3\7\3\u00a4\n\3\f\3\16")
        buf.write("\3\u00a7\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\6\5\u00b3\n\5\r\5\16\5\u00b4\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\5\7\u00c1\n\7\3\b\3\b\5\b\u00c5\n\b\3")
        buf.write("\t\7\t\u00c8\n\t\f\t\16\t\u00cb\13\t\3\t\6\t\u00ce\n\t")
        buf.write("\r\t\16\t\u00cf\3\t\7\t\u00d3\n\t\f\t\16\t\u00d6\13\t")
        buf.write("\5\t\u00d8\n\t\3\n\6\n\u00db\n\n\r\n\16\n\u00dc\3\n\3")
        buf.write("\n\3\n\3\13\7\13\u00e3\n\13\f\13\16\13\u00e6\13\13\3\13")
        buf.write("\6\13\u00e9\n\13\r\13\16\13\u00ea\3\13\7\13\u00ee\n\13")
        buf.write("\f\13\16\13\u00f1\13\13\5\13\u00f3\n\13\3\f\6\f\u00f6")
        buf.write("\n\f\r\f\16\f\u00f7\3\f\3\f\3\f\3\r\3\r\3\r\6\r\u0100")
        buf.write("\n\r\r\r\16\r\u0101\3\r\3\r\3\r\5\r\u0107\n\r\3\16\3\16")
        buf.write("\5\16\u010b\n\16\3\17\3\17\3\17\7\17\u0110\n\17\f\17\16")
        buf.write("\17\u0113\13\17\3\17\3\17\3\20\3\20\5\20\u0119\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\7\25\u0131\n\25\f\25\16\25\u0134\13\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0145\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\5!\u0174\n!\3\"\3\"\3\"\3\"\7\"\u017a")
        buf.write("\n\"\f\"\16\"\u017d\13\"\3\"\3\"\3\"\3\"\7\"\u0183\n\"")
        buf.write("\f\"\16\"\u0186\13\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01aa")
        buf.write("\n\"\3#\3#\3#\7#\u01af\n#\f#\16#\u01b2\13#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\5$\u01bb\n$\3%\3%\3%\7%\u01c0\n%\f%\16%\u01c3")
        buf.write("\13%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01d2\n")
        buf.write("%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01e9\n\'\3(\3(\3(\3(\3")
        buf.write("(\5(\u01f0\n(\3)\3)\3)\3)\5)\u01f6\n)\3*\3*\3*\3*\5*\u01fc")
        buf.write("\n*\3+\3+\3+\7+\u0201\n+\f+\16+\u0204\13+\3+\3+\5+\u0208")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\7,\u021e\n,\f,\16,\u0221\13,\3,\3,\3,\3,\5")
        buf.write(",\u0227\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u023b\n-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u024a\n\62\3\62\5\62\u024d")
        buf.write("\n\62\3\62\3\62\3\62\7\62\u0252\n\62\f\62\16\62\u0255")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\5\63\u025c\n\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\6\67\u0270\n\67\r\67\16")
        buf.write("\67\u0271\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38\3")
        buf.write("9\39\39\79\u0284\n9\f9\169\u0287\139\39\39\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0297\n:\3;\3;\3;\7;\u029c")
        buf.write("\n;\f;\16;\u029f\13;\3;\3;\3<\3<\3<\7<\u02a6\n<\f<\16")
        buf.write("<\u02a9\13<\3<\3<\3=\3=\5=\u02af\n=\3>\3>\3>\3>\3>\3?")
        buf.write("\3?\3?\3?\3?\3@\3@\3@\7@\u02be\n@\f@\16@\u02c1\13@\3@")
        buf.write("\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u02cf\n@\3@\3@\3")
        buf.write("@\3@\6@\u02d5\n@\r@\16@\u02d6\5@\u02d9\n@\3A\3A\3A\3A")
        buf.write("\3A\3A\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u02ef")
        buf.write("\nC\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3F\3F\3F\6F\u02fe\n")
        buf.write("F\rF\16F\u02ff\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F")
        buf.write("\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\5F\u0347\nF\3F\2\2G\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\2\b\3\2UV\5\2\t\t\24\24\26\32\4\2\t\t\33#\3\2$(\3\2M")
        buf.write("P\3\2\64\65\u0364\2\u008e\3\2\2\2\4\u0090\3\2\2\2\6\u00aa")
        buf.write("\3\2\2\2\b\u00af\3\2\2\2\n\u00b8\3\2\2\2\f\u00c0\3\2\2")
        buf.write("\2\16\u00c4\3\2\2\2\20\u00d7\3\2\2\2\22\u00da\3\2\2\2")
        buf.write("\24\u00f2\3\2\2\2\26\u00f5\3\2\2\2\30\u0106\3\2\2\2\32")
        buf.write("\u010a\3\2\2\2\34\u010c\3\2\2\2\36\u0118\3\2\2\2 \u011a")
        buf.write("\3\2\2\2\"\u0121\3\2\2\2$\u0126\3\2\2\2&\u0128\3\2\2\2")
        buf.write("(\u012d\3\2\2\2*\u0137\3\2\2\2,\u013c\3\2\2\2.\u013e\3")
        buf.write("\2\2\2\60\u0144\3\2\2\2\62\u0146\3\2\2\2\64\u0150\3\2")
        buf.write("\2\2\66\u015b\3\2\2\28\u0165\3\2\2\2:\u0167\3\2\2\2<\u0169")
        buf.write("\3\2\2\2>\u016b\3\2\2\2@\u0173\3\2\2\2B\u01a9\3\2\2\2")
        buf.write("D\u01ab\3\2\2\2F\u01ba\3\2\2\2H\u01d1\3\2\2\2J\u01d3\3")
        buf.write("\2\2\2L\u01e8\3\2\2\2N\u01ef\3\2\2\2P\u01f5\3\2\2\2R\u01fb")
        buf.write("\3\2\2\2T\u0207\3\2\2\2V\u0226\3\2\2\2X\u023a\3\2\2\2")
        buf.write("Z\u023c\3\2\2\2\\\u023e\3\2\2\2^\u0240\3\2\2\2`\u0242")
        buf.write("\3\2\2\2b\u0244\3\2\2\2d\u025b\3\2\2\2f\u025d\3\2\2\2")
        buf.write("h\u0262\3\2\2\2j\u0267\3\2\2\2l\u026c\3\2\2\2n\u0275\3")
        buf.write("\2\2\2p\u0280\3\2\2\2r\u0296\3\2\2\2t\u0298\3\2\2\2v\u02a2")
        buf.write("\3\2\2\2x\u02ae\3\2\2\2z\u02b0\3\2\2\2|\u02b5\3\2\2\2")
        buf.write("~\u02d8\3\2\2\2\u0080\u02da\3\2\2\2\u0082\u02e0\3\2\2")
        buf.write("\2\u0084\u02ee\3\2\2\2\u0086\u02f0\3\2\2\2\u0088\u02f5")
        buf.write("\3\2\2\2\u008a\u0346\3\2\2\2\u008c\u008f\5\4\3\2\u008d")
        buf.write("\u008f\5b\62\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\3\3\2\2\2\u0090\u0091\7\3\2\2\u0091\u0092\7\4\2")
        buf.write("\2\u0092\u0094\5\6\4\2\u0093\u0095\5\b\5\2\u0094\u0093")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096")
        buf.write("\u0098\5\n\6\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u009a\3\2\2\2\u0099\u009b\5&\24\2\u009a\u0099\3")
        buf.write("\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009e")
        buf.write("\5(\25\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u00a1\5\34\17\2\u00a0\u009f\3\2\2")
        buf.write("\2\u00a0\u00a1\3\2\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4")
        buf.write("\5\60\31\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7\5\2\2\u00a9\5\3\2\2")
        buf.write("\2\u00aa\u00ab\7\3\2\2\u00ab\u00ac\7\6\2\2\u00ac\u00ad")
        buf.write("\7U\2\2\u00ad\u00ae\7\5\2\2\u00ae\7\3\2\2\2\u00af\u00b0")
        buf.write("\7\3\2\2\u00b0\u00b2\7\7\2\2\u00b1\u00b3\7D\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\7")
        buf.write("\5\2\2\u00b7\t\3\2\2\2\u00b8\u00b9\7\3\2\2\u00b9\u00ba")
        buf.write("\7\b\2\2\u00ba\u00bb\5\20\t\2\u00bb\u00bc\7\5\2\2\u00bc")
        buf.write("\13\3\2\2\2\u00bd\u00c1\7Q\2\2\u00be\u00c1\7R\2\2\u00bf")
        buf.write("\u00c1\7T\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c1\r\3\2\2\2\u00c2\u00c5\5\f\7")
        buf.write("\2\u00c3\u00c5\7S\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\17\3\2\2\2\u00c6\u00c8\7U\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00d8\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cc\u00ce\5\22\n\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d4\3\2\2\2\u00d1\u00d3\7U\2\2\u00d2\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00c9")
        buf.write("\3\2\2\2\u00d7\u00cd\3\2\2\2\u00d8\21\3\2\2\2\u00d9\u00db")
        buf.write("\7U\2\2\u00da\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00df\7\t\2\2\u00df\u00e0\5\30\r\2\u00e0\23\3\2")
        buf.write("\2\2\u00e1\u00e3\7W\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6")
        buf.write("\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00f3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e9\5\26\f")
        buf.write("\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ef\3\2\2\2\u00ec")
        buf.write("\u00ee\7W\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f3\3")
        buf.write("\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00e4\3\2\2\2\u00f2\u00e8")
        buf.write("\3\2\2\2\u00f3\25\3\2\2\2\u00f4\u00f6\7W\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\7\t\2\2")
        buf.write("\u00fa\u00fb\5\32\16\2\u00fb\27\3\2\2\2\u00fc\u00fd\7")
        buf.write("\3\2\2\u00fd\u00ff\7\n\2\2\u00fe\u0100\5\32\16\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\7")
        buf.write("\5\2\2\u0104\u0107\3\2\2\2\u0105\u0107\5\32\16\2\u0106")
        buf.write("\u00fc\3\2\2\2\u0106\u0105\3\2\2\2\u0107\31\3\2\2\2\u0108")
        buf.write("\u010b\7U\2\2\u0109\u010b\5\16\b\2\u010a\u0108\3\2\2\2")
        buf.write("\u010a\u0109\3\2\2\2\u010b\33\3\2\2\2\u010c\u010d\7\3")
        buf.write("\2\2\u010d\u0111\7\13\2\2\u010e\u0110\5\36\20\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3")
        buf.write("\2\2\2\u0114\u0115\7\5\2\2\u0115\35\3\2\2\2\u0116\u0119")
        buf.write("\5 \21\2\u0117\u0119\5\"\22\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\37\3\2\2\2\u011a\u011b\7\3\2\2\u011b")
        buf.write("\u011c\5$\23\2\u011c\u011d\5\24\13\2\u011d\u011e\7\5\2")
        buf.write("\2\u011e\u011f\7\t\2\2\u011f\u0120\5\32\16\2\u0120!\3")
        buf.write("\2\2\2\u0121\u0122\7\3\2\2\u0122\u0123\5$\23\2\u0123\u0124")
        buf.write("\5\24\13\2\u0124\u0125\7\5\2\2\u0125#\3\2\2\2\u0126\u0127")
        buf.write("\t\2\2\2\u0127%\3\2\2\2\u0128\u0129\7\3\2\2\u0129\u012a")
        buf.write("\7\f\2\2\u012a\u012b\5\20\t\2\u012b\u012c\7\5\2\2\u012c")
        buf.write("\'\3\2\2\2\u012d\u012e\7\3\2\2\u012e\u0132\7\r\2\2\u012f")
        buf.write("\u0131\5*\26\2\u0130\u012f\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3")
        buf.write("\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\7\5\2\2\u0136)")
        buf.write("\3\2\2\2\u0137\u0138\7\3\2\2\u0138\u0139\5,\27\2\u0139")
        buf.write("\u013a\5\24\13\2\u013a\u013b\7\5\2\2\u013b+\3\2\2\2\u013c")
        buf.write("\u013d\7U\2\2\u013d-\3\2\2\2\u013e\u013f\7U\2\2\u013f")
        buf.write("/\3\2\2\2\u0140\u0145\5\62\32\2\u0141\u0145\5\66\34\2")
        buf.write("\u0142\u0145\5J&\2\u0143\u0145\5\64\33\2\u0144\u0140\3")
        buf.write("\2\2\2\u0144\u0141\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0145\61\3\2\2\2\u0146\u0147\7\3\2\2\u0147\u0148")
        buf.write("\7L\2\2\u0148\u0149\58\35\2\u0149\u014a\7\16\2\2\u014a")
        buf.write("\u014b\7\3\2\2\u014b\u014c\5\24\13\2\u014c\u014d\7\5\2")
        buf.write("\2\u014d\u014e\5> \2\u014e\u014f\7\5\2\2\u014f\63\3\2")
        buf.write("\2\2\u0150\u0151\7\3\2\2\u0151\u0152\7\17\2\2\u0152\u0153")
        buf.write("\5:\36\2\u0153\u0154\7\16\2\2\u0154\u0155\7\3\2\2\u0155")
        buf.write("\u0156\5\24\13\2\u0156\u0157\7\5\2\2\u0157\u0158\7\20")
        buf.write("\2\2\u0158\u0159\5B\"\2\u0159\u015a\7\5\2\2\u015a\65\3")
        buf.write("\2\2\2\u015b\u015c\7\3\2\2\u015c\u015d\7\21\2\2\u015d")
        buf.write("\u015e\5<\37\2\u015e\u015f\7\16\2\2\u015f\u0160\7\3\2")
        buf.write("\2\u0160\u0161\5\24\13\2\u0161\u0162\7\5\2\2\u0162\u0163")
        buf.write("\5> \2\u0163\u0164\7\5\2\2\u0164\67\3\2\2\2\u0165\u0166")
        buf.write("\t\2\2\2\u01669\3\2\2\2\u0167\u0168\7U\2\2\u0168;\3\2")
        buf.write("\2\2\u0169\u016a\t\2\2\2\u016a=\3\2\2\2\u016b\u016c\7")
        buf.write("\\\2\2\u016c\u016d\5@!\2\u016d\u016e\7]\2\2\u016e\u016f")
        buf.write("\5T+\2\u016f?\3\2\2\2\u0170\u0171\7\3\2\2\u0171\u0174")
        buf.write("\7\5\2\2\u0172\u0174\5B\"\2\u0173\u0170\3\2\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174A\3\2\2\2\u0175\u01aa\5D#\2\u0176")
        buf.write("\u0177\7\3\2\2\u0177\u017b\7E\2\2\u0178\u017a\5B\"\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017b\3")
        buf.write("\2\2\2\u017e\u01aa\7\5\2\2\u017f\u0180\7\3\2\2\u0180\u0184")
        buf.write("\7G\2\2\u0181\u0183\5B\"\2\u0182\u0181\3\2\2\2\u0183\u0186")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u01aa\7\5\2\2")
        buf.write("\u0188\u0189\7\3\2\2\u0189\u018a\7F\2\2\u018a\u018b\5")
        buf.write("B\"\2\u018b\u018c\7\5\2\2\u018c\u01aa\3\2\2\2\u018d\u018e")
        buf.write("\7\3\2\2\u018e\u018f\7H\2\2\u018f\u0190\5B\"\2\u0190\u0191")
        buf.write("\5B\"\2\u0191\u0192\7\5\2\2\u0192\u01aa\3\2\2\2\u0193")
        buf.write("\u0194\7\3\2\2\u0194\u0195\7I\2\2\u0195\u0196\7\3\2\2")
        buf.write("\u0196\u0197\5\24\13\2\u0197\u0198\7\5\2\2\u0198\u0199")
        buf.write("\5B\"\2\u0199\u019a\7\5\2\2\u019a\u01aa\3\2\2\2\u019b")
        buf.write("\u019c\7\3\2\2\u019c\u019d\7J\2\2\u019d\u019e\7\3\2\2")
        buf.write("\u019e\u019f\5\24\13\2\u019f\u01a0\7\5\2\2\u01a0\u01a1")
        buf.write("\5B\"\2\u01a1\u01a2\7\5\2\2\u01a2\u01aa\3\2\2\2\u01a3")
        buf.write("\u01a4\7\3\2\2\u01a4\u01a5\5^\60\2\u01a5\u01a6\5F$\2\u01a6")
        buf.write("\u01a7\5F$\2\u01a7\u01a8\7\5\2\2\u01a8\u01aa\3\2\2\2\u01a9")
        buf.write("\u0175\3\2\2\2\u01a9\u0176\3\2\2\2\u01a9\u017f\3\2\2\2")
        buf.write("\u01a9\u0188\3\2\2\2\u01a9\u018d\3\2\2\2\u01a9\u0193\3")
        buf.write("\2\2\2\u01a9\u019b\3\2\2\2\u01a9\u01a3\3\2\2\2\u01aaC")
        buf.write("\3\2\2\2\u01ab\u01ac\7\3\2\2\u01ac\u01b0\5,\27\2\u01ad")
        buf.write("\u01af\5F$\2\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b3\u01b4\7\5\2\2\u01b4E\3\2\2")
        buf.write("\2\u01b5\u01bb\7U\2\2\u01b6\u01bb\7X\2\2\u01b7\u01bb\7")
        buf.write("W\2\2\u01b8\u01bb\7\22\2\2\u01b9\u01bb\5H%\2\u01ba\u01b5")
        buf.write("\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbG\3\2\2\2\u01bc")
        buf.write("\u01bd\7\3\2\2\u01bd\u01c1\5$\23\2\u01be\u01c0\5F$\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3")
        buf.write("\2\2\2\u01c4\u01c5\7\5\2\2\u01c5\u01d2\3\2\2\2\u01c6\u01c7")
        buf.write("\7\3\2\2\u01c7\u01c8\5Z.\2\u01c8\u01c9\5F$\2\u01c9\u01ca")
        buf.write("\5F$\2\u01ca\u01cb\7\5\2\2\u01cb\u01d2\3\2\2\2\u01cc\u01cd")
        buf.write("\7\3\2\2\u01cd\u01ce\5\\/\2\u01ce\u01cf\5F$\2\u01cf\u01d0")
        buf.write("\7\5\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01bc\3\2\2\2\u01d1")
        buf.write("\u01c6\3\2\2\2\u01d1\u01cc\3\2\2\2\u01d2I\3\2\2\2\u01d3")
        buf.write("\u01d4\7\3\2\2\u01d4\u01d5\7\23\2\2\u01d5\u01d6\5\24\13")
        buf.write("\2\u01d6\u01d7\5B\"\2\u01d7\u01d8\7\5\2\2\u01d8K\3\2\2")
        buf.write("\2\u01d9\u01da\7\3\2\2\u01da\u01db\7\24\2\2\u01db\u01dc")
        buf.write("\5N(\2\u01dc\u01dd\7\5\2\2\u01dd\u01e9\3\2\2\2\u01de\u01df")
        buf.write("\7\3\2\2\u01df\u01e0\7\24\2\2\u01e0\u01e1\5P)\2\u01e1")
        buf.write("\u01e2\7\5\2\2\u01e2\u01e9\3\2\2\2\u01e3\u01e4\7\3\2\2")
        buf.write("\u01e4\u01e5\7\24\2\2\u01e5\u01e6\5R*\2\u01e6\u01e7\7")
        buf.write("\5\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01d9\3\2\2\2\u01e8\u01de")
        buf.write("\3\2\2\2\u01e8\u01e3\3\2\2\2\u01e9M\3\2\2\2\u01ea\u01eb")
        buf.write("\5H%\2\u01eb\u01ec\7\22\2\2\u01ec\u01f0\3\2\2\2\u01ed")
        buf.write("\u01ee\7\22\2\2\u01ee\u01f0\5H%\2\u01ef\u01ea\3\2\2\2")
        buf.write("\u01ef\u01ed\3\2\2\2\u01f0O\3\2\2\2\u01f1\u01f2\7X\2\2")
        buf.write("\u01f2\u01f6\7\22\2\2\u01f3\u01f4\7\22\2\2\u01f4\u01f6")
        buf.write("\7X\2\2\u01f5\u01f1\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6")
        buf.write("Q\3\2\2\2\u01f7\u01f8\7W\2\2\u01f8\u01fc\7\22\2\2\u01f9")
        buf.write("\u01fa\7\22\2\2\u01fa\u01fc\7W\2\2\u01fb\u01f7\3\2\2\2")
        buf.write("\u01fb\u01f9\3\2\2\2\u01fcS\3\2\2\2\u01fd\u01fe\7\3\2")
        buf.write("\2\u01fe\u0202\7E\2\2\u01ff\u0201\5V,\2\u0200\u01ff\3")
        buf.write("\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3\2\2\2\u0205")
        buf.write("\u0208\7\5\2\2\u0206\u0208\5V,\2\u0207\u01fd\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208U\3\2\2\2\u0209\u020a\7\3\2\2\u020a")
        buf.write("\u020b\7J\2\2\u020b\u020c\7\3\2\2\u020c\u020d\5\24\13")
        buf.write("\2\u020d\u020e\7\5\2\2\u020e\u020f\5T+\2\u020f\u0210\7")
        buf.write("\5\2\2\u0210\u0227\3\2\2\2\u0211\u0212\7\3\2\2\u0212\u0213")
        buf.write("\7K\2\2\u0213\u0214\5B\"\2\u0214\u0215\5X-\2\u0215\u0216")
        buf.write("\7\5\2\2\u0216\u0227\3\2\2\2\u0217\u0218\7\3\2\2\u0218")
        buf.write("\u0219\7K\2\2\u0219\u021a\5B\"\2\u021a\u021b\7\3\2\2\u021b")
        buf.write("\u021f\7E\2\2\u021c\u021e\5X-\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2")
        buf.write("\u0220\u0222\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0223\7")
        buf.write("\5\2\2\u0223\u0224\7\5\2\2\u0224\u0227\3\2\2\2\u0225\u0227")
        buf.write("\5X-\2\u0226\u0209\3\2\2\2\u0226\u0211\3\2\2\2\u0226\u0217")
        buf.write("\3\2\2\2\u0226\u0225\3\2\2\2\u0227W\3\2\2\2\u0228\u0229")
        buf.write("\7\3\2\2\u0229\u022a\7\25\2\2\u022a\u022b\5H%\2\u022b")
        buf.write("\u022c\5F$\2\u022c\u022d\7\5\2\2\u022d\u023b\3\2\2\2\u022e")
        buf.write("\u022f\7\3\2\2\u022f\u0230\5`\61\2\u0230\u0231\5H%\2\u0231")
        buf.write("\u0232\5F$\2\u0232\u0233\7\5\2\2\u0233\u023b\3\2\2\2\u0234")
        buf.write("\u0235\7\3\2\2\u0235\u0236\7F\2\2\u0236\u0237\5D#\2\u0237")
        buf.write("\u0238\7\5\2\2\u0238\u023b\3\2\2\2\u0239\u023b\5D#\2\u023a")
        buf.write("\u0228\3\2\2\2\u023a\u022e\3\2\2\2\u023a\u0234\3\2\2\2")
        buf.write("\u023a\u0239\3\2\2\2\u023bY\3\2\2\2\u023c\u023d\t\3\2")
        buf.write("\2\u023d[\3\2\2\2\u023e\u023f\t\4\2\2\u023f]\3\2\2\2\u0240")
        buf.write("\u0241\t\5\2\2\u0241_\3\2\2\2\u0242\u0243\t\6\2\2\u0243")
        buf.write("a\3\2\2\2\u0244\u0245\7\3\2\2\u0245\u0246\7\4\2\2\u0246")
        buf.write("\u0247\5f\64\2\u0247\u0249\5h\65\2\u0248\u024a\5\b\5\2")
        buf.write("\u0249\u0248\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024c\3")
        buf.write("\2\2\2\u024b\u024d\5j\66\2\u024c\u024b\3\2\2\2\u024c\u024d")
        buf.write("\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f\5p9\2\u024f\u0253")
        buf.write("\5z>\2\u0250\u0252\5d\63\2\u0251\u0250\3\2\2\2\u0252\u0255")
        buf.write("\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write("\u0256\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0257\7\5\2\2")
        buf.write("\u0257c\3\2\2\2\u0258\u025c\5|?\2\u0259\u025c\5l\67\2")
        buf.write("\u025a\u025c\5\u0080A\2\u025b\u0258\3\2\2\2\u025b\u0259")
        buf.write("\3\2\2\2\u025b\u025a\3\2\2\2\u025ce\3\2\2\2\u025d\u025e")
        buf.write("\7\3\2\2\u025e\u025f\7)\2\2\u025f\u0260\7U\2\2\u0260\u0261")
        buf.write("\7\5\2\2\u0261g\3\2\2\2\u0262\u0263\7\3\2\2\u0263\u0264")
        buf.write("\7*\2\2\u0264\u0265\7U\2\2\u0265\u0266\7\5\2\2\u0266i")
        buf.write("\3\2\2\2\u0267\u0268\7\3\2\2\u0268\u0269\7+\2\2\u0269")
        buf.write("\u026a\5\20\t\2\u026a\u026b\7\5\2\2\u026bk\3\2\2\2\u026c")
        buf.write("\u026d\7\3\2\2\u026d\u026f\7,\2\2\u026e\u0270\5n8\2\u026f")
        buf.write("\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u026f\3\2\2\2")
        buf.write("\u0271\u0272\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0274\7")
        buf.write("\5\2\2\u0274m\3\2\2\2\u0275\u0276\7\3\2\2\u0276\u0277")
        buf.write("\7U\2\2\u0277\u0278\7\t\2\2\u0278\u0279\5\f\7\2\u0279")
        buf.write("\u027a\7-\2\2\u027a\u027b\7X\2\2\u027b\u027c\7.\2\2\u027c")
        buf.write("\u027d\7X\2\2\u027d\u027e\7/\2\2\u027e\u027f\7\5\2\2\u027f")
        buf.write("o\3\2\2\2\u0280\u0281\7\3\2\2\u0281\u0285\7[\2\2\u0282")
        buf.write("\u0284\5r:\2\u0283\u0282\3\2\2\2\u0284\u0287\3\2\2\2\u0285")
        buf.write("\u0283\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0288\3\2\2\2")
        buf.write("\u0287\u0285\3\2\2\2\u0288\u0289\7\5\2\2\u0289q\3\2\2")
        buf.write("\2\u028a\u0297\5v<\2\u028b\u028c\7\3\2\2\u028c\u028d\7")
        buf.write("F\2\2\u028d\u028e\5v<\2\u028e\u028f\7\5\2\2\u028f\u0297")
        buf.write("\3\2\2\2\u0290\u0291\7\3\2\2\u0291\u0292\7&\2\2\u0292")
        buf.write("\u0293\5t;\2\u0293\u0294\5x=\2\u0294\u0295\7\5\2\2\u0295")
        buf.write("\u0297\3\2\2\2\u0296\u028a\3\2\2\2\u0296\u028b\3\2\2\2")
        buf.write("\u0296\u0290\3\2\2\2\u0297s\3\2\2\2\u0298\u0299\7\3\2")
        buf.write("\2\u0299\u029d\5.\30\2\u029a\u029c\5x=\2\u029b\u029a\3")
        buf.write("\2\2\2\u029c\u029f\3\2\2\2\u029d\u029b\3\2\2\2\u029d\u029e")
        buf.write("\3\2\2\2\u029e\u02a0\3\2\2\2\u029f\u029d\3\2\2\2\u02a0")
        buf.write("\u02a1\7\5\2\2\u02a1u\3\2\2\2\u02a2\u02a3\7\3\2\2\u02a3")
        buf.write("\u02a7\5,\27\2\u02a4\u02a6\5x=\2\u02a5\u02a4\3\2\2\2\u02a6")
        buf.write("\u02a9\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a7\u02a8\3\2\2\2")
        buf.write("\u02a8\u02aa\3\2\2\2\u02a9\u02a7\3\2\2\2\u02aa\u02ab\7")
        buf.write("\5\2\2\u02abw\3\2\2\2\u02ac\u02af\7U\2\2\u02ad\u02af\7")
        buf.write("X\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02ad\3\2\2\2\u02afy\3")
        buf.write("\2\2\2\u02b0\u02b1\7\3\2\2\u02b1\u02b2\7\60\2\2\u02b2")
        buf.write("\u02b3\5B\"\2\u02b3\u02b4\7\5\2\2\u02b4{\3\2\2\2\u02b5")
        buf.write("\u02b6\7\3\2\2\u02b6\u02b7\7\61\2\2\u02b7\u02b8\5~@\2")
        buf.write("\u02b8\u02b9\7\5\2\2\u02b9}\3\2\2\2\u02ba\u02bb\7\3\2")
        buf.write("\2\u02bb\u02bf\7E\2\2\u02bc\u02be\5~@\2\u02bd\u02bc\3")
        buf.write("\2\2\2\u02be\u02c1\3\2\2\2\u02bf\u02bd\3\2\2\2\u02bf\u02c0")
        buf.write("\3\2\2\2\u02c0\u02c2\3\2\2\2\u02c1\u02bf\3\2\2\2\u02c2")
        buf.write("\u02d9\7\5\2\2\u02c3\u02c4\7\3\2\2\u02c4\u02c5\7J\2\2")
        buf.write("\u02c5\u02c6\7\3\2\2\u02c6\u02c7\5\24\13\2\u02c7\u02c8")
        buf.write("\7\5\2\2\u02c8\u02c9\5~@\2\u02c9\u02ca\7\5\2\2\u02ca\u02d9")
        buf.write("\3\2\2\2\u02cb\u02cc\7\3\2\2\u02cc\u02ce\7\62\2\2\u02cd")
        buf.write("\u02cf\7U\2\2\u02ce\u02cd\3\2\2\2\u02ce\u02cf\3\2\2\2")
        buf.write("\u02cf\u02d0\3\2\2\2\u02d0\u02d1\5\u008aF\2\u02d1\u02d2")
        buf.write("\7\5\2\2\u02d2\u02d9\3\2\2\2\u02d3\u02d5\5\u008aF\2\u02d4")
        buf.write("\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u02d4\3\2\2\2")
        buf.write("\u02d6\u02d7\3\2\2\2\u02d7\u02d9\3\2\2\2\u02d8\u02ba\3")
        buf.write("\2\2\2\u02d8\u02c3\3\2\2\2\u02d8\u02cb\3\2\2\2\u02d8\u02d4")
        buf.write("\3\2\2\2\u02d9\177\3\2\2\2\u02da\u02db\7\3\2\2\u02db\u02dc")
        buf.write("\7\63\2\2\u02dc\u02dd\5\u0082B\2\u02dd\u02de\5\u0084C")
        buf.write("\2\u02de\u02df\7\5\2\2\u02df\u0081\3\2\2\2\u02e0\u02e1")
        buf.write("\t\7\2\2\u02e1\u0083\3\2\2\2\u02e2\u02ef\5H%\2\u02e3\u02e4")
        buf.write("\5\u0086D\2\u02e4\u02e5\5\u0088E\2\u02e5\u02ef\3\2\2\2")
        buf.write("\u02e6\u02e7\5\u0088E\2\u02e7\u02e8\5\u0086D\2\u02e8\u02ef")
        buf.write("\3\2\2\2\u02e9\u02ef\7\66\2\2\u02ea\u02eb\7\3\2\2\u02eb")
        buf.write("\u02ec\7\67\2\2\u02ec\u02ed\7U\2\2\u02ed\u02ef\7\5\2\2")
        buf.write("\u02ee\u02e2\3\2\2\2\u02ee\u02e3\3\2\2\2\u02ee\u02e6\3")
        buf.write("\2\2\2\u02ee\u02e9\3\2\2\2\u02ee\u02ea\3\2\2\2\u02ef\u0085")
        buf.write("\3\2\2\2\u02f0\u02f1\7\3\2\2\u02f1\u02f2\78\2\2\u02f2")
        buf.write("\u02f3\5H%\2\u02f3\u02f4\7\5\2\2\u02f4\u0087\3\2\2\2\u02f5")
        buf.write("\u02f6\7\3\2\2\u02f6\u02f7\79\2\2\u02f7\u02f8\5H%\2\u02f8")
        buf.write("\u02f9\7\5\2\2\u02f9\u0089\3\2\2\2\u02fa\u02fb\7\3\2\2")
        buf.write("\u02fb\u02fd\7E\2\2\u02fc\u02fe\5\u008aF\2\u02fd\u02fc")
        buf.write("\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff\u02fd\3\2\2\2\u02ff")
        buf.write("\u0300\3\2\2\2\u0300\u0301\3\2\2\2\u0301\u0302\7\5\2\2")
        buf.write("\u0302\u0347\3\2\2\2\u0303\u0304\7\3\2\2\u0304\u0305\7")
        buf.write("J\2\2\u0305\u0306\7\3\2\2\u0306\u0307\5\24\13\2\u0307")
        buf.write("\u0308\7\5\2\2\u0308\u0309\5\u008aF\2\u0309\u030a\7\5")
        buf.write("\2\2\u030a\u0347\3\2\2\2\u030b\u030c\7\3\2\2\u030c\u030d")
        buf.write("\7:\2\2\u030d\u030e\5B\"\2\u030e\u030f\7\5\2\2\u030f\u0347")
        buf.write("\3\2\2\2\u0310\u0311\7\3\2\2\u0311\u0312\7;\2\2\u0312")
        buf.write("\u0313\5B\"\2\u0313\u0314\7\5\2\2\u0314\u0347\3\2\2\2")
        buf.write("\u0315\u0316\7\3\2\2\u0316\u0317\7<\2\2\u0317\u0318\5")
        buf.write("B\"\2\u0318\u0319\7\5\2\2\u0319\u0347\3\2\2\2\u031a\u031b")
        buf.write("\7\3\2\2\u031b\u031c\7=\2\2\u031c\u031d\7X\2\2\u031d\u031e")
        buf.write("\5B\"\2\u031e\u031f\7\5\2\2\u031f\u0347\3\2\2\2\u0320")
        buf.write("\u0321\7\3\2\2\u0321\u0322\7>\2\2\u0322\u0323\5B\"\2\u0323")
        buf.write("\u0324\7\5\2\2\u0324\u0347\3\2\2\2\u0325\u0326\7\3\2\2")
        buf.write("\u0326\u0327\7?\2\2\u0327\u0328\5B\"\2\u0328\u0329\5B")
        buf.write("\"\2\u0329\u032a\7\5\2\2\u032a\u0347\3\2\2\2\u032b\u032c")
        buf.write("\7\3\2\2\u032c\u032d\7@\2\2\u032d\u032e\5B\"\2\u032e\u032f")
        buf.write("\5B\"\2\u032f\u0330\7\5\2\2\u0330\u0347\3\2\2\2\u0331")
        buf.write("\u0332\7\3\2\2\u0332\u0333\7A\2\2\u0333\u0334\7X\2\2\u0334")
        buf.write("\u0335\5B\"\2\u0335\u0336\5B\"\2\u0336\u0337\7\5\2\2\u0337")
        buf.write("\u0347\3\2\2\2\u0338\u0339\7\3\2\2\u0339\u033a\7B\2\2")
        buf.write("\u033a\u033b\7X\2\2\u033b\u033c\7X\2\2\u033c\u033d\5B")
        buf.write("\"\2\u033d\u033e\7\5\2\2\u033e\u0347\3\2\2\2\u033f\u0340")
        buf.write("\7\3\2\2\u0340\u0341\7C\2\2\u0341\u0342\7X\2\2\u0342\u0343")
        buf.write("\5B\"\2\u0343\u0344\7\5\2\2\u0344\u0347\3\2\2\2\u0345")
        buf.write("\u0347\5B\"\2\u0346\u02fa\3\2\2\2\u0346\u0303\3\2\2\2")
        buf.write("\u0346\u030b\3\2\2\2\u0346\u0310\3\2\2\2\u0346\u0315\3")
        buf.write("\2\2\2\u0346\u031a\3\2\2\2\u0346\u0320\3\2\2\2\u0346\u0325")
        buf.write("\3\2\2\2\u0346\u032b\3\2\2\2\u0346\u0331\3\2\2\2\u0346")
        buf.write("\u0338\3\2\2\2\u0346\u033f\3\2\2\2\u0346\u0345\3\2\2\2")
        buf.write("\u0347\u008b\3\2\2\2?\u008e\u0094\u0097\u009a\u009d\u00a0")
        buf.write("\u00a5\u00b4\u00c0\u00c4\u00c9\u00cf\u00d4\u00d7\u00dc")
        buf.write("\u00e4\u00ea\u00ef\u00f2\u00f7\u0101\u0106\u010a\u0111")
        buf.write("\u0118\u0132\u0144\u0173\u017b\u0184\u01a9\u01b0\u01ba")
        buf.write("\u01c1\u01d1\u01e8\u01ef\u01f5\u01fb\u0202\u0207\u021f")
        buf.write("\u0226\u023a\u0249\u024c\u0253\u025b\u0271\u0285\u0296")
        buf.write("\u029d\u02a7\u02ae\u02bf\u02ce\u02d6\u02d8\u02ee\u02ff")
        buf.write("\u0346")
        return buf.getvalue()


class fstripsParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"'define'", u"')'", u"'domain'", 
                     u"':requirements'", u"':types'", u"'-'", u"'either'", 
                     u"':functions'", u"':constants'", u"':predicates'", 
                     u"':parameters'", u"':constraint'", u"':condition'", 
                     u"':event'", u"'#t'", u"':derived'", u"'*'", u"'assign'", 
                     u"'+'", u"'/'", u"'^'", u"'max'", u"'min'", u"'sin'", 
                     u"'cos'", u"'sqrt'", u"'tan'", u"'acos'", u"'asin'", 
                     u"'atan'", u"'exp'", u"'abs'", u"'>'", u"'<'", u"'='", 
                     u"'>='", u"'<='", u"'problem'", u"':domain'", u"':objects'", 
                     u"':bounds'", u"'['", u"'..'", u"']'", u"':goal'", 
                     u"':constraints'", u"'preference'", u"':metric'", u"'minimize'", 
                     u"'maximize'", u"'(total-time)'", u"'is-violated'", 
                     u"':terminal'", u"':stage'", u"'at-end'", u"'always'", 
                     u"'sometime'", u"'within'", u"'at-most-once'", u"'sometime-after'", 
                     u"'sometime-before'", u"'always-within'", u"'hold-during'", 
                     u"'hold-after'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'scale-up'", u"'scale-down'", u"'int'", u"'float'", 
                     u"'object'", u"'number'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"REQUIRE_KEY", u"K_AND", 
                      u"K_NOT", u"K_OR", u"K_IMPLY", u"K_EXISTS", u"K_FORALL", 
                      u"K_WHEN", u"K_ACTION", u"K_INCREASE", u"K_DECREASE", 
                      u"K_SCALEUP", u"K_SCALEDOWN", u"INT_T", u"FLOAT_T", 
                      u"OBJECT_T", u"NUMBER_T", u"NAME", u"EXTNAME", u"VARIABLE", 
                      u"NUMBER", u"LINE_COMMENT", u"WHITESPACE", u"K_INIT", 
                      u"K_PRECONDITION", u"K_EFFECT", u"DOMAIN", u"DOMAIN_NAME", 
                      u"REQUIREMENTS", u"TYPES", u"EITHER_TYPE", u"CONSTANTS", 
                      u"FUNCTIONS", u"FREE_FUNCTIONS", u"PREDICATES", u"ACTION", 
                      u"CONSTRAINT", u"EVENT", u"GLOBAL_CONSTRAINT", u"DURATIVE_ACTION", 
                      u"PROBLEM", u"PROBLEM_NAME", u"PROBLEM_DOMAIN", u"OBJECTS", 
                      u"INIT", u"FUNC_HEAD", u"PRECONDITION", u"EFFECT", 
                      u"AND_GD", u"OR_GD", u"NOT_GD", u"IMPLY_GD", u"EXISTS_GD", 
                      u"FORALL_GD", u"COMPARISON_GD", u"AND_EFFECT", u"FORALL_EFFECT", 
                      u"WHEN_EFFECT", u"ASSIGN_EFFECT", u"NOT_EFFECT", u"PRED_HEAD", 
                      u"GOAL", u"BINARY_OP", u"EQUALITY_CON", u"MULTI_OP", 
                      u"MINUS_OP", u"UNARY_MINUS", u"INIT_EQ", u"INIT_AT", 
                      u"NOT_PRED_INIT", u"PRED_INST", u"PROBLEM_CONSTRAINT", 
                      u"PROBLEM_METRIC" ]

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
    RULE_constant_declaration = 18
    RULE_predicate_definition_block = 19
    RULE_single_predicate_definition = 20
    RULE_predicate = 21
    RULE_function_name = 22
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
    RULE_atomicTermFormula = 33
    RULE_term = 34
    RULE_functionTerm = 35
    RULE_derivedDef = 36
    RULE_processEffectExp = 37
    RULE_processFunctionEff = 38
    RULE_processConstEff = 39
    RULE_processVarEff = 40
    RULE_effect = 41
    RULE_single_effect = 42
    RULE_atomic_effect = 43
    RULE_builtin_binary_function = 44
    RULE_builtin_unary_function = 45
    RULE_builtin_binary_predicate = 46
    RULE_assignOp = 47
    RULE_problem = 48
    RULE_problemMeta = 49
    RULE_problemDecl = 50
    RULE_problemDomain = 51
    RULE_object_declaration = 52
    RULE_boundsDecl = 53
    RULE_typeBoundsDefinition = 54
    RULE_init = 55
    RULE_init_element = 56
    RULE_flat_term = 57
    RULE_flat_atom = 58
    RULE_constant_name = 59
    RULE_goal = 60
    RULE_probConstraints = 61
    RULE_prefConGD = 62
    RULE_metricSpec = 63
    RULE_optimization = 64
    RULE_metricFExp = 65
    RULE_terminalCost = 66
    RULE_stageCost = 67
    RULE_conGD = 68

    ruleNames =  [ "pddlDoc", "domain", "domainName", "requireDef", "declaration_of_types", 
                   "numericBuiltinType", "builtinType", "possibly_typed_name_list", 
                   "name_list_with_type", "possibly_typed_variable_list", 
                   "variable_list_with_type", "typename", "primitive_type", 
                   "function_definition_block", "single_function_definition", 
                   "typed_function_definition", "untyped_function_definition", 
                   "logical_symbol_name", "constant_declaration", "predicate_definition_block", 
                   "single_predicate_definition", "predicate", "function_name", 
                   "structureDef", "actionDef", "constraintDef", "eventDef", 
                   "actionName", "constraintSymbol", "eventSymbol", "actionDefBody", 
                   "precondition", "goalDesc", "atomicTermFormula", "term", 
                   "functionTerm", "derivedDef", "processEffectExp", "processFunctionEff", 
                   "processConstEff", "processVarEff", "effect", "single_effect", 
                   "atomic_effect", "builtin_binary_function", "builtin_unary_function", 
                   "builtin_binary_predicate", "assignOp", "problem", "problemMeta", 
                   "problemDecl", "problemDomain", "object_declaration", 
                   "boundsDecl", "typeBoundsDefinition", "init", "init_element", 
                   "flat_term", "flat_atom", "constant_name", "goal", "probConstraints", 
                   "prefConGD", "metricSpec", "optimization", "metricFExp", 
                   "terminalCost", "stageCost", "conGD" ]

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
    REQUIRE_KEY=66
    K_AND=67
    K_NOT=68
    K_OR=69
    K_IMPLY=70
    K_EXISTS=71
    K_FORALL=72
    K_WHEN=73
    K_ACTION=74
    K_INCREASE=75
    K_DECREASE=76
    K_SCALEUP=77
    K_SCALEDOWN=78
    INT_T=79
    FLOAT_T=80
    OBJECT_T=81
    NUMBER_T=82
    NAME=83
    EXTNAME=84
    VARIABLE=85
    NUMBER=86
    LINE_COMMENT=87
    WHITESPACE=88
    K_INIT=89
    K_PRECONDITION=90
    K_EFFECT=91
    DOMAIN=92
    DOMAIN_NAME=93
    REQUIREMENTS=94
    TYPES=95
    EITHER_TYPE=96
    CONSTANTS=97
    FUNCTIONS=98
    FREE_FUNCTIONS=99
    PREDICATES=100
    ACTION=101
    CONSTRAINT=102
    EVENT=103
    GLOBAL_CONSTRAINT=104
    DURATIVE_ACTION=105
    PROBLEM=106
    PROBLEM_NAME=107
    PROBLEM_DOMAIN=108
    OBJECTS=109
    INIT=110
    FUNC_HEAD=111
    PRECONDITION=112
    EFFECT=113
    AND_GD=114
    OR_GD=115
    NOT_GD=116
    IMPLY_GD=117
    EXISTS_GD=118
    FORALL_GD=119
    COMPARISON_GD=120
    AND_EFFECT=121
    FORALL_EFFECT=122
    WHEN_EFFECT=123
    ASSIGN_EFFECT=124
    NOT_EFFECT=125
    PRED_HEAD=126
    GOAL=127
    BINARY_OP=128
    EQUALITY_CON=129
    MULTI_OP=130
    MINUS_OP=131
    UNARY_MINUS=132
    INIT_EQ=133
    INIT_AT=134
    NOT_PRED_INIT=135
    PRED_INST=136
    PROBLEM_CONSTRAINT=137
    PROBLEM_METRIC=138

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
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
            if isinstance( listener, fstripsListener ):
                listener.enterPddlDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitPddlDoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitPddlDoc(self)
            else:
                return visitor.visitChildren(self)




    def pddlDoc(self):

        localctx = fstripsParser.PddlDocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pddlDoc)
        try:
            self.state = 140
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.domain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
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


        def constant_declaration(self):
            return self.getTypedRuleContext(fstripsParser.Constant_declarationContext,0)


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
            if isinstance( listener, fstripsListener ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitDomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitDomain(self)
            else:
                return visitor.visitChildren(self)




    def domain(self):

        localctx = fstripsParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(fstripsParser.T__0)
            self.state = 143
            self.match(fstripsParser.T__1)
            self.state = 144
            self.domainName()
            self.state = 146
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 145
                self.requireDef()


            self.state = 149
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 148
                self.declaration_of_types()


            self.state = 152
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 151
                self.constant_declaration()


            self.state = 155
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 154
                self.predicate_definition_block()


            self.state = 158
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 157
                self.function_definition_block()


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 160
                self.structureDef()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
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
            if isinstance( listener, fstripsListener ):
                listener.enterDomainName(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitDomainName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitDomainName(self)
            else:
                return visitor.visitChildren(self)




    def domainName(self):

        localctx = fstripsParser.DomainNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_domainName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(fstripsParser.T__0)
            self.state = 169
            self.match(fstripsParser.T__3)
            self.state = 170
            self.match(fstripsParser.NAME)
            self.state = 171
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
            if isinstance( listener, fstripsListener ):
                listener.enterRequireDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitRequireDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitRequireDef(self)
            else:
                return visitor.visitChildren(self)




    def requireDef(self):

        localctx = fstripsParser.RequireDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_requireDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(fstripsParser.T__0)
            self.state = 174
            self.match(fstripsParser.T__4)
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 175
                self.match(fstripsParser.REQUIRE_KEY)
                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.REQUIRE_KEY):
                    break

            self.state = 180
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
            if isinstance( listener, fstripsListener ):
                listener.enterDeclaration_of_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitDeclaration_of_types(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitDeclaration_of_types(self)
            else:
                return visitor.visitChildren(self)




    def declaration_of_types(self):

        localctx = fstripsParser.Declaration_of_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration_of_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(fstripsParser.T__0)
            self.state = 183
            self.match(fstripsParser.T__5)
            self.state = 184
            self.possibly_typed_name_list()
            self.state = 185
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NumericBuiltinTypeContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_T(self):
            return self.getToken(fstripsParser.INT_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(NumericBuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NumericBuiltinTypeContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_T(self):
            return self.getToken(fstripsParser.FLOAT_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(NumericBuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.NumericBuiltinTypeContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_T(self):
            return self.getToken(fstripsParser.NUMBER_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)



    def numericBuiltinType(self):

        localctx = fstripsParser.NumericBuiltinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numericBuiltinType)
        try:
            self.state = 190
            token = self._input.LA(1)
            if token in [fstripsParser.INT_T]:
                localctx = fstripsParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(fstripsParser.INT_T)

            elif token in [fstripsParser.FLOAT_T]:
                localctx = fstripsParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(fstripsParser.FLOAT_T)

            elif token in [fstripsParser.NUMBER_T]:
                localctx = fstripsParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.match(fstripsParser.NUMBER_T)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.BuiltinTypeContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_T(self):
            return self.getToken(fstripsParser.OBJECT_T, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterObjectBuiltin(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitObjectBuiltin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitObjectBuiltin(self)
            else:
                return visitor.visitChildren(self)


    class NumericBuiltinContext(BuiltinTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.BuiltinTypeContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def numericBuiltinType(self):
            return self.getTypedRuleContext(fstripsParser.NumericBuiltinTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterNumericBuiltin(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitNumericBuiltin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitNumericBuiltin(self)
            else:
                return visitor.visitChildren(self)



    def builtinType(self):

        localctx = fstripsParser.BuiltinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_builtinType)
        try:
            self.state = 194
            token = self._input.LA(1)
            if token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.NUMBER_T]:
                localctx = fstripsParser.NumericBuiltinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.numericBuiltinType()

            elif token in [fstripsParser.OBJECT_T]:
                localctx = fstripsParser.ObjectBuiltinContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(fstripsParser.OBJECT_T)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_name_listContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.NAME)
            else:
                return self.getToken(fstripsParser.NAME, i)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSimpleNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSimpleNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSimpleNameList(self)
            else:
                return visitor.visitChildren(self)


    class ComplexNameListContext(Possibly_typed_name_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_name_listContext)
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
            if isinstance( listener, fstripsListener ):
                listener.enterComplexNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitComplexNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitComplexNameList(self)
            else:
                return visitor.visitChildren(self)



    def possibly_typed_name_list(self):

        localctx = fstripsParser.Possibly_typed_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_possibly_typed_name_list)
        self._la = 0 # Token type
        try:
            self.state = 213
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.SimpleNameListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.NAME:
                    self.state = 196
                    self.match(fstripsParser.NAME)
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = fstripsParser.ComplexNameListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 203 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 202
                        self.name_list_with_type()

                    else:
                        raise NoViableAltException(self)
                    self.state = 205 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.NAME:
                    self.state = 207
                    self.match(fstripsParser.NAME)
                    self.state = 212
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
            if isinstance( listener, fstripsListener ):
                listener.enterName_list_with_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitName_list_with_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitName_list_with_type(self)
            else:
                return visitor.visitChildren(self)




    def name_list_with_type(self):

        localctx = fstripsParser.Name_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_name_list_with_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 215
                self.match(fstripsParser.NAME)
                self.state = 218 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.NAME):
                    break

            self.state = 220
            self.match(fstripsParser.T__6)
            self.state = 221
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_variable_listContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(fstripsParser.VARIABLE)
            else:
                return self.getToken(fstripsParser.VARIABLE, i)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterUntypedVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitUntypedVariableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitUntypedVariableList(self)
            else:
                return visitor.visitChildren(self)


    class TypedVariableListContext(Possibly_typed_variable_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Possibly_typed_variable_listContext)
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
            if isinstance( listener, fstripsListener ):
                listener.enterTypedVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTypedVariableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTypedVariableList(self)
            else:
                return visitor.visitChildren(self)



    def possibly_typed_variable_list(self):

        localctx = fstripsParser.Possibly_typed_variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_possibly_typed_variable_list)
        self._la = 0 # Token type
        try:
            self.state = 240
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.UntypedVariableListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.VARIABLE:
                    self.state = 223
                    self.match(fstripsParser.VARIABLE)
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = fstripsParser.TypedVariableListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 230 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 229
                        self.variable_list_with_type()

                    else:
                        raise NoViableAltException(self)
                    self.state = 232 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.VARIABLE:
                    self.state = 234
                    self.match(fstripsParser.VARIABLE)
                    self.state = 239
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
            if isinstance( listener, fstripsListener ):
                listener.enterVariable_list_with_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitVariable_list_with_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitVariable_list_with_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_list_with_type(self):

        localctx = fstripsParser.Variable_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_list_with_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.match(fstripsParser.VARIABLE)
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.VARIABLE):
                    break

            self.state = 247
            self.match(fstripsParser.T__6)
            self.state = 248
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
            if isinstance( listener, fstripsListener ):
                listener.enterTypename(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTypename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTypename(self)
            else:
                return visitor.visitChildren(self)




    def typename(self):

        localctx = fstripsParser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typename)
        self._la = 0 # Token type
        try:
            self.state = 260
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(fstripsParser.T__0)
                self.state = 251
                self.match(fstripsParser.T__7)
                self.state = 253 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 252
                    self.primitive_type()
                    self.state = 255 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (fstripsParser.INT_T - 79)) | (1 << (fstripsParser.FLOAT_T - 79)) | (1 << (fstripsParser.OBJECT_T - 79)) | (1 << (fstripsParser.NUMBER_T - 79)) | (1 << (fstripsParser.NAME - 79)))) != 0)):
                        break

                self.state = 257
                self.match(fstripsParser.T__2)

            elif token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.OBJECT_T, fstripsParser.NUMBER_T, fstripsParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.primitive_type()

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
            if isinstance( listener, fstripsListener ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitPrimitive_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = fstripsParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primitive_type)
        try:
            self.state = 264
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(fstripsParser.NAME)

            elif token in [fstripsParser.INT_T, fstripsParser.FLOAT_T, fstripsParser.OBJECT_T, fstripsParser.NUMBER_T]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.builtinType()

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
            if isinstance( listener, fstripsListener ):
                listener.enterFunction_definition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFunction_definition_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFunction_definition_block(self)
            else:
                return visitor.visitChildren(self)




    def function_definition_block(self):

        localctx = fstripsParser.Function_definition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_definition_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(fstripsParser.T__0)
            self.state = 267
            self.match(fstripsParser.T__8)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 268
                self.single_function_definition()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
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
            if isinstance( listener, fstripsListener ):
                listener.enterSingle_function_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSingle_function_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSingle_function_definition(self)
            else:
                return visitor.visitChildren(self)




    def single_function_definition(self):

        localctx = fstripsParser.Single_function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_single_function_definition)
        try:
            self.state = 278
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.typed_function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
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
            if isinstance( listener, fstripsListener ):
                listener.enterTyped_function_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTyped_function_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTyped_function_definition(self)
            else:
                return visitor.visitChildren(self)




    def typed_function_definition(self):

        localctx = fstripsParser.Typed_function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typed_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(fstripsParser.T__0)
            self.state = 281
            self.logical_symbol_name()
            self.state = 282
            self.possibly_typed_variable_list()
            self.state = 283
            self.match(fstripsParser.T__2)
            self.state = 284
            self.match(fstripsParser.T__6)
            self.state = 285
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
            if isinstance( listener, fstripsListener ):
                listener.enterUntyped_function_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitUntyped_function_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitUntyped_function_definition(self)
            else:
                return visitor.visitChildren(self)




    def untyped_function_definition(self):

        localctx = fstripsParser.Untyped_function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_untyped_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(fstripsParser.T__0)
            self.state = 288
            self.logical_symbol_name()
            self.state = 289
            self.possibly_typed_variable_list()
            self.state = 290
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
            if isinstance( listener, fstripsListener ):
                listener.enterLogical_symbol_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitLogical_symbol_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitLogical_symbol_name(self)
            else:
                return visitor.visitChildren(self)




    def logical_symbol_name(self):

        localctx = fstripsParser.Logical_symbol_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logical_symbol_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            _la = self._input.LA(1)
            if not(_la==fstripsParser.NAME or _la==fstripsParser.EXTNAME):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def possibly_typed_name_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_name_listContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_constant_declaration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterConstant_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConstant_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConstant_declaration(self)
            else:
                return visitor.visitChildren(self)




    def constant_declaration(self):

        localctx = fstripsParser.Constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(fstripsParser.T__0)
            self.state = 295
            self.match(fstripsParser.T__9)
            self.state = 296
            self.possibly_typed_name_list()
            self.state = 297
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
            if isinstance( listener, fstripsListener ):
                listener.enterPredicate_definition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitPredicate_definition_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitPredicate_definition_block(self)
            else:
                return visitor.visitChildren(self)




    def predicate_definition_block(self):

        localctx = fstripsParser.Predicate_definition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_predicate_definition_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(fstripsParser.T__0)
            self.state = 300
            self.match(fstripsParser.T__10)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 301
                self.single_predicate_definition()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
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
            if isinstance( listener, fstripsListener ):
                listener.enterSingle_predicate_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSingle_predicate_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSingle_predicate_definition(self)
            else:
                return visitor.visitChildren(self)




    def single_predicate_definition(self):

        localctx = fstripsParser.Single_predicate_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_single_predicate_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(fstripsParser.T__0)
            self.state = 310
            self.predicate()
            self.state = 311
            self.possibly_typed_variable_list()
            self.state = 312
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
            if isinstance( listener, fstripsListener ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = fstripsParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(fstripsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFunction_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFunction_name(self)
            else:
                return visitor.visitChildren(self)




    def function_name(self):

        localctx = fstripsParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
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


        def getRuleIndex(self):
            return fstripsParser.RULE_structureDef

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterStructureDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitStructureDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitStructureDef(self)
            else:
                return visitor.visitChildren(self)




    def structureDef(self):

        localctx = fstripsParser.StructureDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_structureDef)
        try:
            self.state = 322
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.actionDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.eventDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.derivedDef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.constraintDef()
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

        def K_ACTION(self):
            return self.getToken(fstripsParser.K_ACTION, 0)

        def actionName(self):
            return self.getTypedRuleContext(fstripsParser.ActionNameContext,0)


        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)


        def actionDefBody(self):
            return self.getTypedRuleContext(fstripsParser.ActionDefBodyContext,0)


        def getRuleIndex(self):
            return fstripsParser.RULE_actionDef

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterActionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitActionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitActionDef(self)
            else:
                return visitor.visitChildren(self)




    def actionDef(self):

        localctx = fstripsParser.ActionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_actionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(fstripsParser.T__0)
            self.state = 325
            self.match(fstripsParser.K_ACTION)
            self.state = 326
            self.actionName()
            self.state = 327
            self.match(fstripsParser.T__11)
            self.state = 328
            self.match(fstripsParser.T__0)
            self.state = 329
            self.possibly_typed_variable_list()
            self.state = 330
            self.match(fstripsParser.T__2)
            self.state = 331
            self.actionDefBody()
            self.state = 332
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
            if isinstance( listener, fstripsListener ):
                listener.enterConstraintDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConstraintDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConstraintDef(self)
            else:
                return visitor.visitChildren(self)




    def constraintDef(self):

        localctx = fstripsParser.ConstraintDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_constraintDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(fstripsParser.T__0)
            self.state = 335
            self.match(fstripsParser.T__12)
            self.state = 336
            self.constraintSymbol()
            self.state = 337
            self.match(fstripsParser.T__11)
            self.state = 338
            self.match(fstripsParser.T__0)
            self.state = 339
            self.possibly_typed_variable_list()
            self.state = 340
            self.match(fstripsParser.T__2)
            self.state = 341
            self.match(fstripsParser.T__13)
            self.state = 342
            self.goalDesc()
            self.state = 343
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
            if isinstance( listener, fstripsListener ):
                listener.enterEventDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitEventDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitEventDef(self)
            else:
                return visitor.visitChildren(self)




    def eventDef(self):

        localctx = fstripsParser.EventDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_eventDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(fstripsParser.T__0)
            self.state = 346
            self.match(fstripsParser.T__14)
            self.state = 347
            self.eventSymbol()
            self.state = 348
            self.match(fstripsParser.T__11)
            self.state = 349
            self.match(fstripsParser.T__0)
            self.state = 350
            self.possibly_typed_variable_list()
            self.state = 351
            self.match(fstripsParser.T__2)
            self.state = 352
            self.actionDefBody()
            self.state = 353
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
            if isinstance( listener, fstripsListener ):
                listener.enterActionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitActionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitActionName(self)
            else:
                return visitor.visitChildren(self)




    def actionName(self):

        localctx = fstripsParser.ActionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_actionName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            _la = self._input.LA(1)
            if not(_la==fstripsParser.NAME or _la==fstripsParser.EXTNAME):
                self._errHandler.recoverInline(self)
            else:
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
            if isinstance( listener, fstripsListener ):
                listener.enterConstraintSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConstraintSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConstraintSymbol(self)
            else:
                return visitor.visitChildren(self)




    def constraintSymbol(self):

        localctx = fstripsParser.ConstraintSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_constraintSymbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
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
            if isinstance( listener, fstripsListener ):
                listener.enterEventSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitEventSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitEventSymbol(self)
            else:
                return visitor.visitChildren(self)




    def eventSymbol(self):

        localctx = fstripsParser.EventSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_eventSymbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==fstripsParser.NAME or _la==fstripsParser.EXTNAME):
                self._errHandler.recoverInline(self)
            else:
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
            if isinstance( listener, fstripsListener ):
                listener.enterActionDefBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitActionDefBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitActionDefBody(self)
            else:
                return visitor.visitChildren(self)




    def actionDefBody(self):

        localctx = fstripsParser.ActionDefBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_actionDefBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(fstripsParser.K_PRECONDITION)
            self.state = 362
            self.precondition()
            self.state = 363
            self.match(fstripsParser.K_EFFECT)
            self.state = 364
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PreconditionContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterRegularPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitRegularPrecondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitRegularPrecondition(self)
            else:
                return visitor.visitChildren(self)


    class TrivialPreconditionContext(PreconditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PreconditionContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTrivialPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTrivialPrecondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTrivialPrecondition(self)
            else:
                return visitor.visitChildren(self)



    def precondition(self):

        localctx = fstripsParser.PreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_precondition)
        try:
            self.state = 369
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.TrivialPreconditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(fstripsParser.T__0)
                self.state = 367
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.RegularPreconditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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



    class BuiltinBinaryAtomContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def builtin_binary_predicate(self):
            return self.getTypedRuleContext(fstripsParser.Builtin_binary_predicateContext,0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterBuiltinBinaryAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitBuiltinBinaryAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitBuiltinBinaryAtom(self)
            else:
                return visitor.visitChildren(self)


    class AndGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_AND(self):
            return self.getToken(fstripsParser.K_AND, 0)
        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAndGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAndGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAndGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class OrGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_OR(self):
            return self.getToken(fstripsParser.K_OR, 0)
        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterOrGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitOrGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitOrGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class UniversalGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_FORALL(self):
            return self.getToken(fstripsParser.K_FORALL, 0)
        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterUniversalGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitUniversalGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitUniversalGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class TermGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicTermFormula(self):
            return self.getTypedRuleContext(fstripsParser.AtomicTermFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTermGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTermGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTermGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class ExistentialGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_EXISTS(self):
            return self.getToken(fstripsParser.K_EXISTS, 0)
        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterExistentialGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitExistentialGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitExistentialGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class NotGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_NOT(self):
            return self.getToken(fstripsParser.K_NOT, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterNotGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitNotGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitNotGoalDesc(self)
            else:
                return visitor.visitChildren(self)


    class ImplyGoalDescContext(GoalDescContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.GoalDescContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_IMPLY(self):
            return self.getToken(fstripsParser.K_IMPLY, 0)
        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterImplyGoalDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitImplyGoalDesc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitImplyGoalDesc(self)
            else:
                return visitor.visitChildren(self)



    def goalDesc(self):

        localctx = fstripsParser.GoalDescContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_goalDesc)
        self._la = 0 # Token type
        try:
            self.state = 423
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.TermGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.atomicTermFormula()
                pass

            elif la_ == 2:
                localctx = fstripsParser.AndGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(fstripsParser.T__0)
                self.state = 373
                self.match(fstripsParser.K_AND)
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 374
                    self.goalDesc()
                    self.state = 379
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 380
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.OrGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(fstripsParser.T__0)
                self.state = 382
                self.match(fstripsParser.K_OR)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 383
                    self.goalDesc()
                    self.state = 388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 389
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.NotGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 390
                self.match(fstripsParser.T__0)
                self.state = 391
                self.match(fstripsParser.K_NOT)
                self.state = 392
                self.goalDesc()
                self.state = 393
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 5:
                localctx = fstripsParser.ImplyGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 395
                self.match(fstripsParser.T__0)
                self.state = 396
                self.match(fstripsParser.K_IMPLY)
                self.state = 397
                self.goalDesc()
                self.state = 398
                self.goalDesc()
                self.state = 399
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 6:
                localctx = fstripsParser.ExistentialGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 401
                self.match(fstripsParser.T__0)
                self.state = 402
                self.match(fstripsParser.K_EXISTS)
                self.state = 403
                self.match(fstripsParser.T__0)
                self.state = 404
                self.possibly_typed_variable_list()
                self.state = 405
                self.match(fstripsParser.T__2)
                self.state = 406
                self.goalDesc()
                self.state = 407
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 7:
                localctx = fstripsParser.UniversalGoalDescContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 409
                self.match(fstripsParser.T__0)
                self.state = 410
                self.match(fstripsParser.K_FORALL)
                self.state = 411
                self.match(fstripsParser.T__0)
                self.state = 412
                self.possibly_typed_variable_list()
                self.state = 413
                self.match(fstripsParser.T__2)
                self.state = 414
                self.goalDesc()
                self.state = 415
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 8:
                localctx = fstripsParser.BuiltinBinaryAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 417
                self.match(fstripsParser.T__0)
                self.state = 418
                self.builtin_binary_predicate()
                self.state = 419
                self.term()
                self.state = 420
                self.term()
                self.state = 421
                self.match(fstripsParser.T__2)
                pass


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
            if isinstance( listener, fstripsListener ):
                listener.enterAtomicTermFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAtomicTermFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAtomicTermFormula(self)
            else:
                return visitor.visitChildren(self)




    def atomicTermFormula(self):

        localctx = fstripsParser.AtomicTermFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_atomicTermFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(fstripsParser.T__0)
            self.state = 426
            self.predicate()
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0 or _la==fstripsParser.T__15 or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (fstripsParser.NAME - 83)) | (1 << (fstripsParser.VARIABLE - 83)) | (1 << (fstripsParser.NUMBER - 83)))) != 0):
                self.state = 427
                self.term()
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 433
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTermObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTermObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTermObject(self)
            else:
                return visitor.visitChildren(self)


    class TermTimeStepContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTermTimeStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTermTimeStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTermTimeStep(self)
            else:
                return visitor.visitChildren(self)


    class TermFunctionContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTermFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTermFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTermFunction(self)
            else:
                return visitor.visitChildren(self)


    class TermVariableContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(fstripsParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTermVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTermVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTermVariable(self)
            else:
                return visitor.visitChildren(self)


    class TermNumberContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.TermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTermNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTermNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTermNumber(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = fstripsParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_term)
        try:
            self.state = 440
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                localctx = fstripsParser.TermObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(fstripsParser.NAME)

            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.TermNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(fstripsParser.NUMBER)

            elif token in [fstripsParser.VARIABLE]:
                localctx = fstripsParser.TermVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(fstripsParser.VARIABLE)

            elif token in [fstripsParser.T__15]:
                localctx = fstripsParser.TermTimeStepContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.match(fstripsParser.T__15)

            elif token in [fstripsParser.T__0]:
                localctx = fstripsParser.TermFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.functionTerm()

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FunctionTermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def builtin_unary_function(self):
            return self.getTypedRuleContext(fstripsParser.Builtin_unary_functionContext,0)

        def term(self):
            return self.getTypedRuleContext(fstripsParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterUnaryArithmeticFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitUnaryArithmeticFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitUnaryArithmeticFunctionTerm(self)
            else:
                return visitor.visitChildren(self)


    class BinaryArithmeticFunctionTermContext(FunctionTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FunctionTermContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def builtin_binary_function(self):
            return self.getTypedRuleContext(fstripsParser.Builtin_binary_functionContext,0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.TermContext)
            else:
                return self.getTypedRuleContext(fstripsParser.TermContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterBinaryArithmeticFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitBinaryArithmeticFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitBinaryArithmeticFunctionTerm(self)
            else:
                return visitor.visitChildren(self)


    class GenericFunctionTermContext(FunctionTermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.FunctionTermContext)
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
            if isinstance( listener, fstripsListener ):
                listener.enterGenericFunctionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitGenericFunctionTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitGenericFunctionTerm(self)
            else:
                return visitor.visitChildren(self)



    def functionTerm(self):

        localctx = fstripsParser.FunctionTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_functionTerm)
        self._la = 0 # Token type
        try:
            self.state = 463
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.GenericFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(fstripsParser.T__0)
                self.state = 443
                self.logical_symbol_name()
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0 or _la==fstripsParser.T__15 or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (fstripsParser.NAME - 83)) | (1 << (fstripsParser.VARIABLE - 83)) | (1 << (fstripsParser.NUMBER - 83)))) != 0):
                    self.state = 444
                    self.term()
                    self.state = 449
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 450
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.BinaryArithmeticFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(fstripsParser.T__0)
                self.state = 453
                self.builtin_binary_function()
                self.state = 454
                self.term()
                self.state = 455
                self.term()
                self.state = 456
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.UnaryArithmeticFunctionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.match(fstripsParser.T__0)
                self.state = 459
                self.builtin_unary_function()
                self.state = 460
                self.term()
                self.state = 461
                self.match(fstripsParser.T__2)
                pass


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
            if isinstance( listener, fstripsListener ):
                listener.enterDerivedDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitDerivedDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitDerivedDef(self)
            else:
                return visitor.visitChildren(self)




    def derivedDef(self):

        localctx = fstripsParser.DerivedDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_derivedDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(fstripsParser.T__0)
            self.state = 466
            self.match(fstripsParser.T__16)
            self.state = 467
            self.possibly_typed_variable_list()
            self.state = 468
            self.goalDesc()
            self.state = 469
            self.match(fstripsParser.T__2)
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def processFunctionEff(self):
            return self.getTypedRuleContext(fstripsParser.ProcessFunctionEffContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterFunctionalProcessEffectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFunctionalProcessEffectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFunctionalProcessEffectExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConstProcessEffectExprContext(ProcessEffectExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def processConstEff(self):
            return self.getTypedRuleContext(fstripsParser.ProcessConstEffContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterConstProcessEffectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConstProcessEffectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConstProcessEffectExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableProcessEffectExprContext(ProcessEffectExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ProcessEffectExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def processVarEff(self):
            return self.getTypedRuleContext(fstripsParser.ProcessVarEffContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterVariableProcessEffectExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitVariableProcessEffectExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitVariableProcessEffectExpr(self)
            else:
                return visitor.visitChildren(self)



    def processEffectExp(self):

        localctx = fstripsParser.ProcessEffectExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_processEffectExp)
        try:
            self.state = 486
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.FunctionalProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(fstripsParser.T__0)
                self.state = 472
                self.match(fstripsParser.T__17)
                self.state = 473
                self.processFunctionEff()
                self.state = 474
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ConstProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.match(fstripsParser.T__0)
                self.state = 477
                self.match(fstripsParser.T__17)
                self.state = 478
                self.processConstEff()
                self.state = 479
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.VariableProcessEffectExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 481
                self.match(fstripsParser.T__0)
                self.state = 482
                self.match(fstripsParser.T__17)
                self.state = 483
                self.processVarEff()
                self.state = 484
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
            if isinstance( listener, fstripsListener ):
                listener.enterProcessFunctionEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProcessFunctionEff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProcessFunctionEff(self)
            else:
                return visitor.visitChildren(self)




    def processFunctionEff(self):

        localctx = fstripsParser.ProcessFunctionEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_processFunctionEff)
        try:
            self.state = 493
            token = self._input.LA(1)
            if token in [fstripsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.functionTerm()
                self.state = 489
                self.match(fstripsParser.T__15)

            elif token in [fstripsParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.match(fstripsParser.T__15)
                self.state = 492
                self.functionTerm()

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
            if isinstance( listener, fstripsListener ):
                listener.enterProcessConstEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProcessConstEff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProcessConstEff(self)
            else:
                return visitor.visitChildren(self)




    def processConstEff(self):

        localctx = fstripsParser.ProcessConstEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_processConstEff)
        try:
            self.state = 499
            token = self._input.LA(1)
            if token in [fstripsParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(fstripsParser.NUMBER)
                self.state = 496
                self.match(fstripsParser.T__15)

            elif token in [fstripsParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.match(fstripsParser.T__15)
                self.state = 498
                self.match(fstripsParser.NUMBER)

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
            if isinstance( listener, fstripsListener ):
                listener.enterProcessVarEff(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProcessVarEff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProcessVarEff(self)
            else:
                return visitor.visitChildren(self)




    def processVarEff(self):

        localctx = fstripsParser.ProcessVarEffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_processVarEff)
        try:
            self.state = 505
            token = self._input.LA(1)
            if token in [fstripsParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(fstripsParser.VARIABLE)
                self.state = 502
                self.match(fstripsParser.T__15)

            elif token in [fstripsParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(fstripsParser.T__15)
                self.state = 504
                self.match(fstripsParser.VARIABLE)

            else:
                raise NoViableAltException(self)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.EffectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def single_effect(self):
            return self.getTypedRuleContext(fstripsParser.Single_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSingleEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSingleEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSingleEffect(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctiveEffectFormulaContext(EffectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.EffectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_AND(self):
            return self.getToken(fstripsParser.K_AND, 0)
        def single_effect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Single_effectContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Single_effectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterConjunctiveEffectFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConjunctiveEffectFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConjunctiveEffectFormula(self)
            else:
                return visitor.visitChildren(self)



    def effect(self):

        localctx = fstripsParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.state = 517
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctiveEffectFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(fstripsParser.T__0)
                self.state = 508
                self.match(fstripsParser.K_AND)
                self.state = 512
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 509
                    self.single_effect()
                    self.state = 514
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 515
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.SingleEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.single_effect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_effectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_single_effect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SingleConditionalEffectContext(Single_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Single_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_WHEN(self):
            return self.getToken(fstripsParser.K_WHEN, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)

        def atomic_effect(self):
            return self.getTypedRuleContext(fstripsParser.Atomic_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSingleConditionalEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSingleConditionalEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSingleConditionalEffect(self)
            else:
                return visitor.visitChildren(self)


    class MultipleConditionalEffectContext(Single_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Single_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_WHEN(self):
            return self.getToken(fstripsParser.K_WHEN, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)

        def K_AND(self):
            return self.getToken(fstripsParser.K_AND, 0)
        def atomic_effect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Atomic_effectContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Atomic_effectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterMultipleConditionalEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitMultipleConditionalEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitMultipleConditionalEffect(self)
            else:
                return visitor.visitChildren(self)


    class UniversallyQuantifiedEffectContext(Single_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Single_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_FORALL(self):
            return self.getToken(fstripsParser.K_FORALL, 0)
        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def effect(self):
            return self.getTypedRuleContext(fstripsParser.EffectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterUniversallyQuantifiedEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitUniversallyQuantifiedEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitUniversallyQuantifiedEffect(self)
            else:
                return visitor.visitChildren(self)


    class AtomicEffectContext(Single_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Single_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_effect(self):
            return self.getTypedRuleContext(fstripsParser.Atomic_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAtomicEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAtomicEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAtomicEffect(self)
            else:
                return visitor.visitChildren(self)



    def single_effect(self):

        localctx = fstripsParser.Single_effectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_single_effect)
        self._la = 0 # Token type
        try:
            self.state = 548
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.UniversallyQuantifiedEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.match(fstripsParser.T__0)
                self.state = 520
                self.match(fstripsParser.K_FORALL)
                self.state = 521
                self.match(fstripsParser.T__0)
                self.state = 522
                self.possibly_typed_variable_list()
                self.state = 523
                self.match(fstripsParser.T__2)
                self.state = 524
                self.effect()
                self.state = 525
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.SingleConditionalEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(fstripsParser.T__0)
                self.state = 528
                self.match(fstripsParser.K_WHEN)
                self.state = 529
                self.goalDesc()
                self.state = 530
                self.atomic_effect()
                self.state = 531
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.MultipleConditionalEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 533
                self.match(fstripsParser.T__0)
                self.state = 534
                self.match(fstripsParser.K_WHEN)
                self.state = 535
                self.goalDesc()
                self.state = 536
                self.match(fstripsParser.T__0)
                self.state = 537
                self.match(fstripsParser.K_AND)
                self.state = 541
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 538
                    self.atomic_effect()
                    self.state = 543
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 544
                self.match(fstripsParser.T__2)
                self.state = 545
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AtomicEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 547
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_NOT(self):
            return self.getToken(fstripsParser.K_NOT, 0)
        def atomicTermFormula(self):
            return self.getTypedRuleContext(fstripsParser.AtomicTermFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterDeleteAtomEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitDeleteAtomEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitDeleteAtomEffect(self)
            else:
                return visitor.visitChildren(self)


    class AssignEffectContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignOp(self):
            return self.getTypedRuleContext(fstripsParser.AssignOpContext,0)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)

        def term(self):
            return self.getTypedRuleContext(fstripsParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAssignEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAssignEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAssignEffect(self)
            else:
                return visitor.visitChildren(self)


    class AssignConstantContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)

        def term(self):
            return self.getTypedRuleContext(fstripsParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAssignConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAssignConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAssignConstant(self)
            else:
                return visitor.visitChildren(self)


    class AddAtomEffectContext(Atomic_effectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Atomic_effectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicTermFormula(self):
            return self.getTypedRuleContext(fstripsParser.AtomicTermFormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAddAtomEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAddAtomEffect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAddAtomEffect(self)
            else:
                return visitor.visitChildren(self)



    def atomic_effect(self):

        localctx = fstripsParser.Atomic_effectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_atomic_effect)
        try:
            self.state = 568
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.AssignConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.match(fstripsParser.T__0)
                self.state = 551
                self.match(fstripsParser.T__18)
                self.state = 552
                self.functionTerm()
                self.state = 553
                self.term()
                self.state = 554
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.AssignEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.match(fstripsParser.T__0)
                self.state = 557
                self.assignOp()
                self.state = 558
                self.functionTerm()
                self.state = 559
                self.term()
                self.state = 560
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.DeleteAtomEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 562
                self.match(fstripsParser.T__0)
                self.state = 563
                self.match(fstripsParser.K_NOT)
                self.state = 564
                self.atomicTermFormula()
                self.state = 565
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AddAtomEffectContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 567
                self.atomicTermFormula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Builtin_binary_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_builtin_binary_function

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterBuiltin_binary_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitBuiltin_binary_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitBuiltin_binary_function(self)
            else:
                return visitor.visitChildren(self)




    def builtin_binary_function(self):

        localctx = fstripsParser.Builtin_binary_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_builtin_binary_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__6) | (1 << fstripsParser.T__17) | (1 << fstripsParser.T__19) | (1 << fstripsParser.T__20) | (1 << fstripsParser.T__21) | (1 << fstripsParser.T__22) | (1 << fstripsParser.T__23))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Builtin_unary_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_builtin_unary_function

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterBuiltin_unary_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitBuiltin_unary_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitBuiltin_unary_function(self)
            else:
                return visitor.visitChildren(self)




    def builtin_unary_function(self):

        localctx = fstripsParser.Builtin_unary_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_builtin_unary_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__6) | (1 << fstripsParser.T__24) | (1 << fstripsParser.T__25) | (1 << fstripsParser.T__26) | (1 << fstripsParser.T__27) | (1 << fstripsParser.T__28) | (1 << fstripsParser.T__29) | (1 << fstripsParser.T__30) | (1 << fstripsParser.T__31) | (1 << fstripsParser.T__32))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Builtin_binary_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_builtin_binary_predicate

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterBuiltin_binary_predicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitBuiltin_binary_predicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitBuiltin_binary_predicate(self)
            else:
                return visitor.visitChildren(self)




    def builtin_binary_predicate(self):

        localctx = fstripsParser.Builtin_binary_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_builtin_binary_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << fstripsParser.T__33) | (1 << fstripsParser.T__34) | (1 << fstripsParser.T__35) | (1 << fstripsParser.T__36) | (1 << fstripsParser.T__37))) != 0)):
                self._errHandler.recoverInline(self)
            else:
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

        def K_SCALEUP(self):
            return self.getToken(fstripsParser.K_SCALEUP, 0)

        def K_SCALEDOWN(self):
            return self.getToken(fstripsParser.K_SCALEDOWN, 0)

        def K_INCREASE(self):
            return self.getToken(fstripsParser.K_INCREASE, 0)

        def K_DECREASE(self):
            return self.getToken(fstripsParser.K_DECREASE, 0)

        def getRuleIndex(self):
            return fstripsParser.RULE_assignOp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAssignOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAssignOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAssignOp(self)
            else:
                return visitor.visitChildren(self)




    def assignOp(self):

        localctx = fstripsParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            _la = self._input.LA(1)
            if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (fstripsParser.K_INCREASE - 75)) | (1 << (fstripsParser.K_DECREASE - 75)) | (1 << (fstripsParser.K_SCALEUP - 75)) | (1 << (fstripsParser.K_SCALEDOWN - 75)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
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
            if isinstance( listener, fstripsListener ):
                listener.enterProblem(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProblem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProblem(self)
            else:
                return visitor.visitChildren(self)




    def problem(self):

        localctx = fstripsParser.ProblemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_problem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(fstripsParser.T__0)
            self.state = 579
            self.match(fstripsParser.T__1)
            self.state = 580
            self.problemDecl()
            self.state = 581
            self.problemDomain()
            self.state = 583
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 582
                self.requireDef()


            self.state = 586
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 585
                self.object_declaration()


            self.state = 588
            self.init()
            self.state = 589
            self.goal()
            self.state = 593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 590
                self.problemMeta()
                self.state = 595
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 596
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
            if isinstance( listener, fstripsListener ):
                listener.enterProblemMeta(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProblemMeta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProblemMeta(self)
            else:
                return visitor.visitChildren(self)




    def problemMeta(self):

        localctx = fstripsParser.ProblemMetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_problemMeta)
        try:
            self.state = 601
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.probConstraints()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.boundsDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
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
            if isinstance( listener, fstripsListener ):
                listener.enterProblemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProblemDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProblemDecl(self)
            else:
                return visitor.visitChildren(self)




    def problemDecl(self):

        localctx = fstripsParser.ProblemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_problemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(fstripsParser.T__0)
            self.state = 604
            self.match(fstripsParser.T__38)
            self.state = 605
            self.match(fstripsParser.NAME)
            self.state = 606
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
            if isinstance( listener, fstripsListener ):
                listener.enterProblemDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProblemDomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProblemDomain(self)
            else:
                return visitor.visitChildren(self)




    def problemDomain(self):

        localctx = fstripsParser.ProblemDomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_problemDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(fstripsParser.T__0)
            self.state = 609
            self.match(fstripsParser.T__39)
            self.state = 610
            self.match(fstripsParser.NAME)
            self.state = 611
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
            if isinstance( listener, fstripsListener ):
                listener.enterObject_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitObject_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitObject_declaration(self)
            else:
                return visitor.visitChildren(self)




    def object_declaration(self):

        localctx = fstripsParser.Object_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_object_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.match(fstripsParser.T__0)
            self.state = 614
            self.match(fstripsParser.T__40)
            self.state = 615
            self.possibly_typed_name_list()
            self.state = 616
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
            if isinstance( listener, fstripsListener ):
                listener.enterBoundsDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitBoundsDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitBoundsDecl(self)
            else:
                return visitor.visitChildren(self)




    def boundsDecl(self):

        localctx = fstripsParser.BoundsDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_boundsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.match(fstripsParser.T__0)
            self.state = 619
            self.match(fstripsParser.T__41)
            self.state = 621 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 620
                self.typeBoundsDefinition()
                self.state = 623 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==fstripsParser.T__0):
                    break

            self.state = 625
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
            if isinstance( listener, fstripsListener ):
                listener.enterTypeBoundsDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTypeBoundsDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTypeBoundsDefinition(self)
            else:
                return visitor.visitChildren(self)




    def typeBoundsDefinition(self):

        localctx = fstripsParser.TypeBoundsDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_typeBoundsDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(fstripsParser.T__0)
            self.state = 628
            self.match(fstripsParser.NAME)
            self.state = 629
            self.match(fstripsParser.T__6)
            self.state = 630
            self.numericBuiltinType()
            self.state = 631
            self.match(fstripsParser.T__42)
            self.state = 632
            self.match(fstripsParser.NUMBER)
            self.state = 633
            self.match(fstripsParser.T__43)
            self.state = 634
            self.match(fstripsParser.NUMBER)
            self.state = 635
            self.match(fstripsParser.T__44)
            self.state = 636
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

        def init_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Init_elementContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Init_elementContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = fstripsParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(fstripsParser.T__0)
            self.state = 639
            self.match(fstripsParser.K_INIT)
            self.state = 643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.T__0:
                self.state = 640
                self.init_element()
                self.state = 645
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 646
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Init_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_init_element

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InitFunctionAssignmentContext(Init_elementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Init_elementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def flat_term(self):
            return self.getTypedRuleContext(fstripsParser.Flat_termContext,0)

        def constant_name(self):
            return self.getTypedRuleContext(fstripsParser.Constant_nameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterInitFunctionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitInitFunctionAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitInitFunctionAssignment(self)
            else:
                return visitor.visitChildren(self)


    class InitNegativeLiteralContext(Init_elementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Init_elementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_NOT(self):
            return self.getToken(fstripsParser.K_NOT, 0)
        def flat_atom(self):
            return self.getTypedRuleContext(fstripsParser.Flat_atomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterInitNegativeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitInitNegativeLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitInitNegativeLiteral(self)
            else:
                return visitor.visitChildren(self)


    class InitPositiveLiteralContext(Init_elementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Init_elementContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def flat_atom(self):
            return self.getTypedRuleContext(fstripsParser.Flat_atomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterInitPositiveLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitInitPositiveLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitInitPositiveLiteral(self)
            else:
                return visitor.visitChildren(self)



    def init_element(self):

        localctx = fstripsParser.Init_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_init_element)
        try:
            self.state = 660
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.InitPositiveLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.flat_atom()
                pass

            elif la_ == 2:
                localctx = fstripsParser.InitNegativeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 649
                self.match(fstripsParser.T__0)
                self.state = 650
                self.match(fstripsParser.K_NOT)
                self.state = 651
                self.flat_atom()
                self.state = 652
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.InitFunctionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 654
                self.match(fstripsParser.T__0)
                self.state = 655
                self.match(fstripsParser.T__35)
                self.state = 656
                self.flat_term()
                self.state = 657
                self.constant_name()
                self.state = 658
                self.match(fstripsParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Flat_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_name(self):
            return self.getTypedRuleContext(fstripsParser.Function_nameContext,0)


        def constant_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Constant_nameContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Constant_nameContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_flat_term

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterFlat_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFlat_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFlat_term(self)
            else:
                return visitor.visitChildren(self)




    def flat_term(self):

        localctx = fstripsParser.Flat_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_flat_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self.match(fstripsParser.T__0)
            self.state = 663
            self.function_name()
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.NAME or _la==fstripsParser.NUMBER:
                self.state = 664
                self.constant_name()
                self.state = 669
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 670
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Flat_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(fstripsParser.PredicateContext,0)


        def constant_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.Constant_nameContext)
            else:
                return self.getTypedRuleContext(fstripsParser.Constant_nameContext,i)


        def getRuleIndex(self):
            return fstripsParser.RULE_flat_atom

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterFlat_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFlat_atom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFlat_atom(self)
            else:
                return visitor.visitChildren(self)




    def flat_atom(self):

        localctx = fstripsParser.Flat_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_flat_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.match(fstripsParser.T__0)
            self.state = 673
            self.predicate()
            self.state = 677
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==fstripsParser.NAME or _la==fstripsParser.NUMBER:
                self.state = 674
                self.constant_name()
                self.state = 679
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 680
            self.match(fstripsParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constant_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fstripsParser.RULE_constant_name

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Numeric_constantContext(Constant_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Constant_nameContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterNumeric_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitNumeric_constant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitNumeric_constant(self)
            else:
                return visitor.visitChildren(self)


    class Symbolic_constantContext(Constant_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.Constant_nameContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSymbolic_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSymbolic_constant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSymbolic_constant(self)
            else:
                return visitor.visitChildren(self)



    def constant_name(self):

        localctx = fstripsParser.Constant_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_constant_name)
        try:
            self.state = 684
            token = self._input.LA(1)
            if token in [fstripsParser.NAME]:
                localctx = fstripsParser.Symbolic_constantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 682
                self.match(fstripsParser.NAME)

            elif token in [fstripsParser.NUMBER]:
                localctx = fstripsParser.Numeric_constantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 683
                self.match(fstripsParser.NUMBER)

            else:
                raise NoViableAltException(self)

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
            if isinstance( listener, fstripsListener ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitGoal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitGoal(self)
            else:
                return visitor.visitChildren(self)




    def goal(self):

        localctx = fstripsParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self.match(fstripsParser.T__0)
            self.state = 687
            self.match(fstripsParser.T__45)
            self.state = 688
            self.goalDesc()
            self.state = 689
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
            if isinstance( listener, fstripsListener ):
                listener.enterProbConstraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProbConstraints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProbConstraints(self)
            else:
                return visitor.visitChildren(self)




    def probConstraints(self):

        localctx = fstripsParser.ProbConstraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_probConstraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(fstripsParser.T__0)
            self.state = 692
            self.match(fstripsParser.T__46)
            self.state = 693
            self.prefConGD()
            self.state = 694
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_FORALL(self):
            return self.getToken(fstripsParser.K_FORALL, 0)
        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def prefConGD(self):
            return self.getTypedRuleContext(fstripsParser.PrefConGDContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterUniversallyQuantifiedConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitUniversallyQuantifiedConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitUniversallyQuantifiedConstraint(self)
            else:
                return visitor.visitChildren(self)


    class PlainConstraintListContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def conGD(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.ConGDContext)
            else:
                return self.getTypedRuleContext(fstripsParser.ConGDContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterPlainConstraintList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitPlainConstraintList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitPlainConstraintList(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionOfConstraintsContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_AND(self):
            return self.getToken(fstripsParser.K_AND, 0)
        def prefConGD(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.PrefConGDContext)
            else:
                return self.getTypedRuleContext(fstripsParser.PrefConGDContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterConjunctionOfConstraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConjunctionOfConstraints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConjunctionOfConstraints(self)
            else:
                return visitor.visitChildren(self)


    class PreferenceConstraintContext(PrefConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.PrefConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def conGD(self):
            return self.getTypedRuleContext(fstripsParser.ConGDContext,0)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterPreferenceConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitPreferenceConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitPreferenceConstraint(self)
            else:
                return visitor.visitChildren(self)



    def prefConGD(self):

        localctx = fstripsParser.PrefConGDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_prefConGD)
        self._la = 0 # Token type
        try:
            self.state = 726
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctionOfConstraintsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 696
                self.match(fstripsParser.T__0)
                self.state = 697
                self.match(fstripsParser.K_AND)
                self.state = 701
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==fstripsParser.T__0:
                    self.state = 698
                    self.prefConGD()
                    self.state = 703
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 704
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.UniversallyQuantifiedConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 705
                self.match(fstripsParser.T__0)
                self.state = 706
                self.match(fstripsParser.K_FORALL)
                self.state = 707
                self.match(fstripsParser.T__0)
                self.state = 708
                self.possibly_typed_variable_list()
                self.state = 709
                self.match(fstripsParser.T__2)
                self.state = 710
                self.prefConGD()
                self.state = 711
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.PreferenceConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 713
                self.match(fstripsParser.T__0)
                self.state = 714
                self.match(fstripsParser.T__47)
                self.state = 716
                _la = self._input.LA(1)
                if _la==fstripsParser.NAME:
                    self.state = 715
                    self.match(fstripsParser.NAME)


                self.state = 718
                self.conGD()
                self.state = 719
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.PlainConstraintListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 722 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 721
                        self.conGD()

                    else:
                        raise NoViableAltException(self)
                    self.state = 724 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricSpecContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def optimization(self):
            return self.getTypedRuleContext(fstripsParser.OptimizationContext,0)

        def metricFExp(self):
            return self.getTypedRuleContext(fstripsParser.MetricFExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterProblemMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitProblemMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitProblemMetric(self)
            else:
                return visitor.visitChildren(self)



    def metricSpec(self):

        localctx = fstripsParser.MetricSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_metricSpec)
        try:
            localctx = fstripsParser.ProblemMetricContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 728
            self.match(fstripsParser.T__0)
            self.state = 729
            self.match(fstripsParser.T__48)
            self.state = 730
            self.optimization()
            self.state = 731
            self.metricFExp()
            self.state = 732
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
            if isinstance( listener, fstripsListener ):
                listener.enterOptimization(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitOptimization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitOptimization(self)
            else:
                return visitor.visitChildren(self)




    def optimization(self):

        localctx = fstripsParser.OptimizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_optimization)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            _la = self._input.LA(1)
            if not(_la==fstripsParser.T__49 or _la==fstripsParser.T__50):
                self._errHandler.recoverInline(self)
            else:
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionTerm(self):
            return self.getTypedRuleContext(fstripsParser.FunctionTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterFunctionalExprMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitFunctionalExprMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitFunctionalExprMetric(self)
            else:
                return visitor.visitChildren(self)


    class CompositeMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def terminalCost(self):
            return self.getTypedRuleContext(fstripsParser.TerminalCostContext,0)

        def stageCost(self):
            return self.getTypedRuleContext(fstripsParser.StageCostContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterCompositeMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitCompositeMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitCompositeMetric(self)
            else:
                return visitor.visitChildren(self)


    class IsViolatedMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(fstripsParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterIsViolatedMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitIsViolatedMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitIsViolatedMetric(self)
            else:
                return visitor.visitChildren(self)


    class TotalTimeMetricContext(MetricFExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.MetricFExpContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterTotalTimeMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTotalTimeMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTotalTimeMetric(self)
            else:
                return visitor.visitChildren(self)



    def metricFExp(self):

        localctx = fstripsParser.MetricFExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_metricFExp)
        try:
            self.state = 748
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.FunctionalExprMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 736
                self.functionTerm()
                pass

            elif la_ == 2:
                localctx = fstripsParser.CompositeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 737
                self.terminalCost()
                self.state = 738
                self.stageCost()
                pass

            elif la_ == 3:
                localctx = fstripsParser.CompositeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 740
                self.stageCost()
                self.state = 741
                self.terminalCost()
                pass

            elif la_ == 4:
                localctx = fstripsParser.TotalTimeMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 743
                self.match(fstripsParser.T__51)
                pass

            elif la_ == 5:
                localctx = fstripsParser.IsViolatedMetricContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 744
                self.match(fstripsParser.T__0)
                self.state = 745
                self.match(fstripsParser.T__52)
                self.state = 746
                self.match(fstripsParser.NAME)
                self.state = 747
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
            if isinstance( listener, fstripsListener ):
                listener.enterTerminalCost(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitTerminalCost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitTerminalCost(self)
            else:
                return visitor.visitChildren(self)




    def terminalCost(self):

        localctx = fstripsParser.TerminalCostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_terminalCost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            self.match(fstripsParser.T__0)
            self.state = 751
            self.match(fstripsParser.T__53)
            self.state = 752
            self.functionTerm()
            self.state = 753
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
            if isinstance( listener, fstripsListener ):
                listener.enterStageCost(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitStageCost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitStageCost(self)
            else:
                return visitor.visitChildren(self)




    def stageCost(self):

        localctx = fstripsParser.StageCostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_stageCost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(fstripsParser.T__0)
            self.state = 756
            self.match(fstripsParser.T__54)
            self.state = 757
            self.functionTerm()
            self.state = 758
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_FORALL(self):
            return self.getToken(fstripsParser.K_FORALL, 0)
        def possibly_typed_variable_list(self):
            return self.getTypedRuleContext(fstripsParser.Possibly_typed_variable_listContext,0)

        def conGD(self):
            return self.getTypedRuleContext(fstripsParser.ConGDContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterForallConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitForallConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitForallConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAlwaysConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAlwaysConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAlwaysConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AtEndConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAtEndConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAtEndConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAtEndConstraint(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctiveConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_AND(self):
            return self.getToken(fstripsParser.K_AND, 0)
        def conGD(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.ConGDContext)
            else:
                return self.getTypedRuleContext(fstripsParser.ConGDContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterConjunctiveConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitConjunctiveConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitConjunctiveConstraint(self)
            else:
                return visitor.visitChildren(self)


    class SometimeConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSometimeConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSometimeConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSometimeConstraint(self)
            else:
                return visitor.visitChildren(self)


    class WithinConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterWithinConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitWithinConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitWithinConstraint(self)
            else:
                return visitor.visitChildren(self)


    class HoldAfterConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fstripsParser.NUMBER, 0)
        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterHoldAfterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitHoldAfterConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitHoldAfterConstraint(self)
            else:
                return visitor.visitChildren(self)


    class SometimeBeforeConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSometimeBeforeConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSometimeBeforeConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSometimeBeforeConstraint(self)
            else:
                return visitor.visitChildren(self)


    class SometimeAfterConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fstripsParser.GoalDescContext)
            else:
                return self.getTypedRuleContext(fstripsParser.GoalDescContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterSometimeAfterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitSometimeAfterConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitSometimeAfterConstraint(self)
            else:
                return visitor.visitChildren(self)


    class HoldDuringConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
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
            if isinstance( listener, fstripsListener ):
                listener.enterHoldDuringConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitHoldDuringConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitHoldDuringConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AlwaysWithinConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
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
            if isinstance( listener, fstripsListener ):
                listener.enterAlwaysWithinConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAlwaysWithinConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAlwaysWithinConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AlternativeAlwaysConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAlternativeAlwaysConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAlternativeAlwaysConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAlternativeAlwaysConstraint(self)
            else:
                return visitor.visitChildren(self)


    class AtMostOnceConstraintContext(ConGDContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fstripsParser.ConGDContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def goalDesc(self):
            return self.getTypedRuleContext(fstripsParser.GoalDescContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.enterAtMostOnceConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, fstripsListener ):
                listener.exitAtMostOnceConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, fstripsVisitor ):
                return visitor.visitAtMostOnceConstraint(self)
            else:
                return visitor.visitChildren(self)



    def conGD(self):

        localctx = fstripsParser.ConGDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_conGD)
        self._la = 0 # Token type
        try:
            self.state = 836
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = fstripsParser.ConjunctiveConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 760
                self.match(fstripsParser.T__0)
                self.state = 761
                self.match(fstripsParser.K_AND)
                self.state = 763 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 762
                    self.conGD()
                    self.state = 765 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==fstripsParser.T__0):
                        break

                self.state = 767
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 2:
                localctx = fstripsParser.ForallConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 769
                self.match(fstripsParser.T__0)
                self.state = 770
                self.match(fstripsParser.K_FORALL)
                self.state = 771
                self.match(fstripsParser.T__0)
                self.state = 772
                self.possibly_typed_variable_list()
                self.state = 773
                self.match(fstripsParser.T__2)
                self.state = 774
                self.conGD()
                self.state = 775
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 3:
                localctx = fstripsParser.AtEndConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 777
                self.match(fstripsParser.T__0)
                self.state = 778
                self.match(fstripsParser.T__55)
                self.state = 779
                self.goalDesc()
                self.state = 780
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 4:
                localctx = fstripsParser.AlwaysConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 782
                self.match(fstripsParser.T__0)
                self.state = 783
                self.match(fstripsParser.T__56)
                self.state = 784
                self.goalDesc()
                self.state = 785
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 5:
                localctx = fstripsParser.SometimeConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 787
                self.match(fstripsParser.T__0)
                self.state = 788
                self.match(fstripsParser.T__57)
                self.state = 789
                self.goalDesc()
                self.state = 790
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 6:
                localctx = fstripsParser.WithinConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 792
                self.match(fstripsParser.T__0)
                self.state = 793
                self.match(fstripsParser.T__58)
                self.state = 794
                self.match(fstripsParser.NUMBER)
                self.state = 795
                self.goalDesc()
                self.state = 796
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 7:
                localctx = fstripsParser.AtMostOnceConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 798
                self.match(fstripsParser.T__0)
                self.state = 799
                self.match(fstripsParser.T__59)
                self.state = 800
                self.goalDesc()
                self.state = 801
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 8:
                localctx = fstripsParser.SometimeAfterConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 803
                self.match(fstripsParser.T__0)
                self.state = 804
                self.match(fstripsParser.T__60)
                self.state = 805
                self.goalDesc()
                self.state = 806
                self.goalDesc()
                self.state = 807
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 9:
                localctx = fstripsParser.SometimeBeforeConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 809
                self.match(fstripsParser.T__0)
                self.state = 810
                self.match(fstripsParser.T__61)
                self.state = 811
                self.goalDesc()
                self.state = 812
                self.goalDesc()
                self.state = 813
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 10:
                localctx = fstripsParser.AlwaysWithinConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 815
                self.match(fstripsParser.T__0)
                self.state = 816
                self.match(fstripsParser.T__62)
                self.state = 817
                self.match(fstripsParser.NUMBER)
                self.state = 818
                self.goalDesc()
                self.state = 819
                self.goalDesc()
                self.state = 820
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 11:
                localctx = fstripsParser.HoldDuringConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 822
                self.match(fstripsParser.T__0)
                self.state = 823
                self.match(fstripsParser.T__63)
                self.state = 824
                self.match(fstripsParser.NUMBER)
                self.state = 825
                self.match(fstripsParser.NUMBER)
                self.state = 826
                self.goalDesc()
                self.state = 827
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 12:
                localctx = fstripsParser.HoldAfterConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 829
                self.match(fstripsParser.T__0)
                self.state = 830
                self.match(fstripsParser.T__64)
                self.state = 831
                self.match(fstripsParser.NUMBER)
                self.state = 832
                self.goalDesc()
                self.state = 833
                self.match(fstripsParser.T__2)
                pass

            elif la_ == 13:
                localctx = fstripsParser.AlternativeAlwaysConstraintContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 835
                self.goalDesc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




