#!/usr/bin/env python3 

import sys
import re


def main():
    filePath = sys.argv[1]
    file = open(filePath)
    listJolts = []
    for line in file:
        listJolts.append(line)
    file.close()
    
    finalJoltCount = 0
    
    for x in listJolts:
        digitList = list(str(x))

        #Find first digit
        pos = 0
        a = digitList[pos]
        count = 1

        while count < len(digitList) -2:
            if digitList[count] > a:
                a = digitList[count]
                pos = count
            count+=1
        
        
        #find second digit
        b = digitList[pos + 1]
        count = pos + 2
        while count < len(digitList):
            if digitList[count] > b:
                b = digitList[count]
            count+=1
        
        ab = str(a) + str(b)

        print("The largest number is " + ab)

        finalJoltCount += int(ab)
    
    print("The final jolt count is " + str(finalJoltCount))





if __name__ == "__main__": 
  main()