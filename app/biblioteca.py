import pandas as pd
import os

class Biblioteca:
    def __init__(self, archivo='data/autores.csv'):
        self.archivo = archivo
        if not os.path.exists(archivo) or os.stat(archivo).st_size == 0:
            pd.DataFrame(columns=['Nombre', 'Género', 'Categoría', 'Fecha de Publicación']).to_csv(archivo, index=False)
        self.df = pd.read_csv(archivo)

    def add_author(self, nombre, genero, categoria, fecha_publicacion):
        nuevo_autor = pd.DataFrame({'Nombre': [nombre], 'Género': [genero], 'Categoría': [categoria], 'Fecha de Publicación': [fecha_publicacion]})
        self.df = pd.concat([self.df, nuevo_autor], ignore_index=True)
        self.df.to_csv(self.archivo, index=False)

    def search_author(self, nombre):
        return self.df[self.df['Nombre'].str.contains(nombre, case=False)]

    def delete_author(self, nombre):
        antes = len(self.df)
        print(f"Intentando eliminar al autor: {nombre}")
        print(f"Antes de eliminar: {antes} filas")
    
    # Usar una condición más estricta para la eliminación
        self.df = self.df[self.df['Nombre'].str.lower() != nombre.lower()]
    
        despues = len(self.df)
        print(f"Después de eliminar: {despues} filas")
    
        if antes > despues:
            self.df.to_csv(self.archivo, index=False)
            print(f"Autor '{nombre}' eliminado con éxito")
            return True
        else:
            print(f"No se pudo eliminar el autor '{nombre}'. No se encontró una coincidencia exacta.")
            return False

    def get_all_authors(self):
        return self.df