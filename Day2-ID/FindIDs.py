#!/usr/bin/env python3 

import sys
import re


def main():
    filePath = sys.argv[1]
    file = open(filePath)
    line = file.readline()
    file.close()

    idList = line.split(",")

    finalIDCount = 0

    # Find all invalid ID's in each range
    for range in idList:
        ab = range.split("-")
        a = int(ab[0])
        b = int(ab[1])

        while a <= b:
            if checkPattern(a):
                finalIDCount+=a
            a+=1

    print("The final count is: "+ str(finalIDCount))
        

def checkPattern(x):
    digitList = list(str(x))
    print(digitList)

    digits = len(digitList)
    y = digits/2
    
    divider =1 # divider = number of digits in sequence
    while divider <= y: 
        isPattern = 0 # 0 = untouched, 1 = true, 2 = false
        
        div = digits/divider

        #only whole sequences of number lengths divisible by the divider
        if int(div) != div:
            divider+=1
            continue
        
        a = ""

        # find sequence a
        countSeqDigits = 0
        while countSeqDigits < divider:
            a += digitList[countSeqDigits]
            countSeqDigits+=1

        #check for sequence in following numbers
        while countSeqDigits < digits:
            if isPattern == 2: #if found sequence not a pattern already
                countSeqDigits+=1
                continue
            
            b = ""
            seqDigitCount = 0 # always count to number of sequence, and start again
            while seqDigitCount < divider:
                b += digitList[countSeqDigits]
                seqDigitCount+=1
                countSeqDigits+=1
            if a == b and isPattern<2:
                isPattern = 1
            else:
                isPattern = 2

        if isPattern == 1:
            return True
        divider+=1
    # if not returned true yet, return false
    return False



if __name__ == "__main__": 
  main()