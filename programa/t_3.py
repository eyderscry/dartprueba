import time

#ambos contadores deben tener el mismo valor
Cont_notas = 10#cantidad de notas que pide el programa
Cont = 10


Suma_ingresada = float(0)#inicializacion de variable suma
#pide las notas
while Cont_notas >=1:
    Numero_ingresada = float(input("ingrese la nota a promediar : "))
    Suma_ingresada += Numero_ingresada
    Cont_notas -=1

#saca el promedio y lo trunca a la decima
Note_prom = float(Suma_ingresada / Cont )
#print(Note_prom)
Note_prom = str(Note_prom)
Note_prom = Note_prom[0:3]
Note_prom = float(Note_prom)

print("la suma de las notas es : ",Suma_ingresada,"\n")
print("el promedio es : ",Note_prom)
