import random
while True:
    try:
        x = int(input("Choose a number from 1 to 20 for me to guess: "))
        while x < 1 or x > 20:
            x = int(input("Number must be from 1 to 20: "))
        break
    except ValueError:
        print("Must be an integer")



#creating list 1 through 20 for comp to choose from
#prevents comp from choosing same number multiple times
y = []
for _ in range(1,21):
    y.append(_)
comp_choice  = random.choice(y)



guess_count = 0
print(comp_choice)
guess_count += 1

while comp_choice != x:
    guess_count += 1
    y.remove(comp_choice)
    comp_choice  = random.choice(y)
    print(comp_choice)

print(f"It took me {guess_count} guesses")







