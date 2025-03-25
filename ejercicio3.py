# coding=utf-8
__Author__="José Gaspar Sánchez García"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utilice la estructura de control if-elif-else.
- Impltemente una función obtenerCalificacion(nota)."""

# Implemente función obtenerCalificacion
def obtenerCalificaion(nota) :
    
    if(nota > 0 and nota < 3):
        calificacion="Muy deficiente"
    elif(nota >=3 and nota <5):
        calificacion="Insuficiente"
    elif(nota>=5 and nota <6):
        calificacion="Suficiente"
    elif(nota>=6 and nota <7):
        calificacion="Bien"
    elif(nota>=7 and nota <9):
        calificacion="Notable"
    elif(nota>=9 and nota <10):
        calificacion="Sobresaliente"
    else:
        calificacion="Incorrecta"
   # Implemente aquí ... Si (condición) entonces ... sino ... si (condición) entonces ... sino ...
    return calificacion

# Programa principal
def main():
    n=int(input("Introduzca la nota: "));
    print('Calificación: '+obtenerCalificaion(n));
if __name__== "__main__" :
   main()
