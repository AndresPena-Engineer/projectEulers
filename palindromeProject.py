#Project Euler 4
#Ran on python 3.6


# Like in the problem of the given Euler, we need to find the palindrome of the largest number. 
# This code is able to find it and give the largest palindrome for the given 3 multiple of 3 digit number

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 is equal to 91 times 99. 
# Find the largest palindrome
# made from the product of two 3-digit numbers.

def isPalindrome(palindrome):
    stringOfNum = str(palindrome)
    reverseTheString = ""
    
    for i in range (len(stringOfNum) - 1, -1, -1):
        reverseTheString += stringOfNum[i]

    return reverseTheString == stringOfNum

# This part of the code returns the largest palindrome that is a multiple of two 3 digit numbers

def largestPalindromeFound():
    palindromeNum = -1
    
    # This is using the "range" that will start at 999 and end at 99 that will find the palindrome
    
    for i in range (999, 99, -1):
        
        #This is the nested loop used
        
        for j in range (i, 99, -1):
            
            # the reason I named it "notPalindrome" is because if the product is
            # palindrome and is greater than last recorded palindrome, then the code will continue
            # if not, then it will not be a palindrome
            
            if isPalindrome(i * j) and i * j > palindromeNum:
                palindromeNum = i * j
                
    # It will return -1 if a palindrome doesn't exist
    
    return palindromeNum;

#Prints out the palindrome

print ("This is the highest palindrome made from the product of two 3-digit numbers:")
print (largestPalindromeFound())