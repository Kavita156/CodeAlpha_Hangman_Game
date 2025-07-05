import random

# 1. Predefined list of 5 words
word_list = ["apple", "tiger", "robot", "plane", "river"]

# 2. Randomly select one word from the list
secret_word = random.choice(word_list)

# 3. Initialize variables
guessed_letters = []             # list to store guessed letters
max_wrong_guesses = 6
wrong_guesses = 0

# 4. Helper function to display the word with blanks
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# 5. Start the game loop
print("🎮 Welcome to Hangman!")
print(f"You have {max_wrong_guesses} chances to guess the word.")

while wrong_guesses < max_wrong_guesses:
    print("\nWord:", display_word())
    guess = input("Guess a letter: ").lower()

    # 6. Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # 7. Check guess
    if guess in secret_word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print(f"❌ Incorrect! {max_wrong_guesses - wrong_guesses} guesses left.")

    # 8. Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 You win! The word was:", secret_word)
        break
else:
    print("\n💀 Out of guesses! The word was:", secret_word)
