# CoLAB paired programming code 2019
#
# This code is from paired programming workshops
#
# Contact John T Haworth for questions

import random


#define list of possible 8 ball answers
answers=[
    "It Is Certain",
    "Outlook Is Good",
    "You May Rely On It",
    "Ask Again Later",
    "Concentrate and Ask Again",
    "Reply Hazy. Try Again",
    "My Reply Is No",
    "My Sources Say No"
]

#defining function to start the program.
def start():
    input("welcome to the magic 8 ball please ask a question about your future \n> ")


#defining function to have user play program again.
def play_again():
    user_input = input("\nWould you like to ask another question? \n > ").lower()
    if user_input == "yes":
        return start()
    elif user_input == "no":
        return exit
    else:
        return "Please answer yes or no."
        
#start the whole program.
start()
print("\nThe magic 8-ball says: ", random.choice(answers))
play_again()




