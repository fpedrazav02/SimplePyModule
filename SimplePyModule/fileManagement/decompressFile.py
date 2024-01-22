import zipfile
import tarfile
import os

def decompressFile(filepath):
    """
    Decompress files in ZIP or TAR.GZ.

    Args:
    filepath (str): Path to the file.

    Returns:
    str: Message with the operation status
    """
    if filepath.endswith('.zip'):
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(filepath))
            return "File correctly decompressed"
    elif filepath.endswith('.tar.gz'):
        with tarfile.open(filepath, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(filepath))
            return "TAR.GZ decompressed correctly."
    else:
        return "Error: Make sure your file is either .zip o .tar.gz."
