import os
import random


stages = ['''
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
''']

# you can add as much as words you want
word_set = ["cow", "seat", "function", "hangman", "parameter", "computer", "wordgame", "playground", "country"]
selected_word = random.choice(word_set)  # to get a random word

# to display the blanks for the word
word_length = len(selected_word)
created_word = []
for i in range(word_length):
    created_word += "_"

wrong_choice = 0
while '_' in created_word:
    print(created_word)

    letter = input("please insert a letter:\t").lower()  # to get guessed letter from player
    for i in range(word_length):
        if created_word[i] == letter:  # prohibiting the player from reentering the correct letter
            print("you have already entered the letter, please insert a new one:\t")

        elif selected_word[i] == letter:  # adding the guessed to display
            created_word[i] = letter

    if letter not in selected_word:
        wrong_choice += 1
        print(stages[-wrong_choice])

    if wrong_choice == 6:
        print("you have hanged")
        break
    if '_' not in created_word:
        print("you won the game")

print(f"the word was {selected_word}")
os.system("PAUSE")
