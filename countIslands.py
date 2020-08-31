#!/bin/env python3

from random import randint

def depth_first_search(array, i, j):
    # check if the out of bounds on array or if the next position is zero
    if i < 0 or i >= len(array):    # check if the given value is at an impossible position horizontally
        return 0
    if j < 0 or j >= len(array[i]): # check if the given value is at an impossible position vertically
        return 0
    if array[i][j] == 0:    # check if the index is already a zero
        return 0
    array[i][j] = 0 # since it is a 1, change it to a zero as it has been counted already
    depth_first_search(array, i + 1, j) # recursively check the index to the right
    depth_first_search(array, i - 1, j) # recursively check the index to the left
    depth_first_search(array, i, j + 1) # recursively check the index above
    depth_first_search(array, i, j - 1) # recursively check the index below


def count_islands(array):   # function to count the number of instances of 1s seperated
    i, j, temp = 0, 0, 0
    counter = 0     # incremental counter of islands

    if len(array) == 0: # check if the array is empty
        return counter
    for i in range (len(array)):        # search the rows
        for j in range (len(array[i])): # search the columns
            if array[i][j] == 1:    # if 1 piece of land is found
                counter += 1    # increment counter
                depth_first_search(array, i, j) # do a depth first search on the surroundings for island parts

    return counter


array = []      # define empty array
i, j = 0, 0
rows = randint(3, 6)   # rows of array
cols = randint(3, 6)    # columns of array

for i in range(rows):   # loop through array adding random values
    temp = []           # declare temp array
    for j in range(cols):
        k = randint(0, 1)         # assign k a random value for islands
        temp.append(k)  # add the new k value into the temp array
    array.append(temp)  # add the new number onto the final array

print ("\nSearched Oceanic Tiles:")  # another word for the given 2D array
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) # print statement to print out rows and cols
      for row in array]))   # display array as 2D object rather than all on one row

islands = count_islands(array)  # call the count islands function and return the number of islands

print ("\nNumber of Islands:", islands, "\n") # print the results

# # function to call and execute other functions
# def main():
#     taskNum, activities = createRandomArray()
#
#     print ("Number of Activities =", taskNum)     # prints the number of tasks
#     print ("Activities Array:", activities) # prints the entire activities array
#
#     activity_selection(taskNum, activities) # executes the activity selection algorithm and prints out the answers
#
# # beginning of the program to call main and start execution
# if __name__ == "__main__":
# 	main()
