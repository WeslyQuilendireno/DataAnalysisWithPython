import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    years_all = range(df['Year'].min(), 2051)
    sea_level_all = [slope * year + intercept for year in years_all]
    ax.plot(years_all, sea_level_all, color='red', label='Best Fit Line (All Data)')

    # Line of best fit using data from 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(
        df_2000['Year'], df_2000['CSIRO Adjusted Sea Level']
    )
    years_2000 = range(2000, 2051)
    sea_level_2000 = [slope_2000 * year + intercept_2000 for year in years_2000]
    ax.plot(years_2000, sea_level_2000, color='green', label='Best Fit Line (2000+)')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return ax