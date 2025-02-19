from random import randint
plnum = int(input("Enter your number:"))
comnum = randint(1,21)
if plnum == comnum:
    print("You Won!")
else:
    print("Better luck next time")