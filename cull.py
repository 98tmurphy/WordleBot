import fileinput
import os

def cullWordlist():
    lines = []
    
    with open("words.txt", "r") as wordFile:
        lines = wordFile.readlines()
    with open("5_letter_wrods.txt", 'w') as flfile:
        flfile.truncate()

    flfile = open("5_letter_wrods.txt", 'w')

    count = 0
    for line in lines:
        if(len(line) == 6):
            flfile.writelines(line)
            count += 1

    

    print("Words are culled\n")
    print("Number of 5 letter words = ", count)
    wordFile.close()
    flfile.close()

cullWordlist()