# to find whether the given word is a palindrome.
def reverse(word):
    return word[::-1]

#calling rev function
def ispalindrome(word):
    rev = reverse(word)
#checking if the word is equal from both sides
    if(word ==rev):
        return True
    return False    

word= "malayalam"    
output = ispalindrome(word)

if output == 1:
    print("Yes")
else:
    print("No")    