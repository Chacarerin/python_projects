import pandas as pd
import re

# Cargar el archivo de origen y el archivo de destino
df_origen = pd.read_excel('informe (24).xlsx')
df_destino = pd.read_excel('Declaracion Jurada B.xlsx')

# Copiar las columnas generales sin eliminar columnas en df_destino
df_destino['Fecha'] = df_origen['Fecha']                  # Fecha a Fecha
df_destino['Nro Factura'] = df_origen['Folio']            # Folio a Nro Factura
df_destino['Nombre Cliente'] = df_origen['Razon Social']  # Razón Social a Nombre Cliente
df_destino['RUT'] = df_origen['Rut']                      # Rut a RUT
df_destino['TOTAL FACTURA'] = df_origen['Total']          # Total a TOTAL FACTURA

# Mapeo de kilos y tipo a las columnas en el archivo de destino
kilos_tipo_column_map = {
    '5 normal': '5n',
    '11 normal': '11n',
    '15 normal': '15n',
    '45 normal': '45n',
    '5 catalitico': '5c',
    '11 catalitico': '11c',
    '15 catalitico': '15c',
    '45 catalitico': '45c',
}

# Iterar sobre cada fila del archivo de origen para obtener la cantidad y código
for index, row in df_origen.iterrows():
    # Obtener datos de la fila
    codigo = str(row['Codigo'])  # Convertir a cadena de texto por seguridad
    cantidad = row['Cant.']      # Obtener la cantidad de la columna Cant.
    producto = str(row['Producto'])  # Convertir a cadena de texto para búsqueda de palabras

    # Asignación de valores de kilos "normal" y "catalítico"
    for clave, columna_destino in kilos_tipo_column_map.items():
        if clave in codigo:
            # Verificar si la columna de destino existe en df_destino y asignar la cantidad
            if columna_destino in df_destino.columns:
                df_destino.at[index, columna_destino] = cantidad  # Asignar la cantidad
                print(f"Asignado {cantidad} a columna '{columna_destino}' en fila {index + 1}")
            else:
                print(f"Columna '{columna_destino}' no encontrada en el archivo de destino.")

    # Asignación de valores para "Aluminio" y "Fierro" en la columna Producto
    if "Aluminio" in producto:
        if 'Aluminio' in df_destino.columns:
            df_destino.at[index, 'Aluminio'] = cantidad  # Asigna la cantidad a la columna Aluminio
            print(f"Asignado {cantidad} a columna 'Aluminio' en fila {index + 1}")
        else:
            print("Columna 'Aluminio' no encontrada en el archivo de destino.")
    
    if "Fierro" in producto:
        if 'Fierro' in df_destino.columns:
            df_destino.at[index, 'Fierro'] = cantidad  # Asigna la cantidad a la columna Fierro
            print(f"Asignado {cantidad} a columna 'Fierro' en fila {index + 1}")
        else:
            print("Columna 'Fierro' no encontrada en el archivo de destino.")

# Guardar el archivo de destino actualizado con todas las columnas intactas
df_destino.to_excel('Declaracion_Jurada_Aba_actualizado.xlsx', index=False)