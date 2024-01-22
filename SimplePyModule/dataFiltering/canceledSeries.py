import pandas as pd

def canceledSeries(df: pd.DataFrame) -> list:
    """
    Obtains and prints the first 20 names of series that started in 2023 and have been canceled.

    Args:
    df (pd.DataFrame): DataFrame containing series information.

    Returns:
    list: List of series names.
    """
    canceled_series = df[(df['first_air_date'].str.startswith('2023')) & (df['status'] == 'Canceled')]['name'].tolist()
    print(canceled_series[:20])
    return canceled_series
