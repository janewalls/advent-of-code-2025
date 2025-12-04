#!/usr/bin/env python3 

import sys
import re


def main():
    filePath = sys.argv[1]
    file = open(filePath)
    listRows = []
    for line in file:
        items = list(line)
        if "\n" in items:
            items.remove("\n")
        listRows.append(items)
    file.close()

    overallCount = 0
    rowPos = 0

    print(len(listRows))

    for row in listRows:
        colPos = 0
        print(row)
        for place in row:
            rollCount = 0
            print("I am looking at " + place)
            if place == "@":
                # Check all positions
                if colPos > 0 and rowPos > 0:
                    if listRows[rowPos-1][colPos-1] == "@":
                        rollCount+=1
                if rowPos > 0: 
                    if listRows[rowPos-1][colPos] == "@":
                        rollCount+=1
                if rowPos > 0:
                    if colPos < len(listRows[rowPos-1]) -1 and listRows[rowPos-1][colPos+1] == "@":
                        rollCount+=1
                if colPos > 0:
                    if listRows[rowPos][colPos-1] == "@":
                        rollCount+=1
                if colPos < len(listRows[rowPos]) -1 and listRows[rowPos][colPos+1] == "@":
                    rollCount+=1
                if colPos > 0:
                    if rowPos < len(listRows) -1 and listRows[rowPos+1][colPos-1] == "@":
                        rollCount+=1
                if rowPos < len(listRows) -1 and listRows[rowPos+1][colPos] == "@":
                    rollCount+=1
                if rowPos < len(listRows) -1:
                    if colPos < len(listRows[rowPos+1]) -1:
                        if listRows[rowPos+1][colPos+1] == "@":
                            rollCount+=1

                if rollCount < 4:
                    overallCount+=1
            colPos+=1
        rowPos+=1 
    print("the final roll count is " + str(overallCount))





if __name__ == "__main__": 
  main()