#Definiendo funciones

valor_numerico= int(input("Agrega un valor:"))
valor_numerico2= int(input("Agrega un valor:"))

def sumar(valor_numerico,valor_numerico2):
    agregar= valor_numerico + valor_numerico2
    return agregar
print(sumar(valor_numerico,valor_numerico2))

def resta(valor_numerico,valor_numerico2):
    quitar= valor_numerico - valor_numerico2
    return quitar
print(resta(valor_numerico,valor_numerico2))

def multiplicar(valor_numerico,valor_numerico2):
    multiplica= valor_numerico * valor_numerico2
    return multiplica
print(multiplicar(valor_numerico,valor_numerico2))

def residuo(valor_numerico,valor_numerico2):
    resto= valor_numerico // valor_numerico2
    return resto
print(residuo(valor_numerico,valor_numerico2))