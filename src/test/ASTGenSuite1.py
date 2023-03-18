import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def testCase1(self):
        """test var declaration"""
        input = """a: string;"""
        expect = """Program([
	VarDecl(a, StringType)
])"""
        self.assertTrue(TestAST.test(input,expect,301))
        
    def testCase2(self):
        """test var declaration"""
        input = """a, b: auto = a, b;"""
        expect = """Program([
	VarDecl(a, AutoType, Id(a))
	VarDecl(b, AutoType, Id(b))
])"""
        self.assertTrue(TestAST.test(input,expect,302))
        
    def testCase3(self):
        """test var declaration"""
        input = """a, b: boolean;"""
        expect = """Program([
	VarDecl(a, BooleanType)
	VarDecl(b, BooleanType)
])"""
        self.assertTrue(TestAST.test(input,expect,303))
        
    def testCase4(self):
        """test var declaration"""
        input = """a: array[1] of float;"""
        expect = """Program([
	VarDecl(a, ArrayType([1], FloatType))
])"""
        self.assertTrue(TestAST.test(input,expect,304))
        
    def testCase5(self):
        """test var declaration"""
        input = """a: array[0,1] of float;"""
        expect = """Program([
	VarDecl(a, ArrayType([0, 1], FloatType))
])"""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def testCase6(self):
        """test var declaration"""
        input = """str: string = "string";"""
        expect = """Program([
	VarDecl(str, StringType, StringLit(string))
])"""
        self.assertTrue(TestAST.test(input,expect,306))
 
# TODO EXPECTED RA 0.023        
#     def testCase7(self):
#         """test var declaration"""
#         input = """a, b, c: array[0,1] of float = 1, "string", 0.23E-1;"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([0, 1], FloatType), IntegerLit(1))
# 	VarDecl(b, ArrayType([0, 1], FloatType), StringLit(string))
# 	VarDecl(c, ArrayType([0, 1], FloatType), FloatLit(0.023))
# ])"""
        self.assertTrue(TestAST.test(input,expect,307))
        
    def testCase8(self):
        """test var declaration"""
        input = """a: array[0,3,5] of integer = {1,2,3};"""
        expect = """Program([
	VarDecl(a, ArrayType([0, 3, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input,expect,308))
        
    def testCase9(self):
        """test var declaration"""
        input = """a,b,c: integer = {3,2,1}, {0,-1,-2}, {-3,-4,-5};
        d,e,f: float = {1,2,3}, {4,5,6}, {7,8,9};"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(3), IntegerLit(2), IntegerLit(1)]))
	VarDecl(b, IntegerType, ArrayLit([IntegerLit(0), UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(2))]))
	VarDecl(c, IntegerType, ArrayLit([UnExpr(-, IntegerLit(3)), UnExpr(-, IntegerLit(4)), UnExpr(-, IntegerLit(5))]))
	VarDecl(d, FloatType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(e, FloatType, ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
	VarDecl(f, FloatType, ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)]))
])"""
        self.assertTrue(TestAST.test(input,expect,309))
        
    def testCase10(self):
        """test var declaration"""
        input = """a: integer; b: string; c: boolean; d: float; e: auto; f: array[0,1] of integer;"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, StringType)
	VarDecl(c, BooleanType)
	VarDecl(d, FloatType)
	VarDecl(e, AutoType)
	VarDecl(f, ArrayType([0, 1], IntegerType))
])"""
        self.assertTrue(TestAST.test(input,expect,310))

    def testCase11(self):
        """test var declaration"""
        input = """a: integer = printInt(a+1*2);"""
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(printInt, [BinExpr(+, Id(a), BinExpr(*, IntegerLit(1), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,311))
        
    def testCase12(self):
        """test var declaration"""
        input = """a: integer = arr[0,1,2]; b: boolean = c||(true&&false);"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(arr, [IntegerLit(0), IntegerLit(1), IntegerLit(2)]))
	VarDecl(b, BooleanType, BinExpr(||, Id(c), BinExpr(&&, BooleanLit(True), BooleanLit(False))))
])"""
        self.assertTrue(TestAST.test(input,expect,312))
        
    def testCase13(self):
        """test var declaration"""
        input = """a,b,c: integer = readInt(),{1,2,3},x[6];"""
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(readInt, []))
	VarDecl(b, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(c, IntegerType, ArrayCell(x, [IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input,expect,313))
        
    def testCase14(self):
        """test var declaration"""
        input = """a: integer = super(!!!x[6,5,4]+a*b);"""
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(super, [BinExpr(+, UnExpr(!, UnExpr(!, UnExpr(!, ArrayCell(x, [IntegerLit(6), IntegerLit(5), IntegerLit(4)])))), BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,314))
        
    def testCase15(self):
        """test var declaration"""
        input = """a: integer = ----3--2-1;"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(-, BinExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(3))))), UnExpr(-, IntegerLit(2))), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input,expect,315))
        
    def testCase16(self):
        """test function declaration"""
        input = """a: function void(){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,316))
        
    def testCase17(self):
        """test function declaration"""
        input = """a: function void(){} b: function void(){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([]))
	FuncDecl(b, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,317))
        
    def testCase18(self):
        """test function declaration"""
        input = """a: function integer(){}
        b: function float(){}
        c: function string(){}
        d: function boolean(){}"""
        expect = """Program([
	FuncDecl(a, IntegerType, [], None, BlockStmt([]))
	FuncDecl(b, FloatType, [], None, BlockStmt([]))
	FuncDecl(c, StringType, [], None, BlockStmt([]))
	FuncDecl(d, BooleanType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,318))
        
    def testCase19(self):
        """test function declaration"""
        input = """a: function array[1] of float(){}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], FloatType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,319))
        
    def testCase20(self):
        """test function declaration"""
        input = """a: function void(x: integer){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(x, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,320))

    def testCase21(self):
        """test function declaration"""
        input = """a: function void(x: array[1] of float){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(x, ArrayType([1], FloatType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,321))
        
    def testCase22(self):
        """test function declaration"""
        input = """a: function void(x: integer, y: float, z: string, t: boolean){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(x, IntegerType), Param(y, FloatType), Param(z, StringType), Param(t, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,322))
        
    def testCase23(self):
        """test function declaration"""
        input = """a: function void(x: auto){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(x, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,323))
        
    def testCase24(self):
        """test function declaration"""
        input = """a: function void() inherit b {}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], b, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def testCase25(self):
        """test function declaration"""
        input = """a: function void() inherit b {}
        b: function void() inherit a {}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], b, BlockStmt([]))
	FuncDecl(b, VoidType, [], a, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,325))
        
    def testCase26(self):
        """test function declaration"""
        input = """a: function void(inherit x: integer){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(x, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,326))
        
    def testCase27(self):
        """test function declaration"""
        input = """a: function void(out x: integer){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [OutParam(x, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,327))
        
    def testCase28(self):
        """test function declaration"""
        input = """a: function void(inherit out x: integer, inherit y: auto, out z: array[1] of boolean){}"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritOutParam(x, IntegerType), InheritParam(y, AutoType), OutParam(z, ArrayType([1], BooleanType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,328))
        
    def testCase29(self):
        """test function declaration"""
        input = """a: function void(){a: string;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, StringType)]))
])"""
        self.assertTrue(TestAST.test(input,expect,329))
        
# TODO EXPECTED NHAN VO LUON 
#     def testCase30(self):
#         """test function with variable"""
#         input = """a: function void(){a: string; b: array[2,3] of float = {0.123E3};}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, StringType), VarDecl(b, ArrayType([2, 3], FloatType), ArrayLit([FloatLit(123.0)]))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,330))
        
    def testCase31(self):
        """test function with variable"""
        input = """a: function void(){a, b, c: integer = "hi", true, x[6];}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, StringLit(hi)), VarDecl(b, IntegerType, BooleanLit(True)), VarDecl(c, IntegerType, ArrayCell(x, [IntegerLit(6)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,331))
        
    def testCase32(self):
        """test function with variable"""
        input = """a: function void(delta: integer){delta: integer = fact(3);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(delta, IntegerType)], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,332))
        
    def testCase33(self):
        """test function with variable"""
        input = """a: function void(inherit out x: string) inherit b {a, b: auto;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritOutParam(x, StringType)], b, BlockStmt([VarDecl(a, AutoType), VarDecl(b, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input,expect,333))
        
    def testCase34(self):
        """test function with variable"""
        input = """a: function void() inherit b {a, b, c: auto = !x[6], -y[7], (z[8]::t[9])::u[10];}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], b, BlockStmt([VarDecl(a, AutoType, UnExpr(!, ArrayCell(x, [IntegerLit(6)]))), VarDecl(b, AutoType, UnExpr(-, ArrayCell(y, [IntegerLit(7)]))), VarDecl(c, AutoType, BinExpr(::, BinExpr(::, ArrayCell(z, [IntegerLit(8)]), ArrayCell(t, [IntegerLit(9)])), ArrayCell(u, [IntegerLit(10)])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,334))
        
    def testCase35(self):
        """test function with variable"""
        input = """a: function void(){a: boolean = ("a"::"b") == ("c"::"d");}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BinExpr(==, BinExpr(::, StringLit(a), StringLit(b)), BinExpr(::, StringLit(c), StringLit(d))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,335))
        
    def testCase36(self):
        """test function with if statement"""
        input = """a: function void(){if (true) return true; else return true;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,336))
        
    def testCase37(self):
        """test function with if statement and assignment statement"""
        input = """a: function void(){if (false) a=2; else a[0,1]=2;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(False), AssignStmt(Id(a), IntegerLit(2)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,337))
        
    def testCase38(self):
        """test function with if statement and break statement"""
        input = """a: function void(){if (true) if (true) return false; else return true;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ReturnStmt(BooleanLit(False)), ReturnStmt(BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,338))
        
    def testCase39(self):
        """test function with if statement and continue statement"""
        input = """a: function void(){if (true) if (true) continue; else if (false) continue;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ContinueStmt(), IfStmt(BooleanLit(False), ContinueStmt())))]))
])"""
        self.assertTrue(TestAST.test(input,expect,339))
        
    def testCase40(self):
        """test function with if statement and return statement"""
        input = """a: function void(){if (true) if (true) return false; else if (false) return true; else return false;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ReturnStmt(BooleanLit(False)), IfStmt(BooleanLit(False), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,340))
        
    def testCase41(self):
        """test function with if statement and block statement"""
        input = """a: function void(){if (n!=m) {}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BinExpr(!=, Id(n), Id(m)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,341))
        
    def testCase42(self):
        """test function with if statement and for statement"""
        input = """a: function void(){if (true) for(i=0,i<10,i+1){}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,342))
        
    def testCase43(self):
        """test function with if statement and while statement"""
        input = """a: function void(){if (true) while(a>3){} else a=3;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), WhileStmt(BinExpr(>, Id(a), IntegerLit(3)), BlockStmt([])), AssignStmt(Id(a), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,343))
        
    def testCase44(self):
        """test function with if statement and do while statement"""
        input = """a: function void(){if (true) if (true) do {} while(true);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), DoWhileStmt(BooleanLit(True), BlockStmt([]))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,344))
        
    def testCase45(self):
        """test function with if statement and call statement"""
        input = """a: function void(){if (true) return true; else if (false) foo(n-b*2);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(BooleanLit(True)), IfStmt(BooleanLit(False), CallStmt(foo, BinExpr(-, Id(n), BinExpr(*, Id(b), IntegerLit(2))))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,345))
        
    def testCase46(self):
        """test function with for statement"""
        input = """a: function void(){for(i=0,i<10,i+1){}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,346))
        
    def testCase47(self):
        """test function with for statement and assignment statement"""
        input = """a: function void(){for(i=0,i<10,i+1) arr[5,3] = a*(6+35__2%7)==true;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [IntegerLit(5), IntegerLit(3)]), BinExpr(==, BinExpr(*, Id(a), BinExpr(+, IntegerLit(6), BinExpr(%, IntegerLit(352), IntegerLit(7)))), BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,347))
        
    def testCase48(self):
        """test function with for statement and call statement"""
        input = """a: function void(){for(i=0,i<10,i+1) a("hi",i);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(a, StringLit(hi), Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,348))
        
    def testCase49(self):
        """test function with for statement and if statement"""
        input = """a: function void(){for(i=0,i<10,i+1) if (true) i=i+1;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BooleanLit(True), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,349))
        
    def testCase50(self):
        """test function with for statement and return statement"""
        input = """a: function void(){for(i=0,i<10,i+1) return i;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ReturnStmt(Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,350))
        
    def testCase51(self):
        """test function with for statement and block statement"""
        input = """a: function void(){for(x=0,x<10,x+1){for(y=0,y<10,y+1){{}{}}{}}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(0)), BinExpr(<, Id(x), IntegerLit(10)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), IntegerLit(10)), BinExpr(+, Id(y), IntegerLit(1)), BlockStmt([BlockStmt([]), BlockStmt([])])), BlockStmt([])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,351))
        
    def testCase52(self):
        """test function with for statement and while statement"""
        input = """a: function void(){for(i=0,i<10,i+1){while(i>3) printInteger(i);}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(>, Id(i), IntegerLit(3)), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,352))
        
    def testCase53(self):
        """test function with if statement and do while statement"""
        input = """a: function void(){for(i=0,i<10,i+1){do {readInteger();} while(i>3);}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(3)), BlockStmt([CallStmt(readInteger, )]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,353))
        
    def testCase54(self):
        """test function with if statement and break statement"""
        input = """a: function void(){for(i=0,i<10,i+1){if (true) break;}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BooleanLit(True), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,354))
        
    def testCase55(self):
        """test function with if statement and continue"""
        input = """a: function void(){for(i=0,i<10,i+1){if (true) if (false) continue;}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(False), ContinueStmt()))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,355))
        
    def testCase56(self):
        """test function with while statement"""
        input = """a: function void(){while(i+1){}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,356))
        
    def testCase57(self):
        """test function with while statement and assignment statement"""
        input = """a: function void(){while(i<10) i=i*2;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(10)), AssignStmt(Id(i), BinExpr(*, Id(i), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,357))
        
    def testCase58(self):
        """test function with while statement and call statement"""
        input = """a: function void(){while(i!="true") i("true",true);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(i), StringLit(true)), CallStmt(i, StringLit(true), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,358))
        
    def testCase59(self):
        """test function with while statement and if statement"""
        input = """a: function void(){while(i!="true") if (i=="true") {a="valid"; printString(a);}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(i), StringLit(true)), IfStmt(BinExpr(==, Id(i), StringLit(true)), BlockStmt([AssignStmt(Id(a), StringLit(valid)), CallStmt(printString, Id(a))])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,359))
        
    def testCase60(self):
        """test function with while statement and return statement"""
        input = """a: function void(){while(i!="true") return i&&(true||false);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(i), StringLit(true)), ReturnStmt(BinExpr(&&, Id(i), BinExpr(||, BooleanLit(True), BooleanLit(False)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,360))
    
    def testCase61(self):
        """test function with while statement and for statement"""
        input = """a: function void(){while(i==-6){for(y=0,y<10,y+1) i[8]=y(8);}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(i), UnExpr(-, IntegerLit(6))), BlockStmt([ForStmt(AssignStmt(Id(y), IntegerLit(0)), BinExpr(<, Id(y), IntegerLit(10)), BinExpr(+, Id(y), IntegerLit(1)), AssignStmt(ArrayCell(i, [IntegerLit(8)]), FuncCall(y, [IntegerLit(8)])))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,361))
        
    def testCase62(self):
        """test function with while statement and block statement"""
        input = """a: function void(){while(i>3){{} printInteger(i); {}}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>, Id(i), IntegerLit(3)), BlockStmt([BlockStmt([]), CallStmt(printInteger, Id(i)), BlockStmt([])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,362))
        
    def testCase63(self):
        """test function with while statement and do while statement"""
        input = """a: function void(){while(n+m){do {} while(m-n);}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(+, Id(n), Id(m)), BlockStmt([DoWhileStmt(BinExpr(-, Id(m), Id(n)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,363))
        
    def testCase64(self):
        """test function with while statement and break statement"""
        input = """a: function void(){while(inc(6.7)>=12){break;}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, FuncCall(inc, [FloatLit(6.7)]), IntegerLit(12)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,364))
        
    def testCase65(self):
        """test function with while statement and continue"""
        input = """a: function void(){while(inc(6.7)>=12){continue;}}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, FuncCall(inc, [FloatLit(6.7)]), IntegerLit(12)), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,365))
        
    def testCase66(self):
        """test function with do while statement"""
        input = """a: function void(){do {} while(i+1);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,366))
        
    def testCase67(self):
        """test function with do while statement and assignment statement"""
        input = """a: function void(){do {i=i*2;} while(i<10);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([AssignStmt(Id(i), BinExpr(*, Id(i), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,367))
        
    def testCase68(self):
        """test function with do while statement and call statement"""
        input = """a: function void(){do {i("true",true);} while(i!="true");}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(i), StringLit(true)), BlockStmt([CallStmt(i, StringLit(true), BooleanLit(True))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,368))
        
    def testCase69(self):
        """test function with do while statement and if statement"""
        input = """a: function void(){do {if ((i||a)==false) {a="invalid"; printString(a);}} while(i!="true");}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(i), StringLit(true)), BlockStmt([IfStmt(BinExpr(==, BinExpr(||, Id(i), Id(a)), BooleanLit(False)), BlockStmt([AssignStmt(Id(a), StringLit(invalid)), CallStmt(printString, Id(a))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,369))
        
    def testCase70(self):
        """test function with do while statement and return statement"""
        input = """a: function void(){do {return i&&a;} while(i==(a||true));}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(i), BinExpr(||, Id(a), BooleanLit(True))), BlockStmt([ReturnStmt(BinExpr(&&, Id(i), Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,370))
        
    def testCase71(self):
        """test function with while statement and for statement"""
        input = """a: function void(){do {for(i=0,i<10,i+1) a[i%4,i*3]=x;} while (x::a=="aaa");}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, Id(x), BinExpr(==, Id(a), StringLit(aaa))), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(a, [BinExpr(%, Id(i), IntegerLit(4)), BinExpr(*, Id(i), IntegerLit(3))]), Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,371))
        
    def testCase72(self):
        """test function with while statement and block statement"""
        input = """a: function void(){do {{} {{} {}}} while(i>3);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(3)), BlockStmt([BlockStmt([]), BlockStmt([BlockStmt([]), BlockStmt([])])]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,372))
        
    def testCase73(self):
        """test function with do while statement and while statement"""
        input = """a: function void(){do {while(n+m){do {} while(m-n);}} while (true);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BinExpr(+, Id(n), Id(m)), BlockStmt([DoWhileStmt(BinExpr(-, Id(m), Id(n)), BlockStmt([]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,373))
        
#     def testCase74(self):
#         """test function with while statement and break statement"""
#         input = """a: function void(){do {if (x != false) break;} while(inc[324_34_2.004E873%2,!(x||true)]>=12);}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>=, ArrayCell(inc, [BinExpr(%, FloatLit(inf), IntegerLit(2)), UnExpr(!, BinExpr(||, Id(x), BooleanLit(True)))]), IntegerLit(12)), BlockStmt([IfStmt(BinExpr(!=, Id(x), BooleanLit(False)), BreakStmt())]))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,374))
        
    def testCase75(self):
        """test function with while statement and continue"""
        input = """a: function void(){do {{} continue;} while(inc(6.7)>=12);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>=, FuncCall(inc, [FloatLit(6.7)]), IntegerLit(12)), BlockStmt([BlockStmt([]), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,375))
        
    def testCase76(self):
        """test function call"""
        input = """a: function void(){ a(); }"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(a, )]))
])"""
        self.assertTrue(TestAST.test(input,expect,376))

# TODO WRITEFLOAT LA FUNCCALL        
#     def testCase77(self):
#         """test function call"""
#         input = """a: function void(){x,y: float = 0.1, writeFloat(x);}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.1)), VarDecl(y, FloatType, FuncCall(writeFloat, [Id(x)]))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,377))

# TODO WRITEFLOAT LA FUNCCALL        
#     def testCase78(self):
#         """test function call"""
#         input = """a: function void(){x: float = writeFloat(y); writeFloat(x);}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FuncCall(writeFloat, [Id(y)])), CallStmt(writeFloat, Id(x))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,378))
        
    def testCase79(self):
        """test function call"""
        input = """a: function void(){x,y: float = 0.1, 0.2; writeFloat(stringg); writeFloat(integerr);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.1)), VarDecl(y, FloatType, FloatLit(0.2)), CallStmt(writeFloat, Id(stringg)), CallStmt(writeFloat, Id(integerr))]))
])"""
        self.assertTrue(TestAST.test(input,expect,379))
        
    def testCase80(self):
        """test function call"""
        input = """a: function void(){x,y: float = 0.1, 0.2; writeFloat(x); writeFloat(y);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(0.1)), VarDecl(y, FloatType, FloatLit(0.2)), CallStmt(writeFloat, Id(x)), CallStmt(writeFloat, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input,expect,380))
        
    def testCase81(self):
        """test function call"""
        input = """a: function void(){printString(x); writeFloat(y); printBoolean(z); printInteger(t);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(printString, Id(x)), CallStmt(writeFloat, Id(y)), CallStmt(printBoolean, Id(z)), CallStmt(printInteger, Id(t))]))
])"""
        self.assertTrue(TestAST.test(input,expect,381))
        
    def testCase82(self):
        """test function call"""
        input = """a: function void(){readString(); readFloat(); readBoolean(); readInteger();}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(readString, ), CallStmt(readFloat, ), CallStmt(readBoolean, ), CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input,expect,382))

# TODO XEM LAI OUTPUT        
#     def testCase83(self):
#         """test function call"""
#         input = """a: function void(){printString(a[sdw]::b&&a); writeFloat(true); printBoolean("str"); printInteger(23.4e-23%17);}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(printString, BinExpr(::, ArrayCell(a, [Id(sdw)]), BinExpr(&&, Id(b), Id(a)))), CallStmt(writeFloat, BooleanLit(True)), CallStmt(printBoolean, StringLit(str)), CallStmt(printInteger, BinExpr(%, FloatLit(2.34e-22), IntegerLit(17)))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,383))
        
    def testCase84(self):
        """test function call"""
        input = """a: function void(){readString(); printBoolean(bool);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(readString, ), CallStmt(printBoolean, Id(bool))]))
])"""
        self.assertTrue(TestAST.test(input,expect,384))

# TODO READSTRING LA FUNCCALL        
#     def testCase85(self):
#         """test function call"""
#         input = """a: function void(){printString(readString());}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(printString, FuncCall(readString, []))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,385))
        
    def testCase86(self):
        """test expression"""
        input = """a: function void(){a: integer = (b==c)!=d;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(!=, BinExpr(==, Id(b), Id(c)), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,386))
        
    def testCase87(self):
        """test expression"""
        input = """a: function void(){a: integer = b==(c!=d);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(==, Id(b), BinExpr(!=, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,387))
        
    def testCase88(self):
        """test expression"""
        input = """a: function void(){a: integer = b---c;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, Id(b), UnExpr(-, UnExpr(-, Id(c)))))]))
])"""
        self.assertTrue(TestAST.test(input,expect,388))
        
    def testCase89(self):
        """test expression"""
        input = """a: function void(){a,b: integer = -9-4-5, 0--9-4;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(-, UnExpr(-, IntegerLit(9)), IntegerLit(4)), IntegerLit(5))), VarDecl(b, IntegerType, BinExpr(-, BinExpr(-, IntegerLit(0), UnExpr(-, IntegerLit(9))), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,389))
        
    def testCase90(self):
        """test expression"""
        input = """a: function void(){a: integer = ((a<b)>=((c<=d)>e))==f;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(==, BinExpr(>=, BinExpr(<, Id(a), Id(b)), BinExpr(>, BinExpr(<=, Id(c), Id(d)), Id(e))), Id(f)))]))
])"""
        self.assertTrue(TestAST.test(input,expect,390))
        
    def testCase91(self):
        """test all"""
        input = """a: function void(out voidd: auto) inherit functionn {voiddd: auto = functionnn(c);}"""
        expect = """Program([
	FuncDecl(a, VoidType, [OutParam(voidd, AutoType)], functionn, BlockStmt([VarDecl(voiddd, AutoType, FuncCall(functionnn, [Id(c)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,391))

# TODO a["string",x,y] DIMEN PHAI LA INT         
#     def testCase92(self):
#         """test all"""
#         input = """a: function void(x: string){} b: function void(inherit out y:string) inherit a {c: string = a["string",x,y]; if (c != "hi") if (printString(c)) return b(-345_678); else return "invalid";}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [Param(x, StringType)], None, BlockStmt([]))
# 	FuncDecl(b, VoidType, [InheritOutParam(y, StringType)], a, BlockStmt([VarDecl(c, StringType, ArrayCell(a, [StringLit(string), Id(x), Id(y)])), IfStmt(BinExpr(!=, Id(c), StringLit(hi)), IfStmt(FuncCall(printString, [Id(c)]), ReturnStmt(FuncCall(b, [UnExpr(-, IntegerLit(345678))])), ReturnStmt(StringLit(invalid))))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,392))

# TODO preventDefault la funcall        
#     def testCase93(self):
#         """test all"""
#         input = """a: function void(x: string){do {{c: auto = super(b(preventDefault()));} while !(a==(n!=b)) continue;} while((a::b)::c=="cba"+printBoolean(bool));} b: function void(inherit y:string) inherit a {}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [Param(x, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(::, BinExpr(::, Id(a), Id(b)), BinExpr(==, Id(c), BinExpr(+, StringLit(cba), FuncCall(printBoolean, [Id(bool)])))), BlockStmt([BlockStmt([VarDecl(c, AutoType, FuncCall(super, [FuncCall(b, [FuncCall(preventDefault, [])])]))]), WhileStmt(UnExpr(!, BinExpr(==, Id(a), BinExpr(!=, Id(n), Id(b)))), ContinueStmt())]))]))
# 	FuncDecl(b, VoidType, [InheritParam(y, StringType)], a, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,393))

# TODO E NHAN VAO        
#     def testCase94(self):
#         """test all"""
#         input = """a: function void(){if (a[-9.53%55_5.E+2*writeFloat(writeFloatt)]) then=a; else if (1+1<2) {{{} {}} {n=N::n+"hi"; return n;}} else if (readFloat()==readInteger()) break;}"""
#         expect = """Program([
# 	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(ArrayCell(a, [BinExpr(*, BinExpr(%, UnExpr(-, FloatLit(9.53)), FloatLit(55500.0)), FuncCall(writeFloat, [Id(writeFloatt)]))]), AssignStmt(Id(then), Id(a)), IfStmt(BinExpr(<, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(2)), BlockStmt([BlockStmt([BlockStmt([]), BlockStmt([])]), BlockStmt([AssignStmt(Id(n), BinExpr(::, Id(N), BinExpr(+, Id(n), StringLit(hi)))), ReturnStmt(Id(n))])]), IfStmt(BinExpr(==, FuncCall(readFloat, []), FuncCall(readInteger, [])), BreakStmt())))]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,394))
        
    def testCase95(self):
        """test all"""
        input = """a: function auto(autoo: auto){}"""
        expect = """Program([
	FuncDecl(a, AutoType, [Param(autoo, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,395))
        
    def testCase96(self):
        """test all"""
        input = """a: function array[1,2,3,4,5,6,7,8,9,10] of integer (b: array[1,2,3,4,5,6,7,8,9,10] of string){}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], IntegerType), [Param(b, ArrayType([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], StringType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input,expect,396))
        
    def testCase97(self):
        """test all"""
        input = """a: function auto(autoo: string){continue; {for(x=2435_23,x!=m,x==s) {__sadf=2; c: array[2,35,643,234____3,999] of string="hi"+x::"hi";}}}"""
        expect = """Program([
	FuncDecl(a, AutoType, [Param(autoo, StringType)], None, BlockStmt([ContinueStmt(), BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(243523)), BinExpr(!=, Id(x), Id(m)), BinExpr(==, Id(x), Id(s)), BlockStmt([AssignStmt(Id(__sadf), IntegerLit(2)), VarDecl(c, ArrayType([2, 35, 643, 2343, 999], StringType), BinExpr(::, BinExpr(+, StringLit(hi), Id(x)), StringLit(hi)))]))])]))
])"""
        self.assertTrue(TestAST.test(input,expect,397))

# TODO WHILE CUOI THIEU BRACKET       
#     def testCase98(self):
#         """test all"""
#         input = """a: function auto(autoo: string){{} {for(x=2435_23,x!=(mx==s),a>0) {do {c: array[2,35,643,234____3,999] of string="hi"::"hi";} while b(autoo, voidd, forr, superr);}}}"""
#         expect = """Program([
# 	FuncDecl(a, AutoType, [Param(autoo, StringType)], None, BlockStmt([BlockStmt([]), BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(243523)), BinExpr(!=, Id(x), BinExpr(==, Id(mx), Id(s))), BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([DoWhileStmt(FuncCall(b, [Id(autoo), Id(voidd), Id(forr), Id(superr)]), BlockStmt([VarDecl(c, ArrayType([2, 35, 643, 2343, 999], StringType), BinExpr(::, BinExpr(+, StringLit(hi), Id(x)), StringLit(hi)))]))]))])]))
# ])"""
#         self.assertTrue(TestAST.test(input,expect,398))
        
    def testCase99(self):
        """test all"""
        input = """a: function void(){superr,superrr: auto = supersuper(super(superr+superrr),sup,supper,supe),sup+super(supper(sup[super(supe),super()]));}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(superr, AutoType, FuncCall(supersuper, [FuncCall(super, [BinExpr(+, Id(superr), Id(superrr))]), Id(sup), Id(supper), Id(supe)])), VarDecl(superrr, AutoType, BinExpr(+, Id(sup), FuncCall(super, [FuncCall(supper, [ArrayCell(sup, [FuncCall(super, [Id(supe)]), FuncCall(super, [])])])])))]))
])"""
        self.assertTrue(TestAST.test(input,expect,399))
        
    def testCase100(self):
        """test all"""
        input = """a: function void(){return "Good luck on this testcases!";}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ReturnStmt(StringLit(Good luck on this testcases!))]))
])"""
        self.assertTrue(TestAST.test(input,expect,400))