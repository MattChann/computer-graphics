from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname)
    lines = [line.strip() for line in file.readlines()]
    file.close()
    
    i = 0
    while i < len(lines):
        if lines[i] == 'line':
            lines[i+1] = [int(arg) for arg in lines[i+1].split(' ')]
            add_edge(points, lines[i+1][0], lines[i+1][1], lines[i+1][2], lines[i+1][3], lines[i+1][4], lines[i+1][5])
            i = i+1
        elif lines[i] == 'ident':
            ident(transform)
        elif lines[i] == 'scale':
            lines[i+1] = [int(arg) for arg in lines[i+1].split(' ')]
            matrix_mult(make_scale(lines[i+1][0], lines[i+1][1], lines[i+1][2]), transform)
            i = i+1
        elif lines[i] == 'move':
            lines[i+1] = [int(arg) for arg in lines[i+1].split(' ')]
            matrix_mult(make_translate(lines[i+1][0], lines[i+1][1], lines[i+1][2]), transform)
            i = i+1
        elif lines[i] == 'rotate':
            lines[i+1] = lines[i+1].split(' ')
            lines[i+1][1] = int(lines[i+1][1])
            if lines[i+1][0] == 'x':
                matrix_mult(make_rotX(lines[i+1][1]), transform)
            elif lines[i+1][0] == 'y':
                matrix_mult(make_rotY(lines[i+1][1]), transform)
            elif lines[i+1][0] == 'z':
                matrix_mult(make_rotZ(lines[i+1][1]), transform)
            i = i+1
        elif lines[i] == 'apply':
            matrix_mult(transform, points)
        elif lines[i] == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif lines[i] == 'save':
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, lines[i+1])
            i = i+1
        elif lines[i] == 'quit':
            break
        
        i = i+1