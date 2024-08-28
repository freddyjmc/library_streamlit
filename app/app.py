import streamlit as st
import pandas as pd
from biblioteca import Biblioteca
from logger import setup_logger

# Configurar logger
logger = setup_logger()

# Inicializar biblioteca
biblioteca = Biblioteca()

# Título de la aplicación
st.title("HCSCJ")

# Funcionalidades de la aplicación
opcion = st.sidebar.selectbox("Elige una opción", ["Añadir Autor", "Buscar Autor", "Eliminar Autor", "Mostrar Todos"])

generos_ficcion = [
    "Novela", "Cuento", "Fantasía", "Ciencia ficción", "Terror", "Misterio/Policiaco", 
    "Romance", "Aventura", "Histórica", "Realismo mágico", "Distopía/Utopía", "Thriller"
]
generos_no_ficcion = [
    "Biografía/Autobiografía", "Ensayo", "Historia", "Ciencia", "Autoayuda", 
    "Memorias", "Viajes", "Religión/Espiritualidad", "Política", "Economía"
]
otros_generos = ["Poesía", "Teatro", "Cómic/Novela gráfica", "Fábulas y cuentos infantiles", "Mitos/Leyendas"]
generos_hibridos = ["Ficción histórica", "Ciencia ficción distópica", "Romance paranormal"]

todos_los_generos = {
    "Ficción": generos_ficcion,
    "No Ficción": generos_no_ficcion,
    "Otros Géneros": otros_generos,
    "Géneros Híbridos": generos_hibridos
}

if opcion == "Añadir Autor":
    st.subheader("Añadir un nuevo autor")
    nombre = st.text_input("Nombre del autor")
    
    # Seleccionar categoría y género
    categoria = st.selectbox("Selecciona la categoría", list(todos_los_generos.keys()))
    genero = st.selectbox("Selecciona el género", todos_los_generos[categoria])
    
    fecha_publicacion = st.date_input("Fecha de Publicación")
    
    if st.button("Guardar"):
        if nombre and genero and categoria and fecha_publicacion:
            biblioteca.add_author(nombre, genero, categoria, str(fecha_publicacion))
            st.success(f"Autor '{nombre}' añadido con éxito.")
            logger.info(f"Añadido autor: {nombre}")
        else:
            st.error("Todos los campos son obligatorios.")

elif opcion == "Buscar Autor":
    st.subheader("Buscar un autor")
    nombre = st.text_input("Nombre del autor a buscar")
    if st.button("Buscar"):
        resultado = biblioteca.search_author(nombre)
        if not resultado.empty:
            st.write("Autor(es) encontrado(s):")
            st.write(resultado)
            logger.info(f"Autor(es) encontrado(s) para la búsqueda: {nombre}")
        else:
            st.warning(f"No se encontró ningún autor con el nombre '{nombre}'.")

elif opcion == "Eliminar Autor":
    st.subheader("Eliminar un autor")
    nombre = st.text_input("Nombre del autor a eliminar")
    if st.button("Buscar para eliminar"):
        resultado = biblioteca.search_author(nombre)
        if not resultado.empty:
            st.write("Autor(es) encontrado(s):")
            st.write(resultado)
            autor_seleccionado = st.selectbox("Selecciona el autor a eliminar", resultado['Nombre'].tolist())
            if st.button("Confirmar eliminación"):
                if biblioteca.delete_author(autor_seleccionado):
                    st.success(f"Autor '{autor_seleccionado}' eliminado con éxito.")
                    logger.info(f"Autor eliminado: {autor_seleccionado}")
                    # Forzar una recarga de la página para mostrar los cambios
                    st.experimental_rerun()
                else:
                    st.error(f"No se pudo eliminar el autor '{autor_seleccionado}'. Por favor, intenta de nuevo.")
        else:
            st.warning(f"No se encontró ningún autor con el nombre '{nombre}'.")

    # Mostrar la lista actualizada de autores después de cada acción
    st.subheader("Lista actualizada de autores:")
    autores_actualizados = biblioteca.get_all_authors()
    st.write(autores_actualizados)
    
elif opcion == "Mostrar Todos":
    st.subheader("Lista de todos los autores")
    autores = biblioteca.get_all_authors()
    st.write(autores)
    logger.info("Mostrando todos los autores")