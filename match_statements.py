# coding in match function
# making for code phone authorizations

name = input("Enter your name: ")

match name:
    case 'Ahmad':
        print("Welcome back to Naravo students club")
    case 'Hammad':
        print("Welcome back to Naravo students club")
    case 'Saleem':
        print("Welcome back to Naravo students club")
    case 'Sudais':
        print("Welcome back to Naravo students club")

    case _:
        print("You are not in the Naravo group")
    