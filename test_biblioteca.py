import sys
import os
import unittest
from app.biblioteca import Biblioteca  # type: ignore # Importación ajustada con la ruta correcta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca(archivo='test_autores.csv')
        # Limpiar el DataFrame al inicio de cada prueba
        self.biblioteca.df = self.biblioteca.df[0:0]
        self.biblioteca.df.to_csv('test_autores.csv', index=False)

    def tearDown(self):
        os.remove('test_autores.csv')

    def test_add_author_ficcion(self):
        self.biblioteca.add_author("Gabriel García Márquez", "Realismo mágico", "1927-03-06")
        self.assertIn("Gabriel García Márquez", self.biblioteca.df['Nombre'].values)
        self.assertIn("Realismo mágico", self.biblioteca.df['Género'].values)

    def test_add_author_no_ficcion(self):
        self.biblioteca.add_author("Stephen Hawking", "Ciencia", "1942-01-08")
        self.assertIn("Stephen Hawking", self.biblioteca.df['Nombre'].values)
        self.assertIn("Ciencia", self.biblioteca.df['Género'].values)

    def test_add_author_otros_generos(self):
        self.biblioteca.add_author("Pablo Neruda", "Poesía", "1904-07-12")
        self.assertIn("Pablo Neruda", self.biblioteca.df['Nombre'].values)
        self.assertIn("Poesía", self.biblioteca.df['Género'].values)

    def test_add_author_hibrido(self):
        self.biblioteca.add_author("Isaac Asimov", "Ciencia ficción distópica", "1920-01-02")
        self.assertIn("Isaac Asimov", self.biblioteca.df['Nombre'].values)
        self.assertIn("Ciencia ficción distópica", self.biblioteca.df['Género'].values)

    def test_search_author_by_genre(self):
        self.biblioteca.add_author("Gabriel García Márquez", "Realismo mágico", "1927-03-06")
        result = self.biblioteca.search_author("Gabriel")
        self.assertEqual(len(result), 1)
        self.assertIn("Realismo mágico", result['Género'].values)

    def test_delete_author(self):
        self.biblioteca.add_author("Gabriel García Márquez", "Realismo mágico", "1927-03-06")
        self.biblioteca.delete_author("Gabriel García Márquez")
        self.assertNotIn("Gabriel García Márquez", self.biblioteca.df['Nombre'].values)

    def test_get_all_authors_with_various_genres(self):
        self.biblioteca.add_author("Gabriel García Márquez", "Realismo mágico", "1927-03-06")
        self.biblioteca.add_author("Stephen Hawking", "Ciencia", "1942-01-08")
        self.biblioteca.add_author("Pablo Neruda", "Poesía", "1904-07-12")
        self.biblioteca.add_author("Isaac Asimov", "Ciencia ficción distópica", "1920-01-02")
        autores = self.biblioteca.get_all_authors()
        self.assertEqual(len(autores), 4)
        self.assertIn("Realismo mágico", autores['Género'].values)
        self.assertIn("Ciencia", autores['Género'].values)
        self.assertIn("Poesía", autores['Género'].values)
        self.assertIn("Ciencia ficción distópica", autores['Género'].values)

if __name__ == "__main__":
    unittest.main()
