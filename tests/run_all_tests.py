import sys
import os
import unittest
import argparse

sys.path.append(os.path.abspath('.'))

def clean_data_folder():
    data_folder = 'data'
    csv_files = ['TMDB_distribution.csv', 'TMDB_info.csv', 'TMDB_overview.csv']

    for file in csv_files:
        file_path = os.path.join(data_folder, file)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Archivo '{file}' eliminado.")

def run_all_tests(clean=False):
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

    if clean:
        clean_data_folder()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true', help='Limpiar archivos CSV después de ejecutar tests')
    args = parser.parse_args()

    run_all_tests(clean=args.clean)
