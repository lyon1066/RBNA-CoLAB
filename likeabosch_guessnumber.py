import random
s = random.randrange(1,100)
guess= 101
guesscount = 0
while guess != s:
    print("What is your guess")
    guesscount = 1 + guesscount
    guess = input()
    guess= int(guess)
    if guess > s:
        print("You are too high")
    elif guess < s:
        print("You are too low")
    elif guess == s:
        print("You got it, Congrats!")
    else:
        print("Error")
    
print("Your attempts were" + str(guesscount))