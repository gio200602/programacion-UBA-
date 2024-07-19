# -*- coding: utf-8 -*-
"""
Escribir un programa que decida si una palabra (longitud 5) es palíndromo
"""

def es_palindromo(palabra):
    palindromo = ''
    for i in range(5):
        palindromo = palindromo + palabra[4-i]
        
    if palabra == palindromo:
        print('son palindromos')
        return True
    else:
        print('no son palindromos')
        return False

# version para cualquier palabra
def es_palindromo_todos(palabra):
    tamaño = len(palabra)
    palindromo = ''
    for i in range(tamaño):
        palindromo = palindromo + palabra[tamaño-1-i]
        
    if palabra == palindromo:
        print('son palindromos')
        return True
    else:
        print('no son palindromos')
        return False
#%%
"""
Escribir un programa que imprima en pantalla los números enteros entre 0 y 
213 que sean divisibles por 13.
"""
print(1)
for i in range(0,213,13):
    print(i)
#%%

"""
Una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir de ahí, 
cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. 
¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el obelisco?
Datos: espesor del billete: 0.11 mm, altura obelisco: 67.5 m.
"""
def pila_de_billetes(espesor,altura):
    billetes = espesor/1000 #pasa a metros
    dias = 1
    while billetes < altura :
        billetes = billetes*2
        dias=dias+1
        
    return dias

print(pila_de_billetes(0.11, 67.5))
#%%


