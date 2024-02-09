#Step 1

# word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import requests
import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
chosen_word = random.choice(WORDS).decode('utf-8')
print(str(chosen_word))
covered_char = ["_"] * len(chosen_word)
print(covered_char)

lives = 6
while lives > 0:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            covered_char[position] = guess
    print(covered_char)
    if guess not in chosen_word:
        print("Incorrect!")
        lives -= 1
        print("You have " + str(lives) + " lives left.")
    else:
        print("Correct!")
    if "_" not in covered_char:
        print("You win!")
        break
    print(stages[lives])
if "_" in covered_char:
    print(f"You lost, the word was {chosen_word} !")
