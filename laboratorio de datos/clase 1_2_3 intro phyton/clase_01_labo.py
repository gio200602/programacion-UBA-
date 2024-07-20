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
"""
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', 
o 'pu' según corresponda luego de cada vocal.
"""

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        capadepenapa = capadepenapa + c + 'p' + c
    else:
        capadepenapa = capadepenapa + c


#version para cualquier palabra
def geringoso(palabra):
    palabra_geringoso = ''
    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            palabra_geringoso = palabra_geringoso + letra + 'p' + letra
        else:
            palabra_geringoso = palabra_geringoso + letra
    print(palabra_geringoso)
    return palabra_geringoso
#%%
"""
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 
de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla 
mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes
"""
altura = 100
for i in range(0,10):
    altura = altura * 3/5
    print(altura)

#version cualquier altura para la pelota
def rebote_pelota(pelota):
    for i in range(0,10):
        pelota = pelota * 3/5
        print(pelota)
#%%
"""
El siguiente es un programa que calcula el monto total que pagará David a lo 
largo de los años:
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
print('Total pagado', round(total_pagado, 2))
#%%
"""
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado 
junto con la cantidad de meses requeridos.
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000
mes = 0
total_pagado = 0.0
while saldo > 0:
    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
print('Total pagado', round(total_pagado, 2))
print('cantidad de meses',mes)
#%%
# programa para otros casos
# precondicion prestamo > 0, 0 < tasa < 1, 0 < pago_mensual,  pago_extra < prestamo, 0 < meses_adelanto 
# pago_prestamo(500000.0,0.05,2684.11,1000,61,108) lo que pide el ejercicio
def pago_prestamo(prestamo,tasa,pago_mensual,pago_extra,
pago_extra_inicio_mes,pago_extra_fin_mes):
    mes = 0
    total_pagado = 0.0
    while prestamo > 0:
        if mes > pago_extra_inicio_mes and mes < pago_extra_fin_mes :
            prestamo = prestamo * (1+tasa/12) - pago_mensual - pago_extra
            total_pagado = total_pagado + pago_mensual + pago_extra
        else:
            prestamo = prestamo * (1+tasa/12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
        mes = mes + 1
    #modifico para pagar lo justo y necesario
    total_pagado = total_pagado + prestamo
    print('Total pagado', round(total_pagado, 2))
    print('cantidad de meses',mes)
#%%
    
