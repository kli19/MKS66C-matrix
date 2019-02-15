"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    string = ""
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            string += str(matrix[j][i])
            string += " "
        string += "\n"
    print(string)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if len(m1) != len(m2[0]):
        print("matrix_mult error: num cols in m1 not equal to num rows in m2")
    else:
        m = new_matrix(len(m1[0]),len(m2))
        print_matrix(m)
        for i in range(len(m)):
            for j in range(len(m[0])):
                num = 0                
                m[i][j] = num
                        
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

m1 = [[1,4],[2,5],[3,6]]
m2 = new_matrix(3,3)
ident(m2)
print_matrix(m1)
print_matrix(m2)
matrix_mult(m1,m2)
