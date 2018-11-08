
number_to_guess = 2

user_number = int(input("Introduce un numero: "))

if number_to_guess == user_number:
    print("Has ganado")
else:
    print("Has perdido")
    user_number = int(input("Introduce otro numero: "))
    if number_to_guess == user_number:
        print ("Has ganado")
    else:
        print("Has perdido")
        user_number =int(input("Introduce otro numero: "))
        if number_to_guess == user_number:
            print("Has ganado")
        else:
            print("Has perdido")
            user_number = int(input("Introduce otro numero: "))
            if number_to_guess == user_number:
                print("Has ganado")
            else:
                print("Has perdido")
                user_number = int(input("Introduce otro numero: "))
                if number_to_guess == user_number:
                    print("Has ganado")
                else:
                    print("Has perdido, fin del juego")
