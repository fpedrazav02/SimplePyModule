import pandas as pd

def jpDataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Obtains a DataFrame with names, original names, broadcasting platforms, and production companies
    of all series in Japanese language and displays the first 20 records.

    Args:
    df (pd.DataFrame): DataFrame containing series information.

    Returns:
    pd.DataFrame: Filtered DataFrame with Japanese series.
    """
    japanese_series = df[df['languages'].str.contains('ja')][['name', 'original_name', 'networks', 'production_companies']]
    print(japanese_series.head(20))
    return japanese_series
