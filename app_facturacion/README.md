# 🚀 Sistema de Automatización de Facturación (PDF → Excel)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![pdfplumber](https://img.shields.io/badge/pdfplumber-PDF%20Parsing-red?style=flat-square&logo=adobeacrobatreader&logoColor=white)](#)
[![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20Output-green?style=flat-square&logo=microsoftexcel&logoColor=white)](#)

Sistema de procesamiento de documentos que extrae información estructurada desde facturas en formato PDF y la consolida automáticamente en hojas de cálculo Excel, eliminando la captura de datos manual.

## 🧠 Contexto Pedagógico y Teórico
La extracción de información de PDFs es una problemática recurrente en la automatización de procesos de negocio (RPA - Robotic Process Automation). Este proyecto demuestra el patrón **ETL** (Extract, Transform, Load) a escala básica: se extrae texto de PDFs no estructurados, se transforma mediante expresiones regulares para identificar campos relevantes, y se carga en un formato tabular (Excel) para análisis posterior. Este enfoque es la base técnica de sistemas más complejos como la integración con ERP o facturación electrónica.

## ⚙️ Tecnologías y Frameworks Aplicados
* **`pdfplumber`**: Seleccionado por su capacidad de extracción de texto con alta fidelidad posicional. A diferencia de alternativas como PyPDF2, `pdfplumber` preserva mejor el layout del documento, siendo clave para facturas con formatos tabularizados.
* **`re` (Expresiones Regulares)**: Módulo estándar de Python para la etapa de *Transformación*. Las regex permiten definir patrones estructurales (número de factura, fecha, monto) que son robustos ante variaciones menores en el formato del documento.

## 🛠️ Desglose Técnico (El "Cómo")
* **`extraer_datos_factura(pdf_path)`**: Función principal que abre un PDF, concatena el texto de todas sus páginas y aplica tres patrones regex para extraer: número de factura, fecha y monto total.
* **Plantillas Excel (`plantilla_facturas.xlsx`)**: Archivo de destino que actúa como la capa de salida del pipeline ETL, donde los datos extraídos se consolidan en filas estructuradas.

*Desarrollado por Rubén Schnettler.*
