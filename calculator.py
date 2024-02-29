"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_input = input("Enter your equation: ").lower()
    user_input = user_input.split(" ")

    if user_input[0] == 'q':
        print("You will exit.")
        break

    elif user_input[0] == '+':
        print(add(float(user_input[1]), float(user_input[2])))
    
    elif user_input[0] == '-':
        print(subtract(user_input[1], user_input[2]))
    
    elif user_input[0] == '*':
        print(multiply(user_input[1], user_input[2]))

    elif user_input[0] == '/':
        divide(user_input[1], user_input[2])

    elif user_input[0] == 'square':
        square(user_input[1], user_input[2])

    elif user_input[0] == 'cube':
        cube(user_input[1], user_input[2])

    elif user_input[0] == 'pow':
        power(user_input[1], user_input[2])

    elif user_input[0] == 'mod':
        mod(user_input[1], user_input[2])

    else:
        print("Please type that again.")

    






