from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES / 2, s, c)
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

#octants 8 and 4
c[BLUE] = 255
draw_line(0, YRES-1, XRES-1, 0, s, c)
draw_line(0, YRES-1, XRES-1, YRES/2, s, c)
draw_line(XRES-1, 0, 0, YRES/2, s, c)

#octants 2 and 6
c[RED] = 255
c[GREEN] = 0
c[BLUE] = 0
draw_line(0, 0, XRES/2, YRES-1, s, c)
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c)

#octants 7 and 3
c[BLUE] = 255
draw_line(0, YRES-1, XRES/2, 0, s, c)
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c)

#horizontal and vertical
c[BLUE] = 0
c[GREEN] = 255
draw_line(0, YRES/2, XRES-1, YRES/2, s, c)
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')



#==================================================================================================
# import math

# s = new_screen()
# c = [ 255, 255, 255 ]

# RADIUS = 250

# for i in range(100):
#     theta = i * ((2 * math.pi)/100)

#     offsets = [0, (math.pi * 9 / 10), (math.pi / 7), (math.pi * 7 / 8)]
#     points = list()
#     for theta_offset in offsets:
#         points.append(((RADIUS * math.cos(theta + theta_offset)) + RADIUS, (RADIUS * math.sin(theta + theta_offset)) + RADIUS))
#     for point in points:
#         for other_point in points:
#             if point != other_point:
#                 draw_line(point[0], point[1], other_point[0], other_point[1], s, c)

# display(s)
# save_ppm(s, 'binary.ppm')
# save_ppm_ascii(s, 'ascii.ppm')
# save_extension(s, 'img.png')