import matplotlib.pyplot as plt
import pandas as pd


def seriesByGenre(df: pd.DataFrame) -> None:
    """
    Obtains the number of series per genre and displays the percentage in a pie chart.
    Genres representing less than 1% of the total are included in the 'Other' category.

    Args:
    df (pd.DataFrame): DataFrame containing series information.
    """
    genre_counts = df['genres'].str.get_dummies(sep=', ').sum().sort_values(ascending=False)
    other_count = genre_counts[genre_counts / genre_counts.sum() < 0.01].sum()
    genre_counts = genre_counts[genre_counts / genre_counts.sum() >= 0.01]
    genre_counts['Other'] = other_count
    genre_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Percentage of Series by Genre')
    plt.ylabel('')
    plt.show()
