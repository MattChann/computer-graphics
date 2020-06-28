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
    matrixString = ""
    for row in matrix:
        for column in row:
            matrixString += str(column) + ' '
        matrixString += '\n'
    print(matrixString)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#===Helper Functions===
def getColumn(matrix, colNum):
    col = list()
    for row in matrix:
        col.append(row[colNum])
    return col

def dotProduct(row, col):
    result = 0
    for i in range(len(row)):
        result += (row[i] * col[i])
    return result
#======================


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if len(m1[0]) == len(m2):
        result = new_matrix(rows=len(m1), cols=len(m2[0]))
        for row in range(len(result)):
            for column in range(len(result[0])):
                result[row][column] = dotProduct(m1[row], getColumn(m2, column))
        m2.clear()
        for row in result:
            m2.append(row)
        return m2




def new_matrix(rows = 4, cols = 4):
    # m = []
    # for c in range( cols ):
    #     m.append( [] )
    #     for r in range( rows ):
    #         m[c].append( 0 )
    # return m
    matrix = list()
    for row in range(rows):
        matrix.append(list())
        for column in range(cols):
            matrix[row].append(0)
    return matrix