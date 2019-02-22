# coding: utf-8

# !/usr/bin/python -tt

# Tidying Data
# Use pivot and melt to clean up the data.


def main():
    # Import the necessary libraries (pandas named pd)
    import pandas as pd

    # Import the tuberculosis data.
    tuberculosis_df = pd.read_csv('tb.csv')

    # Melt the data
    tuberculosis_df_melt = pd.melt(frame=tuberculosis_df, id_vars=['iso2', 'year'])

    # Create a new column for sex.
    tuberculosis_df_melt['sex'] = tuberculosis_df_melt.variable.str[7]

    # Create a new column for age.
    tuberculosis_df_melt['age'] = tuberculosis_df_melt.variable.str[8:]

    # Remove all the rows with a NAN value in the value, sex and age column.
    tuberculosis_df_melt = tuberculosis_df_melt.dropna(subset=['value', 'sex', 'age'])

    # Remove the variable column which was made from melting.
    tuberculosis_df_melt = tuberculosis_df_melt.drop(['variable'], axis=1)

    # Print the table.
    print(tuberculosis_df_melt)

    # Specify the url for the weather data.
    weather_url = 'http://stat405.had.co.nz/data/weather.txt'
    # Import the weather data.
    weather_df = pd.read_csv(weather_url, sep='\t')

    # Melt the table to tidy the days.
    weather_df_melt = pd.melt(frame=weather_df, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='reading')

    # Remove the d in front of the day number.
    weather_df_melt['day'] = weather_df_melt.day.str[1:]

    # Pivot the table by the tmax and tmin variable.
    weather_df_pivot = weather_df_melt.pivot_table(index=['id', 'year', 'month', 'day'], columns='element', values='reading')

    print(weather_df_pivot)

    # Specify the url for the pew data.
    pew_url = 'http://stat405.had.co.nz/data/pew.txt'
    # Import the pew data.
    pew_df = pd.read_csv(pew_url, sep='\t')

    # Melt the pew data to create an income and frequency column
    pew_df_melt = pd.melt(frame=pew_df, id_vars=['religion'], var_name='income', value_name='frequency')

    print(pew_df_melt)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
