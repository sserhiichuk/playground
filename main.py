import words_fetcher
import random


def congratulate_user(guesses):

    print("=============================")
    print("= Congratulations! You won! =")
    print("=============================")
    print(f"Your words: {guesses}")


def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


def guess_is_valid(candidate, errors):
    for letter in candidate:
        if letter not in word:
            errors += 1
            print(f"You can not use letter {letter}")
            return False, errors
        count = word.count(letter)
        if count < candidate.count(letter):
            errors += 1
            print(f"You can use letter {letter} only {count} times")
            return False, errors
    return True
def loss_event():
    print('Unfortunately( You have lost!')

guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
    guess = input("Your next take: ")
    print(errors)

    if guess in guesses:
        print('You have already entered this word')
        errors += 1

    if not guess_is_valid(guess, errors):
        continue

    if guess in full_list:
        guessed += 1
        guesses.append(guess)
        if guessed == WORDS_TO_WIN:
            congratulate_user(guesses)
            exit()
        print(f"That's right! {WORDS_TO_WIN - guessed} to go")
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
    if errors == ERRORS_TO_LOSE:
        loss_event()
