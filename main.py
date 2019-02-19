from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

print("Testing matrices")
m2 = new_matrix(4,2)
print ("m2 = ")
print_matrix(m2)
print ("Testing add_edge. Adding (1,2,3), (4,5,6) m2 =")
add_edge(m2,1,2,3,4,5,6)
print ("m2=")
print_matrix(m2)
m1 = new_matrix()
print("m1 = ")
print_matrix(m1)
print("Testing ident. m1 =")
ident(m1)
print_matrix(m1)
print("Testing matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)
print("m1 = ")
m1 = new_matrix()
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,10,11,12)
print_matrix(m1)
print("Testing matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)


#draw_lines( m2, screen, color )
display(screen)
