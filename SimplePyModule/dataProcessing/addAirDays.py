import pandas as pd
from datetime import datetime

def addAirDays(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a new column 'air_days' to the DataFrame indicating the number of days
    the series has been on air. Displays the top 10 records with the most air days.

    Args:
    df (pd.DataFrame): DataFrame containing the series data.

    Returns:
    pd.DataFrame: Updated DataFrame with the 'air_days' column.
    """
    df['air_days'] = (pd.to_datetime('today') - pd.to_datetime(df['first_air_date'])).dt.days
    print(df.nlargest(10, 'air_days'))
    return df
