import unittest
import pandas as pd
from SimplePyModule.dataProcessing import addAirDays
from datetime import datetime

class TestAddAirDays(unittest.TestCase):

    def test_add_air_days(self):
        data = {
            'id': [1, 2],
            'name': ['Serie A', 'Serie B'],
            'first_air_date': ['2000-01-01', '2010-01-01']
        }
        df = pd.DataFrame(data)
        result_df = addAirDays(df)

        self.assertIn('air_days', result_df.columns)
        today = pd.to_datetime('today')
        expected_days_a = (today - pd.to_datetime('2000-01-01')).days
        expected_days_b = (today - pd.to_datetime('2010-01-01')).days
        self.assertEqual(result_df.loc[result_df['id'] == 1, 'air_days'].iloc[0], expected_days_a)
        self.assertEqual(result_df.loc[result_df['id'] == 2, 'air_days'].iloc[0], expected_days_b)
        self.assertEqual(len(df), len(result_df))

    def test_add_air_days_real_data(self):
        df = pd.read_csv('data/TMDB_info.csv')
        self.assertIn('first_air_date', df.columns)
        result_df = addAirDays(df)
        self.assertIn('air_days', result_df.columns)

        self.assertTrue(all(result_df['air_days'] >= 0))
        self.assertEqual(len(df), len(result_df))

if __name__ == '__main__':
    unittest.main()
