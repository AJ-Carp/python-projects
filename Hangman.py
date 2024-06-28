import random

words = ["python", "java", "kotlin", "javascript", "ruby", "swift"]

chosen_word = random.choice(words)
word_display = ["_" for _ in chosen_word]
attempts = 8

print("Welcome to hangman!!")
while attempts > 0 and "_" in word_display:
    print("\n" + " " .join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Nope!!!")
        attempts -= 1

if "_" not in word_display:
    print("You guessed the word")
    print(" " .join(word_display))
    print("You win!!!")

else:
    print(f"You've been hung, the word was {chosen_word}")
    



    




