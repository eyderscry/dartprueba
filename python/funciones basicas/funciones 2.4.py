def procedimiento(x):
    for i in x:
        for n in range(i):
            print("*" ,end="")
        print("")
    return True
num = [4,9,7]
print(procedimiento(num))
