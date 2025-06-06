
print("Ejercicios de variables y operaciones básicas")
print("1. Intercambio de valores sin variable auxiliar")
print("2. Suma de cuadrados de dos números")
print("3. Conversión de tipos de datos")
print("4. Redondeo y formato de un número")
print("5. Concatenación de variables en un mensaje")
print("6. Cálculo de edad actual")
print("7. Cuenta regresiva con una sola variable")
print("8. Valor absoluto sin usar abs()")
print("9. Incremento/decremento según paridad")
print("10. Máximo entre tres números sin usar max()")

opcion = int(input("Elige un ejercicio (1-10): "))
def ejercicio_variables(opcion):
    match opcion:
        case 1:
            a = 5
            b = 3
            print(f"Antes: a = {a}, b = {b}")
            a, b = b, a
            print(f"Después: a = {a}, b = {b}")

        case 2:
            a = 5
            b = 3
            c = a**2 + b**2
            print(f"a² + b² = {c}")

        case 3:
            numero = 7
            como_string = str(numero)
            como_float = float(como_string)
            como_int = int(como_float)
            print(f"Original: {numero}, como string: {como_string}, como float: {como_float}, de nuevo int: {como_int}")

        case 4:
            numero = 17.8567
            redondeado = round(numero, 2)
            mensaje = f"Resultado: {str(redondeado)}"
            print(mensaje)

        case 5:
            nombre = "Juan"
            edad = 25
            mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
            print(mensaje)

        case 6:
            anio_actual = 2025
            anio_nacimiento = 2000
            edad = anio_actual - anio_nacimiento
            print(f"Tienes {edad} años.")

        case 7:
            i = 10
            while i >= 0:
                print(i)
                i -= 1

        case 8:
            numero = -15
            valor_absoluto = numero if numero >= 0 else -numero
            print(f"Valor absoluto de {numero} es {valor_absoluto}")

        case 9:
            n = 6
            if n % 2 == 0:
                n += 1
            else:
                n -= 1
            print(f"Nuevo valor de n: {n}")

        case 10:
            a = 4
            b = 9
            c = 2
            if a >= b and a >= c:
                mayor = a
            elif b >= a and b >= c:
                mayor = b
            else:
                mayor = c
            print(f"El mayor es: {mayor}")

        case _:
            print("Opción no válida. Elige un número del 1 al 10.")

print(f"Ejercicio seleccionado: {opcion}")
ejercicio_variables(opcion)