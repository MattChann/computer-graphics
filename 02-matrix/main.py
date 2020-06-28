from display import *
from draw import *
from matrix import *

#===TESTING===
print('Testing printing new matrix. m1 =')
m1 = new_matrix()
print_matrix(m1)

print('Testing printing identity matrix. m1 =')
ident(m1)
print_matrix(m1)

print('Manual new matrix. m2 =')
m2 = [[1, 4],
      [2, 5],
      [3, 6],
      [1, 1]]
print_matrix(m2)

print('Testing matrix multiplication. m1 * m2 =')
matrix_mult(m1, m2)
print_matrix(m2)

print('Testing matrix multiplication. m1 =')
m1 = [[1, 4, 7, 10],
      [2, 5, 8, 11],
      [3, 6, 9, 12],
      [1, 1, 1, 1]]
print_matrix(m1)
print_matrix(m2)

print('Testing matrix multiplication. m1 * m2 =')
matrix_mult(m1, m2)
print_matrix(m2)

print('Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =')
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
#=============

screen = new_screen()
color = [153, 218, 255]
edges = new_matrix(rows=4, cols=0)

# add_edge(edges, 50, 450, 0, 100, 450, 0);
# add_edge(edges, 50, 450, 0, 50, 400, 0);
# add_edge(edges, 100, 450, 0, 100, 400, 0);
# add_edge(edges, 100, 400, 0, 50, 400, 0);

# add_edge(edges, 200, 450, 0, 250, 450, 0);
# add_edge(edges, 200, 450, 0, 200, 400, 0);
# add_edge(edges, 250, 450, 0, 250, 400, 0);
# add_edge(edges, 250, 400, 0, 200, 400, 0);

# add_edge(edges, 150, 400, 0, 130, 360, 0);
# add_edge(edges, 150, 400, 0, 170, 360, 0);
# add_edge(edges, 130, 360, 0, 170, 360, 0);

# add_edge(edges, 100, 340, 0, 200, 340, 0);
# add_edge(edges, 100, 320, 0, 200, 320, 0);
# add_edge(edges, 100, 340, 0, 100, 320, 0);
# add_edge(edges, 200, 340, 0, 200, 320, 0);

ENDPOINT_1 = (0, 450)
ENDPOINT_2 = (450, 0)

INCREMENT = 5

for i in range(0, 1000, INCREMENT):
    add_edge(edges, i, 0, 0, ENDPOINT_1[0], ENDPOINT_1[1], 0)
    add_edge(edges, 0, i, 0, ENDPOINT_2[0], ENDPOINT_2[1], 0)

draw_lines( edges, screen, color )
display(screen)