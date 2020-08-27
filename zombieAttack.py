#!/bin/env python3

from random import randint

def zombie_attack(array):   # function to count the number of new zombies
    i, j = 0, 0
    zom_loc = []    # store location of zombies in array
    humans = 0  # count number of humans in array
    zombies = 0 # count number of zombies in array
    days = 0    # count number of days that have gone by

    for i in range(len(array)): # loop through array and find all zombies and humans
        for j in range(len(array[i])):
            if array[i][j] == 2:    # check for zombies
                zom_loc.append([i, j])  # add zombie coordinates to zombies array
            elif array[i][j] == 1:  # check for humans
                humans += 1         # add human to human counter
    if humans == 0: # if there are no humans then return 0 days
        return 0
    zombies = len(zom_loc)
    local = [[-1,0], [1,0], [0,-1], [0,1]]
    while (zom_loc):    # loop through all zombies until they have finished attacking
        days += 1   # increment number of days
        for i in range(len(zom_loc)):   # loop through
            attacking_zombie = zom_loc.pop(0)   # remove the first zombie location and search surrounding areas
            for j in local: # look through all adjacent indexes
                attack = [attacking_zombie[0] + j[0], attacking_zombie[1] + j[1]]   # position of local indexes
                if (attack[0] >= 0 and attack[0] < len(array)):         # if width is valid
                    if (attack[1] >= 0 and attack[1] < len(array[0])):  # if height is valid
                        if (array[attack[0]][attack[1]] == 1):  # if there is a human at the spot of attack
                            array[attack[0]][attack[1]] = 2     # convert human to zombie
                            humans -= 1     # decrement number of humans
                            zombies += 1    # increment number of zombies
                            if humans == 0: # if no more humans
                                return days, humans, zombies, days  # return that the zombies won
                            zom_loc.append(attack)  # add the zombie to the array

    return -1, humans, zombies, days    # return that humans survived the attack


array = []      # define empty array
i, j, humans, zombies, days = 0, 0, 0, 0, 0
rows = randint(3, 10)   # length of array
cols = randint(3, 10)    # width of array
results = -5

for i in range(rows):   # loop through array adding random values
    temp = []    # declare temp array
    for j in range(cols):
        k = randint(0, 2)         # assign k a random value for islands
        temp.append(k)  # add the new k value into the temp array
    array.append(temp)  # add the new number onto the final array

print ("\nInfected City Square ( Day 0 ): ")   # another word for the 2D array
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) # print statement to print out rows and cols
      for row in array]))   # display array as 2D object rather than all on one row

results, humans, zombies, days = zombie_attack(array)

if results == -5:   # if the value for results has not changed it is an error
    print ("\n\nError in Zombie Attack\n")

if results == 0:    # if there were no humans to begin with and zombies
    print("No Humans in the Square")

if results == -1:   # if the humans have survived the zombie attack and can not be turned
    print("\n\nThe Humans Have Survived!\n")

else:   # the zombies have beaten all humans
    print("\n\nThe Zombies Have Won.\n")

print("Number of Survivors:", humans)   # printing function stats for humans
print("Number of Zombies:  ", zombies)  # printing function stats for zombies
print("Days Survived:      ", days)           # printing function stats for days

print ("\nInfected City Square ( Day", days, "):")  # print before city square with how many days before function ended
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) # print statement to print out rows and cols
      for row in array]))   # display array as 2D object rather than all on one row
print()
