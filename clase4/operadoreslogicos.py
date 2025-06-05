print("EJERCICIOS CON OPERADORES LÓGICOS")
print("1. AND: ¿Puede conducir?")
print("2. OR: ¿Puede entrar al cine?")
print("3. NOT: ¿Tiene acceso restringido?")

opcion = int(input("Elige una opción (1-3): "))

match opcion:
    case 1:
        edad = int(input("Ingresa tu edad: "))
        tiene_licencia = input("¿Tienes licencia? (sí/no): ") == "sí"
        puede_conducir = edad >= 18 and tiene_licencia
        print("¿Puede conducir?:", puede_conducir)

    case 2:
        tiene_entrada = input("¿Tienes entrada? (sí/no): ")== "sí"
        es_personal = input("¿Eres parte del personal? (sí/no): ")== "sí"
        puede_entrar = tiene_entrada or es_personal
        print("¿Puede entrar al cine?:", puede_entrar)

    case 3:
        es_admin = input("¿Eres administrador? (sí/no): ")== "sí"
        acceso_restringido = not es_admin
        print("¿Acceso restringido?:", acceso_restringido)

    case _:
        print("Opción no válida")
