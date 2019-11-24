# CoLAB paired programming code 2019
#
# This code is from paired programming workshops
#
# Contact John T Haworth for questions

# function to reverse the order of a word
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

# start running form here  
print('Enter a word')
s = input()
s1 = reverse(s)

if s == s1:
    print(s + ' is a palindrome')
else:
    print(s + ' is not a palindrome')
    
