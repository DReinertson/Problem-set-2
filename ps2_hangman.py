# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def Blank(word):
    ##Will return blanks for every letter in word from choose_word(wordlist).
    ##These blanks will then get replaced by correctly guessed letters.
    ##Must convert word from string to list in order to change mutable object
    s_word = list(word)
    blank_word = ""
    for i in range(0, len(s_word)):
##        blank_word += "_"
        s_word[i] = "_ "
    return s_word

def String(list):
    word = ''.join(list)
    return word

def remove_letter():
    remaining = list(remaining)
    remaining.remove(letter)

        
        
def Hangman():
    ##Guesses initally set to n = 8, will reduce to n - 1 if guess is incorrect
    ##Initially shows word of all blanks and will replaced blank(s) with correct guess
    ##
    n = 8
    remaining = "abcdefghijklmnopqrstuvwxyz"
    word = choose_word(wordlist)
    blank_word = Blank(word)
    print "Hello, welcome to Hangman. Let's play!"
    print "Your word is ", String(blank_word)
    print "Letters remaining: ", remaining
    while (n > 0):
        print "You have ", n, "guesses remaining,"
        letter = raw_input("Please guess a letter: ").lower()
        if letter not in list(remaining):
            print "That is not a valid letter."
            letter = raw_input("Please guess a letter: ").lower()
        if letter in word:
            for i in range (0, len(word)):
                if word[i] == letter:
                    blank_word[i] = letter
##                blank_word[word.find(letter)] = letter
            
        else:
            n -= 1
            if n == 1:
                print "Ooooo, not quite. You have ", n, "guess left"
                print "Please guess another letter: "
            else:
                print "Ooooo, not quite. You have ", n, "guesses left"
                print "Please guess another letter: "
            
                
        remaining = list(remaining)
        remaining.remove(letter)
        print "Letters remaining: ", String(remaining)
        print String(blank_word)
        if String(blank_word) == word:
            print "Congratulations you have won!"
            Choice = raw_input("Would you like to play again? (y or n): ").lower()
            if Choice == "y":
                Hangman()
            else:
                print "Come back and play again sometime!"
        print ""
        
    print "You have run out of guesses!"
    print "The word is: ", word
    Choice = raw_input("Would you like to play again? (y or n): ").lower()
    if Choice == "y":
        Hangman()
    else:
        print "Come back and play again sometime!"


##        for i in range(0, len(word)):
##            if word[i] == letter:
##                blank_word[i] = letter

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
Hangman()
