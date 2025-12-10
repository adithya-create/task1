import random

# Predefined word list
words = ["python", "computer", "program", "hangman", "developer"]

# Pick a random word
secret_word = random.choice(words)

# Variables
guessed_letters = []
attempts = 6
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word:")

# Main game loop
while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print(f"Incorrect attempts left: {attempts}")
    
    guess = input("Enter a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only one alphabet letter!")
        continue
    
    if guess in guessed_letters:
        print("⚠️ Already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in secret_word:
        print("✔️ Correct guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Game result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Out of attempts! The word was:", secret_word)
