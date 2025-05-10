import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

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
    st.header("Filtros")

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

# Visualización: Mapa de ubicaciones
st.subheader("Mapa de Ubicaciones de los Casos (aproximadas):")

# Función para extraer latitud y longitud de la columna 'Ubicacion'
def extraer_coordenadas(ubicacion_str):
    if isinstance(ubicacion_str, str):
        if ubicacion_str.startswith("POINT ("):
            coordenadas_str = ubicacion_str[7:-1].split()
            try:
                longitud = float(coordenadas_str[0])
                latitud = float(coordenadas_str[1])
                return [longitud, latitud]  # pydeck espera [longitud, latitud]
            except (ValueError, IndexError) as e:
                st.error(f"Error al convertir coordenadas: {e} en '{ubicacion_str}'")
                return None
        else:
            st.warning(f"Formato de ubicación inesperado: '{ubicacion_str}'")
            return None
    return None

df_filtrado['coordenadas'] = df_filtrado['Ubicación'].apply(extraer_coordenadas)
df_con_coordenadas = df_filtrado.dropna(subset=['coordenadas'])

if not df_con_coordenadas.empty:
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df_con_coordenadas,
        get_position='coordenadas',
        get_color=[200, 30, 0, 160],  # Color de los puntos (RGBA)
        get_radius=100,  # Radio de los puntos en metros (ajustar según sea necesario)
        radius_min_pixels=5,  # Radio mínimo en píxeles
        radius_max_pixels=15,  # Radio máximo en píxeles
        pickable=True,
        opacity=0.8,
    )

    view_state = pdk.ViewState(
        latitude=df_con_coordenadas['coordenadas'].apply(lambda x: x[1]).mean() if not df_con_coordenadas.empty else 6.244,
        # Latitud promedio (Medellín como centro aproximado)
        longitude=df_con_coordenadas['coordenadas'].apply(lambda x: x[0]).mean() if not df_con_coordenadas.empty else -75.574,
        # Longitud promedio (Medellín como centro aproximado)
        zoom=8,  # Nivel de zoom inicial
        pitch=50,
    )

    map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"html": "<b>Municipio:</b> {NombreMuni}<br/><b>Casos:</b> {NumeroCasos}"},  # Información al pasar el mouse
    )

    st.pydeck_chart(map)
else:
    st.warning("No hay datos de ubicación disponibles para mostrar en el mapa con los filtros actuales.")

# Tabla de datos filtrados
st.subheader("Tabla de Datos Filtrados")
st.dataframe(df_filtrado)
