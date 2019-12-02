  
# CoLAB paired programming code 2019
#
# This code is from paired programming workshops
# -- Verified function

# Contact John T Haworth for questions
#ask user if wants hex to decimal or decimal to hex
guess = input("Enter '1' for Hex to Dec conversion, any other positive value for decimal to hex: ")
guess = int(guess)

if guess > 1:
    decVal = input("Enter Decimal value: ")
    print("The original Decimal value you entered: " + str(decVal))
    #the next statement is not converting from dec to hex, needs work
    hexVal = int(str(decVal),16)
    hexVal = hex (hexVal)
    print("Your hex value is " + str(hexVal) + " of decimal value of " + str(decVal))

else:
    #asks user for hex input
    hexVal = input("Enter Hex value: ").lstrip("0x")
    print("The original Hex value you entered: " + str(hexVal))
    decimalVal = int(str(hexVal),16)
    #converts input to integer and to a string, ready for printing
    print("Your decimal value is " + str(decimalVal) + " of hex value of " + str(hexVal))
