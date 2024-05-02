from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division
from potencia import potencia
from modulo import modulo

def juego():
    puntuacion = 0
    while True:
        print('----- Menu -----'
              '\n1. Suma'
              '\n2. Resta'
              '\n3. Multiplicacion'
              '\n4. Division'
              '\n5. Potencia'
              '\n6. Modulo'
              '\n7. Salir')
        opcion = int(input('Digite la operacion que desee '))

        if opcion == 7:
            print('Termino el juego'
                  f'\nSu puntuacion fue {puntuacion}')
            break

        num1 = int(input('Digite el primer numero '))
        num2 = int(input('Digite el segundo numero '))
        resultado = int(input('Digite el resultado de la operacion '))

        if opcion == 1:
            resultadoReal = suma(num1,num2)
            if resultado == resultadoReal:
                puntuacion += 1
                print('Su resultado es correcto')
            else:
                print('Su resultado es incorrecto')
        elif opcion == 2:
            resultadoReal = resta(num1,num2)
            if resultado == resultadoReal:
                puntuacion += 1
                print('Su resultado es correcto')
            else:
                print('Su resultado es incorrecto')
        elif opcion == 3:
            resultadoReal = multiplicacion(num1,num2)
            if resultado == resultadoReal:
                puntuacion += 2
                print('Su resultado es correcto')
            else:
                print('Su resultado es incorrecto')
        elif opcion == 4:
            resultadoReal = division(num1,num2)
            if resultado == resultadoReal:
                puntuacion += 2
                print('Su resultado es correcto')
            else:
                print('Su resultado es incorrecto')
        elif opcion == 5:
            resultadoReal = potencia(num1,num2)
            if resultado == resultadoReal:
                puntuacion += 4
                print('Su resultado es correcto')
            else:
                print('Su resultado es incorrecto')
        elif opcion == 6:
            resultadoReal = modulo(num1,num2)
            if resultado == resultadoReal:
                puntuacion += 4
                print('Su resultado es correcto')
            else:
                print('Su resultado es incorrecto')

juego()
