while True:
    try:
        inp = int(input("Type int: "))
        break
    except ValueError:
        print("Must be int")




#numbers can still be typed as long as they are with another type of character
while True:
    try:
        inp = float(input("Type anything but number: "))
        print("cant be number")
    except ValueError:
        break





#certain characters restricted
not_allowed_chars = (".", "/", ";")

while True:
    bad_char_counter = 0

    username = input("Enter username: ")

    for char in not_allowed_chars:
        if char in username:
            bad_char_counter += 1
    
    if bad_char_counter > 0:
        print("Invalid username")
    
    else:
        break

print(f"Your username is {username}")



#basically same as above but restricted values are numbers
#way of assuring no number are typed
no_nums = []
for _ in ("0123456789"):
    no_nums.append(_)

while True:
    no_num_counter = 0

    username = input("Type anything but numbers: ")

    for num in no_nums:
        if num in username:
            no_num_counter += 1
    
    if no_num_counter > 0:
        print("Invalid username")
    
    else:
        break

print(f"Your username is {username}")

