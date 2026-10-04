

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\nEjercicio 1:")
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)
print(lista1)

lista1.insert(2,10)
print(lista1)

lista1[0] = 0 
print(lista1)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

print("\nEjercicio 2:")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
print(f"Unir ambas listas: {lista_a}")
lista_a.remove(1)
elemento_eliminado = lista_a.pop(3)
print(f"Elemento eliminado: {elemento_eliminado}")
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print("\nEjercicio 3:")
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista2[1:4]
print(f"Lista despues de eliminar dichos numeros: {lista2}")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print("\nEjercicio 4:")
lista3 = [5, 2, 8, 1, 9, 4, 2]
lista3.sort()
print(f"Lista ordenada: {lista3}")
print("Numero de veces que aparece el numero 2:", lista3.count(2))
print("¿Aparece el numero 7 en la lista? :", 7 in lista3)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

print("\nEjercicio 5:")
lista_original = [1, 2, 3]
copia_1 = lista_original[:]
copia_2 = copia_1.copy()
referencia = lista_original
referencia[0] = 10
print(f"Lista original: {lista_original}")
print(f"Copia 1 (slicing): {copia_1}")
print(f"Copia 2 (copy()): {copia_2}")
print(f"Referencia: {referencia}")


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print("\nEjercicio 6:")
frutas = ["Manzanas", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)
