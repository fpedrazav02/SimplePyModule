import unittest
import pandas as pd
from SimplePyModule.dataProcessing import seriesIntoDict

class TestSeriesIntoDict(unittest.TestCase):

    def test_series_into_dict(self):
        data = {
            'original_name': ['Serie A', 'Serie B'],
            'homepage': ['http://homepageA.com/', None],
            'poster_path': ['/posterA.jpg', '/posterB.jpg']
        }
        df = pd.DataFrame(data)

        series_dict = seriesIntoDict(df)
        self.assertIsInstance(series_dict, dict)
        self.assertListEqual(list(series_dict.keys()), ['Serie A', 'Serie B'])

        self.assertEqual(series_dict['Serie A'], 'http://homepageA.com/posterA.jpg')
        self.assertEqual(series_dict['Serie B'], 'NOT AVAILABLE')

    def test_series_into_dict_real_data(self):
        df = pd.read_csv('data/TMDB_overview.csv')
        self.assertIn('original_name', df.columns)
        self.assertIn('homepage', df.columns)
        self.assertIn('poster_path', df.columns)

        series_dict = seriesIntoDict(df)
        self.assertIsInstance(series_dict, dict)

        self.assertEqual(series_dict['Game of Thrones'], 'http://www.hbo.com/game-of-thrones/1XS1oqL89opfnbLl8WnZY1O1uJx.jpg')
        self.assertEqual(series_dict['La Casa de Papel'], 'https://www.netflix.com/title/80192098/reEMJA1uzscCbkpeRJeTT2bjqUp.jpg')

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
