#CoLAB paired programming code 2019
#
# This code is from paired programming workshops
# -- Verified basic function
#
# Contact John T Haworth for questions

import random
import nltk #python3 -m pip install nltk
from nltk.corpus import stopwords #nltk.download('stopwords')
import requests as req
import urllib
from urllib.request import urlopen
#import urlopen #python3 -m pip install urlopen

from bs4 import BeautifulSoup 
import operator 
from collections import Counter 

stop_words = set(stopwords.words('english'))

stop_words_list = []
for word in stop_words:
    stop_words_list.append(word)
    
stop_words_list.sort()

def start(url):
    wordlist = [] 
    source_code = req.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for each_text in soup.findAll('div', {'class':'entry-content'}): 
        content = each_text.text
        words = content.lower().split() 
    for each_word in words: 
        if each_word == words[-1]:
            return clean_wordlist(wordlist)
        else:
            wordlist.append(each_word) 
            clean_wordlist(wordlist)

def clean_wordlist(wordlist): 
    clean_list =[] 
    for word in wordlist: 
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '         
        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '')             
        if len(word) > 0:
            if word not in stop_words_list:
                clean_list.append(word) 
    return create_dictionary(clean_list)
    
def create_dictionary(clean_list): 
    word_count = {} 
      
    for word in clean_list: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
    c = Counter(word_count) 
      
    # returns the most occurring elements 
    top = c.most_common(10)
    return top


top10 = start("https://www.geeksforgeeks.org/programming-language-choose/") #does not work on certain websites - unsure why
top = []
for tops in top10:
    top.append(tops[0])



#default list of words - different choice from online words
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
used = top
#defining function to start the program.
def start():
    user_input = input("Welcome to catchphrase would you like use online (1) or default (2)? \n>")
    if user_input == "1":
        used = top
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