from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = 20

dice_type = document.getElementById("diesides").value 
print (dice_type)
if dice_type == "D2":
    dice_type = 2 
elif dice_type == "D4":
    dice_type = 4 
elif dice_type == "D6":
    dice_type= 6
elif dice_type == "D8":
    dice_type = 8
elif dice_type== "D10":
    dice_type = 10
elif dice_type == "D12":
    dice_type = 12
elif dice_type == "D20":
    dice_type = 20 
elif dice_type == "D100":
    dice_type = 100


def select_face_option(event):
    global dice_type  # use global var named dice_type

    dice_type = document.getElementById("diesides").value 
    print (dice_type)
    if dice_type == "D2":
        dice_type = 2 
    elif dice_type == "D4":
        dice_type = 4 
    elif dice_type == "D6":
        dice_type= 6
    elif dice_type == "D8":
        dice_type = 8
    elif dice_type== "D10":
        dice_type = 10
    elif dice_type == "D12":
        dice_type = 12
    elif dice_type == "D20":
        dice_type = 20 
    elif dice_type == "D100":
        dice_type = 100

def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    rolltimes = document.getElementById("rolltimes").value 
    rolltimes = int(rolltimes)  
    #document.querySelector("div#roll-history").innerHTML = ""
    
    output = "the rolls are . . . "
    for roll in range(rolltimes):
        result = dice.roll_dice(dice_type)
        output = output + str(result) + ", "
    document.querySelector("div#roll-history").innerHTML = output 

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""
