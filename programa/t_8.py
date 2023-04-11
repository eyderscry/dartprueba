a=int(input("Ingrese un numero entero mayor a 0 :"))
b=0
if a>=0:
    while b != a:
        b+=1
        print(b)
else:
    print("El valor no es admitido(",a,")")
