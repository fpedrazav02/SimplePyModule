import unittest
from SimplePyModule.fileManagement import csvToDictionary

class TestCsvToDictionary(unittest.TestCase):

    def test_csv_to_dictionary(self):
        csv_file = 'data/TMDB_overview.csv'
        series_dict = csvToDictionary([csv_file])

        self.assertIsInstance(series_dict, dict)

        for key, value in series_dict.items():
            url = value.get('homepage', '') + value.get('poster_path', '')

            # Verificar si la URL comienza con 'http://' o 'https://', o si es 'NOT AVAILABLE' o una cadena vacía
            self.assertTrue(url.startswith('http://') or url.startswith('https://') or url == 'NOT AVAILABLE' or url == '')

if __name__ == '__main__':
    unittest.main()

