import matplotlib.pyplot as plt
import pandas as pd

def seriesByStartYear(df: pd.DataFrame) -> None:
    """
    Displays a bar chart showing the number of series per start year.

    Args:
    df (pd.DataFrame): DataFrame containing series information.
    """
    series_count_by_year = df['first_air_date'].str[:4].value_counts().sort_index()
    series_count_by_year.plot(kind='bar')
    plt.xlabel('Year')
    plt.ylabel('Number of Series')
    plt.title('Number of Series by Start Year')
    plt.show()
