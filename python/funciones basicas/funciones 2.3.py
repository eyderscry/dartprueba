def max(x,c):
    if x > c:
        return x
    elif c > x:
        return c
    else:
        return print("{} es igual a {}".format(x,c))
    return True

print(max(3,3))
