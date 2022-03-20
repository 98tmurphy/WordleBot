import os
import random
def pickRandomWord():
    lines = []
    with open("5_letter_wrods.txt") as file:
        lines = file.readlines()

    chosenWord = random.choice(lines)

    print("Word Chosen!")
    print(chosenWord)
    return chosenWord

def getPlayerGuess():
    while(True):
        guess = input("Make your guess: ")
        if(len(guess)==5):
            break
        else:
            print("Invalid guess, must contain 5 characters")
    return guess

def checkGuess(guess, answer):
        
    if(guess == answer.strip()):
        print('Correct!')
        return True
    
    i = 0
    clue =""
    for letter in guess:
        if(letter in answer):
            index = answer.index(letter)
            if(index == i):
                clue = clue + '*'
            else:
                clue = clue + '!'
        else:
            clue = clue + '-'
        i+=1

    print(clue)
    return False

def main():
    answer = pickRandomWord()
    won = False
    while(won!=True):
        guess  = getPlayerGuess()
        won = checkGuess(guess, answer)

main()