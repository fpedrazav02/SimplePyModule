import pandas as pd

def jpDataframe(df_info: pd.DataFrame, df_distribution: pd.DataFrame) -> pd.DataFrame:
    """
    Obtains a DataFrame with names and production companies
    of all series in Japanese language and displays the first 20 records.

    Args:
    df_info (pd.DataFrame): DataFrame containing series information.
    df_distribution (pd.DataFrame): DataFrame containing distribution information.

    Returns:
    pd.DataFrame: Filtered DataFrame with Japanese series.
    """
    df_combined = df_info.merge(df_distribution, on='id')
    japanese_series = df_combined[df_combined['languages'].str.contains('ja', na=False)][['name', 'production_companies']]
    print(japanese_series.head(20))
    return japanese_series



