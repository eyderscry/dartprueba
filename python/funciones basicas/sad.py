print("presione la tecla d ")
try:
    raise KeyboardInterrupt

except KeyboardInterrupt:
    Ver_salida = input("has presionado ctrl+c ,desea salir : ")
    Ver_salida = str(Ver_salida.lower())
    Ver_salida = Ver_salida[0]
    if Ver_salida == "s":
        print("has salido del programa \n")
        break
    else:
        print("presiona s para terminar el programa \n")
        
print("fin del programa")
