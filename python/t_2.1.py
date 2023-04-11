num1 = int(input("primer numero :"))
#while num1<=0:
    #num1 = int(input("p :"))
num2=int(input("segundo numero : "))
while num2<=num1:
    num2=int(input("ingrese un valor superior al primer numero : "))
for x in range (num1,num2+1):
    if x%num1==1:
        div=float(x/2)
        print(x,end="-")
        print(div,end=',')
