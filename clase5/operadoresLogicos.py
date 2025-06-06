print("Ejercicios de operadores lógicos:")
print("21. ¿Puede votar?")
print("22. Control de acceso lógico")
print("23. Validación XOR")
print("24. Validación compuesta múltiple")
print("25. Condición contradictoria")
print("26. Negación lógica")
print("27. Aprobación de estudiante")
print("28. Simulación de alarma")
print("29. Contraseña segura")
print("30. Doble negación lógica")

opcion = int(input("Elige un ejercicio (21-30): "))
def ejercicios_python(opcion):
    match opcion:
        case 21:
            edad = 20
            tiene_documento = True
            puede_votar = edad >= 18 and tiene_documento
            print(f"¿Puede votar? {puede_votar}")

        case 22:
            tiene_pase_vip = False
            pago_entrada = True
            esta_ebrio = False
            puede_entrar = tiene_pase_vip or (pago_entrada and not esta_ebrio)
            print(f"¿Puede entrar? {puede_entrar}")

        case 23:
            cond1 = True
            cond2 = False
            xor = cond1 != cond2  # XOR lógico
            print(f"¿Exactamente una es verdadera? {xor}")

        case 24:
            n = 12
            valido = n > 0 and (n % 2 == 0 or n % 3 == 0)
            print(f"¿{n} es > 0 y múltiplo de 2 o 3? {valido}")

        case 25:
            x = 5
            contradictoria = x > 10 and x < 1
            print(f"¿x > 10 y x < 1? {contradictoria}")

        case 26:
            x = 8
            equivalente = not (x <= 10)  # igual que x > 10
            print(f"¿x > 10 usando not? {equivalente}")

        case 27:
            nota = 3.5
            asistencia = 85
            aprueba = nota >= 3.0 and asistencia >= 80
            print(f"¿El estudiante aprueba? {aprueba}")

        case 28:
            temperatura = 39
            humedad = 85
            alarma = (temperatura < 0 or temperatura > 38) and humedad > 80
            print(f"¿Se activa la alarma? {alarma}")

        case 29:
            contraseña = "python123"
            es_larga = len(contraseña) > 8
            tiene_numero = any(char.isdigit() for char in contraseña)
            es_segura = es_larga and tiene_numero
            print(f"¿La contraseña es segura? {es_segura}")

        case 30:
            tiene_acceso = True
            resultado = not (not tiene_acceso)
            print(f"No es falso que tiene acceso: {resultado}")

        case _:
            print("Opción no válida. Elige del 21 al 30.")

ejercicios_python(opcion)