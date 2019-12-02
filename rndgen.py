import random
rand_num = random.randint(1,50)
rndnumstr=str(rand_num)
           
name = input("What is your name? ")
my_number = input("Hello "+name+", please choose a number between 1 and 50: ")
my_number = int(my_number) 


if(my_number == rand_num):
    print("That number is correct!");
    quit()
if(my_number < rand_num):
    print("That's too small!")
if(my_number > rand_num):
    print("That's too big!")
my_number = input("please choose a number between 1 and 50: ")
my_number = int(my_number)

if(my_number == rand_num):
    print("That number is correct!");
    quit()
if(my_number < rand_num):
    print("That's too small!")
if(my_number > rand_num):
    print("That's too big!")
my_number = input("please choose a number between 1 and 50: ")
my_number = int(my_number)

if(my_number == rand_num):
    print("That number is correct!");
    quit()
if(my_number < rand_num):
    print("That's too small!")
if(my_number > rand_num):
    print("That's too big!")
my_number = input("please choose a number between 1 and 50: ")
my_number = int(my_number)

if(my_number == rand_num):
    print("That number is correct!");
    quit()
if(my_number < rand_num):
    print("That's too small!")
if(my_number > rand_num):
    print("That's too big!")
my_number = input("please choose a number between 1 and 50: ")
my_number = int(my_number)

if(my_number == rand_num):
    print("That number is correct!");
    quit()
if(my_number < rand_num):
    print("That's too small!")
if(my_number > rand_num):
    print("That's too big!")
print("Sorry you lost, my number was "+rndnumstr+"")

