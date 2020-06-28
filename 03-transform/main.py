from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
transform = new_matrix()

# print_matrix(make_translate(7,8,9))
# print_matrix(make_scale(7,8,9))
# print_matrix(make_rotX(90))
# print_matrix(make_rotY(90))
# print_matrix(make_rotZ(90))

parse_file( 'script', edges, transform, screen, color )

# parse_file( 'image_script', edges, transform, screen, color )