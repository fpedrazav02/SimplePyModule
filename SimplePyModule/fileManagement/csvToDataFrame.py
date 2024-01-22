import pandas as pd
import time

def csvToDataFrame(filepaths):
    """
    Lee múltiples archivos CSV y los combina en un único DataFrame de Pandas.

    Args:
    filepaths (list): Lista de rutas de archivos CSV a leer.

    Returns:
    DataFrame: DataFrame de Pandas combinado.
    """
    start_time = time.time()
    dataframes = [pd.read_csv(file) for file in filepaths]
    merged_df = pd.concat(dataframes).drop_duplicates(subset='id').set_index('id')
    end_time = time.time()
    print(f"Tiempo de procesamiento: {end_time - start_time} segundos")
    return merged_df
