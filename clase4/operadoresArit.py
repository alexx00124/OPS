# Número base
casa =int(input("ingrese un numero "))

# Pedimos al usuario que elija una operación
opcion = int(input("Elige una operación:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División entera\n6. Módulo\n7. Potencia\n\nIngresa el número de la operación: "))

match opcion:
    case 1:
        resultado = casa + 5
        print("Suma: 1 + 5 =", resultado)
    case 2:
        resultado = casa - 2
        print("Resta: 1 - 2 =", resultado)
    case 3:
        resultado = casa * 4
        print("Multiplicación: 1 * 4 =", resultado)
    case 4:
        resultado = casa / 2
        print("División: 1 / 2 =", resultado)
    case 5:
        resultado = casa // 2
        print("División entera: 1 // 2 =", resultado)
    case 6:
        resultado = casa % 2
        print("Módulo: 1 % 2 =", resultado)
    case 7:
        resultado = casa ** 3
        print("Potencia: 1 ** 3 =", resultado)
    case _:
        print("Opción no válida")
