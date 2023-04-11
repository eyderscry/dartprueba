value=float(input("ingrese el radio en centimetros :"))
#formula
vol=((4/3)*(3.1416*(value*value*value)))
vol = str(vol)
vol = vol[0:6]
print("El volumen de la esfera es : ",vol," cm")
