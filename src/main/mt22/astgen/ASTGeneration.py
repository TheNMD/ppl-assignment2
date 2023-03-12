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
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl(): 
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.middle(): 
            pass
        idlist = self.visit(ctx.idlist())
        # idxlist = self.visit(ctx.idxlist())
        vartyp = self.visit(ctx.vartyp())
        return VarDecl(idlist, vartyp)
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 2:
            #return ctx.ID().getText() + self.visit(ctx.ids())
            pass
        return ctx.ID().getText()
    def visitIds(self, ctx: MT22Parser.IdsContext):
        if ctx.ID():
            return ctx.ID().getText()
        return []
    def visitVartyp(self, ctx: MT22Parser.VartypContext):
        if ctx.KWINT():
            return IntegerType()
        elif ctx.KWFLOAT():
            return FloatType()
        elif ctx.KWBOO():
            return BooleanType()
        return StringType()