import csv
import time

def csvToDictionary(filepaths):
    """
    Lee múltiples archivos CSV y los combina en un único diccionario.

    Args:
    filepaths (list): Lista de rutas de archivos CSV a leer.

    Returns:
    dict: Diccionario combinado con 'id' como claves.
    """
    start_time = time.time()
    data_dict = {}
    for filepath in filepaths:
        with open(filepath, mode='r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                key = row.pop('id')
                if key in data_dict:
                    data_dict[key].update(row)
                else:
                    data_dict[key] = row
    end_time = time.time()
    print(f"Tiempo de procesamiento: {end_time - start_time} segundos")
    return data_dict
