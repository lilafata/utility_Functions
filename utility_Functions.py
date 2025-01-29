##########################################################################################################
#
# DATE  :      01/24/2025
# AUTHOR:      Lila Fata
# FILE  :      utility_Functions.py
# DESCRIPTION: This script file contains the following utility functions:
#
#              * FibonacciNumber() - determines the Fibonacci of input number
#              * FactorialNumber() - determines the Factorial of input number
#              * ReverseString() - reverses the input string
#              * PrimeNumber() - determines if input number is prime
#              * Palindrome() - provides the palindrome of the input string
#              * LongestWord() - determines the longest word from input string
#              * UserNameValidation() - determines if input string is valid user name
#              * MaxStockProfit() - determines the maximum profit from list of prices
#
# NOTE:
# 1) This program was executed using the IDLE Python 3.7 Shell on a Windows 10 laptop
# 2) Sample Output 'utility_Functions_SAMPLEOutput.txt is included
#
##########################################################################################################

import os
import math
import re


def FibonacciNumber(nbr):
    if nbr < 0:
        print("Incorrect input")
    elif nbr == 0:
        return 0
    elif nbr == 1 or nbr == 2:
        return 1
    else:
        return FibonacciNumber(nbr-1) + FibonacciNumber(nbr-2)
    
def FactorialNumber(nbr):

    print ("num = ", nbr)
    if nbr < 2:
        return int(1)
    else:
        return nbr * FactorialNumber(nbr-1)

def ReverseString(inputStr):

  print("Input String = ", inputStr)
  inputStr = inputStr[::-1]
  return inputStr

def PrimeNumber(nbr):

    print ("num = ", nbr)
    isPrime = False
    cnt = 0
    for i in range(1, int(nbr)+1):
        if nbr % i == 0:
            cnt=cnt+1
            if cnt > 2:
                isPrime = False
                break
    if nbr <= 1 or cnt > 2:
        isPrime = False
        print(nbr, "is not a prime number")
    else:
        print(nbr, "is a prime number")
    return

def Palindrome(inputStr):

    print ("Input String = ", inputStr)
    if inputStr == inputStr[::-1]:
        print(inputStr, "is a palindrome")
    else:
        print(inputStr, "is not a palindrome")

def LongestWord(inputStr):

    print ("Input String = ", inputStr)
    words = re.split("[^a-zA-Z0-9]+",inputStr)
    longestWord = ""
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    print("Longest Word is: ", longestWord)
    return

def UserNameValidation(inputStr):

    print ("Input String = ", inputStr)
    validation = True
    if inputStr[-1] == "_":
        validation = False
        print (inputStr, " is an invalid user name")
        return
    if len(inputStr) >= 4 and len(inputStr) <= 25 and inputStr[0].isalpha():
        for char in inputStr:
            if not (char.isalnum() or char == '_'):
                validation = False
                print (inputStr, " is an invalid user name")
                break
    else:
        validation = False
        print (inputStr, " is an invalid user name")
    if validation == True:
        print (inputStr, " is a valid user name")
    return

def MaxStockProfit(inputArray):

    print ("Input Prices = ", inputArray)
    priceList = inputArray.split(",")
    prices = [int(nbr) for nbr in priceList]
    curProfit = 0
    profit = 0
    buyPrice = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] > prices[i]:
                buyPrice = prices[i]
                sellPrice = prices[j]
                curProfit = sellPrice - buyPrice
            if curProfit > profit:
                profit = curProfit
        if profit == 0:
            profit = -1
    print ("Max profit is: ", profit)
    return


def main():
    
    while True:
        numFib = input("Enter input for FibonacciNumber:  ")
        if numFib == "q":
            break
        print(FibonacciNumber(int(numFib)))
        
    while True:
        numFact = input("Enter input for FactorialNumber:  ")
        if numFact == "q":
            break
        print(FactorialNumber(int(numFact)))

    while True:
        inputReverse = input("Enter input for ReverseString:  ")
        if inputReverse == "q":
            break
        print(ReverseString(inputReverse))

    while True:
        numPrime = input("Enter input for PrimeNumber:  ")
        if numPrime == "q":
            break
        PrimeNumber(int(numPrime))

    while True:
        inputPalindrome = input("Enter input for Palindrome:  ")
        if inputPalindrome == "q":
            break
        Palindrome(inputPalindrome)

    while True:
        inputWords = input("Enter input for LongestWord:  ")
        if inputWords == "q":
            break
        LongestWord(inputWords)

    while True:
        inputUserName = input("Enter input for UserName:  ")
        if inputUserName == "q":
            break
        UserNameValidation(inputUserName)
        
    while True:
        inputPrices = input("Enter input StockPrices:  ")
        if inputPrices == "q":
            break
        MaxStockProfit(inputPrices)
        

if __name__ == "__main__":
    main()
