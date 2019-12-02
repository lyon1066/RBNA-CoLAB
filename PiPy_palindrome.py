word = input('Please input a word: ')
print (word)

length = len(word)

n = 0
while n <= (length - 1):
    if word[n] == word[length - (n + 1)]:
        n += 1
      
    else:
        print("Word is not a palindrome.")
        break
    
    if n == length:
        print("Word is a palindrome.")