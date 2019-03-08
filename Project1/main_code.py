# coding: utf-8

# !/usr/bin/python -tt


def main():
    import pandas as pd

    # Import the game review data.
    vg = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

    # Start Code (John)

    # Question 1.
    # Which console had the most sales?

    var = vg.groupby(["Platform"]).sum().sort_values("Global_Sales", ascending=False)
    print(var, '\n')

    # Question 3.
    # Relation to user and critic score?

    avg_critic = vg["Critic_Score"].mean()
    print("The average overall critic score is: ", avg_critic, '\n')

    # Check highest critic score.
    high_critic = vg.sort_values(by=['Critic_Score'], ascending=False).head(1)
    print(high_critic, '\n')

    # Question 4.
    # Compare critic and user score by year.

    # year_group = vg.groupby(["Year_Of_Release"])
    # Year will be rows(observations) columns will be the scores.
    vg_melt = pd.melt(vg, id_vars=["Year_of_Release", "Name"], value_vars=["Critic_Score", "User_Score"])
    print(vg_melt.head(), '\n')

    # Question 7
    # Best selling game of all time?

    high_global_sales = vg.sort_values(by=['Global_Sales'])
    print(high_global_sales.head(1), '\n')

    # Question 8
    # Lowest critically scored published?

    low_critic = vg.sort_values(by=["Critic_Score"])
    print(low_critic.head(1), '\n')

    # End Code (John)

    # Start Code (Nick)

    # Question 2.
    # Which publisher had the overall highest review rating?

    # Get the indices for rows with 'tbd' as the value for the User_Score column.
    tbd_index = vg[vg['User_Score'] == "tbd"].index

    # Copy the dataframe to a new variable for editing.
    no_tbd_df = vg

    # Remove all the indices with 'tbd'.
    no_tbd_df.drop(tbd_index, inplace=True)

    # Change the dtype from object to float for averaging.
    no_tbd_df['User_Score'] = no_tbd_df['User_Score'].astype('float64')

    # Group all the same publishers together.
    publisher_df = no_tbd_df.groupby('Publisher')

    # Get the average user score and find the top value.
    print(publisher_df['User_Score'].mean().sort_values(ascending=False).head(1), '\n')

    # Question 5.
    # Best rated game publisher by average critic rating?

    # Group all the same publishers.
    publisher_df_2 = vg.groupby('Publisher')
    
    # Get the average critic score and find the top value.
    print(publisher_df_2['Critic_Score'].mean().sort_values(ascending=False).head(1), '\n')

    # Question 6
    # Publisher that sells the most games?

    # Sum up all the global sales for each publisher and get the highest sales publisher.
    print(publisher_df_2['Global_Sales'].sum().sort_values(ascending=False).head(1), '\n')

    # Question 9
    # Games sales by ESRB rating?

    # Group all the ESRB ratings together.
    esrb_df = vg.groupby('Rating')

    # Sum up all the global sales of each ESRB rating.
    print(esrb_df['Global_Sales'].sum().sort_values(ascending=False).head(20), '\n')

    # Question 10
    # Game review score by ESRB rating?

    # Average all the critic scores for each ESRB rating.
    print(esrb_df['Critic_Score'].mean().sort_values(ascending=False).head(20), '\n')

    # End Code (Nick)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
