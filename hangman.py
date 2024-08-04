import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "peach"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 5

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    while True:
        print("\nWord: " + display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("Wrong guess!")
            if attempts_left == 0:
                print("Sorry, you've run out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

hangman()
