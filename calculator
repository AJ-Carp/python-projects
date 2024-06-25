def calculator():
    def value_collector():

        while True:
            try:
                value = float(input("Enter number: "))

                break
            except ValueError:
                print("value must be an integer or float")
        return value


    operators = ["+", "-", "/", "*", "**"]


    x = value_collector()

    op = input("Enter operation: (+  -  /  *  **) ").strip()
    while op not in operators:
        op = input("Can only choose one of these operations: (+  -  /  *  **), Enter operation: ").strip()
    y = value_collector()


    if op == "+":
        print(f"{x} + {y} = {x + y}")
    elif op == "/" and y == 0:
        print("Cannot divide by zero... restart process")
        calculator()
    elif op == "-":
        print(f"{x} - {y} = {x - y}")
    elif op == "/":
        print(f"{x} / {y} = {x / y}")
    elif op == "*":
        print(f"{x} * {y} = {x * y}")
    else:
        print(f"{x} ** {y} = {x ** y}")

    answers = ["yes", "no"]
    answer = input("Would you like to make another calculation? (type only yes or no) ").strip().lower()
    if answer == "yes":
        calculator()
    elif answer == "no":
        quit()
    else:
        while answer not in answers:
                answer = input("Would you like to make another calculation? (type only yes or no) ").strip().lower()
                if answer == "yes":
                    calculator()

calculator()