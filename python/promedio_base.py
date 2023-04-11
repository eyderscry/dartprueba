Note_a = float(input("your enter a note 1 = "))
Note_b = float(input("your enter a note 2 = "))
Note_c = float(input("your enter a note 3 = "))

#calcula el promedio y lo trunca a la decima
Note_prom = float((Note_a + Note_b + Note_c) / 3 )
Note_prom = str(Note_prom)
Note_prom = Note_prom[0:3]
Note_prom = float(Note_prom)

#print(Note_prom,"\n ")#revisa si esta bien el promedio

#verifica si esta aprobado
if Note_prom >= 4.0:
    print("your are approve with ", Note_prom)
    if Note_prom < 5.0:
        print("you should study more")
else :
    print("you are reprobate with ", Note_prom)