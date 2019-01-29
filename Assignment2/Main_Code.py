# coding: utf-8

# !/usr/bin/python -tt
# Credit guipsamora on Github
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Data exploration with Pandas
# Getting and Knowing your Data
# Fill in the code for the functions below, as discussed in class.
# This time you are going to add your code directly in main()
# Tests will be embedded in your code, printing 'OK' when each part is correct.
# Please do not edit anything that is within these two lines
# #### BEGIN DO NOT EDIT and
# #### END DO NOT EDIT lines

# NOTE: In order for tests to run you need to assign to variable called out
# the answer of the question
# looks like this: out = your answer code


# Provided simple test() function used in main() to # what each function
# returns vs. what it's supposed to return.
def test(got, expected, points=1):
	if got == expected:
		prefix = ' OK '
	else:	
		prefix = '  X '
	print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

	grade = 0
	if prefix == ' OK ':
		grade = points
	
	return grade


def main():
	score = 0
	# This time we are going to pull data directly from the internet.
	# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
	# 
	# ### Step 1. Import the necessary libraries (pandas named pd and numpy named np)

	# Import pandas and numpy for use.
	import pandas as pd
	import numpy as np

	# ### Step 2-3. Import the dataset from this [address]
	# (https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv).
	# ### Assign it to a variable called chipo.

	# Setup the url as a variable.
	url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
	# Pass the url into the read function with a tab delimiter.
	chipo = pd.read_csv(url, sep='\t')

	# ### Step 4. See the first 10 entries

	# Print the first 10 entries in the table.
	print(chipo.head(10))

	# ### Step 5. What is the number of observations in the dataset?
	# NOTE: In order for tests to run you need to assign to variable called out the answer of the question
	# looks like this: out = your answer code
	# #### BEGIN DO NOT EDIT 
	out = 0
	# #### END DO NOT EDIT 

	# Calculate the length of the indices (number of indices).
	out = len(chipo.index)

	# #### BEGIN DO NOT EDIT 
	score += test(out, 4622)
	# #### END DO NOT EDIT 

	# ### Step 6. What is the number of columns in the dataset?

	# Calculate the length of the columns (number of columns).
	out = len(chipo.columns)

	# #### BEGIN DO NOT EDIT 
	score += test(out, 5, 2)
	# #### END DO NOT EDIT 

	# ### Step 7. Get the name of all the columns.

	# Get column names.
	out = chipo.columns

	# #### BEGIN DO NOT EDIT 
	score += test(str(out), "Index(['order_id', 'quantity', 'item_name', 'choice_description',\n       'item_price'],\n      dtype='object')")
	# #### END DO NOT EDIT 

	# ### Step 8. How is the dataset indexed?

	# Get the indexing types.
	out = chipo.index

	# #### BEGIN DO NOT EDIT 
	score += test(str(out), 'RangeIndex(start=0, stop=4622, step=1)',2)
	# #### END DO NOT EDIT 

	# ### Step 9. How many times was the most ordered item ordered?

	# Get the head of the item_name frequency count list. This will be the value with the highest frequency in the table.
	highest_purchased_item = chipo.item_name.describe()['top']

	# Reset out to 0 for counting.
	out = 0

	# Iterate through each row.
	for row in chipo.itertuples():
		# Compare the row at column 'item_name' with the result from the frequency count head.
		if row.item_name == highest_purchased_item:
			# Increase the quantity by how many was purchased.
			out += row.quantity

	# #### BEGIN DO NOT EDIT
	score += test(out, 761, 2)
	# #### END DO NOT EDIT 

	# ### Step 10. How many items were ordered?

	# Reset out to 0 for counting.
	out = 0

	# Iterate through the table and add all the quantity values.
	for row in chipo.itertuples():
		out += row.quantity

	# #### BEGIN DO NOT EDIT 
	score += test(out, 4972, 2)
	# #### END DO NOT EDIT 

	# ### Step 11. How many times was the most ordered item in the choice_description column ordered?

	# Reset out to 0 for counting.
	out = 0

	# Find the highest purchased choice_description item.
	highest_purchased_choice = chipo.choice_description.describe()['top']

	# Iterate through each row.
	for row in chipo.itertuples():
		# Compare the row at column 'choice_description' with the result from the frequency count head.
		if row.choice_description == highest_purchased_choice:
			# Increase the quantity by how many was purchased.
			out += row.quantity

	# #### BEGIN DO NOT EDIT 
	# Diet Coke 159
	score += test(out, 159, 2)
	# #### END DO NOT EDIT 

	# ### Step 13. Turn the item price into a float
	# This one is done for you, use the exact code here
	dollarizer = lambda x: float(x[1:-1])
	chipo.item_price = chipo.item_price.apply(dollarizer)

	# ### Step 14. How much was the revenue for the period in the dataset?

	# Reset out to 0 for counting.
	out = 0

	# Iterate through the rows of the table and add the product of the item_price and quantity.
	for row in chipo.itertuples():
		out += (row.item_price * row.quantity)

	# #### BEGIN DO NOT EDIT 
	score += test(out, 39237.020000000055, 2)
	# #### END DO NOT EDIT 

	# ### Step 15. How many orders were made in the period?

	# Get the maximum value of the order_id column.
	out = chipo.order_id.describe()['max']

	# #### BEGIN DO NOT EDIT 
	score += test(out, 1834, 2)
	# #### END DO NOT EDIT 

	# ### Step 16. What is the average amount per order?

	# Calculate the sum of the item_price and divide it by the total number of orders (order_id max).
	out = (float(chipo.item_price.sum()) / chipo.order_id.describe()['max'])

	# #### BEGIN DO NOT EDIT 
	score += test(out, 18.811428571428689, 2)
	# #### END DO NOT EDIT

	# ### Step 17. How many different items are sold?

	out = chipo.item_name.describe()['unique']
	
	# #### BEGIN DO NOT EDIT 
	score += test(out, 50, 2)
	# #### END DO NOT EDIT 

	print('Your current score is: {}'.format(score))

	f_temp = open("temp_grade", "w+")
	f_temp.write(str(score))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
