import pandas as pd
import os
from inline_sql import sql, sql_val

casos = pd.read_csv('casos.csv')
departamento = pd.read_csv('departamento.csv')
grupo = pd.read_csv('grupoetario.csv')
provincia = pd.read_csv('provincia.csv')
evento = pd.read_csv('tipoevento.csv')

# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(sql^ consultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()


# =============================================================================
consigna    = """a. Listar sólo los nombres de todos los departamentos que hay en la tabla
departamento (dejando los registros repetidos)."""
    
consultaSQL = """
                    SELECT descripcion
                    FROM departamento;
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """b.Listar sólo los nombres de todos los departamentos que hay en la tabla
departamento (eliminando los registros repetidos)"""
    
consultaSQL = """
                    SELECT DISTINCT descripcion
                    FROM departamento;
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """c. Listar sólo los códigos de departamento y sus nombres de todos los
departamentos que hay en la tabla departamento"""
    
consultaSQL = """
                    SELECT id, descripcion
                    FROM departamento;
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """d. Listar todas las columnas de la tabla departamento."""
    
consultaSQL = """
                    SELECT *
                    FROM departamento;
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """e. Listar los códigos de departamento y nombres de todos los departamentos
que hay en la tabla departamento. Utilizar los siguientes alias para las
columnas: codigo_depto, nombre_depto"""
    
consultaSQL = """
                    SELECT id AS codigo_depto, descripcion AS nombre_depto
                    FROM departamento;
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """f. Listar los códigos de departamento y sus nombres, ordenados por sus
nombres de manera descendentes (de la Z a la A). En caso de empate,
desempatar por código de departamento de manera ascendente.
"""
    
consultaSQL = """
                    SELECT id,descripcion
                    FROM departamento
                    ORDER BY descripcion DESC,id ASC
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """g. Listar los registros de la tabla departamento cuyo código de provincia es
igual a 54
"""
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE id_provincia=54
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """h. Listar los registros de la tabla departamento cuyo código de provincia es
igual a 22, 78 u 86. """
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE id_provincia=22 OR id_provincia=78 OR id_provincia=86
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """i. Listar los registros de la tabla departamento cuyos códigos de provincia se
encuentren entre el 50 y el 59 (ambos valores inclusive)
"""
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE id_provincia>=50 AND id_provincia<=59
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """j. Listar los registros de la tabla provincia cuyos nombres comiencen con la
letra M. """
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE descripcion LIKE 'M%'
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """k. Listar los registros de la tabla provincia cuyos nombres comiencen con la
letra S y su quinta letra sea una letra A.
 """
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE descripcion LIKE 'S%' AND descripcion LIKE '____a%'
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """l. Listar los registros de la tabla provincia cuyos nombres terminan con la
letra A.
 """
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE descripcion LIKE '%a'
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """m. Listar los registros de la tabla provincia cuyos nombres tengan
exactamente 5 letras. """
    
consultaSQL = """
                    SELECT *
                    FROM departamento
                    WHERE descripcion LIKE '_____'
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """n. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
alguna parte de su nombre. """
    
consultaSQL = """
                    SELECT *
                    FROM provincia
                    WHERE descripcion LIKE '%do%'
                    
              """

imprimirEjercicio(consigna, [provincia], consultaSQL)
# =============================================================================
consigna    = """o. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
alguna parte de su nombre y su código sea menor a 30. """
    
consultaSQL = """
                    SELECT *
                    FROM provincia
                    WHERE descripcion LIKE '%do%' AND id<30
                    
              """

imprimirEjercicio(consigna, [provincia], consultaSQL)
# =============================================================================
consigna    = """p. Listar los registros de la tabla departamento cuyos nombres tengan ”san”
en alguna parte de su nombre. Listar sólo id y descripcion. Utilizar los
siguientes alias para las columnas: codigo_depto y nombre_depto,
respectivamente. El resultado debe estar ordenado por sus nombres de
manera descendentes (de la Z a la A). """
    
consultaSQL = """
                    SELECT id AS codigo_depto, descripcion AS nombre_depto
                    FROM departamento
                    WHERE nombre_depto LIKE '%San%'
                    ORDER BY nombre_depto DESC
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================

# B. Consultas multitabla (INNER JOIN)

# =============================================================================
consigna    = """a. Devolver una lista con los código y nombres de departamentos, asociados al
nombre de la provincia al que pertenecen."""
    
consultaSQL = """
                    SELECT d.id, d.descripcion AS nombre_depto , p.descripcion AS provincia_
                    FROM departamento AS d
                    INNER JOIN provincia AS p
                    ON d.id_provincia=p.id
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """b. Devolver una lista con los código y nombres de departamentos, asociados al
nombre de la provincia al que pertenecen. Ordenar el resultado por nombre
de provincia de manera ascendente, y dentro de cada una de ellas por
nombre de departamento, también de manera ascendente."""
    
consultaSQL = """
                    SELECT d.id, d.descripcion AS nombre_depto , p.descripcion AS provincia_
                    FROM departamento AS d
                    INNER JOIN provincia AS p
                    ON d.id_provincia=p.id
                    ORDER BY provincia_ , nombre_depto
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)

# =============================================================================
consigna    = """c. Devolver los casos registrados en la provincia de “Chaco”."""
    
consultaSQL = """
                    SELECT *
                    FROM departamento AS d
                    INNER JOIN provincia AS p
                    ON d.id_provincia=p.id
                    WHERE P.DESCRIPCION='Chaco'
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """d. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
cantidad supere los 10 casos."""
    
consultaSQL = """
    SELECT d.descripcion AS depto_descripcion,d.id_provincia,p.descripcion AS provincia_,
    c.id AS id_c,c.cantidad
    FROM departamento AS d
    INNER JOIN provincia AS p
    ON d.id_provincia=p.id
    INNER JOIN casos AS c
    ON d.id=c.id_depto
    WHERE provincia_='Buenos Aires' AND c.cantidad>10
                    
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """e. Devolver aquellos casos de las provincias cuyo nombre terminen con la letra
a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de
departamento, año, semana epidemiológica, descripción de grupo etario y
cantidad. Ordenar el resultado por la cantidad (descendente), luego por el
nombre de la provincia (ascendente), nombre del departamento
(ascendente), año (ascendente) y la descripción del grupo etario
(ascendente)."""
    
consultaSQL = """
        SELECT p.descripcion AS nombre_prov,d.descripcion AS nombre_depto,
        c.anio,c.semana_epidemiologica,gp.descripcion AS grupo_etario,c.cantidad
        FROM departamento AS d
        INNER JOIN provincia AS p
        ON d.id_provincia=p.id
        INNER JOIN casos AS c
        ON d.id=c.id_depto
        INNER JOIN grupo AS gp
        ON gp.id=c.id_grupoetario
        WHERE nombre_prov LIKE '%a' AND c.cantidad>10
        ORDER BY c.cantidad DESC, nombre_prov ASC, nombre_depto ASC, c.anio ASC, grupo_etario ASC
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)
# =============================================================================
consigna    = """f. Ídem anterior, pero devolver sólo aquellas tuplas que tienen el máximo en el
campo cantidad.
"""
    
consultaSQL = """
        SELECT p.descripcion AS nombre_prov,d.descripcion AS nombre_depto,
        c.anio,c.semana_epidemiologica,gp.descripcion AS grupo_etario,c.cantidad
        FROM departamento AS d
        INNER JOIN provincia AS p
        ON d.id_provincia=p.id
        INNER JOIN casos AS c
        ON d.id=c.id_depto
        INNER JOIN grupo AS gp
        ON gp.id=c.id_grupoetario
        WHERE nombre_prov LIKE '%a' AND c.cantidad= (SELECT MAX(c.cantidad) FROM casos)
        ORDER BY c.cantidad DESC, nombre_prov ASC, nombre_depto ASC, c.anio ASC, grupo_etario ASC
              """

imprimirEjercicio(consigna, [departamento], consultaSQL)

