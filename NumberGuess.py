from random import *
 
class NumberGuess:
    def __init__(self):
        self.secret_number = None

    # generating a secret number for guess
    def generateSecretNumber(self):
        start=int(input("Enter starting point ="))
        end=int(input("Enter ending point ="))
        self.secret_number=randint(start,end)
    
    # checks the guessed number is correct or not.
    def guessNumber(self,guessed_number):
        if guessed_number==self.secret_number:
            return True
        else:
            if guess > game.secret_number:
                print("Hint:Your guess is too high !\n")
            else :
                print("Hint:Your guess is too low !\n")
            False


print("-------Number Guessing Game-------")
print("You have a 3 chance.\n")

game=NumberGuess()
game.generateSecretNumber()
chance=0
# print(game.secret_number)
flag=False

while chance<3:
    print(f"Chance ({chance+1}/3)")
    try:
        guess=int(input("Enter your guess = "))
    except:
        print("\nPlease Enter Integer values only! \n")
        continue

    if game.guessNumber(guess):
        print("Your guess is Correct !")
        flag=True
        break
    chance+=1

if flag==False:
    print("You Lose !")



