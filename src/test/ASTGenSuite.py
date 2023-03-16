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
	VarDecl(x, IntegerType, ArrayCell(arr, [IntegerLit(0), IntegerLit(1), IntegerLit(2)]))
	VarDecl(y, IntegerType, ArrayCell(arr1, [IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
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
        input = """main: function void (a : array [1,2] of integer, b : string) {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, ArrayType([1, 2], IntegerType)), Param(b, StringType)], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test22(self):
        """More complex program"""
        input = """main: function array [2,3] of string () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, ArrayType([2, 3], StringType), [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test23(self):
        """More complex program"""
        input = """func1 : function auto (out a : array [3,8] of integer, inherit b : float) {
            randfloat : float = 1_332.33e-23 ;
            randarr : array [7] of string ;
            return 2233;
            }
        func2 : function void (c : string, out d : array [2,3] of boolean) inherit func1 {
            if(a == 5) c = a % 7 ;
            else d = a / 8 ;
            randarr = arr1[1+1,3_3/3,5%4] + 332 - arr2[9/3]  ;
            return;
            }"""
        expect = """Program([
	FuncDecl(func1, AutoType, [OutParam(a, ArrayType([3, 8], IntegerType)), InheritParam(b, FloatType)], None, BlockStmt([VarDecl(randfloat, FloatType, FloatLit(1332.33e-23)), VarDecl(randarr, ArrayType([7], StringType)), ReturnStmt(IntegerLit(2233))]))
	FuncDecl(func2, VoidType, [Param(c, StringType), OutParam(d, ArrayType([2, 3], BooleanType))], func1, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), AssignStmt(Id(d), BinExpr(/, Id(a), IntegerLit(8)))), AssignStmt(Id(randarr), BinExpr(-, BinExpr(+, ArrayCell(arr1, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(/, IntegerLit(33), IntegerLit(3)), BinExpr(%, IntegerLit(5), IntegerLit(4))]), IntegerLit(332)), ArrayCell(arr2, [BinExpr(/, IntegerLit(9), IntegerLit(3))]))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test24(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            if(a == 5) c = a % 7 ;
            else if (a == 4) for (i = 8, i < 20, i / 2) { c = c + 1 ; }
            return 1.223e20 ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))), ReturnStmt(FloatLit(1.223e20))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test25(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            if(a == 7) c = a % 7 ;
            else while (i < 20) { c = c + 1 ; }
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(7)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), WhileStmt(BinExpr(<, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
                arr1, arr2, arr3 : array [2,2,2_3] of boolean = {}, {{},{}}, {{{{{}}}}} ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(arr1, ArrayType([2, 2, 23], BooleanType), ArrayLit([])), VarDecl(arr2, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])])), VarDecl(arr3, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test27(self):
        """More complex program"""
        input = """res : float = sin(a,b) / cos(c,d) ;"""
        expect = """Program([
	VarDecl(res, FloatType, BinExpr(/, FuncCall(sin, [Id(a), Id(b)]), FuncCall(cos, [Id(c), Id(d)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test28(self):
        """More complex program"""
        input = """main1 : function string () {
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test29(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = "abc\\t" != "abc\t" ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(!=, StringLit(abc\\t), StringLit(abc	))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test30(self):
        """More complex program"""
        input = """main1 : function string () {
            while(a < 23)
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test31(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = 7 - 9 < 4 - 6 ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(-, IntegerLit(7), IntegerLit(9)), BinExpr(-, IntegerLit(4), IntegerLit(6)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test32(self):
        """More complex program"""
        input = """main1 : function string () {
            str = 7 - 9 * 4 - 6 ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(-, BinExpr(-, IntegerLit(7), BinExpr(*, IntegerLit(9), IntegerLit(4))), IntegerLit(6))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        """More complex program"""
        input = """main1 : function string () {
            str = (8 < 9) || (4 > 6) ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(||, BinExpr(<, IntegerLit(8), IntegerLit(9)), BinExpr(>, IntegerLit(4), IntegerLit(6)))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test34(self):
        """More complex program"""
        input = """main1 : function string () {
            bool = ((1 < 2) < 3) < 4 ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(<, BinExpr(<, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test35(self):
        """More complex program"""
        input = """main1 : function string () {
            str = (("abc" :: "cde") :: "123") :: "456" ;
            return ;
            }"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(::, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(123)), StringLit(456))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test36(self):
        """More complex program"""
        input = """ a : string = "213123213\\'" ;  """
        expect = """Program([
	VarDecl(a, StringType, StringLit(213123213\\'))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test37(self):
        """More complex program"""
        input = """_A330xr : integer ;"""
        expect = """Program([
	VarDecl(_A330xr, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test38(self):
        """More complex program"""
        input = """str : string = "\ttoo(;_;)many(;_;)test(;_;)cases(;_;)\t" ;"""
        expect = """Program([
	VarDecl(str, StringType, StringLit(	too(;_;)many(;_;)test(;_;)cases(;_;)	))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test39(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string (inherit a : array [2,3] of string, out b : array [3,3] of boolean) {
            while(a < 23)
            do {a = a / 9 ;}
            while (a > 100) ;
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [InheritParam(a, ArrayType([2, 3], StringType)), OutParam(b, ArrayType([3, 3], BooleanType))], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test40(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string () {
                if(a < 4)
                {
                        while(a < 23)
                        {
                                for (i = 8, i < 20, i / 2) {c = c + 1 ; }
                        }
                }
                return; 
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(4)), BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))]))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test41(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string () {
                return 0;
                return;
                return 1; 
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([ReturnStmt(IntegerLit(0)), ReturnStmt(), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test42(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) {
                printInteger(a);
                readInteger();
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(printInteger, Id(a)), CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) {
                writeFloat(a);
                readFloat();
                printBoolean(a);
                readBoolean();
                printString(a);
                readString();
                preventDefault();
                super(b);
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(writeFloat, Id(a)), CallStmt(readFloat, ), CallStmt(printBoolean, Id(a)), CallStmt(readBoolean, ), CallStmt(printString, Id(a)), CallStmt(readString, ), CallStmt(preventDefault, ), CallStmt(super, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test44(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) { 
            do { for (i = 7, i < 13, i + 1) printInteger(i) ; }
            while (True) ;
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([DoWhileStmt(Id(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(7)), BinExpr(<, Id(i), IntegerLit(13)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test45(self):
        """More complex program"""
        input = """func1 : function float (c : string, out d : boolean) {
            a,b,c : integer = 1,2,3 ;
            }"""
        expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test46(self):
        """More complex program"""
        input = """a,b,c : array [2_7,3] of float = 1,2,3 ;"""
        expect = """Program([
	VarDecl(a, ArrayType([27, 3], FloatType), IntegerLit(1))
	VarDecl(b, ArrayType([27, 3], FloatType), IntegerLit(2))
	VarDecl(c, ArrayType([27, 3], FloatType), IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test47(self):
        """More complex program"""
        input = """randfloat,b : float = 1_332.33e-23,.332e3 ;"""
        expect = """Program([
	VarDecl(randfloat, FloatType, FloatLit(1332.33e-23))
	VarDecl(b, FloatType, FloatLit(.332e3))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test48(self):
        """More complex program"""
        input = """abc : string = "ddxxdw"::"eerxxz" ; """
        expect = """Program([
	VarDecl(abc, StringType, BinExpr(::, StringLit(ddxxdw), StringLit(eerxxz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test49(self):
        """More complex program"""
        input = """abc : float = a[22,3] / b[8-8,9/3] % c[8%2, 1*7] ; """
        expect = """Program([
	VarDecl(abc, FloatType, BinExpr(%, BinExpr(/, ArrayCell(a, [IntegerLit(22), IntegerLit(3)]), ArrayCell(b, [BinExpr(-, IntegerLit(8), IntegerLit(8)), BinExpr(/, IntegerLit(9), IntegerLit(3))])), ArrayCell(c, [BinExpr(%, IntegerLit(8), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(7))])))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test50(self):
        """More complex program"""
        input = """abc, cde : float = a[22,3] / b[8-8,9/3] % c[8%2, 1*7], abc ; """
        expect = """Program([
	VarDecl(abc, FloatType, BinExpr(%, BinExpr(/, ArrayCell(a, [IntegerLit(22), IntegerLit(3)]), ArrayCell(b, [BinExpr(-, IntegerLit(8), IntegerLit(8)), BinExpr(/, IntegerLit(9), IntegerLit(3))])), ArrayCell(c, [BinExpr(%, IntegerLit(8), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(7))])))
	VarDecl(cde, FloatType, Id(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test51(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test52(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test54(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test55(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test56(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test57(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test58(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test59(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test60(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test61(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test62(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test64(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test65(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test66(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test67(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test68(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test69(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test70(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test71(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test72(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test74(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test75(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test76(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test77(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test78(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test79(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test80(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test81(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test82(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test84(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test85(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test86(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test87(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test88(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test89(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test90(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test91(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test92(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test94(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test95(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test96(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test97(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test98(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test99(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
        
    def test100(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))