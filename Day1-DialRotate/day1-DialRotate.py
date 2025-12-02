#!/usr/bin/env python3 

import sys
import re


def main():
    filePath = sys.argv[1]
    file = open(filePath)
    list = []
    for line in file:
        list.append(line)
    file.close()

    dial = 50
    password = 0

    for x in list:
        nList = re.findall(r'\d+',x)
        n = int(nList[0])
        # print(x[0],n)
        
        # if R count up
        if "R" in x[0]:
            dial += n 
            while dial > 99:
                dial -= 100
                password+=1
        else: # if L count down
            if dial == 0:
                dial = 100 # Account for extra adding
            dial -= n 
            
            while dial < 0:
                dial += 100
                password+=1
                
            if dial == 0:
                password+=1
        # print(dial) 
    
    print("The final password is:")
    print(password)






if __name__ == "__main__": 
  main()