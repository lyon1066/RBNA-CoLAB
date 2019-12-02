import random

while True:
    
    user_question = input("what do you want to ask the magic 8 ball? \n")

    responses = ["it is certain",
                 "it is decidedly so",
                 "without a doubt",
                 "yes",
                 "Most likely",
                 "maybe",
                 "outlook good",
                 "no doubt, bro",
                 "no way, bro",
                 "broooo, maybe"]

    print("\n" + random.choice(responses)+ "\n")

    again = input("do you want to ask another question? yes/no \n").lower() 

    if again == "yes":
        continue
    elif again == "no":
        print("goodbye")
        break
    else:
        print('you did not enter a viable option. program will now end. goodbye!')
        break
        
    




             
             
        


