# This is a sample Python script.
import random as ra



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dice = []
    got_all = False
    tally = 0
    while not got_all:
        dice_num = ra.randrange(1, 7, 1)
        if dice_num not in dice:
            dice.append(dice_num)
            tally = tally + 1
        if tally == 6:
            got_all = True
        print(dice)



print(dice)