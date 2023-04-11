num1=int(input('ingrese un valor : '))
for i in range(num1):
    print('')
    for x in range (0,i+1):
        print(i+1,end='')
for n in range (num1,1,-1):
    print('')
    for m in range (1,n):
        print(n-1,end='')
