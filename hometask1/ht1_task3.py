people = input('How many people? ')
pizza = input('How many pizzas do you have? ')
import sys
if people.isdigit() > 0 and pizza.isdigit() > 0:
    people_digit = int(people)
    pizza_digit = int(pizza)
    pizza_pieces = pizza_digit * 8
    if people_digit == 0 and pizza_digit == 0:
        print('No people no pizza')
        sys.exit(0)
    elif people_digit == 0:
        print('No people')
        sys.exit(0)
    elif pizza_digit == 0:
        print('No pizza')
        sys.exit(0)
    else:
        if pizza_digit == 1 and people_digit == 1:
            print(people_digit, 'person with ', pizza_digit, 'pizza')
            print('Person gets ', pizza_pieces // people_digit, 'pieces of pizza')
        elif pizza_digit == 1:
            print(people_digit, 'people with ', pizza_digit, 'pizza')
            if pizza_pieces // people_digit == 1:
               print('Each person gets ', pizza_pieces // people_digit, 'piece of pizza')
            else:
               print('Each person gets ', pizza_pieces // people_digit, 'pieces of pizza')
        elif people_digit == 1:
            print(people_digit, 'person with ', pizza_digit, 'pizzas')
            print('Person gets ', pizza_pieces // people_digit, 'pieces of pizza')
        else:
            print(people_digit, 'people with ', pizza_digit, 'pizzas')
            print('Each person gets ', pizza_pieces // people_digit, 'pieces of pizza')
        print('There are', pizza_pieces % people_digit, 'leftover pieces')

else:
    print('Not valid input')