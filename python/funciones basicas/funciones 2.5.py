def vol_esfera(x):
    cont_vol = float((4/3)*3.1416 *x**3)
    return cont_vol
rad= int(input("ingrese el valor del  radio : "))
print("El volumen de una esfera con radio {} es {}".format(rad,vol_esfera(rad)))
    
