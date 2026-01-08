import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('Final.xlsx')

# Abrir archivo de salida
with open('dependencias2.txt', 'w', encoding='utf-8') as f:
    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        groupId = row['Paquete (groupId)']
        artifactId = row['Subpaquete (artifactId)']
        version = row['Versión']
        tipo = row['Tipo']
        
        # Escribir el formato XML de dependencia
        f.write('<dependency>\n')
        f.write(f'    <groupId>{groupId}</groupId>\n')
        f.write(f'    <artifactId>{artifactId}</artifactId>\n')
        f.write(f'    <version>{version}</version>\n')
        f.write(f'    <type>{tipo}</type>\n')
        f.write('</dependency>\n\n')

print("Archivo 'dependencias.txt' generado exitosamente!")
