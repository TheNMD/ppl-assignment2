from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([decl for decl in self.visit(ctx.declist())])
    def visitDeclist(self, ctx: MT22Parser.DeclistContext):
        if ctx.declist(): 
            return self.visit(ctx.decl()) + self.visit(ctx.declist())
        return self.visit(ctx.decl())
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl(): 
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.middle():
            idlist = [ctx.ID().getText()]
            valuelist = self.visit(ctx.expr())
            idvaluelist = self.visit(ctx.middle())
            size = len(idvaluelist)
            for i in range(0, int((size - 1) / 2)):
                idlist += idvaluelist[i]
                valuelist += idvaluelist[int((size - 1) / 2 + 1 + i)]
            vartyp = idvaluelist[int((size - 1) / 2)]
            return [VarDecl(id, vartyp, value) for id, value in idlist, valuelist]
        else:
            idlist = self.visit(ctx.idlist())
            vartyp = self.visit(ctx.vartyp())
            if ctx.dimenlist():
                dimenlist = self.visit(ctx.dimenlist())
                return [VarDecl(id, ArrayType(dimenlist, vartyp)) for id in idlist]
            return [VarDecl(id, vartyp) for id in idlist]
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.ids():
            return [ctx.ID().getText()] + self.visit(ctx.ids())
        return [ctx.ID().getText()]
    def visitIds(self, ctx: MT22Parser.IdsContext):
        if ctx.ids():
            return [ctx.ID().getText()] + self.visit(ctx.ids())
        return []
    def visitVartyp(self, ctx: MT22Parser.VartypContext):
        if ctx.KWINT():
            return IntegerType()
        elif ctx.KWFLOAT():
            return FloatType()
        elif ctx.KWBOO():
            return BooleanType()
        return StringType()
    def visitDimenlist(self, ctx: MT22Parser.DimenlistContext):
        if ctx.dimens():
            return [ctx.LITINT().getText()] + self.visit(ctx.dimens())
        return [ctx.LITINT().getText()]
    def visitDimens(self, ctx: MT22Parser.DimensContext):
        if ctx.dimens():
            return [ctx.LITINT().getText()] + self.visit(ctx.dimens())
        return []
    def visitMiddle(self, ctx: MT22Parser.MiddleContext):
        if ctx.middle():
            return [ctx.ID().getText()] + self.visit(ctx.middle()) + self.visit(ctx.expr())
        return [self.visit(ctx.vartyp())]
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        return ["0"]
      