from numpy import *
mat1 = matrix('2 3 4;3 4 2;4 2 2')
mat2 = matrix('2 3 5;2 4 2;4 9 0')
mat3 = mat1 + mat2
mat4 = mat1 * mat2
print("add",mat3)
print("multi",mat4)