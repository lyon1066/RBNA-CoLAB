import Image
hexVal = input("Enter Hex value: ").lstrip("0x")
print("The original Hex value you entered: " + str(hexVal))
decimalVal = int(str(hexVal),16)

print("Your decimal value is " + str(decimalVal) + " of hex value of " + str(hexVal))

image = Image.open('image.jpg')
image.show()