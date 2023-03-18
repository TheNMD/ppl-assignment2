# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *;
studentID = "2052932";
studentName = "Nguyen Manh Dan";



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u023a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\6\13\u00fc\n\13\r\13\16")
        buf.write("\13\u00fd\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0106\n\f\f\f")
        buf.write("\16\f\u0109\13\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7")
        buf.write("\r\u0114\n\r\f\r\16\r\u0117\13\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\7#\u0198\n#\f#")
        buf.write("\16#\u019b\13#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3>\7>\u01db\n>\f>\16>\u01de\13>\3")
        buf.write(">\3>\5>\u01e2\n>\3?\3?\5?\u01e6\n?\3?\5?\u01e9\n?\3?\3")
        buf.write("?\3?\5?\u01ee\n?\3?\3?\5?\u01f2\n?\3?\3?\3?\5?\u01f7\n")
        buf.write("?\3?\5?\u01fa\n?\3?\3?\3?\5?\u01ff\n?\3@\3@\7@\u0203\n")
        buf.write("@\f@\16@\u0206\13@\3A\3A\5A\u020a\nA\3A\6A\u020d\nA\r")
        buf.write("A\16A\u020e\3B\3B\7B\u0213\nB\fB\16B\u0216\13B\3B\3B\3")
        buf.write("B\3C\3C\3C\5C\u021e\nC\3D\3D\7D\u0222\nD\fD\16D\u0225")
        buf.write("\13D\3D\3D\3D\3D\3D\3E\3E\7E\u022e\nE\fE\16E\u0231\13")
        buf.write("E\3E\5E\u0234\nE\3E\3E\3F\3F\3F\3\u0107\2G\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write("\2\u0081\2\u0083A\u0085\2\u0087B\u0089C\u008bD\3\2\r\5")
        buf.write("\2\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\3\2\62;\3\2\63;\4\2\62;aa\4\2GGgg\4\2--//\n\2$$))")
        buf.write("^^ddhhppttvv\6\2\f\f$$))^^\2\u024c\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\3\u008d\3\2\2\2\5\u0099\3\2\2\2\7\u00a3\3\2\2")
        buf.write("\2\t\u00af\3\2\2\2\13\u00ba\3\2\2\2\r\u00c9\3\2\2\2\17")
        buf.write("\u00d6\3\2\2\2\21\u00e1\3\2\2\2\23\u00ee\3\2\2\2\25\u00fb")
        buf.write("\3\2\2\2\27\u0101\3\2\2\2\31\u010f\3\2\2\2\33\u011a\3")
        buf.write("\2\2\2\35\u011f\3\2\2\2\37\u0124\3\2\2\2!\u012c\3\2\2")
        buf.write("\2#\u0132\3\2\2\2%\u013a\3\2\2\2\'\u0141\3\2\2\2)\u0147")
        buf.write("\3\2\2\2+\u014f\3\2\2\2-\u0158\3\2\2\2/\u015d\3\2\2\2")
        buf.write("\61\u0163\3\2\2\2\63\u0167\3\2\2\2\65\u016d\3\2\2\2\67")
        buf.write("\u0170\3\2\2\29\u0176\3\2\2\2;\u017f\3\2\2\2=\u0186\3")
        buf.write("\2\2\2?\u0189\3\2\2\2A\u018e\3\2\2\2C\u0191\3\2\2\2E\u0195")
        buf.write("\3\2\2\2G\u019c\3\2\2\2I\u019e\3\2\2\2K\u01a0\3\2\2\2")
        buf.write("M\u01a2\3\2\2\2O\u01a4\3\2\2\2Q\u01a6\3\2\2\2S\u01a8\3")
        buf.write("\2\2\2U\u01ab\3\2\2\2W\u01ae\3\2\2\2Y\u01b1\3\2\2\2[\u01b4")
        buf.write("\3\2\2\2]\u01b6\3\2\2\2_\u01b9\3\2\2\2a\u01bb\3\2\2\2")
        buf.write("c\u01be\3\2\2\2e\u01c1\3\2\2\2g\u01c3\3\2\2\2i\u01c5\3")
        buf.write("\2\2\2k\u01c7\3\2\2\2m\u01c9\3\2\2\2o\u01cb\3\2\2\2q\u01cd")
        buf.write("\3\2\2\2s\u01cf\3\2\2\2u\u01d1\3\2\2\2w\u01d3\3\2\2\2")
        buf.write("y\u01d5\3\2\2\2{\u01e1\3\2\2\2}\u01fe\3\2\2\2\177\u0200")
        buf.write("\3\2\2\2\u0081\u0207\3\2\2\2\u0083\u0210\3\2\2\2\u0085")
        buf.write("\u021d\3\2\2\2\u0087\u021f\3\2\2\2\u0089\u022b\3\2\2\2")
        buf.write("\u008b\u0237\3\2\2\2\u008d\u008e\7t\2\2\u008e\u008f\7")
        buf.write("g\2\2\u008f\u0090\7c\2\2\u0090\u0091\7f\2\2\u0091\u0092")
        buf.write("\7K\2\2\u0092\u0093\7p\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7i\2\2\u0096\u0097\7g\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\4\3\2\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7H\2\2\u009e\u009f\7n\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1")
        buf.write("\7c\2\2\u00a1\u00a2\7v\2\2\u00a2\6\3\2\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7")
        buf.write("\7f\2\2\u00a7\u00a8\7D\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7c\2\2\u00ad\u00ae\7p\2\2\u00ae\b\3\2\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7f\2\2\u00b3\u00b4\7U\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7i\2\2\u00b9\n\3\2\2\2\u00ba\u00bb\7r\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7x\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7F\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\f\3\2\2\2\u00c9\u00ca\7r\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7K\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7i\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7t\2\2\u00d5\16\3\2\2\2\u00d6\u00d7")
        buf.write("\7y\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7H\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\20\3\2\2\2\u00e1\u00e2\7r\2\2\u00e2\u00e3")
        buf.write("\7t\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7D\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7p\2\2\u00ed\22\3\2\2\2\u00ee\u00ef")
        buf.write("\7r\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7U\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7i\2\2\u00f9\24\3\2\2\2\u00fa\u00fc")
        buf.write("\t\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0100\b\13\2\2\u0100\26\3\2\2\2\u0101\u0102\7\61")
        buf.write("\2\2\u0102\u0103\7,\2\2\u0103\u0107\3\2\2\2\u0104\u0106")
        buf.write("\13\2\2\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u010a\3\2\2\2")
        buf.write("\u0109\u0107\3\2\2\2\u010a\u010b\7,\2\2\u010b\u010c\7")
        buf.write("\61\2\2\u010c\u010d\3\2\2\2\u010d\u010e\b\f\2\2\u010e")
        buf.write("\30\3\2\2\2\u010f\u0110\7\61\2\2\u0110\u0111\7\61\2\2")
        buf.write("\u0111\u0115\3\2\2\2\u0112\u0114\n\3\2\2\u0113\u0112\3")
        buf.write("\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118")
        buf.write("\u0119\b\r\2\2\u0119\32\3\2\2\2\u011a\u011b\7x\2\2\u011b")
        buf.write("\u011c\7q\2\2\u011c\u011d\7k\2\2\u011d\u011e\7f\2\2\u011e")
        buf.write("\34\3\2\2\2\u011f\u0120\7c\2\2\u0120\u0121\7w\2\2\u0121")
        buf.write("\u0122\7v\2\2\u0122\u0123\7q\2\2\u0123\36\3\2\2\2\u0124")
        buf.write("\u0125\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127\7v\2\2\u0127")
        buf.write("\u0128\7g\2\2\u0128\u0129\7i\2\2\u0129\u012a\7g\2\2\u012a")
        buf.write("\u012b\7t\2\2\u012b \3\2\2\2\u012c\u012d\7h\2\2\u012d")
        buf.write("\u012e\7n\2\2\u012e\u012f\7q\2\2\u012f\u0130\7c\2\2\u0130")
        buf.write("\u0131\7v\2\2\u0131\"\3\2\2\2\u0132\u0133\7d\2\2\u0133")
        buf.write("\u0134\7q\2\2\u0134\u0135\7q\2\2\u0135\u0136\7n\2\2\u0136")
        buf.write("\u0137\7g\2\2\u0137\u0138\7c\2\2\u0138\u0139\7p\2\2\u0139")
        buf.write("$\3\2\2\2\u013a\u013b\7u\2\2\u013b\u013c\7v\2\2\u013c")
        buf.write("\u013d\7t\2\2\u013d\u013e\7k\2\2\u013e\u013f\7p\2\2\u013f")
        buf.write("\u0140\7i\2\2\u0140&\3\2\2\2\u0141\u0142\7c\2\2\u0142")
        buf.write("\u0143\7t\2\2\u0143\u0144\7t\2\2\u0144\u0145\7c\2\2\u0145")
        buf.write("\u0146\7{\2\2\u0146(\3\2\2\2\u0147\u0148\7k\2\2\u0148")
        buf.write("\u0149\7p\2\2\u0149\u014a\7j\2\2\u014a\u014b\7g\2\2\u014b")
        buf.write("\u014c\7t\2\2\u014c\u014d\7k\2\2\u014d\u014e\7v\2\2\u014e")
        buf.write("*\3\2\2\2\u014f\u0150\7h\2\2\u0150\u0151\7w\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152\u0153\7e\2\2\u0153\u0154\7v\2\2\u0154")
        buf.write("\u0155\7k\2\2\u0155\u0156\7q\2\2\u0156\u0157\7p\2\2\u0157")
        buf.write(",\3\2\2\2\u0158\u0159\7v\2\2\u0159\u015a\7t\2\2\u015a")
        buf.write("\u015b\7w\2\2\u015b\u015c\7g\2\2\u015c.\3\2\2\2\u015d")
        buf.write("\u015e\7h\2\2\u015e\u015f\7c\2\2\u015f\u0160\7n\2\2\u0160")
        buf.write("\u0161\7u\2\2\u0161\u0162\7g\2\2\u0162\60\3\2\2\2\u0163")
        buf.write("\u0164\7h\2\2\u0164\u0165\7q\2\2\u0165\u0166\7t\2\2\u0166")
        buf.write("\62\3\2\2\2\u0167\u0168\7y\2\2\u0168\u0169\7j\2\2\u0169")
        buf.write("\u016a\7k\2\2\u016a\u016b\7n\2\2\u016b\u016c\7g\2\2\u016c")
        buf.write("\64\3\2\2\2\u016d\u016e\7f\2\2\u016e\u016f\7q\2\2\u016f")
        buf.write("\66\3\2\2\2\u0170\u0171\7d\2\2\u0171\u0172\7t\2\2\u0172")
        buf.write("\u0173\7g\2\2\u0173\u0174\7c\2\2\u0174\u0175\7m\2\2\u0175")
        buf.write("8\3\2\2\2\u0176\u0177\7e\2\2\u0177\u0178\7q\2\2\u0178")
        buf.write("\u0179\7p\2\2\u0179\u017a\7v\2\2\u017a\u017b\7k\2\2\u017b")
        buf.write("\u017c\7p\2\2\u017c\u017d\7w\2\2\u017d\u017e\7g\2\2\u017e")
        buf.write(":\3\2\2\2\u017f\u0180\7t\2\2\u0180\u0181\7g\2\2\u0181")
        buf.write("\u0182\7v\2\2\u0182\u0183\7w\2\2\u0183\u0184\7t\2\2\u0184")
        buf.write("\u0185\7p\2\2\u0185<\3\2\2\2\u0186\u0187\7k\2\2\u0187")
        buf.write("\u0188\7h\2\2\u0188>\3\2\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write("\u018b\7n\2\2\u018b\u018c\7u\2\2\u018c\u018d\7g\2\2\u018d")
        buf.write("@\3\2\2\2\u018e\u018f\7q\2\2\u018f\u0190\7h\2\2\u0190")
        buf.write("B\3\2\2\2\u0191\u0192\7q\2\2\u0192\u0193\7w\2\2\u0193")
        buf.write("\u0194\7v\2\2\u0194D\3\2\2\2\u0195\u0199\t\4\2\2\u0196")
        buf.write("\u0198\t\5\2\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019aF\3\2\2")
        buf.write("\2\u019b\u0199\3\2\2\2\u019c\u019d\7-\2\2\u019dH\3\2\2")
        buf.write("\2\u019e\u019f\7/\2\2\u019fJ\3\2\2\2\u01a0\u01a1\7,\2")
        buf.write("\2\u01a1L\3\2\2\2\u01a2\u01a3\7\61\2\2\u01a3N\3\2\2\2")
        buf.write("\u01a4\u01a5\7\'\2\2\u01a5P\3\2\2\2\u01a6\u01a7\7#\2\2")
        buf.write("\u01a7R\3\2\2\2\u01a8\u01a9\7(\2\2\u01a9\u01aa\7(\2\2")
        buf.write("\u01aaT\3\2\2\2\u01ab\u01ac\7~\2\2\u01ac\u01ad\7~\2\2")
        buf.write("\u01adV\3\2\2\2\u01ae\u01af\7?\2\2\u01af\u01b0\7?\2\2")
        buf.write("\u01b0X\3\2\2\2\u01b1\u01b2\7#\2\2\u01b2\u01b3\7?\2\2")
        buf.write("\u01b3Z\3\2\2\2\u01b4\u01b5\7@\2\2\u01b5\\\3\2\2\2\u01b6")
        buf.write("\u01b7\7@\2\2\u01b7\u01b8\7?\2\2\u01b8^\3\2\2\2\u01b9")
        buf.write("\u01ba\7>\2\2\u01ba`\3\2\2\2\u01bb\u01bc\7>\2\2\u01bc")
        buf.write("\u01bd\7?\2\2\u01bdb\3\2\2\2\u01be\u01bf\7<\2\2\u01bf")
        buf.write("\u01c0\7<\2\2\u01c0d\3\2\2\2\u01c1\u01c2\7\60\2\2\u01c2")
        buf.write("f\3\2\2\2\u01c3\u01c4\7.\2\2\u01c4h\3\2\2\2\u01c5\u01c6")
        buf.write("\7=\2\2\u01c6j\3\2\2\2\u01c7\u01c8\7<\2\2\u01c8l\3\2\2")
        buf.write("\2\u01c9\u01ca\7*\2\2\u01can\3\2\2\2\u01cb\u01cc\7+\2")
        buf.write("\2\u01ccp\3\2\2\2\u01cd\u01ce\7]\2\2\u01cer\3\2\2\2\u01cf")
        buf.write("\u01d0\7_\2\2\u01d0t\3\2\2\2\u01d1\u01d2\7}\2\2\u01d2")
        buf.write("v\3\2\2\2\u01d3\u01d4\7\177\2\2\u01d4x\3\2\2\2\u01d5\u01d6")
        buf.write("\7?\2\2\u01d6z\3\2\2\2\u01d7\u01e2\t\6\2\2\u01d8\u01dc")
        buf.write("\t\7\2\2\u01d9\u01db\t\b\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01df\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\t")
        buf.write("\6\2\2\u01e0\u01e2\b>\3\2\u01e1\u01d7\3\2\2\2\u01e1\u01d8")
        buf.write("\3\2\2\2\u01e2|\3\2\2\2\u01e3\u01e5\5{>\2\u01e4\u01e6")
        buf.write("\5\177@\2\u01e5\u01e4\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write("\u01e8\3\2\2\2\u01e7\u01e9\5\u0081A\2\u01e8\u01e7\3\2")
        buf.write("\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\b?\4\2\u01eb\u01ff\3\2\2\2\u01ec\u01ee\5{>\2\u01ed\u01ec")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01f1\5\177@\2\u01f0\u01f2\5\u0081A\2\u01f1\u01f0\3\2")
        buf.write("\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4")
        buf.write("\b?\5\2\u01f4\u01ff\3\2\2\2\u01f5\u01f7\5{>\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8")
        buf.write("\u01fa\5\177@\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa\3\2\2")
        buf.write("\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\5\u0081A\2\u01fc\u01fd")
        buf.write("\b?\6\2\u01fd\u01ff\3\2\2\2\u01fe\u01e3\3\2\2\2\u01fe")
        buf.write("\u01ed\3\2\2\2\u01fe\u01f6\3\2\2\2\u01ff~\3\2\2\2\u0200")
        buf.write("\u0204\5e\63\2\u0201\u0203\t\6\2\2\u0202\u0201\3\2\2\2")
        buf.write("\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3")
        buf.write("\2\2\2\u0205\u0080\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0209")
        buf.write("\t\t\2\2\u0208\u020a\t\n\2\2\u0209\u0208\3\2\2\2\u0209")
        buf.write("\u020a\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u020d\t\6\2\2")
        buf.write("\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020e\u020f\3\2\2\2\u020f\u0082\3\2\2\2\u0210\u0214")
        buf.write("\7$\2\2\u0211\u0213\5\u0085C\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0215\u0217\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\7")
        buf.write("$\2\2\u0218\u0219\bB\7\2\u0219\u0084\3\2\2\2\u021a\u021b")
        buf.write("\7^\2\2\u021b\u021e\t\13\2\2\u021c\u021e\n\f\2\2\u021d")
        buf.write("\u021a\3\2\2\2\u021d\u021c\3\2\2\2\u021e\u0086\3\2\2\2")
        buf.write("\u021f\u0223\7$\2\2\u0220\u0222\5\u0085C\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u0226\3\2\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0226\u0227\7^\2\2\u0227\u0228\n\13\2\2\u0228\u0229\3")
        buf.write("\2\2\2\u0229\u022a\bD\b\2\u022a\u0088\3\2\2\2\u022b\u022f")
        buf.write("\7$\2\2\u022c\u022e\5\u0085C\2\u022d\u022c\3\2\2\2\u022e")
        buf.write("\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2")
        buf.write("\u0230\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0234\7")
        buf.write("\2\2\3\u0233\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235")
        buf.write("\3\2\2\2\u0235\u0236\bE\t\2\u0236\u008a\3\2\2\2\u0237")
        buf.write("\u0238\13\2\2\2\u0238\u0239\bF\n\2\u0239\u008c\3\2\2\2")
        buf.write("\30\2\u00fd\u0107\u0115\u0199\u01dc\u01e1\u01e5\u01e8")
        buf.write("\u01ed\u01f1\u01f6\u01f9\u01fe\u0204\u0209\u020e\u0214")
        buf.write("\u021d\u0223\u022f\u0233\13\b\2\2\3>\2\3?\3\3?\4\3?\5")
        buf.write("\3B\6\3D\7\3E\b\3F\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    WS = 10
    CCOMMENT = 11
    CPPCOMMENT = 12
    KWVOID = 13
    KWAUTO = 14
    KWINT = 15
    KWFLOAT = 16
    KWBOO = 17
    KWSTR = 18
    KWARR = 19
    KWINHERIT = 20
    KWFUNC = 21
    KWTRUE = 22
    KWFALSE = 23
    KWFOR = 24
    KWWHILE = 25
    KWDO = 26
    KWBRK = 27
    KWCONT = 28
    KWRTN = 29
    KWIF = 30
    KWELSE = 31
    KWOF = 32
    KWOUT = 33
    ID = 34
    ADDOP = 35
    SUBOP = 36
    MULOP = 37
    DIVOP = 38
    MODOP = 39
    EXCOP = 40
    ANDOP = 41
    OROP = 42
    EQLOP = 43
    DIFOP = 44
    LARGEOP = 45
    LEQLOP = 46
    SMALLOP = 47
    SEQLOP = 48
    CONCATOP = 49
    DOT = 50
    CM = 51
    SM = 52
    CL = 53
    LB = 54
    RB = 55
    LSB = 56
    RSB = 57
    LCB = 58
    RCB = 59
    EQL = 60
    LITINT = 61
    LITFLOAT = 62
    LITSTR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSED_STRING = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'readFloat'", "'readBoolean'", "'readString'", 
            "'preventDefault'", "'printInteger'", "'writeFloat'", "'printBoolean'", 
            "'printString'", "'void'", "'auto'", "'integer'", "'float'", 
            "'boolean'", "'string'", "'array'", "'inherit'", "'function'", 
            "'true'", "'false'", "'for'", "'while'", "'do'", "'break'", 
            "'continue'", "'return'", "'if'", "'else'", "'of'", "'out'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", "','", 
            "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
            "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
            "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", 
            "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", 
            "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
            "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "EQL", "LITINT", "LITFLOAT", "LITSTR", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", 
                  "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", 
                  "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", 
                  "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", "KWELSE", 
                  "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", 
                  "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", 
                  "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", 
                  "LITINT", "LITFLOAT", "Decimal", "Exponent", "LITSTR", 
                  "Char", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.LITINT_action 
            actions[61] = self.LITFLOAT_action 
            actions[64] = self.LITSTR_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSED_STRING_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def LITFLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def LITSTR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


