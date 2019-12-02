# Magic 8 ball - A Pear of Pi's stage 1

import random

# define the list of possible 8 ball answers, setup the array

answers = ["Ask your wife!",
           "Stop belly aching",
           "Why are you asking me this",
           "stop your whining",
           "wait until tomorrow and ask",
           "how come you can't figure this out yourself",
           "be patient, answer might come",
           "what is your major malfunction"]
#user_input = "hello"

#Function to start the program

def start():
    input("What is your problem man, ask the 8 ball for help and it might answer? \n> ")
    
# defining function to play again

def play_again():
    user_input = input("\nAre you going to bother me again with more questions? \n>").lower()
    if user_input == "yes":
        #print("User input is: ", user_input)
        #print("Type of user_input is ", type(user_input))
        return user_input #start()
    elif user_input == "no":
        #print("User input is: ", user_input)
        return exit
    else:
        return "Please answer yes or no."

# start the program
start()
print("\nThe magic 8-ball says: ", random.choice(answers))
user_input = play_again()

#print(user_input)

while (user_input == "yes"):
    start()
    print("\nThe magic 8-ball says: ",random.choice(answers))
    user_input = play_again()

    
    
