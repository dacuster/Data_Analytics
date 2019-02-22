# coding: utf-8

# !/usr/bin/python -tt

def main():
    # ### Step 1. Import the necessary libraries (pandas named pd and numpy named np)
    import pandas as pd
    import numpy as np

    # Import the game review data.
    game_review_df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
    print(game_review_df)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
