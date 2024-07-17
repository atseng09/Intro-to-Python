on = True

vowels = "aeiou"
vowels = vowels.split()

while on:
    user_input = input("Enter some text: ").lower()

    if user_input == "quit":
        on = False

    else:
        my_dict = {}

        for s in user_input:
            if s in vowels:
                if s in my_dict.keys():
                    my_dict[s] += 1
                else:
                    my_dict[s] = 1
        
            print(my_dict)
