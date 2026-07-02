import random

def hangman():
    # Predefined list of 5 words
    words = ['python', 'coding', 'alpha', 'dog', 'hangman']
    target_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 5 # Limit incorrect guesses to 5

    print("Welcome to Hangman!")

    #  this is the where we i use the Game loop using key concepts: while loop, if-else, strings, lists
    while incorrect_guesses < max_attempts:
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        
        if "_" not in display_word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in target_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    if incorrect_guesses == max_attempts:
        print(f"\nGame Over! The word was: {target_word}")

if __name__ == "__main__":
    hangman()
