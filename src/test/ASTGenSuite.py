import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
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

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_full_vardecl(self):
        input = """x, y, z: integer = true, false, true;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))
        
#     def test_simple_program(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))

