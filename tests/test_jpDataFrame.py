import unittest
import pandas as pd
from SimplePyModule.dataFiltering import jpDataframe

class TestJpDataframe(unittest.TestCase):

    def test_jp_dataframe(self):
        df_info = pd.read_csv('data/TMDB_info.csv')
        df_distribution = pd.read_csv('data/TMDB_distribution.csv')

        self.assertIn('languages', df_info.columns)

        jp_series_df = jpDataframe(df_info, df_distribution)
        self.assertIsInstance(jp_series_df, pd.DataFrame)

        expected_columns = ['name', 'production_companies']
        for col in expected_columns:
            self.assertIn(col, jp_series_df.columns)

if __name__ == '__main__':
    unittest.main()


