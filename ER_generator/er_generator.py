from eralchemy import render_er

schema = """
[productos] 
    *id: SERIAL
    formato_kilos: INT
    catalitico: BOOLEAN

[vendedores] 
    *id: SERIAL
    nombre: VARCHAR(100)
    meta_mensual: NUMERIC(10,2)

[precios] 
    *id: SERIAL
    producto_id: INT
    fecha: DATE
    precio: NUMERIC(10,2)

[ventas] 
    *id: SERIAL
    vendedor_id: INT
    producto_id: INT
    fecha: DATE
    cantidad: INT
    precio_unitario: NUMERIC(10,2)

[kilometraje] 
    *id: SERIAL
    vendedor_id: INT
    fecha: DATE
    km_inicial: INT
    km_final: INT

productos *--1 precios
productos *--1 ventas
vendedores *--1 ventas
vendedores *--1 kilometraje
"""

render_er(schema, 'er_diagram.png')