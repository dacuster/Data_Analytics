#!/usr/bin/python -tt
# Credit Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# Please do not edit anything within
# #### BEGIN DO NOT EDIT and
# #### END DO NOT EDIT lines

# A. Divide_list
# Divide one list into two lists so that all numbers that are
# smaller than the given midpoint are in the first list called lower and the
# rest are in the second list called upper. Return the lower list
# If midpoint = 5, and the list is range(1,10) lower = [1,2,3,4] and
# upper = [5,6,7,8,9]
# function should return [1,2,3,4]. Numbers should remain in original order in
# the list.


def divide_list(original_list, midpoint):
    # Empty upper and lower value lists.
    lowerList = []
    upperList = []

    # Loop through the given list.
    for currentIndex in original_list:
        # Add the lower value to the lower list.
        if currentIndex < midpoint:
            lowerList.append(currentIndex)
        # Add the higher value to the upper list.
        else:
            upperList.append(currentIndex)

    # Return the lower valued list.
    return lowerList


# B. Find_minimum
# Find minimum of the list. You can assume the maximum value for any list's
# minimum is 10000,
# if it is more than 10000 return a msg that says "Too large"
def find_min(original_list):
    # Create starting reference variables.
    maximum = 10000
    minimum = maximum

    # Iterate through the given list.
    for currentIndex in original_list:
        # The current element is lower than the current value.
        if currentIndex < minimum:
            minimum = currentIndex

    # Return lowest value if it isn't larger than the maximum value.
    if minimum >= maximum:
        return "Too large"
    else:
        return minimum


# C. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    # Create empty result list to return.
    result = []

    # Iterate through the given list.
    for currentIndex in nums:
        # Add the current iteration to the result list if it's empty or is not
        # the same as the last value in the result list.
        if len(result) == 0 or currentIndex != result[-1]:
            result.append(currentIndex)

    # Return the result list.
    return result


# BEGIN DO NOT EDIT
# Provided simple test() function used in main() to # what each function
# returns vs. what it's supposed to return.
def test(got, expected, points=1):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

    grade = 0
    if(prefix == ' OK '):
        grade = points

    return grade


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    score = 0

    print('divide_list')
    # Each line calls divide_list, compares its result to the expected for that
    # call.
    score += test(divide_list(range(10), 5), [0, 1, 2, 3, 4])
    score += test(divide_list([5, 4, 3, 6, 10, 17], 3), [])
    score += test(divide_list([5, 4, 3, 6, 10, 17], 10), [5, 4, 3, 6])
    score += test(divide_list(range(100), 50), list(range(50)))

    score += test(find_min(range(10)), 0)
    score += test(find_min([5, 4, 3, 6, 10, 17, 100001]), 3)
    score += test(find_min([5, 4, 3, 6, 10, 17]), 3)
    score += test(find_min(range(100)), 0)

    print('remove_adjacent')
    score += test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    score += test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    score += test(remove_adjacent([]), [])

    print('Your current score is: {}'.format(score))

    f_temp = open("temp_grade", "w+")
    f_temp.write(str(score))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
# END DO NOT EDIT
