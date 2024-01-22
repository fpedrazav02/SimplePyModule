import unittest
import pandas as pd
from io import StringIO
from SimplePyModule.fileManagement import csvToDataFrame

class TestCsvToDataFrame(unittest.TestCase):
    def test_csv_to_dataframe(self):
        # Crear datos de ejemplo como si fueran archivos CSV
        csv_data1 = StringIO("""id,name,age
                                1,Alice,30
                                2,Bob,25""")
        csv_data2 = StringIO("""id,name,age
                                3,Charlie,35
                                4,Diana,40""")

        # Llama a la función csvToDataFrame con estos datos de prueba
        resultado = csvToDataFrame([csv_data1, csv_data2])

        # Verifica si el resultado es un DataFrame de Pandas
        self.assertIsInstance(resultado, pd.DataFrame)

        # Verifica si el índice 'id' está presente y es único
        self.assertTrue(resultado.index.is_unique)
        self.assertIn('id', resultado.index)

        # Más aserciones según sea necesario, como comprobar la longitud del DataFrame, etc.

if __name__ == '__main__':
    unittest.main()
