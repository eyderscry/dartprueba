Algoritmo hasta_cero
	//definicion de tipos de varibles
	definir num_N, N ,cont_N,cont_Pos,cont_Neg Como Real
	definir cont Como Logico
	//definir valores a variables
	cont<-Falso
	cont_Neg<-0;
	cont_Pos<-0;
	cont_N<-0;
	num_N<-0;
	//bucle principal
	Escribir "Este programa termina al ser ingresado un cero";
	
	Mientras cont != Verdadero Hacer
		Escribir "escriba un numero"
		Leer N
		num_N<-num_N+N
		Si N == 0 Entonces
			cont<-Verdadero
		Fin Si
		Si N < 0 Entonces
			cont_Neg<-cont_Neg + 1;
		SiNo
			cont_Pos<- cont_Pos + 1;
		Fin Si
		cont_N<-cont_N + 1;
	Fin Mientras
	//salida para el usuario
	Escribir "Usted a ingresado ",cont_N, " numeros "Sin Saltar
	Escribir "en que habian ",cont_Pos," numeros positivos y"
	Escribir cont_Neg," numeros negativos "Sin Saltar
	Escribir "los cuales suman ",num_N," en total";
FinAlgoritmo
