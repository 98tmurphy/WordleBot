from asyncio.windows_events import NULL
import enum
from unittest import result

class Solver():
    notUsedLetters = []
    anyPlaceLetters = []
    specificLetters = [None] * 5
    
    def update(guess, result):
        print("Finish this function dipshit")

def main():
    s = Solver()
    
    

def getGuess():
    while(True):
        guess = input("Enter guess: ").upper()
        
        if(len(guess) != 5):
            print("Invalid guess. Please make sure the guess is exactly 5 letters long")
            continue
        
        if(not all(chr.isalpha() or chr.isspace() for chr in guess)):
            print("Invalid guess. Plese make sure that the guess only contains letters")
            continue
        
        return guess

def getResult():
    while(True):
        result = input("Please enter the result of your guess")

        if(len(result) != 5):
            print("invalid result. Result must be 5 characters long")
            continue

        if(not all(chr in "-*!" for chr in result)):
            print("Invalid result. Result must be -, *, or !")
            continue

        return result    

main()