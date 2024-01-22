import pandas as pd
import time

def csvToDataFrame(filepaths):
    """
    This function reads multiple CSV files and combines them into a single pandas DataFrame.

    Args:
    filepaths (list): List of CSV path to read.

    Returns:
    DataFrame: A combined Pandas DataFrame.
    """
    start_time = time.time()
    dataframes = [pd.read_csv(file) for file in filepaths]
    merged_df = pd.concat(dataframes).drop_duplicates(subset='id').set_index('id')
    end_time = time.time()
    print(f"Processed Time: {end_time - start_time} seconds")
    return merged_df
