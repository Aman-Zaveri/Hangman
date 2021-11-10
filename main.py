from webScraping import chosenTheme, chosenWord
import random
import string
from hangmanVisual import livesVisual


def getVaildWord():
    word = chosenWord
    return word.upper()
    print(chosenWord)

def getValidTheme():
    theme = chosenTheme
    return theme

def playHangman():
    word = getVaildWord()
    theme = getValidTheme()
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 7

    print("Welcome to Hangman!")

    while len(wordLetters) > 0 and lives > 0:

        print(f"The theme is {theme}! ")
        print(f"You have {lives} left and you have used these letters: {', '.join(usedLetters)}")
        print()

        wordList = [letter if letter in usedLetters else '-' for letter in word ]
        print(f"Current Word: {' '.join(wordList)}")

        #Getting user input
        userInput = input("Type a letter: ").upper()
        if userInput in alphabet and userInput not in usedLetters:
            usedLetters.update(userInput)
            if userInput in wordLetters:
                wordLetters.remove(userInput)

            else:
                lives -= 1
                print("Your letter is not in the word! ")

            print(livesVisual[lives])

        elif userInput in usedLetters:
            print("You have already used the letter. Please choose another letter! ")

        elif userInput not in alphabet:
            print("You have not typed in a letter! Please type in a letter! ")
        
        print()


    if len(wordLetters) == 0:
        print(f"Congrats! You Won! The word was {word}!")
    else:
        print(f"Sorry! You ran out of lives! The word was {word}!")
    
print("Thank you for playing! Hope you come again! ")

playHangman()