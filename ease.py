import math

EASES = ['linear', 'power1', 'power2', 'power3', 'power4', 'back', 'elastic', 'bounce']

def generate(ease, start, end, frames):
    if start > end:
        delta = (start - end) / (frames-1)
    else:
        delta = (end - start) / (frames-1)
    values = list()

    curr = start
    for f in range(frames):
        values.append(curr)
        curr += delta
    values[-1] = end
    # print(values)

    if ease == 'linear':
        values = [shift(linear(x), start, end) for x in values]
    elif ease == 'power1':
        values = [shift(power1(x), start, end) for x in values]
    elif ease == 'power2':
        values = [shift(power2(x), start, end) for x in values]
    elif ease == 'power3':
        values = [shift(power3(x), start, end) for x in values]
    elif ease == 'power4':
        values = [shift(power4(x), start, end) for x in values]
    elif ease == 'back':
        values = [shift(back(x), start, end) for x in values]
    elif ease == 'elastic':
        values = [shift(elastic(x), start, end) for x in values]
    elif ease == 'bounce':
        values = [shift(bounce(x), start, end) for x in values]
    values[0] = start
    values[-1] = end
    
    return values


def shift(value, start, end):
    if start > end:
        return value * (start - end) * -1 + start
    else:
        return value * (end - start) + start


def linear(x):
    return x

def power1(x):
    return 1 - ((x - 1) ** 2)

def power2(x):
    return 1 + ((x - 1) ** 3)

def power3(x):
    return 1 - ((x - 1) ** 4)

def power4(x):
    return 1 + ((x - 1) ** 5)

def back(x):
    z = 2.75 * (x - 0.0196) + 3
    temp = (-50000000000 / (z ** 20)) * (math.sin(z))
    temp *= 0.25
    return temp + 1

def elastic(x):
    return (-165.702 * (x ** 6)) + (598.676 * (x ** 5)) - (845.428 * (x ** 4)) + (583.861 * (x ** 3)) - (199.602 * (x ** 2)) + (29.1935 * x)

def bounce(x):
    temp = elastic(x)
    return -1 * abs(1 - temp) + 1