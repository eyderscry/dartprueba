a=float(input("ingrese un numero para ´a´ : "))
b=float(input("ingrese un numero para ´b´ : "))
#suma
print("La suma de ",a," + ",b," es :",a+b)
#resta
print("La resta de ",a," - ",b," es :",a-b)
#division
try:
    print("La division de ",a," / ",b," es : ",end="" )
    print(a/b)
except ZeroDivisionError:
    print("no se admite la dision por cero")
#multiplicacion
print("El producto de ",a," x ",b," es :",a*b)
