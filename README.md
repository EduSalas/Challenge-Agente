# Challenge-Agente
Repositorio en GitHub Un repositorio público en GitHub con el código fuente de tu proyecto. Un historial de commits que refleje el desarrollo del proyecto. Una estructura organizada y fácil de comprender.

# 🤖 Challenge Agente IA

## Descripción

Este proyecto implementa un **Agente Inteligente basado en RAG (Retrieval-Augmented Generation)** capaz de responder preguntas utilizando la información contenida en documentos PDF o CSV.

El usuario carga un documento desde una interfaz desarrollada con Streamlit. El contenido se procesa, se divide en fragmentos, se transforma en embeddings y se almacena en una base vectorial FAISS. Finalmente, un modelo de lenguaje genera respuestas utilizando únicamente la información recuperada del documento.

---

# Arquitectura

```
Usuario
      │
      ▼
 Streamlit
      │
      ▼
Carga PDF / CSV
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embeddings
      │
      ▼
FAISS
      │
      ▼
Retriever
      │
      ▼
OpenAI GPT
      │
      ▼
Respuesta
```

---

# Tecnologías

- Python 3.11
- Streamlit
- LangChain
- OpenAI
- FAISS
- PyPDF
- Pandas
- python-dotenv

---

# Estructura del proyecto

```
challenge-agente/

│ app.py
│ README.md
│ requirements.txt
│ .env

├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── agent.py
│   └── utils.py

└── data/doc.pdf
```

---

# Instalación

Clonar el repositorio

```bash
git clone https://github.com/EduSalas/challenge-agente.git
```

Entrar al proyecto

```bash
cd challenge-agente
```

Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear archivo

```
.env
```

Agregar la API Key

```
OPENAI_API_KEY=TU_API_KEY
```

Ejecutar

```bash
streamlit run app.py
```

---

# Uso

1. Abrir la aplicación.
2. Cargar un PDF o CSV.
3. Esperar el procesamiento.
4. Escribir una pregunta.
5. Obtener la respuesta basada en el documento.

---

# Ejemplos de preguntas

- ¿Cuál es el objetivo del documento?
- Resume el contenido.
- ¿Cuáles son las conclusiones?
- ¿Qué información contiene sobre seguridad?
- ¿Qué datos aparecen en el CSV?
- ¿Qué recomendaciones entrega el documento?

---

# Ejemplo de respuesta

Pregunta

> ¿Cuál es el objetivo del documento?

Respuesta

> El documento tiene como objetivo explicar el funcionamiento del sistema y presentar las principales recomendaciones para su implementación.

---

# Despliegue

La aplicación puede desplegarse fácilmente en Streamlit Community Cloud.

Repositorio GitHub:

```
https://github.com/EduSalas/challenge-agente
```

Aplicación:

```
https://challenge-agente-2026.streamlit.app
```

---

# Captura

<img width="1376" height="768" alt="app" src="https://github.com/user-attachments/assets/bb2d7b0d-edc9-47f3-b14f-ebd8c162f798" />

---

