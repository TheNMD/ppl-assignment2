import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """x,y,z,a,b,c: array [1,2,3] of integer; a,b,c: array [4,6,7] of float;"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 2, 3], IntegerType))
	VarDecl(y, ArrayType([1, 2, 3], IntegerType))
	VarDecl(z, ArrayType([1, 2, 3], IntegerType))
	VarDecl(a, ArrayType([1, 2, 3], IntegerType))
	VarDecl(b, ArrayType([1, 2, 3], IntegerType))
	VarDecl(c, ArrayType([1, 2, 3], IntegerType))
	VarDecl(a, ArrayType([4, 6, 7], FloatType))
	VarDecl(b, ArrayType([4, 6, 7], FloatType))
	VarDecl(c, ArrayType([4, 6, 7], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """a, b, c: array[3,4] of integer = {1,2,3}, {}, {};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([3, 4], IntegerType), ArrayLit([]))
	VarDecl(c, ArrayType([3, 4], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """x, y, z: float = 1.2, 3e12, 1_33.33e-23;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.2))
	VarDecl(y, FloatType, FloatLit(3e12))
	VarDecl(z, FloatType, FloatLit(133.33e-23))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """x, y, z: boolean = true, false, true;"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test5(self):
        input = """x, y : integer = func(1,2,3), func1() ;"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, IntegerType, FuncCall(func1, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """x, y : integer = arr[0, 1, 2], arr1[4, 5, 6] ;"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(arr, [0, 1, 2]))
	VarDecl(y, IntegerType, ArrayCell(arr1, [4, 5, 6]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test7(self):
        input = """x, y : integer = a, b ;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(a))
	VarDecl(y, IntegerType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
 
    def test8(self):
        input = """x : string = "abc" ;"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
 
    def test9(self):
        input = """x : string = ("abc"::"cde")::"xyz" ;"""
        expect = """Program([
	VarDecl(x, StringType, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(xyz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 309)) 
  
    def test10(self):
        input = """x : boolean = (a == 9) > (5 == 8) ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(>, BinExpr(==, Id(a), IntegerLit(9)), BinExpr(==, IntegerLit(5), IntegerLit(8))))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
         
    def test11(self):
        input = """x : boolean = a || b || c || d && e ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(||, Id(a), Id(b)), Id(c)), Id(d)), Id(e)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311)) 
  
    def test12(self):
        input = """x : float = 1 * a - 2.33e-32 / 33 + b % 33;"""
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), Id(a)), BinExpr(/, FloatLit(2.33e-32), IntegerLit(33))), BinExpr(%, Id(b), IntegerLit(33))))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))   
 
    def test13(self):
        input = """a,b,c: array[3,4,5] of integer = {},{{},{}}, {{{},{}},{}};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4, 5], IntegerType), ArrayLit([]))
	VarDecl(b, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(c, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([ArrayLit([]), ArrayLit([])]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))    
  
    def test14(self):
        input = """a,b,c: array[3,4,5] of integer = {1,2,3},{{1,2},{3,4}}, {{{1,22},{33,4}},{77,88}};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))
	VarDecl(c, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(22)]), ArrayLit([IntegerLit(33), IntegerLit(4)])]), ArrayLit([IntegerLit(77), IntegerLit(88)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314)) 
  
    def test15(self):
        """Simple program"""
        input = """main: function void () {
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test16(self):
        """Simple program"""
        input = """main: function void (inherit a : integer, out b : float, inherit out c : boolean) {
                int1: integer = a + b / c;
                int2: integer = 1 + 3 - 8 ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritParam(a, IntegerType), OutParam(b, FloatType), InheritOutParam(c, BooleanType)], None, BlockStmt([VarDecl(int1, IntegerType, BinExpr(+, Id(a), BinExpr(/, Id(b), Id(c)))), VarDecl(int2, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(3)), IntegerLit(8)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        """Simple program"""
        input = """main: function void () {
                if (a == 9) b = 7 ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test18(self):
        """Simple program"""
        input = """main: function void () {
                if (a == 9) b = 7 ;
                else if (c == 9) b = 5 ;
                else b = 20 ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(5)), AssignStmt(Id(b), IntegerLit(20))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        """Simple program"""
        input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
        main: function void () {
        {

        }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        """Simple program"""
        input = """main: function void () {
                if (a == 9)
                {
                        for (i = 5, i < 10, i + 1) a = a + i;
                }
                else if (c == 9)
                {
                        i : integer = 23 ;
                        while (i < 5) i = i + 1 ;
                }
                else b = 20 ;
                return ;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), Id(i))))]), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), BlockStmt([VarDecl(i, IntegerType, IntegerLit(23)), WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]), AssignStmt(Id(b), IntegerLit(20)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

