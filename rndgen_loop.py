import random
rand_num = random.randint(1,50)
rndnumstr=str(rand_num)
           
name = input("What is your name? ")
my_number = input("Hello "+name+", please choose a number between 1 and 50: ")
my_number = int(my_number) 
counter = 1
trials = 4
remaining = 4

while counter <= trials:
    if(my_number == rand_num):
        print("That number is correct!");
        quit()
    if(my_number < rand_num):
        print("That's too small!")
        if remaining == 1:
         print ("You have "+str(remaining)+" guess left")
        else:
         print ("You have "+str(remaining)+" guesses left")
    if(my_number > rand_num):
        print("That's too big!")
        if remaining == 1: 
         print ("You have "+str(remaining)+" guess left")
        else:
         print ("You have "+str(remaining)+" guesses left")
    remaining = remaining-1
    my_number = input("please choose a number between 1 and 50: ")
    my_number = int(my_number)
    counter=counter+1


print("Sorry you lost, my number was "+rndnumstr+"")
