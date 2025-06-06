print("Ejercicios de lógica y condiciones:")
print("11. Verificación de rango (10 a 100)")
print("12. Comparación de strings (ignorar mayúsculas)")
print("13. Igualdad entre tres variables")
print("14. Presencia en lista")
print("15. Divisibilidad por 3 y 5")
print("16. Números en orden estricto")
print("17. Comparación doble (valor entre dos límites)")
print("18. Relación proporcional (doble exacto)")
print("19. Cambio de signo si negativo")
print("20. Detección de tipo de dato")

opcion = int(input("Elige un ejercicio (1-20): "))
def python(opcion):
    match opcion:
        # ... ejercicios del 1 al 10 ya definidos arriba ...

        case 11:
            # Verificación de rango (10 a 100 inclusive)
            x = 55
            en_rango = 10 <= x <= 100
            print(f"¿{x} está entre 10 y 100? {en_rango}")

        case 12:
            # Comparación de strings (ignorar mayúsculas)
            a = "Python"
            b = "python"
            iguales = a.lower() == b.lower()
            print(f"¿'{a}' y '{b}' son iguales ignorando mayúsculas? {iguales}")

        case 13:
            # Igualdad entre tres variables
            a, b, c = 7, 7, 7
            iguales = a == b == c
            print(f"¿Las tres variables son iguales? {iguales}")

        case 14:
            # Presencia en lista
            lista = [2, 4, 6, 8, 10]
            x = 6
            encontrado = x in lista
            print(f"¿El número {x} está en la lista? {encontrado}")

        case 15:
            # Divisibilidad por 3 y 5
            n = 30
            divisible = n % 3 == 0 and n % 5 == 0
            print(f"¿{n} es divisible por 3 y 5? {divisible}")

        case 16:
            # Números en orden estricto
            a, b, c = 5, 10, 20
            en_orden = a < b < c
            print(f"¿Están en orden ascendente estricto? {en_orden}")

        case 17:
            # Comparación doble
            x = 15
            a = 10
            b = 20
            dentro = a < x < b
            print(f"¿{x} está estrictamente entre {a} y {b}? {dentro}")

        case 18:
            # Relación proporcional
            a = 40
            b = 20
            es_doble = a == 2 * b
            print(f"¿{a} es el doble de {b}? {es_doble}")

        case 19:
            # Cambio de signo si negativo
            x = -12
            if x < 0:
                x = -x
            print(f"Valor positivo: {x}")

        case 20:
            # Detección de tipo
            x = "hola"
            if isinstance(x, int):
                print("La variable es de tipo entero (int).")
            elif isinstance(x, float):
                print("La variable es de tipo flotante (float).")
            elif isinstance(x, str):
                print("La variable es de tipo cadena (str).")
            else:
                print("Tipo desconocido.")
        case _:
            print("Opción no válida")

python(opcion)