# coding: utf-8

# !/usr/bin/python -tt

# Tidying Data
# Use pivot and melt to clean up the data.


def main():
    # ### Step 1. Import the necessary libraries (pandas named pd and numpy named np)
    import pandas as pd
    import numpy as np

    # Import the tuberculosis data.
    tuberculosis_df = pd.read_csv('tb.csv')
    print(tuberculosis_df)

    tuberculosis_df_melt = pd.melt(frame=tuberculosis_df, id_vars=['iso2'], value_vars=['year'])
    print(tuberculosis_df_melt)

    # Specify the url for the weather data.
    weather_url = 'http://stat405.had.co.nz/data/weather.txt'
    # Import the weather data.
    weather_df = pd.read_csv(weather_url, sep='\t', index_col='id')

    # Specify the url for the pew data.
    pew_url = 'http://stat405.had.co.nz/data/pew.txt'
    # Import the pew data.
    pew_df = pd.read_csv(pew_url, sep='\t', index_col='religion')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
