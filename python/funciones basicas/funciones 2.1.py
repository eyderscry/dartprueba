def evalua(x):
    cont_sum = 0
    for i in range(x,8):
        cont_sum +=(3*i + 4)
    cont_sum = cont_sum * 2
    return cont_sum

print(evalua(3))
