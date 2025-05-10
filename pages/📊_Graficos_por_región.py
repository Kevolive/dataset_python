import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

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
# Título principal de la aplicación
st.title("Análisis Interactivo de Suicidios en Antioquia (2005-2021)")

# Carga el dataset (asegúrate de que la ruta sea correcta)
try:
    df = pd.read_csv('static/datasets/suicidios_antioquia.csv')
except FileNotFoundError:
    st.error("Error: No se encontró el archivo de datos. Asegúrate de que la ruta sea correcta.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al cargar los datos: {e}")
    st.stop()


st.subheader("Dataset Completo:")
st.dataframe(df)
# Barra lateral para los filtros
with st.sidebar:
    st.header("🛠️ Filtros")

    # Filtro por rango de año con slider
    años_unicos = df['Anio'].unique()
    min_anio = int(años_unicos.min())
    max_anio = int(años_unicos.max())
    rango_anios = st.sidebar.slider("Seleccionar Rango de Años", min_value=min_anio, max_value=max_anio, value=(min_anio, max_anio), key="slider_anio")
    anio_inicio, anio_fin = rango_anios

    # Filtro por región (multiselect)
    regiones_unicas = df['NombreRegion'].unique()
    region_seleccionada = st.sidebar.multiselect("Seleccionar Región(es)", regiones_unicas, key="multiselect_region")

    # Opcional: Filtro por código de región (multiselect)
    codigos_region_unicos = df['CodigoRegion'].unique()
    codigo_region_seleccionado = st.sidebar.multiselect("Seleccionar Código de Región(es)", sorted(codigos_region_unicos), key="multiselect_codigo_region")

# Filtrado de datos basado en las selecciones
df_filtrado = df.copy()
df_filtrado = df_filtrado[(df_filtrado['Anio'] >= anio_inicio) & (df_filtrado['Anio'] <= anio_fin)]
if region_seleccionada:
    df_filtrado = df_filtrado[df_filtrado['NombreRegion'].isin(region_seleccionada)]
if codigo_region_seleccionado:
    df_filtrado = df_filtrado[df_filtrado['CodigoRegion'].isin(codigo_region_seleccionado)]

try:
    df = pd.read_csv('static/datasets/suicidios_antioquia.csv')
except FileNotFoundError:
    st.error("Error: No se encontró el archivo de datos. Asegúrate de que la ruta sea correcta.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al cargar los datos: {e}")
    st.stop()


# Visualización: Cantidad de Suicidios por Región (Filtrado)
st.subheader("Cantidad de Suicidios por Región (Filtrado):")
conteo_por_region = df_filtrado.groupby('NombreRegion')['NumeroCasos'].sum().reset_index()
fig_region = px.bar(conteo_por_region, x='NombreRegion', y='NumeroCasos', title='Total de Suicidios por Región')
st.plotly_chart(fig_region)

st.subheader("Datos Filtrados:")
st.dataframe(df_filtrado)