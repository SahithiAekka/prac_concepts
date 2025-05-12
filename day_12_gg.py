import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print(logo)
print("Welcome to the number guessing game!!")
print("I'm thinking a number btw 1 to 100")
diff_level=input("Choose difficulty. type 'easy' or 'hard': ")

chosen_number=random.randint(1, 100)

def play_game(max_attempts):
    for attempt in range(1, max_attempts + 1):
        guess_number = int(input(f"Attempt {attempt}: Make a guess: "))
        if chosen_number > guess_number:
            print("Too low. Guess again.")
        elif chosen_number < guess_number:
            print("Too high. Guess again.")
        else:
            print(f"That is right! You guessed it in {attempt} attempts.")
            return
    print(f"Sorry, you've run out of attempts. The correct number was {chosen_number}.")

if diff_level== "easy":
    print("You have 10 attempts to finish this game")
    play_game(10)

if diff_level == "hard":
    print("You have 5 attempts to finish the game")
    play_game(5)


