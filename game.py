
import random

print("Rules of the game: \n" + "Rock beats scissors \n" + "Paper beats rock \n" + "Scissors beats paper")

aList = ["R", "S", "P"]

while True:
    print("Enter your choice \n R for Rock, \n P for Paper, \n and \n S for Scissors")

    option = input("User turn: ")

    while option not in aList:
        option = input("Enter a correct choice ")
    if option == "R":
        name = "Rock"
    elif option == "P":
        name = "Paper"
    else:
        name = "Scissors"

    print("User choice is " + name)
    print("\nNow its computer's turn .......")

    comp = random.choice(aList) 
    if comp == option:
        print("It's a tie.")
        continue
    if comp == "[R]":
        comp_name = "Rock"
    elif comp == "[P]":
        comp_name = "Paper"
    else:
        comp_name = "Scissors"

    print("Computer choice is " + comp_name)

    if ((option == 'R' and comp == ['P']) or (comp == ['R'] and option == 'P')):
        print("Paper wins", end = "")
        result = "Paper"
    elif ((option=='R' and comp==['S']) or (option=='S' and comp==['R'])):
        print('Rock wins', end = '')
        result = 'Rock'
    else:
        print("Scissors wins", end = "")
        result = "Scissors"

    if result == name:
        print('\n<== User wins ==>')
    else:
        print('\n<== Computer wins ==>')

    print("Do you want to play again? (Yes/No)") 
    ans = input()

    if ans == 'Yes' or 'yes':
        continue
    else:
        break

print("\nThanks for playing")

