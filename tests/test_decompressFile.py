import unittest
import os
from SimplePyModule.fileManagement import decompressFile

class TestDecompressFile(unittest.TestCase):

    def test_decompress_zip(self):
        test_zip_file = 'data/TMDB.zip'
        self.assertTrue(os.path.exists(test_zip_file))

        decompressFile(test_zip_file)
        expected_files = ['data/TMDB_distribution.csv', 'data/TMDB_info.csv', 'data/TMDB_overview.csv']

        for file in expected_files:
            print(file)
            self.assertTrue(os.path.exists(file))

        # Eliminar CSVs
        # for file in expected_files:
        #     os.remove(file)

if __name__ == '__main__':
    unittest.main()

