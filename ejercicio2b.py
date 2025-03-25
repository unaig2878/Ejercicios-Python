# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)
def esMayorEdad(edad):
    return edad>=18

# Programa principal
def main():
    nombre = input("Introduzca su nombre: ")
    edad = int(input(f"Introduzca su edad {nombre}: "))

    if esMayorEdad(edad):
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

if __name__== "__main__" :
   main()
