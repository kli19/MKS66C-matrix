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
    for i in range(4):
        for j in range(len(matrix)):
            string += str(matrix[j][i])
            string += " "
        string += "\n"
    print(string)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

matrix = [[0,1,2,1],[3,4,5,1],[6,7,8,1]]
print_matrix(matrix)
