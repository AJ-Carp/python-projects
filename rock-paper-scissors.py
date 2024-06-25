import random
RPS = ["rock", "paper", "scissors"]
comp_choice = random.choice(RPS)
my_score = 3
comp_score = 3

print("\n")
my_choice = input("Lets play rock-paper-scissors, ready go! ")
while my_choice not in RPS or my_choice == comp_choice:
    print(comp_choice)
    my_choice = input("oops, try again ")
    comp_choice = random.choice(RPS)
print(comp_choice)
if my_choice == "rock" and comp_choice == "scissors":
    comp_score -= 1
elif my_choice == "paper" and comp_choice == "rock":
    comp_score -= 1
elif my_choice == "scissors" and comp_choice == "paper":
    comp_score -= 1
else:
    my_score -= 1

if my_score > comp_score:
    print("You Win!!")
else:
    print("I Win!! ")