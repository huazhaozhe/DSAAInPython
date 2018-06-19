def sqrt(x):
    y = 1.0
    i = 1
    while abs(y * y - x) > 1e-10:
        i += 1
        y = (y + x/y)/2
    print('loop count:', i)
    return y