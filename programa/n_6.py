far=float(input("ingrese la temperatura en fahrenheit : "))
cel=((far-32)/1.8)
cel= str(cel)
cel = cel[0:6]
print("la temperatura en Fahrenheit(",far,") es igual a Celsius(",cel,")")
