def start_game():
    print("\nWelcome to Mind reading game")
    print("\nHere you can try and guess the nuber which is randomly chosen by me")
    print("\nInput a range for me to pick up a number")

    x = int(input("Enter the lower limit: "))
    y = int(input("Enter the upper limit: "))

    def loop():
        b = int(input("Now try and guess the number: "))

        if int(b)<a:
            print("The number is too low")
            loop()

        elif int(b)>a:
            print("The number is too far")
            loop()

        else:
            print("\nYO...you guessedthe right number!!!")
            start_game()

    import random
    a = random.randint(x,y)
    loop()

start_game()
