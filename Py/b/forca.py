import random

# Define a list of words
words = ["python", "java", "ruby", "javascript", "php", "csharp", "swift", "kotlin", "typescript", "pedro"]

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the hidden word
hidden_word = ["_"] * len(word)

# Set the number of remaining guesses
remaining_guesses = 6

# Define the hangman visuals
hangman_visuals = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

# Define a function to display the hangman
def display_hangman(remaining_guesses):
    print(hangman_visuals[6 - remaining_guesses])

# Define a function to display the hidden word
def display_hidden_word(hidden_word):
    print(" ".join(hidden_word))

# Define a function to check if the word is guessed
def is_word_guessed(hidden_word):
    return "_" not in hidden_word

# Play the game
while remaining_guesses > 0:
    # Display the hangman and the hidden word
    display_hangman(remaining_guesses)
    display_hidden_word(hidden_word)

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter is in the word
    if guess in word:
        # Replace the corresponding underscore(s) with the letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        # Decrease the number of remaining guesses
        remaining_guesses -= 1

    # Check if the word is guessed
    if is_word_guessed(hidden_word):
        # Display the hangman and the hidden word
        display_hangman(remaining_guesses)
        display_hidden_word(hidden_word)

        # Display the result of the game
        print("Parabéns! Você acertou a palavra.")
        break

# If the number of remaining guesses reaches zero, the player loses
if remaining_guesses == 0:
    # Display the hangman and the hidden word
    display_hangman(remaining_guesses)
    display_hidden_word(hidden_word)

    # Display the result of the game
    print("Ups. A palavra era", word + ".")
