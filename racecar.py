# used while loop in order to allow user to continue with program or end it after first round.
while True: 
    user = input("what word do you want to check? \n").lower()


    def pal_checker(user):
        """
        function used to find 
        """
        
        lst = user[:]
        backwards = user[::-1]
        if lst == backwards:
            return "\n Hooray!"
        elif lst != backwards:
            return "\n No, no, no! You lose."
        else:
            return "\n Did you even type anything?"
        
    # calling function with user input as argument    
    print(pal_checker(user))
    
    again = input("\n do you want to check another word? yes/no \n").lower() 

    if again == "yes":
        continue
    elif again == "no":
        print("goodbye")
        break
    else:
        print('you did not enter a viable option. program will now end. goodbye!')
        break
