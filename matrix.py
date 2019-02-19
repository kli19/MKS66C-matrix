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
    m1_rows = []
    m2_cols = []
    
    #make a list of the rows in m1
    for i in range(len(m1[0])):
        row = []
        for j in range(len(m1)):
            row.append(m1[j][i])
        m1_rows.append(row)
    #print_matrix(m1_rows)

    #make a copy of m2
    for i in range(len(m2)):
        col = m2[i][:]
        m2_cols.append(col)
    #print_matrix(m2_cols)

    for i in range(len(m1_rows)):
        for j in range(len(m2_cols)):
            dot = 0
            row = m1_rows[i]
            col = m2_cols[j]
            for n in range(len(row)):
                dot += row[n]*col[n]
            m2[j][i] = dot
    print_matrix(m2)
    
                        
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

m1 = [[5,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,5]]
m2 = [[4,2,1,2],[2,1,2,1],[1,2,1,2],[2,1,2,1],[1,2,1,2],[2,1,2,4]]

print_matrix(m1)
print_matrix(m2)
matrix_mult(m1,m2)
