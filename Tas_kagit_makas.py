import random
List=["stone","paper","scissors"]
pc=random.choice(List)
player=input("[stone,paper,scissors]").capitalize()

print("Computer",pc,"produced your",player,"produced")



if pc==player:
    print("draw")


if pc=="stone" and player=="scissors":
    print("You lost..")

if pc=="scissors" and player=="stone":
    print("You lost..")

if pc=="scissors" and player=="paper":
    print("You lost..")



if pc=="scissors" and player=="stone":
    print("You win..")

if pc=="stone" and player=="paper":
    print("You win..")

if pc=="paper" and player=="scissors":
    print("You win..")    

else:
    print("You have selected an option not on the list.")
