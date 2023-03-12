from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([self.visit(ctx.declist())])
    def visitDeclist(self, ctx: MT22Parser.DeclistContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.decl())
        return self.visit(ctx.declist())
    def visitDeclist(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.decl())
