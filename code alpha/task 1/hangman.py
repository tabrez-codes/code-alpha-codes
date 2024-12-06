import random
hangman_graphics = [
    '''
     ------
     |    |
          |
          |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
          |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
          |
    =========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
          |
    =========
    '''
]
def display(word, guessed_letters):
    """Return the current state of the word with underscores for unguessed letters."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])
def hangman():
    words = ['robin', 'nami', 'copper', 'sanji', 'luffy', 'ussopp', 'zoro']
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    while attempts > 0:
        print(hangman_graphics[6 - attempts])  
        print(f"\nYou have {attempts} attempts remaining.")
        print("Current word:", display(word_to_guess, guessed_letters))
        guess = input("Enter a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'. Try another letter.")
            elif guess in word_to_guess:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                guessed_letters.append(guess)
                attempts -= 1
        else:
            print("Please enter a valid single letter.")
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break
    if attempts == 0:
        print(hangman_graphics[6])
        print(f"\nYou've run out of attempts! The word was: {word_to_guess}")
hangman()