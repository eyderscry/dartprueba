cont_cero = 0
cont_uno = 0

num1=int(input('cuantos numeros desea ingresar : '))
for i in range(num1):
    num2=int(input('ingrese un valor : '))
    while num2<0 or num2>=10:
        num2=int(input('ingrese un valor entre 0 y 9 : '))
    if num2 == 0:
        cont_cero += 1
    elif num2 == 1:
        cont_uno +=1
        
if cont_cero>=1 or cont_uno>=1:
    print('se encontraron ',cont_cero, ' cero y',end=" ")
    print(cont_uno,' uno ')
else:
    print('no se encontraron uno o cero')
