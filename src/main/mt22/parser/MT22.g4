grammar MT22;

@lexer::header {
from lexererr import *;
studentID = "2052932";
studentName = "Nguyen Manh Dan";
}

options{
	language=Python3;
}

//==========================================================
// Lexer Rules
//==========================================================
// Whitespace
WS : [ \t\n\r\f\b]+ -> skip ;

// COMMENT
CCOMMENT :  '/*' .*? '*/' -> skip;

CPPCOMMENT : '//' ~ [\r\n]* -> skip;

// KEYWORD
KWVOID : 'void' ;

KWAUTO : 'auto' ;

KWINT :  'integer' ;

KWFLOAT : 'float' ;

KWBOO : 'boolean' ;

KWSTR : 'string' ;

KWARR : 'array' ;

KWINHERIT : 'inherit' ;

KWFUNC : 'function' ;

KWTRUE : 'true' ;

KWFALSE : 'false' ;

KWFOR : 'for' ;

KWWHILE : 'while' ;

KWDO : 'do' ;

KWBRK : 'break' ;

KWCONT : 'continue' ;

KWRTN : 'return' ;

KWIF : 'if' ;

KWELSE : 'else' ;

KWOF : 'of' ;

KWOUT : 'out' ;

// Identifiers
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// Operators
ADDOP : '+' ;

SUBOP : '-' ;

MULOP : '*' ;

DIVOP : '/' ;

MODOP : '%' ;

EXCOP : '!' ;

ANDOP : '&&' ;

OROP : '||' ;

EQLOP : '==' ;

DIFOP : '!=' ;

LARGEOP : '>' ;

LEQLOP : '>=' ;

SMALLOP : '<' ;

SEQLOP : '<=' ;

CONCATOP : '::' ;

// Separators
DOT : '.' ;

CM : ',' ;

SM : ';' ;

CL : ':' ;

LB : '(' ;

RB : ')' ;

LSB : '[' ;

RSB : ']' ;

LCB : '{' ;

RCB : '}' ;

EQL : '=' ;

// Literals
LITINT : [0-9] | [1-9][0-9_]*[0-9] {self.text = self.text.replace('_','')} ;

LITFLOAT : LITINT Decimal? Exponent?  {self.text = self.text.replace('_','')} ;

fragment Decimal : DOT [0-9]* ;

fragment Exponent : [eE] [+-]? [0-9]+ ;

litboo : KWTRUE | KWFALSE ;

LITSTR : '"' Char* '"' {self.text = self.text[1:-1]}  ;

fragment Char : ('\\' [bfrnt'\\"] | ~[\n'\\"]) ; 

//==========================================================
// Parser Rules
//==========================================================

program : declist EOF ;

declist : decl declist | decl ;

decl : vardecl | funcdecl ;

vardecl : idlist CL vartyp SM
		| ID middle expr SM 
		| idlist CL KWARR LSB idxlist RSB KWOF vartyp SM
		| ID middlearr litarr SM ;

idlist : ID ids | ID ;

ids : CM ID ids | ;

middle : CM ID middle expr CM | CL (vartyp | KWAUTO) EQL ;

middlearr : CM ID middlearr litarr CM | CL KWARR LSB idxlist RSB KWOF vartyp EQL ;

litarr : LCB exprlist? RCB ;

vartyp : KWINT | KWFLOAT | KWBOO | KWSTR ;

idxlist : (LITINT | ID) idxs | (LITINT | ID) ;

idxs : CM (LITINT | ID) idxs | ;

funcdecl : ID CL KWFUNC (functyp | KWAUTO) LB paralist RB (KWINHERIT ID)? LCB bodylist RCB
		 | ID CL KWFUNC KWVOID LB paralist RB (KWINHERIT ID)? LCB bodylist RCB ;

paralist : para paras | ;

paras : CM para paras | ;

para :  KWINHERIT? KWOUT? ID CL vartyp ;

functyp :  KWINT | KWFLOAT | KWBOO | KWSTR ;

bodylist : body bodylist | ;

body : vardecl | stmt | ifstmt ;

stmt : assignstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | rtnstmt | callstmt | blockstmt ;

assignstmt : (ID | ID idxop)  EQL expr SM ;

ifstmt : matchstmt | unmatchstmt ;

matchstmt : KWIF LB expr RB matchstmt KWELSE matchstmt | (vardecl | stmt) ;

unmatchstmt : KWIF LB expr RB ifstmt | KWIF LB expr RB matchstmt KWELSE unmatchstmt ;

forstmt : KWFOR LB ID EQL expr CM expr CM expr RB (vardecl | stmt | ifstmt) ;

whilestmt : KWWHILE LB expr RB (vardecl | stmt | ifstmt) ;

dowhilestmt : KWDO blockstmt KWWHILE LB expr RB SM ;

breakstmt : KWBRK SM ;

continuestmt : KWCONT SM ;

rtnstmt : KWRTN (expr)? SM ;

callstmt : (funccall | specialfunc) SM ;

blockstmt : LCB bodylist RCB ;

exprlist : expr exprs | expr ;

exprs : CM expr exprs | ;

expr : expr1 CONCATOP expr1 | expr1 ;

expr1 : expr2 (EQLOP | DIFOP | LARGEOP | LEQLOP | SMALLOP | SEQLOP)  expr2 | expr2 ;

expr2 : expr2 (ANDOP | OROP) expr3 | expr3 ;

expr3 : expr3 (ADDOP | SUBOP) expr4 | expr4 ;

expr4 : expr4 (MULOP | DIVOP | MODOP) expr5 | expr5 ;

expr5 :  EXCOP expr5 | expr6 ;

expr6 : SUBOP expr6 | operand ;

//expr7 : expr7 idxop | operand ;

operand: LITINT | LITFLOAT | litboo | LITSTR | ID idxop? | funccall | subexpr | litarr ;

idxop : LSB idxlist RSB ;

funccall : ID LB exprlist? RB ;

subexpr : LB expr RB ;

specialfunc : ('readInteger' | 'printInteger' | 'readFloat' | 'writeFloat' | 'readBoolean' | 'printBoolean' | 'readString' | 'printString' | 'super' | 'preventDefault') LB exprlist? RB ;

// ERROR TOKENS
ILLEGAL_ESCAPE: '"' Char* ('\\' ~[bfrnt'\\"]) {self.text = self.text[1:]; raise IllegalEscape(self.text)};

UNCLOSED_STRING:  '"' Char* (EOF)? {self.text = self.text[1:]; raise UncloseString(self.text)};

ERROR_CHAR: . {raise ErrorToken(self.text)};
