"""
    Importación de librerias
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show, output_file


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
    2. Eliminar variables irrelevantes y redundantes

    Eliminar variables irrelevantes para la minería
    -   Eliminamos el Distrito por que ya es un dato muy especifico de una localidad exacta dentro de la información, y esta se puede generalizar por cada una de las provincias de la misma
"""
df_modificable = df_modificable.drop(columns=['Distrito'])
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

print(json_Etapas_valor_unico)
# Modificar los valores en 'Departamento' usando el diccionario 'departamento_valor_unico'
df_modificable['Departamento'] = df_modificable['Departamento'].map(json_departamento_valor_unico)
df_modificable['Provincia'] = df_modificable['Provincia'].map(json_provincias_valor_unico)
df_modificable['Sexo'] = df_modificable['Sexo'].map(json_sexos_valor_unico)
df_modificable['Etapa'] = df_modificable['Etapa'].map(json_Etapas_valor_unico)
df_modificable['Diagnostico'] = df_modificable['Diagnostico'].map(json_Diagnosticos_valor_unico)


etapas_valor_texto = {v: k for k, v in json_Etapas_valor_unico.items()}

# Reemplazar los valores numéricos en la columna 'Etapa' con sus equivalentes en texto
df_modificable['Etapa_Texto'] = df_modificable['Etapa'].map(etapas_valor_texto)

# Crear un histograma donde X sea la variable 'Etapa_Texto'
plt.figure(figsize=(10, 6))
sns.histplot(df_modificable['Etapa_Texto'], bins=len(json_Etapas_valor_unico), color='skyblue', edgecolor='black')

# Ajustar el título y etiquetas
plt.title('Histograma por Etapas de Edad')
plt.xlabel('Etapas de Edad')
plt.ylabel('Frecuencia')

# Rotar las etiquetas en X para mejor visualización
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()
plt.show()