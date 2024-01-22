import zipfile
import tarfile
import os

def decompressFile(filepath):
    """
    Descomprime archivos en formato ZIP o TAR.GZ.

    Args:
    filepath (str): Ruta del archivo a descomprimir.

    Returns:
    str: Mensaje que indica el resultado de la descompresión.
    """
    if filepath.endswith('.zip'):
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(filepath))
            return "Archivo ZIP descomprimido con éxito."
    elif filepath.endswith('.tar.gz'):
        with tarfile.open(filepath, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(filepath))
            return "Archivo TAR.GZ descomprimido con éxito."
    else:
        return "Error: El archivo no es .zip o .tar.gz."
