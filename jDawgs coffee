menue = {"items": ["black coffee", "iced coffee", "latte"],
         "prices": [10, 7, 9],
         "time": ["5 minutes", "10 minutes", "7 minutes"]} #time to prepare

while True:
    answer = input("Hi welcome to jdawgs coffee, would you like to see our menue? (please only type yes or no) ").lower()
    if answer == "yes":
        index_counter = 0
        print("Ok here is our menue:")
        for item in menue["items"]:
            print (f"{menue["items"][index_counter]} ${menue["prices"][index_counter]}")
            index_counter += 1
        break
        
    elif answer == "no":
        break


choice = input("\nOk, what can I get you? ").lower()
while choice not in menue["items"]:
    choice = input("\nThats not on our menue, what can I get you? ").lower()
while True:
    try:
        amount = int(input(f"How many {choice}'s would you like? "))
        break
    except ValueError:
        print("You must enter an integer.")


#noob
if choice == menue["items"][0]:
    print(f"Ok, that'll be ${menue["prices"][0] * amount} and should be ready in {menue["time"][0]}.")
elif choice == menue["items"][1]:
    print(f"Ok, that'll be ${menue["prices"][1] * amount} and should be ready in {menue["time"][1]}.")
else: 
    print(f"Ok, that'll be ${menue["prices"][2] * amount} and should be ready in {menue["time"][2]}.")








    
    
       

        
 









