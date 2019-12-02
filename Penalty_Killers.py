# Penalty Killers Ice Hockey Penalty Reference Tool
# Ver 1.0.0  -- 2 December 2019
# Dennis Polehna and Jim Brown


#defining function to start the program.

# -------------------------------------------------------------------------------------------------------------------------
# This portion defines what the start function does.
def start():
    print ("Welcome to the Penaly Killers Ice Hockey Penalty Definition Tool.")
    print ("Below is the list of Penalties and their respective scoresheet abreviation.")
    print ("          Hooking --> 'H'")
    print ("          Tripping -->  'T'")
    print ("          Roughing -->  'R'")    
    print ("          Boarding -->  'B'")    
    print ("          Charging -->  'C'")    
    print ("          Interference -->  'I'")
    print ("          Cross-Checking -->  'X'")    
    print ("          Misconduct -->  'M'")    
    print ("          Unsportsmanlike Conduct -->  'U'")
    print ("          Too Many Men on the Ice -->  'TM'")
    print ("          Bench Minor -->  'BM'")    

# -------------------------------------------------------------------------------------------------------------------------
#
# This command asks the user for the input of the penalty abreviation.
    abrv = input ("Enter penalty abreviation:  ") .upper()
#
# -------------------------------------------------------------------------------------------------------------------------
# The if statements below determine which feedback to give the user based on their input.
    if abrv == "H":
        print ("\nHooking is the use of the stick to slow another player down. \nClassification: Minor\nLength of Penalty: 2 minutes")
    elif abrv == "T":
        print ("\nTripping is the use of a stick or leg to trip an opponent. \nClassification: Minor\nLength of Penalty: 2 minutes") 
    elif abrv == "R":
        print ("\nRoughing is any contact that’s unnecessary such as pushing and shoving or aggressive contact after a whistle. \nClassification: Minor\nLength of Penalty: 2 Minutes")
    elif abrv == "B":
        print ("\nBoarding is any illegal action that causes a player to be thrown into the boards. \nClassification: Minor\nLength of Penalty: 2 or 5 Minutes")
    elif abrv == "C":
        print ("\nCharging is called when a player takes several strides to speed up when checking an opponent. \nClassification: Minor\nLength of Penalty: 2 Minutes")
    elif abrv == "I":
        print ("\nInterference is the use of contact to stop or slow down a player who’s not in possession of the puck. \nClassification: Minor\nLength of Penalty: 2 Minutes")
    elif abrv == "X":
        print ("\nCross-checking occurs when a player has both hands on the stick and uses it to deliver a check when no part of the stick is on the ice. \nClassification: Minor\nLength of Penalty: 2 or 5 Minutes")
    elif abrv == "M":
        print ("\nA misconduct penalty is any action deemed worthy of an extended penalty. Some examples include using abusive language, challenging an official's ruling or intentionally disrupting the game. \nClassification: Major\nLength of Penalty: 10 Minutes")
    elif abrv == "U":
        print ("\nHooking is the use of the stick to slow another player down. \nClassification: Minor\nLength of Penalty: 2 Minutes")
    elif abrv == "TM":
        print ("\nHooking is the use of the stick to slow another player down. \nClassification: Minor\nLength of Penalty: 2 Minutes")
    elif abrv == "BM":
        print ("\nHooking is the use of the stick to slow another player down. \nClassification: Minor\nLength of Penalty: 2 Minutes")

    else:
        return "Please enter valid penalty abreviation."
#    elif abrv == "exit":
#        return exit
    


#defining function to have user play program again.
def play_again():
    user_input = input("\nDefine another penalty? \n > ").lower()
    if user_input == "yes":
        return start()
    elif user_input == "no":
        return exit
    else:
        return "Please answer yes or no."
start()
play_again()