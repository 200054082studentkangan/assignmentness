# put your dice_roll() function in this file
import random as rndm

def roll_dice(sides):
    num = rndm.randint(1,sides)
    return num