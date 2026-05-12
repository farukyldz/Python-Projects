
import random

random=random.randint(1,20)
num=int (input("Guess a number:"))
score=5
while score>0:
    if random==num:
        print("You guessed the number correctly :)",score)
        break

    else:
        print("You didn’t guess the number correctly :(,Your score:",score)
        score=score-1
        num=int (input("Guess a number:"))
        
        

