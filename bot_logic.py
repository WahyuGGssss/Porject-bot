import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    print(password)

def coinflip():
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    else:
        return "Tails"
    
def roll_dice():
    return "the dice is", random.randint(1,6)








