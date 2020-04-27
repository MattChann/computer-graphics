import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    I_ambient = calculate_ambient(ambient, areflect)
    I_diffuse = calculate_diffuse(light, dreflect, normal)
    I_specular = calculate_specular(light, sreflect, view, normal)
    return [
        I_ambient[0] + I_diffuse[0] + I_specular[0],
        I_ambient[1] + I_diffuse[1] + I_specular[1],
        I_ambient[2] + I_diffuse[2] + I_specular[2],
    ]

def calculate_ambient(alight, areflect):
    answer = (
        alight[0] * areflect[0],
        alight[1] * areflect[1],
        alight[2] * areflect[2],
    )
    return [limit_color(color) for color in answer]

def calculate_diffuse(light, dreflect, normal):
    lightVector = light[LOCATION]
    lightColor = light[COLOR]
    normalize(lightVector)
    normalize(normal)
    answer = (
        lightColor[0] * dreflect[0] * dot_product(normal, lightVector),
        lightColor[1] * dreflect[1] * dot_product(normal, lightVector),
        lightColor[2] * dreflect[2] * dot_product(normal, lightVector),
    )
    return [limit_color(color) for color in answer]

def calculate_specular(light, sreflect, view, normal):
    lightVector = light[LOCATION]
    lightColor = light[COLOR]
    normalize(lightVector)
    normalize(normal)
    normalize(view)

    # 2N
    temp = [2*x for x in normal]
    # 2N(N ⋅ L)
    temp = [x*dot_product(normal, lightVector) for x in temp]
    # 2N(N ⋅ L) - L
    temp = [(temp[i] - lightVector[i]) for i in range(3)]
    # (2N(N ⋅ L) - L) ⋅ V
    temp = dot_product(temp, view)

    if temp < 0:
        return [0,0,0]

    # [(2N(N ⋅ L) - L) ⋅ V] ^ n
    vectorMath = temp ** SPECULAR_EXP

    answer = (
        lightColor[0] * sreflect[0] * vectorMath,
        lightColor[1] * sreflect[1] * vectorMath,
        lightColor[2] * sreflect[2] * vectorMath,
    )
    return [limit_color(color) for color in answer]

def limit_color(color):
    if color < 0:
        return 0
    elif color > 255:
        return 255
    else:
        return int(color)

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
