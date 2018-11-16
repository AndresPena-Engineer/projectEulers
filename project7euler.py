# Andres Pena
# Project Euler 7
# 4/22/2018
# Ran on python 3.6


#----Problem 7 --- 

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# This part returns True if parameter n is a prime number, 
# False if composite and "Neither prime, nor composite" if neither. 

def isPrime(n):
    if n < 2: return "Its not prime, and it's not a composite number"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# On this part of the code it returns the nth prime number, if the number is found, 
# which is 104743, then it will print out.

def nthPrime(n):
    numberOfPrimes = 0
    prime = 1

    while numberOfPrimes < n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

# This will print out the 10, 001 st prime number

print ("This is the 10,001 st prime number: ")
print(nthPrime(10001))