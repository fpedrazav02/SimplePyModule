import unittest
import pandas as pd
import io
import sys
from SimplePyModule.dataFiltering import filterKeywords

class TestFilterKeywords(unittest.TestCase):

    def test_filter_keywords(self):
        df_info = pd.read_csv('data/TMDB_info.csv')
        df_overview = pd.read_csv('data/TMDB_overview.csv')
        df_combined = df_info.merge(df_overview, on='id')

        self.assertIn('original_language', df_combined.columns)
        self.assertIn('overview', df_combined.columns)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        filterKeywords(df_combined)
        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

if __name__ == '__main__':
    unittest.main()
