def sumar(numero1, numero2):
    return numero1 + numero2

try:
    numero1 = int(input("Pon un valor numérico: "))
    numero2 = int(input("Pon otro valor numérico: "))
    resultado = sumar(numero1, numero2)
    print(f"La suma es: {resultado}")

    if resultado < 10:
        print("La suma es menor que 10.")
    elif resultado > 10:
        print("La suma es mayor que 10.")   

except ValueError:
    print("Por favor, ingresa solo números enteros.")
