import random
import sys
import os
import math


'''
01/06/2020
This program determine whether a number is a palindrome or not.
The running complication is N/2.

Jordan Yefet.
'''

def paliOrNot(num):
    try:
        test = float(num)
        numToStr = str(num)
        numToStr = numToStr.replace(".", "")
        for i in range(0, math.ceil(len(numToStr)/2)):
            isPali = False
            left = int(numToStr[i])
            right = int(numToStr[len(numToStr)-1-i])
            if(left-right == 0):
                isPali = True
                continue
        if(isPali):
            print(numToStr + " is a palindrome.")
        else:
            print(numToStr + " is NOT palindrome.")
    except:
        print("The input is not a number.")




inputList = [12321, 12.321, 123321, 647293, "jordan"]

for input in inputList:
    paliOrNot(input)







