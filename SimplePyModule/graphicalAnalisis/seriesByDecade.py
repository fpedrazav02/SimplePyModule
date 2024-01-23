import pandas as pd
import matplotlib.pyplot as plt

def seriesByDecade(df: pd.DataFrame) -> None:
    """
    Constructs a line chart showing the number of series of each 'type' produced in each decade since 1940.
    Displays trend changes.

    Args:
    df (pd.DataFrame): DataFrame containing series information.
    """
    df = df.dropna(subset=['first_air_date'])
    df['decade'] = df['first_air_date'].str[:4].astype(int) // 10 * 10
    series_count_by_decade = df[df['decade'] >= 1940].groupby(['decade', 'type']).size().unstack().fillna(0)
    series_count_by_decade.plot(kind='line')
    plt.xlabel('Decade')
    plt.ylabel('Number of Series')
    plt.title('Number of Series by Type and Decade')
    plt.show()

