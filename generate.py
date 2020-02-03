#=================================================================
# Lyapunov Fractal Image Generation...I think?
# Matthew Chan -- 02/02/2020
# Resource: https://en.wikipedia.org/wiki/Lyapunov_fractal
#=================================================================

import math

# Defining variables related to the generated image
HEADER = 'P3'
WIDTH = 500
HEIGHT = 500
MAX_VALUE = 999

# Defining variables related to the Lyapunov Fractal calculations
SEQUENCE = 'AABB'
REGION_X = (0,4)
REGION_Y = (0,4)
START_VALUE = 0.5
LARGE_N = 10


def initialize_ppm(image):
    heading = [str(x) for x in (HEADER, WIDTH, HEIGHT, MAX_VALUE)]
    heading = '\n'.join(heading)
    image.write(heading + '\n')

def format_pixel(r, g, b, x, y):
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > MAX_VALUE:
        r = MAX_VALUE
    if g > MAX_VALUE:
        g = MAX_VALUE
    if b > MAX_VALUE:
        b = MAX_VALUE

    r = int(r)
    g = int(g)
    b = int(b)

    pixel = [str(x) for x in (r, g, b)]
    pixel = ' '.join(pixel)
    if ((x+1) == WIDTH) and ((y+1) == HEIGHT):
        return pixel
    return pixel + ' '

def r(n, x, y):
    S = SEQUENCE[n % len(SEQUENCE)]
    if S == 'A':
        r = x
    elif S == 'B':
        r = y
    return r

CACHE = dict()
def logistic_equation(n, x, y):
    # x_{n+1} = r_{n}x_{n}(1 - x_{n})

    # If n=0, it's the base case
    if n == 0:
        return START_VALUE
    
    if f'{n-1},{x},{y}' in CACHE.keys():
        previous_value = CACHE[f'{n-1},{x},{y}']
    else:
        previous_value = logistic_equation(n-1, x, y)
    value = (r(n, x, y) * previous_value * (1 - previous_value))
    CACHE[f'{n},{x},{y}'] = value
    return value

# approximates the Lyapunov exponent with a suitably large N
def lyapunov_exponent(x, y):
    summation = 0
    for n in range(LARGE_N):
        if n != 0:
            curr_sum = math.fabs(r(n, x, y) * (1 - (2 * logistic_equation(n, x, y))))
            try:
                curr_sum = math.log10(curr_sum)
                summation += curr_sum
            except ValueError:
                summation += 0
    return ((1.0 / LARGE_N) * summation)

def generate_pixels(image):
    exponent_map = list()
    for x in range(WIDTH):
        column = list()
        scaled_x = REGION_X[0] + (((float(REGION_X[1]) - REGION_X[0]) / WIDTH) * x)
        for y in range(HEIGHT):
            scaled_y = REGION_Y[0] + (((float(REGION_Y[1]) - REGION_Y[0]) / HEIGHT) * y)
            exponent = lyapunov_exponent(scaled_x, scaled_y)

            column.append(exponent)
            # print(f'x: {x} || y: {y} || exp: {exponent}')
        exponent_map.append(column)

    min_exponent = min(map(min, exponent_map))
    max_exponent = max(map(max, exponent_map))
    scale = (MAX_VALUE * 3.0) / (max_exponent + math.fabs(min_exponent))

    for x in range(WIDTH):
        for y in range(HEIGHT):
            exponent = exponent_map[x][y] + math.fabs(min_exponent)

            value = exponent * scale
            r = value - MAX_VALUE
            g = value - (MAX_VALUE * 2)
            b = value - (MAX_VALUE * 3)
            
            image.write(format_pixel(r, g, b, x, y))
            # print(f'x: {x} || y: {y} || exp: {exponent}')



image = open('image.ppm', 'w')

initialize_ppm(image)
print("Please remain patient, this may take some time to complete...")
generate_pixels(image)
print("Done!")

image.close()