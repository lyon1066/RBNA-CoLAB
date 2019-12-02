import random

while True:
    question = input("what would you like to ask?")

    response_what= ["sure",
                   "I don't think so",
                   "Tomorrow",
                   "You can do it yourself",
                   "Phone a friend",
                   "Ask your wife"]
    response_when= ["I don't know",
                   "tomorrow",
                   "never",
                   "It was yesterday",
                   "Phone a friend",
                   "Ask your wife"]
    keyword=question.split(" ",1)
    firstword=keyword[0]
    print(firstword)

    if firstword == "what":
        print(random.choice(response_what))
              
    elif firstword == 'when':
        
        print(random.choice(response_when))       
