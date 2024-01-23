import pandas as pd

def seriesIntoDict(df: pd.DataFrame) -> dict:
    """
    Creates an ordered dictionary with the series original name as key and the full web address
    of its poster as value. If 'homepage' or 'poster_path' are NaN or empty, it sets the value to 'NOT AVAILABLE'.
    Displays the first 5 records of the dictionary.

    Args:
    df (pd.DataFrame): DataFrame containing series information.

    Returns:
    dict: Ordered dictionary with series names and poster URLs.
    """
    df.fillna({'homepage': 'NOT AVAILABLE', 'poster_path': 'NOT AVAILABLE'}, inplace=True)
    series_dict = {row['original_name']: (row['homepage'].rstrip('/') + '/' + row['poster_path'].lstrip('/')) if row['homepage'] != 'NOT AVAILABLE' and row['poster_path'] != 'NOT AVAILABLE' else 'NOT AVAILABLE' for index, row in df.iterrows()}
    print(dict(list(series_dict.items())[:5]))
    return series_dict


