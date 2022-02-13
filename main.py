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
        if(len(guess)>6):
            break
        else:
            print("Invalid guess, contains to many charaters")
    return 

def checkGuess(guess, answer, tries):
    if(tries != 6):
        return false
    if(guess == answer):
        return
    
    i = 0
    for letter in answer:
        if(letter == guess[i]):
            

pickRandomWord()
getPlayerGuess()
