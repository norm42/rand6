# we use the python random lib to generate the dice
import random as ra



# Test program for dice generation.
# This one generates a random sequence of dice with unique values
if __name__ == '__main__':
    dice = []
    got_all = False
    tally = 0
    while not got_all:
        # randrange is [), so need to use [1,7)
        # by integer values to get dice 1-6
        # changing 7 to a larger number can see how long it takes to converge
        dice_num = ra.randrange(1, 7, 1)
        # check to see if the dice number does not exist
        # if so then add
        if dice_num not in dice:
            dice.append(dice_num)
            tally = tally + 1
        if tally == 6:
            got_all = True  # we have all 6 slots filled
        print(dice)     # visualize the iterations



print(dice)