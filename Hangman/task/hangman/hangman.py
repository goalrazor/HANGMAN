# Write your code here
import random
import string

import sys

word_list = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")

while True:
    attempts = 8
    menu = input("Type 'play' to play the game, 'exit' to quit: ")
    print()
    if menu == 'exit':
        break
    elif menu == 'play':

        while menu == "play":
            guesses = ''
            answer = random.choice(word_list)
            while attempts > 0:
                fail_counter = 0

                for char in answer:
                    if char in guesses:
                        print(char, end='')
                    else:
                        print('-', end='')
                        fail_counter += 1

                if fail_counter == 0:
                    print()
                    print("You guessed the word!")
                    print("You survived!")
                    menu = input("Type 'play' to play the game, 'exit' to quit: ")
                    print()
                    break
                print()
                input_letter = input("Input a letter: ")

                if len(input_letter) > 1:
                    print("You should print a single letter")
                    print()
                    continue
                if input_letter not in string.ascii_lowercase:
                    print("It is not an ASCII lowercase letter")
                    print()
                    continue
                if input_letter in guesses:
                    print("You already typed this letter")
                    print()
                    continue
                guesses += input_letter
                if input_letter not in answer:
                    print("No such letter in the word")
                    attempts -= 1
                    if attempts == 0:
                        print("You are hanged!")
                        menu = input("Type 'play' to play the game, 'exit' to quit: ")
                        print()
                        if menu == 'exit':
                            sys.exit()
                    print()
                    continue

                print()
    else:
        continue
