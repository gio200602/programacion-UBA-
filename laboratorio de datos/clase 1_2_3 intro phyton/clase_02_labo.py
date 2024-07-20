"""
Definir una función maximo(a,b) que tome dos parámetros numéricos y devuelva el máximo
"""
def maximo(a,b) :
    if a < b :
        mayor = b
    else :
        mayor = a
    return mayor
#%%
"""
Definir una función dos_pertenece(lista) que tome una lista y devuelva True si 
la lista tiene al 2 y False en caso contrario.
"""
def dos_pertenece (lista):
    esta = False
    for i in lista :
        if i==2 :
            esta = True
            return esta
    return esta
"""
Definir una función pertenece(lista, elem) que tome una lista y un elemento y 
devuelva True si la lista tiene al elemento dado y False en caso contrario.
"""
#version 1
def pertenece_a_lista (lista,elem):
    for i in lista:
        if i == elem:
            return True
    return False

#version 2    
def pertenece_lista_2 (lista,elem):
    estat = True
    if elem not in lista:
        estat = False
    return estat
#%%
"""
Definir una función es_par(n) que devuelva True si el número es par y False en 
caso contrario.
"""
def es_par (n):
    if n % 2 == 0 :
        es = True
    else :
        es = False
    return es

#%%
"""
Definir una función mas_larga(lista1, lista2) que tome dos listas y devuelva la más larga.
"""
def mas_larga (lista1,lista2):
    if len(lista1) >= len (lista2) :
        return lista1
    else :
        return lista2
#%%
"""
Definir una función tachar_pares(lista) que tome una lista de números y 
devuelva una similar pero donde los números pares estén reemplazados por ‘x’
"""
def tachar_pares(listanum):
    
    for i in range (0,len(listanum)):
        if listanum[i] % 2 == 0 :
            listanum[i] = "x"
    return listanum
#%%
"""
Definir una función cant_e que tome una lista y devuelva la cantidad de letras ‘e’ que tiene.
"""
def cant_e (listax) :
    contador = 0
    for i in range (0,len(listax)):
        if listax[i] == "e" :
            contador = contador + 1
    return contador
#%%
"""
Definir una función sumar_unos que tome una lista, les sume 1 a todos sus 
elementos, y devuelva la lista modificada.
"""
def sumar_unos (listanum2) :
    for i in range (0,len(listanum2)) :
        listanum2[i]=listanum2[i] + 1
    return listanum2
#%%
"""
Definir la función mezclar(cadena1, cadena2) que tome dos strings y devuelva el resultado de 
intercalar elemento a elemento. Por ejemplo: si intercalamos Pepe con Jose darı́a PJeopsee
"""
def mezclar (cadena1,cadena2) :
    nuevacad = ' '
    for i in range (0,max(len(cadena1),len(cadena2))):
        if i < len(cadena1) and i < len(cadena2) :
            nuevacad = nuevacad + cadena1[i] + cadena2[i]
        elif i < len(cadena1) and i >= len(cadena2) :
            nuevacad = nuevacad + cadena1[i]
        else:
            nuevacad = nuevacad + cadena2[i]
    return nuevacad
#%%
#version 2 de geringoso 
def geringoso(list) :
    capa = ' '
    for c in list :
        capa = capa + c
        if c in 'aeiou' :
            capa = capa + 'p' + c
    return capa

#creo diccionario vacio y voy actualizando por cada palabra
def traductor_geringoso(listapal) :
    listraducida = {}
    for i in listapal:
        palabra_geringoso = geringoso(i)
        listraducida.update({i:palabra_geringoso})
    return listraducida
#%%
import random
x=2
#random hasta ese numero
random.seed(x)
prueba = random.random()
print(prueba)
prueba = random.random()
print(prueba)
prueba = random.random()
print(prueba)
#%%
"""
Escribir una función generala_tirar() que simule una tirada de dados para el juego de la generala. Es 
decir, debe devolver una lista aleatoria de 5 valores de dados. Por ejemplo [2,3,2,1,6].
"""
def generala_tirar():
    lista_generala = []
    for i in range (5):
        lista_generala.append(random.randint(1, 6))
    return lista_generala
