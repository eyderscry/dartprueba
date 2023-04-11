def func_temp(grados_fahr):
    """transformacion de fahrenheit a celsius"""
    grados_cel=(grados_fahr-32)*0.5556
    return grados_cel

grados_fahr=float(input("ingrese los grados fahrenheit : "))
print("la temperatura en celsius es ",func_temp(grados_fahr))
