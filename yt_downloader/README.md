# 🚀 Descargador de Videos de YouTube (Pytube + Streamlit)

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)

Aplicación web interactiva que permite descargar videos de YouTube en el formato y resolución elegidos por el usuario. Construida sobre el paradigma OOP para demostrar cómo encapsular lógica de negocio compleja detrás de una interfaz limpia.

## 🧠 Contexto Pedagógico y Teórico
Este proyecto aplica el paradigma orientado a objetos a un caso de uso real: la gestión de descargas de medios. La clase `YouTubeDownloader` encapsula todo el estado del proceso (URL, objeto YouTube, stream seleccionado) y expone métodos públicos cohesivos. Además, demuestra el patrón de **Callback en programación asíncrona**: el método estático `onProgress` es registrado como callback en `pytube.YouTube` para actualizar la barra de progreso en tiempo real, separando la lógica de descarga de la lógica de presentación.

## ⚙️ Tecnologías y Frameworks Aplicados
* **`pytube`**: Librería de scraping de la API pública de YouTube que abstrae la complejidad del protocolo de streaming adaptativo (DASH/HLS), exponiendo los streams disponibles como objetos Python manipulables.
* **`Streamlit`**: Elegido por su capacidad de convertir scripts Python en aplicaciones web interactivas con mínimo boilerplate. A diferencia de Flask o Django, Streamlit está optimizado para aplicaciones de datos y herramientas internas, permitiendo iterar rápidamente sin necesidad de gestionar templates HTML separados.

## 🛠️ Desglose Técnico (El "Cómo")
* **`showStreams()`**: Recupera todos los streams disponibles del video y los presenta en un `selectbox` de Streamlit, permitiendo al usuario elegir la resolución, FPS y tipo MIME.
* **`onProgress` (Callback estático)**: Calcula el porcentaje de descarga completado en tiempo real y actualiza la barra de progreso de Streamlit.
* **`download()`**: Delega la descarga al stream seleccionado y notifica al usuario mediante `st.success()`.

*Desarrollado por Rubén Schnettler.*
