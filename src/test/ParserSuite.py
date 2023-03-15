import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):


    def test201(self):
        input="""mt222: integer;"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 201))


    def test202(self):
        input="""q1,q2,_q3: auto;"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 202))


    def test203(self):
        input="""math,operatos,something : void;"""
        expect="""Error on line 1 col 26: void"""
        self.assertTrue(TestParser.test(input, expect, 203))


    def test204(self):
        input="""abc,def : ;"""
        expect="""Error on line 1 col 10: ;"""
        self.assertTrue(TestParser.test(input, expect, 204))


    def test205(self):
        input="""x,y,z,t: float;
a,b,c: string;
g,h,i,j,k: auto;
m,q : integer;"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 205))


    def test206(self):
        input="""a,b,c: string;
g,h,i,j,: auto;"""
        expect="""Error on line 2 col 8: :"""
        self.assertTrue(TestParser.test(input, expect, 206))


    def test207(self):
        input="""variab: string = "abcxyz";"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 207))


    def test208(self):
        input="""int1,int2,int3,int4: integer = 100_2,20,40,60;"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 208))


    def test209(self):
        input="""string1,,int2,int3,int4: integer = "abc",129,291,10;"""
        expect="""Error on line 1 col 8: ,"""
        self.assertTrue(TestParser.test(input, expect, 209))


    def test210(self):
        input="""float_a : float = 2.e+10;
integer_b: integer = 1219381_1928218;
boolean_c: boolean = true;
auto_d: auto ="ABCZ";"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 210))


    def test211(self):
        input="""my_array: array[3] of integer = {1,2,3};
my_array_2: array[3] of float = {2e2,0.0,5.2E+10,.E-12};
my_array_: array[3] of string = {"1,2,3", mnpq, "xyz"};"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 211))


    def test212(self):
        input="""a,b,c: float = 1,2;"""
        expect="""Error on line 1 col 18: ;"""
        self.assertTrue(TestParser.test(input, expect, 212))


    def test213(self):
        input="""abc: integer = - (! - foo());"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 213))


    def test214(self):
        input="""a,b,c: string = 1,2,3,4,;"""
        expect="""Error on line 1 col 21: ,"""
        self.assertTrue(TestParser.test(input, expect, 214))


    def test215(self):
        input="""a,b,c,d: void = 1,2,4,5,6;"""
        expect="""Error on line 1 col 9: void"""
        self.assertTrue(TestParser.test(input, expect, 215))


    def test216(self):
        input="""error1,error2 = 4,5;"""
        expect="""Error on line 1 col 14: ="""
        self.assertTrue(TestParser.test(input, expect, 216))


    def test217(self):
        input="""main: function void () {}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 217))


    def test218(self):
        input="""main,vice: function void (a: integer) {}"""
        expect="""Error on line 1 col 11: function"""
        self.assertTrue(TestParser.test(input, expect, 218))

# TODO para la idlist va type la array
#     def test219(self):
#         input="""main: function void (a,b,c:integer,d,e: array[3] of integer) {
# 	break;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 219))

# TODO type la array
#     def test220(self):
#         input="""main: function integer (out a:auto,inherit d,e: array[3] of integer, inherit out v: string) {
# 	break;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 220))

# TODO para la idlist va type la array
#     def test221(self):
#         input="""main: function void (a,b,c:integer,d,e: array[3] of integer) inherit vice {
# 	break;
# 	foo(a,b,c);
# 	continues;
# }"""
#         expect="""Error on line 4 col 10: ;"""
#         self.assertTrue(TestParser.test(input, expect, 221))

# TODO para la idlist va type la array
#     def test222(self):
#         input="""main: function array[5,2] of string (a,b,c:integer,d,e: array[3] of integer) {
# 	return goo(4,5,foo(2,3));
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 222))

# TODO function la array, para la idlist va type la array
#     def test223(self):
#         input="""main: function array[5,2] of string (a,b,c:integer, inherit d,e: array[3] of integer) {
# 	x,y : float = 9e10, 2e5;
# 	if (x!=2) break;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 223))

# TODO function la array, para la idlist va type la array
#     def test224(self):
#         input="""main: function array[5,2] of string (a,b) {
# 	return goo(4,5,foo(2,3));
# }"""
#         expect="""Error on line 1 col 40: )"""
#         self.assertTrue(TestParser.test(input, expect, 224))

# TODO type la array
#     def test225(self):
#         input="""main: function void (argv: array[3] of string, out args: integer ) {
# 	a: integer = 5;
# 	c: auto = 282;
# 	if (c<=100) a = a+100;
# 	else a= a - 100;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 225))

# TODO type la array
#     def test226(self):
#         input="""main: function void (argv: array[3] of string, out args: integer ) {
# 	break;
# 	mul_func: function integer (a,b:integer){
# 		return a*b;
# 	}
# }"""
#         expect="""Error on line 3 col 11: function"""
#         self.assertTrue(TestParser.test(input, expect, 226))


    def test227(self):
        input="""c,d : float = 2.6e2, 10e9;
main: function void (){
if (a!=0){
	expr_val = a * b + c - d /e + g*123%h;
}
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 227))


    def test228(self):
        input="""main: function void(){
}

concat_expr: function float() inherit main{
	str1, str2: string = "abc","";
	if (true) return str1::str2;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 228))


    def test229(self):
        input="""main: function void(){
}

relational_expr: function float() inherit main{
	expr1,expr2,expr3,expr4: integer = {5,6,7,8,9}
}"""
        expect="""Error on line 6 col 0: }"""
        self.assertTrue(TestParser.test(input, expect, 229))


    def test230(self):
        input="""relational_expr: function float() inherit main{
	expr1,expr2: integer = 5,6;
	if (false) return (expr1 == expr2) && (expr1 >= expr2) && (expr1 >= expr2) && (expr1 <= expr2) || (expr1 > expr2) && (expr1 < expr2);
	else break;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 230))


    def test231(self):
        input="""bool_expr: function float() inherit main{
	bolean1, bolean2, bolean3, bolean4: boolean = true,false,false,true;
	if (bolean1 == true) continue;
	else bool_value = !bolean1 && bolean2 || bolean1;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 231))

# TODO declare ID la function
#     def test232(self):
#         input="""index_expr: function float() inherit main{
# 	my_array: array[100] of float;
# 	if (x != 2) new_ele = my_array[2+5,92,17];
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 232))


    def test233(self):
        input="""a : auto = divide(90,foo(a,template(abcs())));"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 233))

# TODO Sua lai cho phep expr trong dimension
#     def test234(self):
#         input="""new_array: array[200] of float;
# main: function void(){
# if (true)
# 	new_array[20] = new_array[-new_array[2] *20 + 82e-7 -100_712 /10 %20];
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 234))


    def test235(self):
        input="""find_gcd: main integer (a,b: integer) inherit break {
	
}"""
        expect="""Error on line 1 col 10: main"""
        self.assertTrue(TestParser.test(input, expect, 235))

# TODO para la idlist
#     def test236(self):
#         input="""find_gcd: function integer (a,b: integer) {
# 	for (i=50,i<20, i+1){
# 		if (i%2==0)	break;
# 	}
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 236))


    def test237(self):
        input="""test_function: function void (){
	while(true){
		x = x + 1;
		if (x>5)
			break;
	}
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 237))


    def test238(self):
        input="""bool_expr: function float() inherit main{
	bolean1, bolean2, bolean3, bolean4: boolean = true,false,,true,true;
	if (bolean1 == true) continue;
	else bool_value = !bolean1 && bolean2 || bolean1;
}"""
        expect="""Error on line 2 col 58: ,"""
        self.assertTrue(TestParser.test(input, expect, 238))


    def test239(self):
        input="""relational_expr: function float() inherit main{
	if () return foo(a,b,c);
}"""
        expect="""Error on line 2 col 5: )"""
        self.assertTrue(TestParser.test(input, expect, 239))

# TODO declare ID la function
#     def test240(self):
#         input="""test_syntax: function array[182_729] of string (string_list: array[10] of string) {
# 	i: integer = 0;
# 	while (true){
# 		a = a::string_list[i];
# 		i = i + 1;
# 	}
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 240))


    def test241(self):
        input="""b: array = {2810},218;"""
        expect="""Error on line 1 col 9: ="""
        self.assertTrue(TestParser.test(input, expect, 241))

# TODO Sua lai cho phep expr trong dimension
#     def test242(self):
#         input="""main: function void() {
#     for(i= new_array[29 *821 %1210 -1128], i <= 1, i+1)
#         for(j = i-1, j!=0, j-1) {
#             print_integer(j,i);
#         }
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 242))


    def test243(self):
        input="""infinite_loop: function void() {
    while(false)
		new_function(a,b,c);
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 243))


    def test244(self):
        input="""main: function void() {
    add_ope(12019_1212,.e+10,"asjcab");
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 244))


    def test245(self):
        input="""infinite_for_loop: function void(){
	for (i=1, i>0, i+1)
		print_float(.1e8)
}"""
        expect="""Error on line 4 col 0: }"""
        self.assertTrue(TestParser.test(input, expect, 245))

# TODO declare ID la function
#     def test246(self):
#         input="""nested_if_func: function boolean (a,b,c,d,e,f: boolean){
# 	if (a){
# 		if (b)
# 		{
# 			if (c)
# 				break;
# 		}
# 	}
# 	else print("nothing happenned");
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 246))


    def test247(self):
        input="""fibonacci_func: function void (n: integer){
	i,a,b: integer = 1,0,1,;
	do {

	}
	while (i<=n){
		c = b;
		b = b+a;
		a = c;
	}

}"""
        expect="""Error on line 2 col 23: ,"""
        self.assertTrue(TestParser.test(input, expect, 247))


    def test248(self):
        input="""simple_encryption: function void (key: string){
	if (!key)
		return -1;
	print("Please enter plaintext");
	print("Your ciphertext is");
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 248))


    def test249(self):
        input="""nested_decl: function void() {
    {
        {
            {
                {
                    array_int: array[5] of integer;
                }
            }
        }
    }"""
        expect="""Error on line 10 col 5: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 249))

# TODO declare ID la function
#     def test250(self):
#         input="""array_type_func: function array[3] of integer(){
#     return {1,2,5};
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 250))

# TODO declare ID la function
#     def test251(self):
#         input="""random_expr: function void(float: a,b,c,d) {
#     a: auto = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
# }"""
#         expect="""Error on line 1 col 27: float"""
#         self.assertTrue(TestParser.test(input, expect, 251))

# TODO declare ID la function
#     def test252(self):
#         input="""compare_concat_string: function boolean(str1,str2: string)){
# 	if (true)
# 		return str1::str2 == str2::str1;
# }"""
#         expect="""Error on line 1 col 58: )"""
#         self.assertTrue(TestParser.test(input, expect, 252))

# TODO declare ID la function
#     def test253(self):
#         input="""exp_call_to_death: function auto (){
# 	while (true)
# 		print(func1(func2(func3(func4(func5(func6(param)))))));
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 253))

# TODO declare ID la function
#     def test254(self):
#         input="""test_expr: function float ()
# 	if (true) print(a+b+c+2.02);
# }"""
#         expect="""Error on line 2 col 1: if"""
#         self.assertTrue(TestParser.test(input, expect, 254))

# TODO para la idlist
#     def test255(self):
#         input="""main: function void(var1,var2: integer) {
#     do {
# 		var1 = var1 - 1;
# 	}
#     while (a+b != 0 && a%b != 0)
# }"""
#         expect="""Error on line 5 col 27: !="""
#         self.assertTrue(TestParser.test(input, expect, 255))


    def test256(self):
        input="""run8: function void(inherit out p: float, out i: float, out d: float){
            p = -24 * i + d / 128;
            i = -837 * 0.612 + 32;
            d = -823 % p * i;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 256))


    def test257(self):
        input="""run10: function void(inherit out p: float, out i: float, out d: float){
            p = -24 * i + d / 128;
            i = -837 * 0.352 + 32;
            d = -823 % p * i;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 257))

#TODO Sai tu lexer chu "prinf"
# def test258(self):
#     input="""main function void() { prinf("Degree of freedom is"); prinf(degreeOfFreedom); prinf("\n"); p: float = 0.328;"""
#     expect=""""""
#     self.assertTrue(TestParser.test(input, expect, 258))

# TODO type la array
#     def test259(self):
#         input="""main: function void (argv: array[3] of string, out args: integer ) {
# 	a: integer = 20;
# 	_abc_xyz: void = 1280.128e2;
# 	if (_abc_xyz<=100) a = a+100;
# 	else a= a - 100;
# }"""
#         expect="""Error on line 3 col 11: void"""
#         self.assertTrue(TestParser.test(input, expect, 259))

# TODO type la array
#     def test260(self):
#         input="""main: function void (argv: array[3] of string, out args: integer ) {
# 	a: integer = 20;
# 	_abc_xyz: auto = 1280.128e2;
# 	if (_abc_xyz<=100) a = a+100;
# 	else a= a - 100;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 260))

# TODO type la array
#     def test261(self):
#         input="""main: function void (argv: array[3] of string, out args: integer ) {
# 	a: integer = 20
# 	_abc_xyz: auto = 1280.128e2;
# 	if (_abc_xyz<=100) a = a+100;
# 	else a= a - 100;
# }"""
#         expect="""Error on line 3 col 1: _abc_xyz"""
#         self.assertTrue(TestParser.test(input, expect, 261))

# TODO Sai tu lexer "print"
#     def test262(self):
#         input="""nested_cond_func: function boolean (){
# 	if (a>=c){
# 		if (a>=b)
# 			print("TRUE");
# 	}
# 	else print("FALSE")
# }"""
#         expect="""Error on line 6 col 1: else"""
#         self.assertTrue(TestParser.test(input, expect, 262))

# TODO type la array
#     def test263(self):
#         input="""
# main: function void (argv: array[100] of string, args: integer){
# 	if (args == 0) break;
# 	else {
# 		expr_val = a * b + c - d /e + g*123%h;
# 	}
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 263))


    def test264(self):
        input="""main: function void() {
    if(condi == true)
	printInteger(129831273);
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 264))


    def test265(self):
        input="""main: function void()"""
        expect="""Error on line 1 col 21: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 265))

# TODO Sai tu lexer "prinf"
#     def test266(self):
#         input="""degreeOfFreedom: auto = 1024;
# batteryLevel: integer = 100;
# main: function void(){
# 	prinf("Degree of freedom is");
# 	prinf(degreeOfFreedom);
# 	prinf("\n");
# 	p,q,r,s: float = 0.328;
# 	i: int = 0.0;
# }"""
#         expect=""""""
#         self.assertTrue(TestParser.test(input, expect, 266))


    def test267(self):
        input="""run8: function void(inherit out p: float, out i: float, out d: float){
            p = -24 * i + d / 128;
            i = -837 * 0.612 + 32;
            d = 82300000000_9999999999e1000000000000 % p * i;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 267))


    def test268(self):
        input="""run6: function void(inherit out p: float, out i: float, out d: float){
            p = -24 * i + d :: 128;
            i = -837 * 0.682 + 32;
            d = -823 % p * i;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 268))


    def test269(self):
        input="""run1: function void(inherit out p: float, out i: float, out d: float){
            p = -24i + d / 128;
            i = -837 * 0.842 + 32;
            d = -823 % p * i;
}"""
        expect="""Error on line 2 col 19: i"""
        self.assertTrue(TestParser.test(input, expect, 269))


    def test270(self):
        input="""run7: function void(inherit out p: float, out i: float, out d: float){
            p = -24 * i + d / 128;
            i = -837 * 0.382 + 32;
            d -823 % p * i;
}"""
        expect="""Error on line 4 col 14: -"""
        self.assertTrue(TestParser.test(input, expect, 270))

# TODO para la idlist
#     def test271(self):
#         input="""index_expr: function float(a,b,c:float,) {
# 	my_array: array[100] of float;
# 	if (x != 2) new_ele = my_array[2+5,92,17];
# }"""
#         expect="""Error on line 1 col 39: )"""
#         self.assertTrue(TestParser.test(input, expect, 271))


    def test272(self):
        input="""new_array: array[200] of float;
main: function(){
if (true)
	new_array[20] = new_array[-new_array[2] *20 + 82e-7 -100_712 /10 %20];
}"""
        expect="""Error on line 2 col 14: ("""
        self.assertTrue(TestParser.test(input, expect, 272))

# TODO para la idlist
#     def test273(self):
#         input="""main: function void (argv,argv2: integer, out args: integer ) {
# 	a: integer = 20;
# 	_abc_xyz: auto = 1280.128e2;
# 	if (_abc_xyz<=100) a = a+100;
# 	else a= a - 100;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 273))


    def test274(self):
        input="""nested_cond_func: function boolean (){
	if (a>=c){
		if (a>=b) else return;
	}
	else print("FALSE")
}"""
        expect="""Error on line 3 col 12: else"""
        self.assertTrue(TestParser.test(input, expect, 274))


    def test275(self):
        input="""main: function void(){
	{
		return true;
	}
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 275))


    def test276(self):
        input="""main: function void() {
    do while (true);
}"""
        expect="""Error on line 2 col 7: while"""
        self.assertTrue(TestParser.test(input, expect, 276))

# TODO Sua lai cho phep expr trong dimension
#     def test277(self):
#         input="""main: function void(){
# a = a+2;
# b = a*a + a/a + a%a + a%b + -a + a[b]; 
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 277))


    def test278(self):
        input="""main: funtion void() {
    foo(out a: string);
}"""
        expect="""Error on line 1 col 6: funtion"""
        self.assertTrue(TestParser.test(input, expect, 278))


    def test279(self):
        input="""main: function void() {
    int1: integer = 123;
    float2: string = "string";
    bool3: boolean = true;
    auto4: auto = int1;
    str5: string = "abc"::"xyz";

}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 279))

# TODO para la idlist
#     def test280(self):
#         input="""main: function void(var1,var2: boolean) {
#     var1: boolean = !!!var2;
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 280))


    def test281(self):
        input="""main: function void() {
    a: string = c||d&&g;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 281))


    def test282(self):
        input="""main: function void() {
    a = (a > b) >= c >= d;
}"""
        expect="""Error on line 2 col 21: >="""
        self.assertTrue(TestParser.test(input, expect, 282))


    def test283(self):
        input="""main: function void() inherit main
    x: boolean = y == z && t != r || z == random_function(random_param) && t != my_array[25];
}"""
        expect="""Error on line 2 col 4: x"""
        self.assertTrue(TestParser.test(input, expect, 283))


    def test284(self):
        input="""main: function void() {
    a: void = "string"::a&&c+2*3==b-2*!-b[1,2,3]||d;
}"""
        expect="""Error on line 2 col 7: void"""
        self.assertTrue(TestParser.test(input, expect, 284))

# TODO para la idlist
#     def test285(self):
#         input="""simple_encryption: function void (key,: string){
# 	if (!key)
# 		return -1;
# 	print("Please enter plaintext");
# 	print("Your ciphertext is");
# }"""
#         expect="""Error on line 1 col 38: :"""
#         self.assertTrue(TestParser.test(input, expect, 285))


    def test286(self):
        input="""simple_encryption: function void key: string){
	if (!key)
		return -1;
	print("Please enter plaintext");
	print("Your ciphertext is");
}"""
        expect="""Error on line 1 col 33: key"""
        self.assertTrue(TestParser.test(input, expect, 286))


    def test287(self):
        input="""main: function void {
	{
		return true;
	}
}"""
        expect="""Error on line 1 col 20: {"""
        self.assertTrue(TestParser.test(input, expect, 287))


    def test288(self):
        input="""nested_cond_func: function void auto integer (){
	if (a>=c){
		if (a>=b)
			print("TRUE");
	}
	else print("FALSE")
}"""
        expect="""Error on line 1 col 32: auto"""
        self.assertTrue(TestParser.test(input, expect, 288))


    def test289(self):
        input="""nested_cond_func: function void auto integer (){
	if a>=c {
		if (a>=b)
			print("TRUE");
	}
	else print("FALSE")
}"""
        expect="""Error on line 1 col 32: auto"""
        self.assertTrue(TestParser.test(input, expect, 289))


    def test290(self):
        input="""random_test_function: function float(){
	a,b: integer = 3,4;
	strin1, strin2 = "akajcsna","jhcbahscb";
	while (true){
		print(a+b);
		a = a - 1;
		b = b%a+a;
		if (a+b <=100)
			break;
	}
}"""
        expect="""Error on line 3 col 16: ="""
        self.assertTrue(TestParser.test(input, expect, 290))


    def test291(self):
        input="""main: function void(out inherit var1: auto) {
	break;
}"""
        expect="""Error on line 1 col 24: inherit"""
        self.assertTrue(TestParser.test(input, expect, 291))


    def test292(self):
        input="""main: function void(){
	new_value : auto = 2109*"jnasbc"+89.e82/831 && (true);
}

random_test_function: function float(){
	a,b: integer = 3,4;
	strin1, strin2 = "akajcsna","jhcbahscb";
	while (true){
		print(a+b);
		a = a - 1;
		b = b%a+a;
		if (a+b <=100)
			break;
	}
}"""
        expect="""Error on line 7 col 16: ="""
        self.assertTrue(TestParser.test(input, expect, 292))


    def test293(self):
        input="""main: function void(){
	new_value : auto = 2109*"jnasbc"+89.e82
	random_test_function: function float(){
	a,b: integer = 3,4;
	strin1, strin2 = "akajcsna","jhcbahscb";
	while (true){
		print(a+b);
		a = a - 1;
		b = b%a+a;
		if (a+b <=100)
			break;
	}
}
}"""
        expect="""Error on line 3 col 1: random_test_function"""
        self.assertTrue(TestParser.test(input, expect, 293))


    def test294(self):
        input="""main: void() {}"""
        expect="""Error on line 1 col 6: void"""
        self.assertTrue(TestParser.test(input, expect, 294))

# TODO para la idlist
#     def test295(self):
#         input="""exchange_value: function void (out a,b: integer){
# 	c: integer = a;
# 	a = b;
# 	b = c;
# 	print("New value of a and b after exchange",a,b);
# }"""
#         expect="""successful"""
#         self.assertTrue(TestParser.test(input, expect, 295))

# TODO para la idlist
#     def test296(self):
#         input="""exchange_value: function void (out a,b: integer){
# 	c: integer = a,b;
# 	a = b;
# 	b = c;
# 	print("New value of a and b after exchange",a,b);
# }"""
#         expect="""Error on line 2 col 15: ,"""
#         self.assertTrue(TestParser.test(input, expect, 296))


    def test297(self):
        input="""function: function void (out a,b: integer){
	c: integer = a;
	a = b;
	b = c;
	print("New value of a and b after exchange",a,b);
}"""
        expect="""Error on line 1 col 0: function"""
        self.assertTrue(TestParser.test(input, expect, 297))


    def test298(self):
        input="""main: function void(){
	for (count_var=0,true,true)
		count_var=count_var+1
}"""
        expect="""Error on line 4 col 0: }"""
        self.assertTrue(TestParser.test(input, expect, 298))


    def test299(self):
        input="""main: function void(){
	for (count_var=0,true,true)
		count_var=count_var+1;
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 299))


    def test300(self):
        input="""main: function void() {
    do {
        booealn = booealn -1;
    } while (true);
}"""
        expect="""successful"""
        self.assertTrue(TestParser.test(input, expect, 300))
