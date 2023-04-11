cont=0
for i in range (3):
    a = float(input("ingrese porcentaje :"))
    if a >= 1:
        a = a / 100
    cont += a
    print(cont)

if cont >= 1:
    print("el porcentaje es mayor al 100% " )
print("fin del programa")
