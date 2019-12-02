# CoLAB paired programming code 2019
#
# This code is from paired programming workshops
# -- Verified basic function
#
# Contact John T Haworth for questions

import random
from lxml import html
import requests
from lxml import html
import requests

page = requests.get('https://www.ef.edu/english-resources/english-vocabulary/top-1000-words')
tree = html.fromstring(page.content)

onlinewords =tree.xpath('//p /text()')
onlinewords.pop(0)

#define list of possible 8 ball answers
answers=[
"whatever",
"chicken",
"bleach",
"cog",
"through",
"cot",
"think",
"inn",
"buddy",
"coop",
"clay",
"twitterpated",
"feudalism",
"blueprint",
"cardboard",
"Zen",
"sip",
"blur",
"blossom",
"wish",
"whiplash",
"beanstalk",
"darts",
"crow",
"chime",
"nes"    
]
used = onlinewords
#defining function to start the program.
def start():
    user_input = input("Welcome to catchphrase would you like use online (1) or stored (2)? \n>")
    if user_input == "1":
        used = onlinewords
    elif user_input == "2":
        used = answers
    else:
        return "Please enter online or stored"
#defining function to have user play program again.
def play_again():
    user_input = input("\nPress enter to play again, type stop to end? \n > ").lower()
    if user_input == "":
        print("\nDescribe: ", random.choice(used))
        return play_again()
    elif user_input == "stop":
        return exit
    else:
        return "Please answer yes or no."
        
#start the whole program.
start()
print("\nDescribe: ", random.choice(used))
play_again()