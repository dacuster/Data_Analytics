# Exercises
# February 24, 2018
# 1  Tips

# 1.0.1  Introduction:
# This exercise was created based on the tutorial and documentation from Seaborn
# The dataset being used is tips from Seaborn.

# 1.0.2  Step 1. Import the necessary libraries:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1.0.3  Step 2. Import the dataset from this address.
# 1.0.4  Step 3. Assign it to a variable called tips
tips = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv")

# 1.0.5  Step 4. Delete the Unnamed 0 column
tips = tips.drop(columns=['Unnamed: 0'])

f, plots = plt.subplots(2, 2)
# 1.0.6  Step 5. Plot the total_bill column histogram
plots[0, 0].hist(tips['total_bill'])
plots[0, 0].plot()
plots[0, 0].set_title('Bill Totals')
plots[0, 0].set_xlabel('Total')
plots[0, 0].set_ylabel('Count')

# 1.0.7  Step 6. Create a scatter plot presenting the relationship between total_bill and tip
plots[0, 1].scatter(x=tips['total_bill'], y=tips['tip'])
plots[0, 1].plot()
plots[0, 1].set_title('Total Bills per Tip')
plots[0, 1].set_xlabel('Bill Total')
plots[0, 1].set_ylabel('Tip')

# 1.0.8  Step 7. Create one image with the relationship of total_bill, tip and size.
# Hint: It is just one function.
plots[1, 0].scatter(x=tips['total_bill'], y=tips['tip'], s=tips['size'])
plots[1, 0].plot()
plots[1, 0].set_title('Total Bills per Tip based on Size')
plots[1, 0].set_xlabel('Bill Total')
plots[1, 0].set_ylabel('Tip')

# 1.0.9  Step 8. Present the relationship between days and total_bill value
plots[1, 1].bar(tips['day'], tips['total_bill'])
plots[1, 1].plot()
plots[1, 1].set_title('Bill Total per Day')
plots[1, 1].set_xlabel('Day')
plots[1, 1].set_ylabel('Bill Total')
f.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()

# 1.0.10  Step 9. Create a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex


# 1.0.11  Step 10. Create a box plot presenting the total_bill per day differetiation the time (Dinner or Lunch)


# 1.0.12  Step 11. Create two histograms of the tip value based for Dinner and Lunch. They must be side by side.


# 1.0.13  Step 12. Create two scatterplots graphs, one for Male and another for Female, presenting the total_bill value and tip relationship, differing by smoker or no smoker
# 1.0.14  They must be side by side.


# 1.0.15  BONUS: Create your own question and answer it using a graph.
