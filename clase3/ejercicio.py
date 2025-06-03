# Ejercicio 1: Suma de dos números
def ejercicio1():
    print("=== Ejercicio 1: Suma de dos números ===")
    try:
        num1 = float(input("Dame el primer número: "))
        num2 = float(input("Dame el segundo número: "))
        print(f"El resultado de sumar {num1} + {num2} es: {num1 + num2}")
    except ValueError:
        print("Por favor, ingresa números válidos.")

# Ejercicio 2: Conversión Celsius a Fahrenheit
def ejercicio2():
    print("\n=== Ejercicio 2: Celsius a Fahrenheit ===")
    try:
        c = float(input("Temperatura en Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C equivalen a {f}°F")
    except ValueError:
        print("Ingresa un número válido para la temperatura.")

# Ejercicio 3: Cálculo del área de un triángulo
def ejercicio3():
    print("\n=== Ejercicio 3: Área del triángulo ===")
    try:
        base = float(input("Base del triángulo: "))
        altura = float(input("Altura del triángulo: "))
        area = 0.5 * base * altura
        print(f"Área calculada: {area}")
    except ValueError:
        print("Valores inválidos para base o altura.")

# Ejercicio 4: Número par o impar
def ejercicio4():
    print("\n=== Ejercicio 4: Par o impar ===")
    try:
        n = int(input("Ingresa un número entero: "))
        if n % 2 == 0:
            print(f"{n} es un número par.")
        else:
            print(f"{n} es un número impar.")
    except ValueError:
        print("Debes ingresar un número entero.")

# Ejercicio 5: Intercambio sin variable temporal
def ejercicio5():
    print("\n=== Ejercicio 5: Intercambiar valores ===")
    a = input("Valor inicial de a: ")
    b = input("Valor inicial de b: ")
    print(f"Antes: a = {a}, b = {b}")
    # Usamos suma y resta solo si son números, si no, usamos tuple unpacking
    try:
        a_num = float(a)
        b_num = float(b)
        a_num = a_num + b_num
        b_num = a_num - b_num
        a_num = a_num - b_num
        print(f"Después (con suma/resta): a = {a_num}, b = {b_num}")
    except ValueError:
        # Si no son números, intercambiamos con desempacado de tupla
        a, b = b, a
        print(f"Después (con desempacado): a = {a}, b = {b}")

# Ejercicio 6: Calculadora básica
def ejercicio6():
    print("\n=== Ejercicio 6: Calculadora simple ===")
    try:
        x = float(input("Número 1: "))
        y = float(input("Número 2: "))
        print(f"Suma: {x + y}")
        print(f"Resta: {x - y}")
        print(f"Multiplicación: {x * y}")
        if y != 0:
            print(f"División: {x / y}")
        else:
            print("No se puede dividir entre cero.")
    except ValueError:
        print("Entrada inválida.")

# Ejercicio 7: Edad en meses y días
def ejercicio7():
    print("\n=== Ejercicio 7: Edad en meses y días ===")
    try:
        edad_años = int(input("Edad en años: "))
        meses = edad_años * 12
        dias = edad_años * 365  # sin considerar años bisiestos
        print(f"Equivalente a {meses} meses y aproximadamente {dias} días.")
    except ValueError:
        print("Debes ingresar un número entero.")

# Ejercicio 8: Encontrar el mayor de tres números
def ejercicio8():
    print("\n=== Ejercicio 8: Número mayor ===")
    try:
        nums = [float(input(f"Número {i}: ")) for i in range(1, 4)]
        mayor = nums[0]
        for num in nums[1:]:
            if num > mayor:
                mayor = num
        print(f"El número mayor es {mayor}")
    except ValueError:
        print("Por favor, ingresa números válidos.")

# Ejercicio 9: Verificar múltiplo
def ejercicio9():
    print("\n=== Ejercicio 9: Múltiplo ===")
    try:
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))
        if n2 == 0:
            print("El segundo número no puede ser cero.")
            return
        if n1 % n2 == 0:
            print(f"{n1} es múltiplo de {n2}")
        else:
            print(f"{n1} no es múltiplo de {n2}")
    except ValueError:
        print("Por favor, introduce números enteros.")

# Ejercicio 10: Salario con bono
def ejercicio10():
    print("\n=== Ejercicio 10: Salario con bonificación ===")
    try:
        salario_base = float(input("Salario base: "))
        bono = salario_base * 0.10
        total = salario_base + bono
        print(f"Salario total con bono (10%): {total}")
    except ValueError:
        print("Introduce un valor numérico válido para el salario.")

# Función principal que ejecuta todos los ejercicios con pausa entre ellos
def main():
    ejercicios = [ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5,
                  ejercicio6, ejercicio7, ejercicio8, ejercicio9, ejercicio10]

    for i, ejercicio in enumerate(ejercicios, 1):
        ejercicio()
        if i != len(ejercicios):
            input("\nPresiona Enter para continuar al siguiente ejercicio...\n")

if __name__ == "__main__":
    main()
