import random
shows = [["Gilmore Girls", "the good place", "Derry Girls"],
        ["the handmaid's tale", "dopesick", "six feet under"]]

movies = [["the pursuit of happyness", "crazy rich asains", "pretty woman"],
         ["the notebook", "titanic", "Romeo and juilet"]]
    


while True:
    try:
        answer = float(input("How many hours of time do you have? "))
        break
    except ValueError:
        print("You must enter a number")

if answer == 0:
    print("Come on now, you aint got time for nothin!!")

elif answer <= 1:
    print("Ok so you probably only have time for a show")
    answer = input("Are you feeling happy or sad? ").lower()
    if answer == "happy":
        x = random.choice(shows[0]).title()
        print(f"Ok you should watch {x}")
    else:
        x = random.choice(shows[1]).title()
        print(f"Ok you should watch {x}")
else:
    print("Ok so you could probably watch a movie")
    answer = input("Are you feeling happy or sad? ").lower()
    if answer == "happy":
        x = random.choice(movies[0]).title()
        print(f"Ok you should watch {x}")
    else:
        x = random.choice(movies[1]).title()
        print(f"Ok you should watch {x}")



    





