# 🚀 Generador de CV en Formato Harvard (Python + python-docx)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![python-docx](https://img.shields.io/badge/python--docx-Document%20Generation-blue?style=flat-square&logo=microsoftword&logoColor=white)](#)

Script de automatización de documentos que genera un Currículum Vitae profesional en formato Harvard directamente como archivo `.docx`, listo para impresión o distribución digital.

## 🧠 Contexto Pedagógico y Teórico
La automatización de generación de documentos es un caso de uso de alto valor en la industria. Este script demuestra un principio clave de la ingeniería de software: **separar los datos de la presentación**. Al codificar el contenido del CV como estructuras de datos Python y delegar el formateo a la biblioteca `python-docx`, el documento se vuelve reproducible, editable programáticamente y fácilmente integrable en un pipeline de generación de informes o portfolios automatizados.

## ⚙️ Tecnologías y Frameworks Aplicados
* **`python-docx`**: Biblioteca elegida por su capacidad de manipular el formato OpenXML de Microsoft Word de forma abstracta. A diferencia de generar PDFs (que requieren herramientas como ReportLab o LaTeX), `python-docx` permite crear documentos editables que el usuario final puede modificar, priorizando la usabilidad práctica.

## 🛠️ Desglose Técnico (El "Cómo")
El script sigue una estructura lineal de programación imperativa orientada a la generación de documentos:
1. **Inicialización**: Se crea un objeto `Document()` en memoria.
2. **Inyección de contenido**: Se añaden secciones jerárquicamente (Headings y Paragraphs) para estructurar el documento según el formato Harvard.
3. **Persistencia**: Se serializa el objeto `Document` al sistema de archivos local mediante `doc.save()`.

*Desarrollado por Rubén Schnettler.*
