# 🚀 Generador de Diagramas Entidad-Relación (ERAlchemy)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![ERAlchemy](https://img.shields.io/badge/ERAlchemy-Database%20Diagrams-orange?style=flat-square&logo=graphql&logoColor=white)](#)

Herramienta de automatización que genera diagramas Entidad-Relación (ER) a partir de una definición de esquema textual, produciendo una imagen `.png` lista para documentación técnica.

## 🧠 Contexto Pedagógico y Teórico
La visualización del esquema de base de datos es una práctica fundamental en el diseño de sistemas. Este script aborda el problema de la **documentación viva**: en lugar de dibujar manualmente un diagrama ER (que se desactualiza rápidamente), el esquema se define en código y el diagrama se regenera automáticamente. El esquema modelado representa un sistema de ventas con entidades para Productos, Vendedores, Precios, Ventas y Kilometraje, con sus respectivas cardinalidades.

## ⚙️ Tecnologías y Frameworks Aplicados
* **`ERAlchemy`**: Elegida por su capacidad de generar diagramas ER desde múltiples fuentes (texto plano, SQLAlchemy models, o conexión directa a una base de datos). Su uso aquí prioriza la **independencia de motor de base de datos**, ya que el schema se define en un DSL (Domain-Specific Language) propio, no en SQL nativo.

## 🛠️ Desglose Técnico (El "Cómo")
* **Schema DSL**: El esquema se define usando la sintaxis de ERAlchemy, especificando tablas con sus columnas (`*id` indica clave primaria) y relaciones entre ellas (`*--1` representa la cardinalidad N:1).
* **`render_er(schema, 'er_diagram.png')`**: Función principal que parsea el DSL, construye el grafo de relaciones usando Graphviz internamente, y lo serializa como imagen PNG.

*Desarrollado por Rubén Schnettler.*
