import unittest
import pandas as pd
from SimplePyModule.dataFiltering import canceledSeries

class TestCanceledSeries(unittest.TestCase):

    def test_canceled_series(self):
        df = pd.read_csv('data/TMDB_info.csv')
        self.assertIn('first_air_date', df.columns)
        self.assertIn('status', df.columns)
        canceled_series_list = canceledSeries(df)
        self.assertIsInstance(canceled_series_list, list)
        if canceled_series_list:
            for series_name in canceled_series_list[:20]:
                series = df[df['name'] == series_name]
                self.assertTrue(series['first_air_date'].str.startswith('2023').any())
                self.assertEqual(series['status'].iloc[0], 'Canceled')
        else:
            print("No hay series que hayan comenzado en 2023 y hayan sido canceladas.")

if __name__ == '__main__':
    unittest.main()

