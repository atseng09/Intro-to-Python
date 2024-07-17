on = True
print("WELCOME TO GUESS THE NUMBER")
print("Think of an integer from 0 to 100")

guess = 50
options = range(0, 101, 1)

while on:
    print(f"Is this number {guess}")
    resp = input("Yes or No?").lower()

    if resp == "yes":
        on = False

    else:
        resp= input(f"Is this number more or less than {guess}?")
        guess = options[len(options)//2]

        if resp == "more":
            options = options[guess:]
        else:
            options = options[:guess]



    #if resp == "equal":
    #    print ("I guessed the number")
    #    break


    if resp == "quit":
        on = False
