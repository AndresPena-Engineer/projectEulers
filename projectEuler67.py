#Project Euler 67
#Python 2.7.14

 # Importing the time module 
import time

 # Start of execution time
start = time.time()

 # Open the text file triangle, given by the problem
with open('triangle.txt') as txt:
 
 # Read All the digits in the file
 digit = txt.read()

 # Splitting the digits into a list
digit = digit.strip().split('\n')

 # Converting the list into an Int
for i in xrange(1,len(digit)):
 digit[i] = digit[i].strip().split(' ')
 digit[i] = [int(x) for x in digit[i]]

 # Stating the first digit in the triangle.txt file
digit[0] = [59]

 # In case the digit of itterations needs to be known, this is the start
itterationNum = 0

 # For loop in order to find the digit
for i in xrange(len(digit)-2,-1,-1):
 for j in xrange(len(digit[i])):
  digit[i][j] = digit[i][j] + max(digit[i+1][j], digit[i+1][j+1])
  itterationNum += 1
 digit.pop()

print 'The digit found is: {} '.format(digit[0][0],itterationNum)
end = time.time()

 # Printing the total time (execution time - total time = time in milliseconds)
print 'Time in milliseconds:'
print end-start 