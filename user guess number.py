import random 
lives = 10
number = random.randint(1,20)
guess_count = 0
while True:
    try:
        guess = int(input("Guess number from 1 to 20: "))
        guess_count += 1
        lives -= 1

        while guess != number and lives > 0:
            guess = int(input("Guess again: "))
            guess_count += 1
            lives -= 1
        if lives == 0:
            print("You ran out of guesses")
            quit()
        break
    except ValueError:
        print("You must type an integer.")

print(f"Good job you guessed the number in {guess_count} trys!!")