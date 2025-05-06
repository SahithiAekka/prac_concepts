# # Hangman problem
# # STEP 1
# import random

# word_list = ["avacardava", "baboon", "camel"]

# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# chosen_word=random.choice(word_list)
# print(chosen_word)

# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess= input("guess a letter: ").lower()
# print(guess)

# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
# #  is, "Wrong" if it's not.
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")

# # STEP 2
# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# guess = input("Guess a letter: ").lower()
# placeholder =""
# for letter in chosen_word:
#     placeholder+="_"
# print(placeholder)

# # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# display =""
# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)



import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
