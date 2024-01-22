import unittest
import os
from tu_paquete.file_decompression_and_reading import decompressFile

class TestDecompressFile(unittest.TestCase):
    def test_decompress_zip(self):
        # Aquí deberías crear un archivo ZIP temporal para probar la descompresión
        # Luego llamar a la función decompressFile y verificar si el archivo se descomprimió correctamente

        self.assertTrue(os.path.exists(ruta_descomprimida))
        # Más aserciones según sea necesario

    # Puedes agregar más métodos de prueba para otros casos (como tar.gz o errores esperados)

if __name__ == '__main__':
    unittest.main()
