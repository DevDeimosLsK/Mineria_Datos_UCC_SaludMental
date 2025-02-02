"""
    Importación de librerias
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import numpy as np
from bokeh.plotting import figure, show, output_file

"""
    1. Integración de los datos
    Para este proceso la información ya venia enlazada con una sola base de datos a la cual llamaremos desde ahora Set de Datos, el cual es un SET de datos de Salud Mental Atendidos en diferentes puntos de una entidad medica IPS en PERU

    Author: Victor Guevara
    Referencia del repositorio: https://github.com/VictorGuevaraP/Mineria-de-datos/blob/master/DAT%20SALUD%20MENTAL%20-%20ATENDIDOS.csv
"""

# Cargar el archivo CSV en un DataFrame
df_original = pd.read_csv('./SetDatos/Datos_MineriaDatos.csv', encoding='latin1') #Debido a el formato en que esta la información se hace la busqueda del encodificador correcto del set de datos

df_modificable = df_original.copy()


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

print("#################### Mapa de Departamentos")
print(json_departamento_valor_unico)
print("#################### Mapa de Provincias")
print(json_provincias_valor_unico)
print("#################### Mapa de Sexos")
print(json_sexos_valor_unico)
print("#################### Mapa de Etapas")
print(json_Etapas_valor_unico)
print("#################### Mapa de Diagnosticos")
print(json_Diagnosticos_valor_unico)


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

## FRECUENCIA DE LA CANTIDAD DE PERSONAS INDEPENDIENTEMENTE DEL DIAGNOSTICOS QUE VAN POR SALUD MENTAL 

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

## DIAGRAMAS DE BARRAS CON CANTIDAD DE PERSONAS FILTRADOS POR DEPARTAMENTO Y SEGUN ESTO CUANTAS PERSONAS HAN SIDO ATENDIDOS

# Agrupar por Provincia y sumar los atendidos
grouped_data = df_modificable.groupby('Departamento')['Atendidos'].sum()

fig, ax = plt.subplots(figsize=(10, 6))
colors = plt.cm.Paired.colors

departamentos = df_modificable['Departamento'].unique() 
wedges, texts = ax.pie(grouped_data, labels=departamentos, startangle=90, colors=colors)

colors_hex = [mcolors.rgb2hex(wedge.get_facecolor()[:3]) for wedge in wedges]
table_data = [[f'{Departamento}', f'{atendido}'] for Departamento, atendido in zip(grouped_data.index, grouped_data)]

tabla = ax.table(cellText=table_data, colLabels=["Departamento", "Atendidos"], loc="right", colColours=['#f5f5f5']*2, cellLoc='center')

for i, color in enumerate(colors_hex):
    tabla.add_cell(i+1, 2, width=0.1, height=0.05, facecolor=color)  # Agregar celda pintada con el color respectivo

tabla.add_cell(0, 2, width=0.1, height=0.05, text="Color", loc='center', facecolor='#f5f5f5')
plt.subplots_adjust(left=0.1, right=0.7)

plt.title('Cantidad de Pacientes Atendidos por Departamento')
plt.show()

## DIAGRAMAS DE BARRAS
## DIAGRAMA DE REPRESENTACION DE LOS DIAGNOSTICOS POR CADA UNA DE LAS ETAPAS
# Agrupar por Diagnostico y Etapa y contar la cantidad de personas
conteo_etapas = df_modificable.groupby(['Diagnostico', 'Etapa_Texto']).size().unstack().fillna(0)

# Crear el gráfico de barras
ax = conteo_etapas.plot(kind='bar', figsize=(12, 7), colormap='tab20')

plt.xlabel('Diagnóstico')
plt.ylabel('Cantidad de Personas')
plt.title('Cantidad de Personas por Etapa para Cada Diagnóstico')
plt.xticks(rotation=0)  # Asegúrate de que las etiquetas estén horizontales
plt.legend(title='Etapa', title_fontsize='13', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

df_modificable.hist()
plt.show()

sns.pairplot(df_modificable.dropna(), height=4,  # Reemplaza 'size' por 'height'
            vars=['Departamento', 'Atendidos', 'Atenciones'], kind='scatter')
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

nulos = df_modificable.isna()
vacios = df_modificable.apply(lambda col: col.map(lambda x: isinstance(x, str) and x.strip() == ''))
nulos_o_vacios = nulos | vacios
df_nulos_vacios = df_modificable[nulos_o_vacios.any(axis=1)]

# Mostrar el DataFrame con los valores nulos o vacíos
#print(df_nulos_vacios)

"""
    6. Analisis de Correlación entre las variables

    Se realiza el analisis de las variables referentes a las variables analisadas en la parte de estadistica descriptiva
"""
df_modificable = df_modificable.drop(columns=['Etapa_Texto'])

# Calcular la matriz de correlación
correlacion = df_modificable.corr()