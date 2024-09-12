"""
    Importación de librerias
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors  # Importar el módulo de colores
import seaborn as sns
import numpy as np
from bokeh.plotting import figure, show, output_file
#import sklearn


# Cargar el archivo CSV en un DataFrame
df_original = pd.read_csv('./SetDatos/Datos_MineriaDatos.csv', encoding='latin1') #Debido a el formato en que esta la información se hace la busqueda del encodificador correcto del set de datos

# Realiza una copia exacta del DataFrame original sacado del Set de Datos
df_modificable = df_original.copy()

"""
    1. Integración de los datos
    Para este proceso la información ya venia enlazada con una sola base de datos a la cual llamaremos desde ahora Set de Datos, el cual es un SET de datos de Salud Mental Atendidos en diferentes puntos de una entidad medica IPS en PERU

    Author: Victor Guevara
    Referencia del repositorio: https://github.com/VictorGuevaraP/Mineria-de-datos/blob/master/DAT%20SALUD%20MENTAL%20-%20ATENDIDOS.csv
"""

"""
    Eliminar variables redundantes
    -   En este paso no se realiza eliminación de datos redundantes, ya que esta trae información limpia y sin redundar en la información puesto que todas son informaciones de diferentes procesos que se realizarón dentro de la inscripción de los pacientes como de su proceso en la entidad IPS en su debida ubicación
    Para este proceso la información ya venia enlazada con una sola base de datos a la cual llamaremos desde ahora Set de Datos, el cual es un SET de datos de Salud Mental Atendidos en diferentes puntos de una entidad medica IPS
"""
#Encapsulamos en listas diferentes cada una de las variables que son en formato de texto y los transformamos a un valor unico por cada valor unico encontrado, Ejemplo Departamento cuando se tenga el Valor ANCASH pertenecera al valor 1

# Obtener los valores únicos de la columna 'Departamento'
departamentos_unicos = df_original['Departamento'].unique()
# Crear un diccionario asignando un valor único (por ejemplo, un número) a cada departamento
json_departamento_valor_unico = {departamento: idx for idx, departamento in enumerate(departamentos_unicos, start=1)}

provincias_unicos = df_original['Provincia'].unique()
json_provincias_valor_unico = {provincias: idx for idx, provincias in enumerate(provincias_unicos, start=1)}

sexos_unicos = df_original['Sexo'].unique()
json_sexos_valor_unico = {sexo: idx for idx, sexo in enumerate(sexos_unicos, start=1)}

Etapas_unicos = df_original['Etapa'].unique()
json_Etapas_valor_unico = {Etapa: idx for idx, Etapa in enumerate(Etapas_unicos, start=1)}

Diagnosticos_unicos = df_original['Diagnostico'].unique()
json_Diagnosticos_valor_unico = {Diagnostico: idx for idx, Diagnostico in enumerate(Diagnosticos_unicos, start=1)}


"""
    Quedan los siguientes sets de datos con los nombres de cada una de las variables que requiramos evaluar o mostrar luego en algun tipo de diagrama

    Mapa/Json de Departamentos: json_departamento_valor_unico
    Mapa/Json de Provincias: json_provincias_valor_unico
    Mapa/Json de Sexos: json_sexos_valor_unico
    Mapa/Json de Etapas: json_Etapas_valor_unico    
    Mapa/Json de Diagnosticos: json_Diagnosticos_valor_unico
"""
# Modificar los valores en 'Departamento' usando el diccionario 'departamento_valor_unico'
df_modificable['Departamento'] = df_modificable['Departamento'].map(json_departamento_valor_unico)
df_modificable['Provincia'] = df_modificable['Provincia'].map(json_provincias_valor_unico)
df_modificable['Sexo'] = df_modificable['Sexo'].map(json_sexos_valor_unico)
df_modificable['Etapa'] = df_modificable['Etapa'].map(json_Etapas_valor_unico)
df_modificable['Diagnostico'] = df_modificable['Diagnostico'].map(json_Diagnosticos_valor_unico)


etapas_valor_texto = {v: k for k, v in json_Etapas_valor_unico.items()}

# Reemplazar los valores numéricos en la columna 'Etapa' con sus equivalentes en texto
df_modificable['Etapa_Texto'] = df_modificable['Etapa'].map(etapas_valor_texto)


# Resumen estadístico de la columna 'Atendidos'
#resumen_estadistico = df_modificable['Atendidos'].describe()
#print(resumen_estadistico)

# Calcular estadísticas de la columna 'Atendidos'
#media = df_modificable['Atendidos'].mean()  # Media
#mediana = df_modificable['Atendidos'].median()  # Mediana
#moda = df_modificable['Atendidos'].mode()[0]  # Moda
#desviacion_estandar = df_modificable['Atendidos'].std()  # Desviación estándar
#varianza = df_modificable['Atendidos'].var()  # Varianza
#maximo = df_modificable['Atendidos'].max()  # Máximo valor
#minimo = df_modificable['Atendidos'].min()  # Mínimo valor
#rango = maximo - minimo  # Rango

# Mostrar resultados
#print("Media:", media)
#print("Mediana:", mediana)
#print("Moda:", moda)
#print("Desviación Estándar:", desviacion_estandar)
#print("Varianza:", varianza)
#print("Máximo:", maximo)
#print("Mínimo:", minimo)
#print("Rango:", rango)

"""
3. Descripción estadística de los datos

Se realiza el analisis de la información utilizando histograma en este caso para evaluar la variable de Etapa
Se realiza el analisis de atendidos por departamentos
"""
# Crear un histograma donde X sea la variable 'Etapa_Texto'
plt.figure(figsize=(10, 6))
sns.histplot(df_modificable['Etapa_Texto'], bins=len(json_Etapas_valor_unico), color='skyblue', edgecolor='black')

# Ajustar el título y etiquetas
plt.title('Histograma de frecuencia por Etapas de Edad')
plt.xlabel('Etapas de Edad')
plt.ylabel('Frecuencia')

# Rotar las etiquetas en X para mejor visualización
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Agrupar por Provincia y sumar los atendidos
grouped_data = df_modificable.groupby('Departamento')['Atendidos'].sum()

# Crear gráfico de torta
fig, ax = plt.subplots(figsize=(10, 6))

# Colores para el gráfico
colors = plt.cm.Paired.colors

# Graficar la torta y mostrar los números de los Departamentos
departamentos = df_modificable['Departamento'].unique()  # Números de departamento para las etiquetas
wedges, texts = ax.pie(grouped_data, labels=departamentos, startangle=90, colors=colors)

# Crear la tabla de resumen con el porcentaje y el color
# Obtener los colores en formato hexadecimal (usamos get_facecolor() y convertimos correctamente)
colors_hex = [mcolors.rgb2hex(wedge.get_facecolor()[:3]) for wedge in wedges]  # Tomamos los primeros 3 valores (RGB)

# Crear la información de la tabla (excepto los colores, que se pintarán)
table_data = [[f'{Departamento}', f'{atendido}'] for Departamento, atendido in zip(grouped_data.index, grouped_data)]

# Agregar tabla a la gráfica
tabla = ax.table(cellText=table_data, colLabels=["Departamento", "Atendidos"], loc="right", colColours=['#f5f5f5']*2, cellLoc='center')

# Pintar las celdas de la columna de colores
for i, color in enumerate(colors_hex):
    tabla.add_cell(i+1, 2, width=0.1, height=0.05, facecolor=color)  # Agregar celda pintada con el color respectivo

# Agregar la columna de título "Color"
tabla.add_cell(0, 2, width=0.1, height=0.05, text="Color", loc='center', facecolor='#f5f5f5')

# Ajustar la posición del gráfico para que la tabla no se superponga
plt.subplots_adjust(left=0.1, right=0.7)

plt.title('Cantidad de Pacientes Atendidos por Departamento')
plt.show()

"""
    2. Eliminar variables irrelevantes y redundantes

    Eliminar variables irrelevantes para la minería
    -   Eliminamos el Distrito por que ya es un dato muy especifico de una localidad exacta dentro de la información, y esta se puede generalizar por cada una de las provincias de la misma
    -   Eliminamos el Anio debido a que este no representa variación segun la base de datos, por lo que nos generara en la correlación de información un valor NaN debido a la variación del mismo
    
"""
df_modificable = df_modificable.drop(columns=['Distrito'])
df_modificable = df_modificable.drop(columns=['Anio'])
df_modificable = df_modificable.drop(columns=['ubigeo'])
df_modificable = df_modificable.drop(columns=['Provincia'])
df_modificable = df_modificable.drop(columns=['Sexo'])


"""
 4. Limpieza de la información
    Se hace la busqueda de datos que se encuentren nulos o esten vacias dentro de todas las columnas y se trae el index de la respectiva columna y el campo que hace falta
    En este caso el propio proyecto nos indica que no se encontraron informaciones con valores nan , null o cadenas vacias
"""
# Buscar valores nulos
nulos = df_modificable.isna()

# Usar apply para aplicar una función map a cada columna y detectar cadenas vacías
vacios = df_modificable.apply(lambda col: col.map(lambda x: isinstance(x, str) and x.strip() == ''))

# Crear un nuevo DataFrame combinando nulos y vacíos
nulos_o_vacios = nulos | vacios

# Filtrar filas donde haya al menos un valor nulo o vacío
df_nulos_vacios = df_modificable[nulos_o_vacios.any(axis=1)]

# Mostrar el DataFrame con los valores nulos o vacíos
#print(df_nulos_vacios)

"""
    6. Analisis de Correlación entre las variables

    Se realiza el analisis de las variables referentes a las variables analisadas en la parte de estadistica descriptiva
"""

#Eliminamos las variables que utilizamos para los graficos
df_modificable = df_modificable.drop(columns=['Etapa_Texto'])

# Calcular la matriz de correlación
correlacion = df_modificable.corr()

# Mostrar la matriz de correlación
print(correlacion)
"""

    Metodo del codo para definir la cantidad de cluster en mi algoritmo de predicción
    Atraves del algoritmo de Kmeans y atraves de su propiedad de inercia .inertia_ ( calculo de error )
    se grafica de manera lineal y de puntos

    El numero de cluster es donde la linea empiece a tomar una linea recta ( se suaviza una curva )

    Los centroides son la cantidad de variables a evaluar

    La reduccion de la dimencionalidad a los datos esto con
    sklearn.decomposition importado de PCA
"""