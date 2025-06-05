print("Ejercicios practicos")
print("1.Escribe una expresión que devuelva True si x es mayor que 10 y menor que 20")
print("2.Escribe una condición que devuelva True si a es igual a b o c es mayor que 100")
print("3.¿Qué devuelve esta expresión y por qué? \n True or False and False")
print("4.Reescribe la siguiente expresión usando operadores relacionales y lógicos not (a < b or b < c)")
print("5.Dado x = 10, y = 20, escribe una condición que devuelva True solo si x y y son diferentes y al menos uno de los dos es mayor que 15")
print("6.Evalúa el resultado de: \n(10 != 5) and (4 == 4) or (2 > 3)")
print("7.Dado el siguiente código, ¿cuál es el valor de resultado? \na = True\nb = False \n resultado = a ^ b")
print("8.¿Qué devuelve esta expresión en Python y por qué? \n(3 > 2) and (2 > 1) ^ False")
print("9. Escribe un programa que reciba dos números y diga si exactamente uno de ellos es positivo (usa xorpara resolverlo)")

opcion = int(input("Elige una opción (1-9): "))

match opcion:
    case 1:
        x = int(input("Ingresa un número: "))
        resultado = x > 10 and x < 20
        print("¿x es mayor que 10 y menor que 20?:", resultado)
    case 2:
        a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        c = int(input("Ingresa el valor de c: "))
        resultado = a == b or c > 100
        print("¿a es igual a b o c es mayor que 100?:", resultado)
    case 3:
        resultado = True or False and False
        print("Resultado de 'True or False and False':", resultado)
    case 4:
        a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        c = int(input("Ingresa el valor de c: "))
        resultado = not (a < b or b < c)
        print("Resultado de 'not (a < b or b < c)':", resultado)
    case 5:
        x = int(input("Ingresa el valor de x: "))
        y = int(input("Ingresa el valor de y: "))
        resultado = (x != y) and (x > 15 or y > 15)
        print("¿x y y son diferentes y al menos uno es mayor que 15?:", resultado)
    case 6:
        resultado = (10 != 5) and (4 == 4) or (2 > 3)
        print("Resultado de '(10 != 5) and (4 == 4) or (2 > 3)':", resultado)
    case 7:
        a = True
        b = False
        resultado = a ^ b  # XOR operation
        print("Valor de resultado (a ^ b):", resultado)
    case 8:
        resultado = (3 > 2) and (2 > 1) ^ False
        print("Resultado de '(3 > 2) and (2 > 1) ^ False':", resultado)
    case 9:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = (num1 > 0) ^ (num2 > 0)  # XOR operation
        print("¿Exactamente uno de los números es positivo?:", resultado)
    case _:
        print("Opción no válida")
print("Fin de los ejercicios prácticos")

