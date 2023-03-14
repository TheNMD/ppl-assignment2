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
            idvaluelist = [ctx.ID().getText()] + self.visit(ctx.middle()) + [self.visit(ctx.expr())]
            size = len(idvaluelist)
            if size % 2 == 0:
                vartyp = idvaluelist[int(size / 2 - 1)]
                dimenlist = idvaluelist[int(size / 2)]
                res = []
                for i in range(0, int(size / 2 - 1)):
                    id = idvaluelist[i]
                    value = idvaluelist[int(size / 2 + 1 + i)]
                    res += [VarDecl(id, ArrayType(dimenlist, vartyp), value)]
                return res
            else:
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
            return [ctx.ID().getText()] + self.visit(ctx.middle()) + [self.visit(ctx.expr())]
        else:
            if ctx.dimenlist():
                return [self.visit(ctx.vartyp())] + [self.visit(ctx.dimenlist())]
            return [self.visit(ctx.vartyp())]
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.exprs():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprs())
        return [self.visit(ctx.expr())]
    def visitExprs(self, ctx: MT22Parser.ExprsContext):
        if ctx.exprs():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprs())
        return []
    def visitExpr(self, ctx: MT22Parser.ExprContext): #TODO
        if ctx.CONCATOP():
            return BinExpr(ctx.CONCATOP(), self.visit(ctx.expr1()[0]), self.visit(ctx.expr1()[1]))
        return self.visit(ctx.expr1()[0])
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.EQLOP():
            return BinExpr(ctx.EQLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.DIFOP():
            return BinExpr(ctx.DIFOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.LARGEOP():
            return BinExpr(ctx.LARGEOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.LEQLOP():
            return BinExpr(ctx.LEQLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.SMALLOP():
            return BinExpr(ctx.SMALLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1])) 
        elif ctx.SEQLOP():
            return BinExpr(ctx.SEQLOP(), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1]))
        return self.visit(ctx.expr2()[0])
    def visitExpr2(self, ctx: MT22Parser.Expr2Context): #TODO
        if ctx.ANDOP():
            return BinExpr(ctx.ANDOP(), self.visit(ctx.expr2()), self.visit(ctx.expr3())) 
        elif ctx.OROP():
            return BinExpr(ctx.OROP(), self.visit(ctx.expr2()), self.visit(ctx.expr3())) 
        return self.visit(ctx.expr3())
    def visitExpr3(self, ctx: MT22Parser.Expr3Context): #TODO
        if ctx.ADDOP():
            return BinExpr(ctx.ADDOP(), self.visit(ctx.expr3()), self.visit(ctx.expr4())) 
        elif ctx.SUBOP():
            return BinExpr(ctx.SUBOP(), self.visit(ctx.expr3()), self.visit(ctx.expr4())) 
        return self.visit(ctx.expr4())
    def visitExpr4(self, ctx: MT22Parser.Expr4Context): #TODO
        if ctx.MULOP():
            return BinExpr(ctx.MULOP(), self.visit(ctx.expr4()), self.visit(ctx.expr5())) 
        elif ctx.DIVOP():
            return BinExpr(ctx.DIVOP(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.MODOP():
            return BinExpr(ctx.MODOP(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))  
        return self.visit(ctx.expr5())
    def visitExpr5(self, ctx: MT22Parser.Expr5Context): #TODO
        if ctx.EXCOP():
            return UnExpr(ctx.EXCOP(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())
    def visitExpr6(self, ctx: MT22Parser.Expr6Context): #TODO
        if ctx.SUBOP():
            return UnExpr(ctx.SUBOP(), self.visit(ctx.expr6()))
        return self.visit(ctx.operand())
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.LITINT():
            return IntegerLit(ctx.LITINT().getText())
        elif ctx.LITFLOAT():
            return FloatLit(ctx.LITFLOAT().getText())
        elif ctx.litboo():
            return self.visit(ctx.litboo())
        elif ctx.LITSTR():
            return StringLit(ctx.LITSTR().getText())
        elif ctx.ID():
            if ctx.idxop():
                return ArrayCell(ctx.ID().getText(), self.visit(ctx.idxop()))
            return Id(ctx.ID().getText())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
        elif ctx.litarr():
            return self.visit(ctx.litarr())
    def visitLitboo(self, ctx: MT22Parser.LitbooContext):
        if ctx.KWTRUE():
            return BooleanLit(True)
        return BooleanLit(False)
    def visitIdxop(self, ctx: MT22Parser.IdxopContext):
        return self.visit(ctx.dimenlist())
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        if ctx.exprlist():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.exprlist()))
        return FuncCall(ctx.ID().getText(), [])
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        return self.visit(ctx.expr())
    def visitLitarr(self, ctx: MT22Parser.LitarrContext):
        if ctx.exprlist():
            return ArrayLit(self.visit(ctx.exprlist()))
        return ArrayLit([])