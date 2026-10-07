import random

words = ["python", "coding", "program", "keyplayer", "internet"]
secret_word = random.choice(words)
guessed_letters = set()
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print(f"Guess the word one letter at a time. You have {max_incorrect_guesses} incorrect guesses.")

while incorrect_guesses < max_incorrect_guesses:
    displayed_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f"\nWord: {displayed_word}")
    print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")

    if all(letter in guessed_letters for letter in secret_word):
        print(f"You win! The word was '{secret_word}'.")
        break

    guess = input("Enter one letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter from A to Z.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("That letter is not in the word.")

if incorrect_guesses == max_incorrect_guesses:
    print(f"\nGame over! The word was '{secret_word}'.")