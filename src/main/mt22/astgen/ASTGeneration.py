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
            idvaluelist = [ctx.ID().getText()] + self.visit(ctx.middle()) + self.visit(ctx.expr())
            size = len(idvaluelist)
            vartyp = idvaluelist[int((size - 1) / 2)]
            res = []
            for i in range(0, int((size - 1) / 2)):
                id = idvaluelist[i]
                value = idvaluelist[int((size - 1) / 2 + 1 + i)]
                res += [VarDecl(id, vartyp, value)]
            return res
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
    def visitExpr(self, ctx: MT22Parser.ExprContext): #TODO
        if ctx.CONCATOP():
            pass
        return self.visit(ctx.expr1()[0])
    def visitExpr1(self, ctx: MT22Parser.Expr1Context): #TODO
        if (ctx.EQLOP() or ctx.DIFOP() or ctx.LARGEOP() or ctx.LEQLOP() or ctx.SMALLOP() or ctx.SEQLOP()):
            pass
        return self.visit(ctx.expr2()[0])
    def visitExpr2(self, ctx: MT22Parser.Expr2Context): #TODO
        if (ctx.ANDOP() or ctx.OROP()):
            pass
        return self.visit(ctx.expr3())
    def visitExpr3(self, ctx: MT22Parser.Expr3Context): #TODO
        if (ctx.ADDOP() or ctx.SUBOP()):
            pass
        return self.visit(ctx.expr4())
    def visitExpr4(self, ctx: MT22Parser.Expr4Context): #TODO
        if (ctx.MULOP() or ctx.DIVOP() or ctx.MODOP()):
            pass
        return self.visit(ctx.expr5())
    def visitExpr5(self, ctx: MT22Parser.Expr5Context): #TODO
        if (ctx.EXCOP()):
            pass
        return self.visit(ctx.expr6())
    def visitExpr6(self, ctx: MT22Parser.Expr6Context): #TODO
        if (ctx.SUBOP()):
            pass
        return self.visit(ctx.operand())
    def visitOperand(self, ctx: MT22Parser.OperandContext): #TODO
        if ctx.LITINT():
            return [IntegerLit(ctx.LITINT().getText())]
        elif ctx.LITFLOAT():
            return [FloatLit(ctx.LITINT().getText())]
        elif ctx.litboo():
            return [self.visit(ctx.litboo())]
        elif ctx.StringLit():
            return [StringLit(ctx.LITINT().getText())]
        elif ctx.ID():
            if ctx.idxop():
                pass #TODO
            return [Id(ctx.ID().getText())]
        elif ctx.funcall():
            pass #TODO
        elif ctx.subexpr():
            return self.visit(ctx.subexpr()) # TODO
        return self.visit(ctx.litarr()) # TODO
    def visitLitboo(self, ctx: MT22Parser.LitbooContext): #TODO
        if ctx.KWTRUE():
            return BooleanLit(True)
        return BooleanLit(False)