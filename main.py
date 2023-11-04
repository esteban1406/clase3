#la entrada de nuestro algoritmo
num = int(input("ingrese un numero de 3 cifras"))


#operaciones
num1 = num % 10
num2 = (num//10) % 10
num3 = (num//100) % 10
#salida de nuestro algoritmo

print(f"el numero invertido es :{num1}{num2}{num3}")
