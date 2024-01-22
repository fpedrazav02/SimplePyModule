import pandas as pd

def filterKeywords(df: pd.DataFrame) -> None:
    """
    Prints the names of series whose original language is English and whose overview contains the words 'mystery' or 'crime', regardless of case.

    Args:
    df (pd.DataFrame): DataFrame containing series information.
    """
    filtered_series = df[(df['original_language'] == 'en') & (df['overview'].str.contains('mystery|crime', case=False, na=False))]
    print(filtered_series['name'])
