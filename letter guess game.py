


def letter_guess(round, correct_letters):
    import string
    import random
    letty = string.ascii_lowercase
    letty = list(letty)
    letter = random.choice(letty)
    guess_count = 5
    print("\n")   
    
    while True:
        try:
            print(letter)

            answer = input("Guess a letter: ").lower()
            while answer != letter and answer in letty and guess_count > 0 and answer != "":
                guess_count -= 1 
                if guess_count == 0:
                    print("You didnt guess the letter.")
                    while round <= 5:
                        print(f"\nRound {round} will now begin.")
                        return
                    if round == 6:
                        return    
                print(f"\nYou have {guess_count} try's left.")
                answer = input("Guess a letter: ").lower()

                

            if answer not in letty or answer == "":
                raise Exception

        except Exception:
            print("\nThats not a letter.")
        
        else:
            if guess_count > 0:
                print("You guessed the letter.")
                correct_letters += 1
                while round <= 5:
                    print(f"\nRound {round} will now begin.")
                    return
                if round == 6:
                    return
                
correct_letters = 0
round_counter = [2,3,4,5,6]
for round in round_counter:
    letter_guess(round, correct_letters)

print(f"\nYou guessed {correct_letters} letters correctly!!")

#correct_letters always comes out to be zero even when its not!!!!!!!