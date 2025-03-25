# coding=utf-8
__Author__="José Gaspar Sánchez García"

def suma(x,y) :
    r = x + y
    return r

def resta(x,y) :
    r = x - y
    return r

def multiplica(x,y) :
    r= x * y
    return r

def divide(x,y) :
    r= x / y
    return r

# Función que crea el menú de la aplicacion.

def menuApp() :
    print("MENU CALCULADORA")
    opcion =-1

    while opcion !=0 :
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion=int(input("Introduzca opción: "))

        if opcion == 1 :
            s1=int(input("Introduzca el primer sumando: "))
            s2=int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1,s2,suma(s1,s2)))
        elif opcion == 2 :
            minuendo=int(input("Introduzca el minuendo: "))
            sustraendo=int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo,sustraendo,resta(minuendo,sustraendo)))
        elif opcion == 3 :
            m1=int(input("Introduzca el primer numero: "))
            m2=int(input("Introduzca por el que se multiplica: "))
            print("La multiplicacion de {0} x {1} = {2}.".format(m1,m2,multiplica(m1,m2)))
        elif opcion == 4 :
            d1=int(input("Introduzca el primer numero: "))
            d2=int(input("Introduzca el divisor: "))
            print("La division de {0} + {1} = {2}.".format(d1,d2,divide(d1,d2)))
        elif opcion == 0 :
            print("Saliendo")
            return 0

        elif opcion !=0 :
            print("Error: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()
