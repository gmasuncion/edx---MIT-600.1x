# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def isWordGuessedv2(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    curr = ''
    for char in secretWord:
        if char not in lettersGuessed:
            curr += ("_ ")
        else:
            curr += char
    return curr



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    current =  list('_' * len(secretWord))
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            current[i] += '' 
        else:
            
            current[i] = secretWord[i]
    return ''.join(current)

            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    avail = list(alph)
    
    for char in lettersGuessed:
        if char in avail:
            avail.remove(char)
        
    return ''.join(avail)
        
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Variables
    n = len(secretWord)
    available = 'abcdefghijklmnopqrstuvwxyz'
    chances = 8
    guessed = []
    
    # Game Intro
    loadWords()
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", n ,"letters long.")
    print('-------------')
    
    # Main Logic
    while chances > 0:
        print("You have", str(chances), "guesses left.")
        print("Available letters:", available)
        guess = input("Please guess a letter: ")
        
        # Guess Checks
        if guess in guessed and guess in secretWord:
            print("Oops! You've already guessed that letter:", isWordGuessedv2(secretWord, guessed))
            print('-------------')
        elif guess in guessed and guess not in secretWord:
            chances -= 1
            print("Oops! You've already guessed that letter:", isWordGuessedv2(secretWord, guessed))
            print('-------------')
        else:
            if guess in secretWord:
                guessed.append(guess)      
                print("Good guess:", isWordGuessedv2(secretWord, guessed))
                available = getAvailableLetters(guessed)
                print('-------------')
            elif guess not in secretWord:
                guessed.append(guess)
                chances -= 1
                print("Oops! That letter is not in my word:", isWordGuessedv2(secretWord, guessed))
                available = getAvailableLetters(guessed)
                print('-------------')
            
        # Winning Scenario    
        if isWordGuessedv2(secretWord, guessed) == secretWord:
            print('Congratulations, you won!')
            break

    if chances == 0:
        print("Sorry, you ran out of guesses. The word was", secretWord + '.')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
