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

        if "\n" in digitList:
            digitList.remove("\n")

        jolt = ""
        digit = 1
        pos = 0

        a = digitList[pos]
        count = 1


        while digit <= 12:
            print("finding digit " + str(digit))
            while count < len(digitList) - (12-digit): # count position should be less than the number of digits you need remaining
                print("looking if " + str(a) + " is still the biggest v " + str(digitList[count]))
                print(" with " + str(len(digitList) - (12-digit)) + " digits remaining" + " at pos " + str(count))
                if digitList[count] > a:
                    a = digitList[count]
                    pos = count
                count+=1
            print("found " + str(a))
            jolt += a

            # set for next digit
            if digit < 12:
                pos+=1
                count = pos
                a = digitList[count]
                count+=1
            digit+=1

        print("The largest number is " + jolt)

        finalJoltCount += int(jolt)
    
    print("The final jolt count is " + str(finalJoltCount))





if __name__ == "__main__": 
  main()