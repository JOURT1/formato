import pandas as pd

# Leer ambas hojas del archivo Excel
df_existentes = pd.read_excel('Dependencias Mobile.xlsx', sheet_name='Paquetes existentes')
df_nuevos = pd.read_excel('Dependencias Mobile.xlsx', sheet_name='Paquetes nuevos')

# Procesar Paquetes existentes
with open('dependencias_existentes.txt', 'w', encoding='utf-8') as f:
    # Iterar sobre cada fila del DataFrame
    for index, row in df_existentes.iterrows():
        groupId = row['Paquete (groupId)']
        artifactId = row['Subpaquete (artifactId)']
        version = row['Versión Requerida']
        tipo = row['Tipo']
        
        # Escribir el formato XML de dependencia
        f.write('<dependency>\n')
        f.write(f'    <groupId>{groupId}</groupId>\n')
        f.write(f'    <artifactId>{artifactId}</artifactId>\n')
        f.write(f'    <version>{version}</version>\n')
        f.write(f'    <type>{tipo}</type>\n')
        f.write('</dependency>\n\n')

print("Archivo 'dependencias_existentes.txt' generado exitosamente!")

# Procesar Paquetes nuevos
with open('dependencias_nuevos.txt', 'w', encoding='utf-8') as f:
    # Iterar sobre cada fila del DataFrame
    for index, row in df_nuevos.iterrows():
        groupId = row['Paquete (groupId)']
        artifactId = row['Subpaquete (artifactId)']
        version = row['Versión Requerida']
        tipo = row['Tipo']
        
        # Escribir el formato XML de dependencia
        f.write('<dependency>\n')
        f.write(f'    <groupId>{groupId}</groupId>\n')
        f.write(f'    <artifactId>{artifactId}</artifactId>\n')
        f.write(f'    <version>{version}</version>\n')
        f.write(f'    <type>{tipo}</type>\n')
        f.write('</dependency>\n\n')

print("Archivo 'dependencias_nuevos.txt' generado exitosamente!")
