import random
print("Number guessing game")
number = random.randint(1, 9)
chances = 0

print("Guess a number between 1 and 9 ")

while chances < 5:
    usrinput = int(input("Enter your guessed Number:- "))
    if usrinput == number:
        print("Congratulation YOU WON!!!")
        break
    elif usrinput < number:
        print("Your guess was too low, Guess a number higher than it ", usrinput)
    else:
        print("Your guess was too high, Guess a number lower than it ", usrinput)
    chances += 1
if chances == 5:
    print("YOU LOSE!!! The number is", number)