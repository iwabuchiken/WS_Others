/* file : 27_11-12.py
   at : 2018/03/18 06:13:04
*/
#ref regular expression upper case https://stackoverflow.com/questions/1159343/convert-a-char-to-upper-case-using-regular-expressions-editpad-proanswered Jul 21 '09 at 14:01
#ref https://github.com/sympy/sympy/wiki/Quick-examples
from sympy import *

a,b,c = symbols('a b c')
A,B,C = symbols('A B C')

a11,a12,a13 = symbols('a11 a12 a13')
b11,b12,b13 = symbols('b11 b12 b13')
b21,b22,b23 = symbols('b21 b22 b23')
b31,b32,b33 = symbols('b31 b32 b33')
c1,c2,c3 = symbols('c1 c2 c3')

#ref http://docs.sympy.org/0.6.7/modules/matrices.html#operations-on-entries
#ref M = Matrix(([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]))
A = Matrix([a11 a12 a13])
A = Matrix(1,3,[a11, a12, a13])
C = Matrix(3,1,[c1, c2, c3])

B = Matrix(3,3,[b11,b12,b13,b21,b22,b23,b31,b32,b33])

# operations
A.dot(B)	#=> error : "Matrix size mismatch: (3, 1) * (3, 3)"
B.dot(C)	#=> list
Matrix(B.dot(C)).shape	#=> (3, 1)
A.dot(B.dot(C))	#=> a11*(b11*c1 + b12*c2 + b13*c3) + a12*(b21*c1 + b22*c2 + b23*c3) + a13*(b31*c1 +b32*c2 + b33*c3)
expand(A.dot(B.dot(C)))	#=> a11*b11*c1 + a11*b12*c2 + a11*b13*c3 + a12*b21*c1 + a12*b22*c2 + a12*b23*c3 + a13*b31*c1 + a13*b32*c2 + a13*b33*c3
