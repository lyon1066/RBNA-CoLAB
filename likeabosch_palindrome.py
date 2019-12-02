def reverse(word):
        str=""
        for i in word:
            str = i+ str
        return str
    

print('Enter Word:')
word = input()
revword = reverse(word.strip())

if word.strip() == revword:
    print('Palindrome confirmed')
    
else:
    print('Not a Palindrome')
    
