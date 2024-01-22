import csv
import time

def csvToDictionary(filepaths):
    """
    This function reads multiple CSV files and combines them into a single Dictionary.

    Args:
    filepaths (list): List of CSV paths to read.

    Returns:
    dict: Dicctionary
    """
    start_time = time.time()
    data_dict = {}
    for filepath in filepaths:
        with open(filepath, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                key = row.pop('id')
                if key in data_dict:
                    data_dict[key].update(row)
                else:
                    data_dict[key] = row
    end_time = time.time()
    print(f"Processed Time: {end_time - start_time} seconds")
    return data_dict
