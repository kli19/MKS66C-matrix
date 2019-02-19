from display import *
from draw import *
from matrix import *

import random

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

drawing = new_matrix()

centerX = XRES/2
centerY = YRES/2

x = 0
y = 0
color = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]

while x <= XRES and y <= YRES:
    add_edge(drawing, centerX+x, centerY+y, 0, centerX+y, centerY-x, 0)
    add_edge(drawing, centerX+y, centerY-x, 0, centerX-x, centerY-y, 0)
    add_edge(drawing, centerX-x, centerY-y, 0, centerX-y, centerY+x, 0)
    add_edge(drawing, centerX-y, centerY+x, 0, centerX+x, centerY+y, 0)
    x+=random.randint(-50,50)
    y+=random.randint(-50,50)

draw_lines( drawing, screen, color )
display(screen)

