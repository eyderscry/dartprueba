def func_Imc(peso, altura):
    """funcion de Imc"""
    Imc=0
    Imc=peso/(altura**2)
    Imc=str(Imc)
    Imc=Imc[0:5]
    return Imc

altura=float(input("ingrese su altura : "))
peso=float(input("ingrese su peso : "))

print("Su Imc es ",func_Imc(peso, altura))

