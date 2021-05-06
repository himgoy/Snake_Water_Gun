import random


def game(comp, you):
    if comp == 's' and you == 'w':
        return comp
    elif comp == 's' and you == 'g':
        return you
    elif comp == 'w' and you == 'g':
        return comp
    elif comp == 'w' and you == 's':
        return you
    elif comp == 'g' and you == 's':
        return comp
    elif comp == 'g' and you == 'w':
        return you
    else:
        return 'none'


def comp_value():
    randNo = random.randint(1, 3)
    if randNo == 1:
        return 's'
    elif randNo == 2:
        return 'w'
    else:
        return 'g'


comp_score = 0
your_score = 0
a = 0
while a != 1:
    print("Computer has chosen its value from Snake(s), Water(w), or Gun(g)")
    Comp = comp_value()
    You = input("Kindly choose from Snake(s), Water(w), or Gun(g) : ")
    if You == 's' or You == 'w' or You == 'g':
        print(f"Computer has chosen {Comp}")
        w = game(Comp, You)
        if w == Comp:
            print("\nComputer is the Winner!")
            comp_score = comp_score + 1
        elif w == You:
            print("\nYou are the Winner!")
            your_score = your_score + 1
        else:
            print("There is a Tie")
        print(f"Player : {your_score}, and Computer : {comp_score}")
    else:
        print("Invalid Character")

    a = input("Press any to Continue and '1' to Exit : ")
    if a == str(2):
        break
    else:
        continue

print("\n")
if comp_score > your_score:
    print(f"The Final WINNER is COMPUTER with {comp_score} points")
elif your_score > comp_score:
    print(f"The Final WINNER is YOU with {your_score} points")
else:
    print(f"There has been a TIE with both, You and Computer Scoring {your_score} points")

while True:
    if int(input("Press 1 to exit : ")) == 1:
        break
