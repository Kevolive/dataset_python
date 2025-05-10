import streamlit as st
import base64
from pathlib import Path



def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
    
image_base64 = get_base64_image("assets/foto.jpg")
# --- Configuración de la página ---
st.set_page_config(
    page_title=" Proyecto Python - Nuevas Tecnologías",
    page_icon="🚀",
    layout="wide"
)

# --- Estilos personalizados ---
st.markdown(f"""
    <style>
        .main-header {{
            font-size: 3rem;
            color: #000000; /* Un azul más vibrante */
            text-align: center;
            margin-bottom: 1.5rem;
            font-family: 'Arial Black', sans-serif; /* Ejemplo de fuente */.
            background-color: #FADBD8;
            font-bold: bold;
        }}
        .sub-header {{
            font-size: 2rem;
            color: #000000; /* Un tono de azul más claro */
            text-align: center;
            margin-bottom: 2.5rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Otra fuente */
            font-style: italic;
            font-bold: bold;
        }}
        .section-title {{
            font-size: 2.2rem;
            color: #2E86C1;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #D4E6F1;
            padding-bottom: 0.5rem;
            background-color: #F4F6F7; /* Fondo suave */
            font-bold: bold;
        }}
        .student-info-container {{
            background-color: #A9D6E5; /* Fondo suave */
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
            font-bold: bold;
        }}
        .student-name {{
            color: #000000;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 10px;
            font-bold: bold;
        }}
        .student-detail {{
            color: #000000;
            font-size: 1.1rem;
            margin-bottom: 8px;
        }}
        .github-link {{
            color: #000000 !important;
            font-weight: bold;
            text-decoration: none !important;
        }}
        .github-link:hover {{
            text-decoration: underline !important;
        }}
        .stButton > button {{
            background-color: #2E86C1;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.7rem 1.5rem;
            border: none;
            transition: background-color 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #1C395A; /* Un tono más oscuro al pasar el ratón */
        }}
    </style>
""", unsafe_allow_html=True)

# --- Estilos personalizados para el sidebar ---
st.markdown(f"""
    <style>
        /* Cambiar el fondo del sidebar */
        [data-testid="stSidebar"] {{
            background-color: #A9D6E5; /* Azul pastel */
            color: #000000; /* Texto negro */
        }}
        /* Opcional: Cambiar el color de los textos dentro del sidebar */
        [data-testid="stSidebar"] .css-1d391kg {{
            color: #000000; /* Texto negro */
        }}
         /* Cambiar el fondo del sidebar */
        [data-testid="stSidebar"] {{
            background-color: #A9D6E5; /* Azul pastel */
            color: #000000; /* Texto negro */
        }}
        /* Cambiar el texto del sidebar a negrita */
        [data-testid="stSidebar"] * {{
            font-weight: bold; /* Texto en negrita */
        }}
            
    </style>
""", unsafe_allow_html=True)
# --- Función para cargar y mostrar el logo SVG (más robusta) ---
def show_svg(filepath, width=None):
    with open(filepath, "r") as f:
        svg_content = f.read()
    if width:
        svg_content = svg_content.replace('<svg', f'<svg width="{width}"')
    st.markdown(svg_content, unsafe_allow_html=True)

#Imagen de Cesde
col1, col2, col3 = st.columns([1, 2, 1])  # Ajusta las proporciones de las columnas
with col2:
    st.image("assets/logo-Cesde-2023.svg", width=650)

# --- Encabezados ---
st.markdown('<h1 class="main-header">¡Analisis de las causas de suicidio en Antioquia!</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Explorando las Nuevas Tecnologías con un DataSet</h2>', unsafe_allow_html=True)

# --- Sección de información del estudiante con diseño mejorado ---
st.markdown('<h2 class="section-title">Desarrolladores</h2>', unsafe_allow_html=True)
st.markdown(f"""
    <div class="student-info-container">
        <div style="display: flex; align-items: center;">
            <div style="margin-right: 30px;">
                <img src="data:image/jpeg;base64, {image_base64}" alt="Foto de perfil" style="border-radius: 50%; width: 150px; height: 150px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
            </div>
            <div>
                <p class="student-name">Kevin Olivella, Marvin García y Paola Murillo </p>
                <p class="student-detail">Programa: <span style="font-weight: bold;">Desarrollo de Software: Nuevas Tecnologías</span></p>
                <p class="student-detail">Semestre: <span style="font-weight: bold;">2025-1</span></p>
                <p class="student-detail">Repositorio: <a href="https://github.com/Kevolive/proyecto-integrador.git" target="_blank" class="github-link">GitHub</a></p>
                <p class="student-detail">¡Apasionados por la creación de soluciones innovadoras con tecnología de punta!</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Introducción interactiva (ejemplo) ---
st.markdown('<h2 class="section-title">¿Qué te interesa explorar hoy?</h2>', unsafe_allow_html=True)
opcion = st.radio(
    "Selecciona un tema:",
    ("Inteligencia Artificial", "Desarrollo Web Moderno", "Análisis de Datos")
)

if opcion == "Inteligencia Artificial":
    st.write("¡Excelente elección! En las siguientes páginas encontrarás información sobre IA.")
elif opcion == "Desarrollo Web Moderno":
    st.write("El desarrollo web está en constante evolución. ¡Descubre las últimas tendencias!")
elif opcion == "Análisis de Datos":
    st.write("El poder de los datos para tomar decisiones informadas. ¡Exploremos!")

# --- Pie de página personalizado ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #777; font-size: 0.9rem; padding-top: 10px;">
        © 2025 Kevin Olivella, Marvin garcía y Paola Murillo - Proyecto para Nuevas Tecnologías de Programación
    </div>
""", unsafe_allow_html=True)