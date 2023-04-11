def promedio(num1, num2):#num1 = suma de notas  num2 = valor que divide las notas
    Note_prom = float((num1) / num2 )
    #print(Note_prom)#revisa el resultado del promedio verdadero
    Note_prom = str(Note_prom)
    Note_prom = Note_prom[0:3]
    return Note_prom

#Inicio declaracion de varibles¡¡¡

#Inicializacion de varibles contadores

Cont_notas = 0#cantidad de notas que pide el programa
Cont = Cont_notas#cantidad que divide la suma de notas

#Varibles para personalizar el programa

Suma_ingresada = float(0)#inicializacion de variable suma(no modificar)
Num_minimo = float(1.0)#numero minimo para calcular el promedio
Num_maximo = float(7.0)#numero maximo para calcular el promedio
Num_seguro = 15#numero para enviar mensaje de confirmacion por exceso de notas

#Fin de las declaracion de varibles!!!

#Entrada de notas(modificacion de varibles contadores)¡¡¡

while Cont_notas <= 0:
    try:
        Cont_notas = int(input("Ingrese la cantidad de notas que quiere promediar : "))
    except ValueError:
        Cont_notas = int(0)
        
    if Cont_notas <= 0:
        print("No has asignado un valor superior a cero")
        print(" o has ingresado algun valor no admitido")
    elif Cont_notas >= Num_seguro:
        print("Has asignado mas de ",Num_seguro," notas, estas seguro que quiere proceder")
        print("para continuar responde ¨s¨, sino cualquier otra letra")
        print("en total se pediran ",Cont_notas," notas")
        Recepcion = str(input("ingrese confirmacion : "))#se creara solo si se excede el limite seguro de notas
        Recepcion = Recepcion.lower()
        Recepcion = Recepcion[0]
        if Recepcion != "s":
            Cont_notas = int(0)
        
    Cont = Cont_notas
#Fin de entrada de notas!!!

#Inicio bucle principal pide, suma y revisa las notas ingresadas¡¡¡

while Cont_notas >=1:
    
    try:#evita que el programa se cierre por un error inesperado en la ejecucion (no cubre todos los errores)
        Numero_ingresado = float(input("Ingrese la nota a promediar : "))
    except ValueError:
        print("has ingresado un valor desconocido\n".capitalize())
        continue
        
    if Numero_ingresado <Num_minimo:#verifica que el numero no sea menor que la nota minima admitida
        print("El numero ingresado",Numero_ingresado," excede el valor minimo de las notas", Num_minimo)
        continue
    
    elif Numero_ingresado >Num_maximo:#verifica que el numero no sea mayor que la nota maxima admitida
        print("El numero ingresado",Numero_ingresado," excede el valor maximo de las notas", Num_maximo)
        continue

    Suma_ingresada += Numero_ingresado
    Cont_notas -=1
    
    #print("NOTAS :",Cont_notas," CONT :",Cont)#descomentar para tener un seguimiento del programa
    
#fin del bucle principal!!!


print("el promedio es : ",promedio(Suma_ingresada, Cont))

#input()#descomentar para que no se cierre la consola en windows
