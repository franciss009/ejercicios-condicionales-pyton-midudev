#Ejercicios de práctica
#Functions:

#ej 1
def saludar_a(nombre):
    print(f"Hola {nombre}")

saludar_a("Fran")
saludar_a("Frannnn")

#ej 2
def sumar(num1,num2):
    resultado = num1 + num2
    return resultado

print(sumar(4,2))

#ej 3
def es_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
    
print(es_positivo(7))
print(es_positivo(-3))


#ej 4
def calcular_doble(numero):
    resultado = numero * 2
    return resultado

print(calcular_doble(3))


#ej 5
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(es_par(4))


#ej 6
def contar_elementos(lista):
    return len(lista)

lista = ["carro","corre"]
print(contar_elementos(lista))

#ej 7
def sumar_lista(numeros):
    contador = 0

    for numero in numeros:
        contador += numero
        
    return contador

numeros = [10, 5, 20]
print(sumar_lista(numeros))

#ej 8
def contar_pares(numeros):
    contador = 0

    for numero in numeros:
        if numero % 2 == 0:
            contador += 1

    return contador

numeros = [1,2,3,4,5,6,7,8,9,99,94]
print(contar_pares(numeros))

