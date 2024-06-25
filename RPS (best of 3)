import random
RPS = ["rock", "paper", "scissors"]
comp_choice = random.choice(RPS)
my_score = 3
comp_score = 3

print("\n")
print("Lets play rock-paper-scissors!!")
while my_score and comp_score > 0:
    my_choice = input("Ready go! ")
    while my_choice not in RPS or my_choice == comp_choice:
        print(comp_choice)
        my_choice = input("oops, try again ")
        comp_choice = random.choice(RPS)
    print(comp_choice)
    if my_choice == "rock" and comp_choice == "scissors":
        comp_score -= 1
        print("You win!!")
    elif my_choice == "paper" and comp_choice == "rock":
        comp_score -= 1
        print("You win!!")
    elif my_choice == "scissors" and comp_choice == "paper":
        comp_score -= 1
        print("You win!!")
    else:
        my_score -= 1
        print("I win!!")
    print("\n")

if my_score == 0:
    print("Thats game, I win!!")
else:
    print("Thats game, you win!!")