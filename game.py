import os
import random
def pickRandomWord():
    lines = []
    with open("answer_words.txt") as file:
        lines = file.readlines()

    chosenWord = random.choice(lines)

    print("Word Chosen!")
    print(chosenWord)
    return chosenWord

def getPlayerGuess():
    with open("5_letter_wrods.txt") as file:
            lines = file.readlines()
    while(True):
        guess = input("Make your guess: ")
        if(validateGuess(guess, lines)):
            return guess
        else:
            print("Invalid word. Please mae sure youre word is 5 letters, is an actual word, has no punctation/spaces/numbers etc")
def validateGuess(guess,lines):
    validWord = False
    if(len(guess)!=5):
        print("here boo")
        return validWord
    for line in lines:
        if line.strip() == guess.strip():
            validWord = True
            break
    return validWord

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
   