import unittest
import pandas as pd
from SimplePyModule.fileManagement import csvToDataFrame

class TestCsvToDataFrame(unittest.TestCase):

    def test_csv_to_dataframe(self):
        # Define la ruta de los archivos CSV
        csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', 'data/TMDB_distribution.csv']

        # Llama a la función csvToDataFrame
        df = csvToDataFrame(csv_files)

        # Verifica si el resultado es un DataFrame de Pandas
        self.assertIsInstance(df, pd.DataFrame)

        # Verifica si las columnas clave están presentes en el DataFrame
        expected_columns = ['name', 'original_name', 'genres', 'networks', 'overview']
        for col in expected_columns:
            self.assertIn(col, df.columns)

        # Verifica si el 'id' es único y utilizado como índice
        self.assertTrue(df.index.is_unique)

if __name__ == '__main__':
    unittest.main()

