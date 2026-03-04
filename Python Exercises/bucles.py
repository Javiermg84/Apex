
numero_tabla_de_multiplicar = int(input("Ingrese el número para la tabla de multiplicar: "))

#Validacion de que el número ingresado es un entero y es mayor a 0
if numero_tabla_de_multiplicar < 1:
    print("Por favor, ingrese un número entero mayor a 0.")
else:
    print(f"Tabla de multiplicar del {numero_tabla_de_multiplicar}:")
    for tabla_numero in range(1, 11):
        resultado = numero_tabla_de_multiplicar * tabla_numero
        print(f"{numero_tabla_de_multiplicar} x {tabla_numero} = {resultado}")

    