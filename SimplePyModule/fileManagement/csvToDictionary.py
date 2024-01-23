import csv
import time

def csvToDictionary(filepaths):
    """
    Reads multiple CSV files and combines them into a single dictionary.

    Args:
    filepaths (list): List of CSV paths to read.

    Returns:
    dict: Dictionary with combined data.
    """
    start_time = time.time()
    data_dict = {}
    for filepath in filepaths:
        with open(filepath, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                key = row.pop('id')
                processed_row = {k: v.strip().lower() if k in ['homepage', 'poster_path'] else v for k, v in row.items()}

                if key in data_dict:
                    data_dict[key].update(processed_row)
                else:
                    data_dict[key] = processed_row

    end_time = time.time()
    print(f"Processed Time: {end_time - start_time} seconds")
    return data_dict
