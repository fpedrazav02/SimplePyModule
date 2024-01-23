import unittest
import pandas as pd
from SimplePyModule.fileManagement import csvToDataFrame

class TestCsvToDataFrame(unittest.TestCase):

    def test_csv_to_dataframe(self):
        csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', 'data/TMDB_distribution.csv']
        df = csvToDataFrame(csv_files)

        self.assertIsInstance(df, pd.DataFrame)
        expected_columns = ['name', 'original_name', 'genres', 'networks', 'overview']
        for col in expected_columns:
            self.assertIn(col, df.columns)
        self.assertTrue(df.index.is_unique)

if __name__ == '__main__':
    unittest.main()

