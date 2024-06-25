#makes sure integer
def must_be_int(measurement):
    while True:
        try:
            number_of_inches = float(input(f"Type number of {measurement}: " ))
            break
        except ValueError:
            print("must be int or float")
    return number_of_inches



print("\n")
#collect data
measurements = ["inches","feet", "yards"]

convert_from = input("Enter starting unit of measurment(inches, feet, yards): ").lower()
while convert_from not in measurements:
    convert_from = input("Invalid input, enter starting unit of measurment(inches, feet, yards): ").lower()
   
if convert_from == "inches":
    number_of_inches = must_be_int("inches")

elif convert_from == "feet":
    number_of_feet = must_be_int("feet")

elif convert_from == "yards":
    number_of_yards = must_be_int("yards")

    
convert_to = input("Enter unit of measurment to convert to(inches, feet, yards): ").lower()
while convert_to not in measurements:
    convert_to = input("Invalid input, enter unit of measurment to convert to(inches, feet, yards): ").lower()


#conversion process
if convert_to == "inches":
    if convert_from == "inches":
        print(f"{number_of_inches} inches")

    elif convert_from == "feet":
        print((number_of_feet * 12), "inches")
    
    elif convert_from == "yards":
        print((number_of_yards * 36), "inches")

elif convert_to == "feet":
    if convert_from == "inches":
        print((number_of_inches / 12), "feet")

    elif convert_from == "feet":
        print(f"{number_of_feet} feet")
    
    elif convert_from == "yards":
        print((number_of_yards * 3), "feet")

elif convert_to == "yards":
    if convert_from == "inches":
        print((number_of_inches / 36), "yards")

    elif convert_from == "feet":
        print((number_of_feet / 3),  "yards")
    
    elif convert_from == "yards":
        print(f"{number_of_yards} yards")



