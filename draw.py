from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    x1 = int(x1)
    y0 = int(y0)
    y1 = int(y1)

    # print(f'({x0},{y0}) -> ({x1},{y1})')

    # switches endpoints so x0 > x1 always
    if x0 <= x1:
        x = x0
        y = y0
    else:
        x = x1
        y = y1
        x1 = x0
        y1 = y0
        x0 = x
        y0 = y

    # print(f'EDITED ({x},{y}) -> ({x1},{y1})')

    # f(x, y) = Ax + By + C
    A = (y1 - y0)
    B = (x0 - x1)
    # m = A / (-1 * B)

    # Octant I & V
    # Interval: 0 <= m <= 1   -->   0 <= A <= -B
    if (0 <= A) and (A <= (-1 * B)):
        d = (2 * A) + B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += (2 * B)
            x += 1
            d += (2 * A)
    
    # Octant II & VI
    # Interval: 1 < m   -->   -B < A
    elif ((-1 * B) < A):
        d = A + (2 * B)
        while y <= y1:
            plot(screen, color, x, y)
            if d <= 0:
                x += 1
                d += (2 * A)
            y += 1
            d += (2 * B)

    # Octant III & VII
    # Interval: m < -1   -->   A < B
    elif (A < B):
        d = A + (-2 * B)
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += (2 * A)
            y -= 1
            d -= (2 * B)
    
    # Octant IV & VIII
    # Interval: -1 <= m <= 0   -->   B <= A <= 0
    elif (B <= A) and (A <= 0):
        d = (-2 * A) + B
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= (2 * B)
            x += 1
            d += (2 * A)
    
    # Vertical Lines
    # Only if B=0
    elif B == 0:
        if y0 > y1:
            y = y1
            y1 = y0
            y0 = y
        while y <= y1:
            plot(screen, color, x, y)
            y += 1