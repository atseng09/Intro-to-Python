#%%
#PROBLEM 1
#1
for i in range(11):
    print(i)

#for organization
print(" ")

#2
name_list = ["Leon", "Jase", "Amelia", "Marco", "William", "Neya", "Ian", "Akash" ]

for name in name_list:
    print("Hello, " + name)

print(" ")

#3
numbers_list = [1, 5, 10 ,8 ,4, 7]

sum = 0
for num in numbers_list:
    sum += num
    print(sum)

print(" ")

#4
for name in name_list:
    reverse = name[::-1]
    print(reverse)

print(" ")

#5
word = "kaleidoscope"
letters = {}

for i in word:
    if i in letters.keys():
        letters[i] +=1
    else:
        letters[i] =1
print(letters)

print(" ")

#6
gradebook = {
    "Darcy": 89,
    "Lauren": 99,
    "Andrew": 45,
    "Renee": 32,
    "Lucas": 76,
    "Sharone": 54
}
print("Students who passed: ")
for student in gradebook:
    if gradebook[student] >= 60:
        print (student, gradebook[student])
    else:
        pass

print(" ")

#7
n = 9
multiple_list = range(11)

for num in multiple_list:
    print( str(n) + " x " + str(num) + " = " + str(n*num))

print(" ")

# %%
#PROBLEM 2
#8
i = 1
while i < 11:
    print(i)
    i += 1

print(" ")

#9
on = True

while on: 
    user_input = input("Write a name or type quit: ").lower()
    if user_input == "quit":
        on = False
    else:
        print(("Hello, " + user_input).title())

print(" ")

# %%
#PROBLEM 3
#10
num = int(input("Write a number: "))

if (num % 2) > 0:
    print(str(num) + " is odd")
else:
    print(str(num) + " is even")

print(" ")

#11
import random

list = [random.randint(1, 100) for _ in range(10)]

small = list[0]
large = list[0]

for number in list:
    if number < small:
        small = number
    elif number > large:
        large = number
    else:
        pass
print(list)
print(f"Largest number: {large}")
print(f"Smallest number: {small}")

print(" ")

#12
on = True

fruit_dict = {
    "apple": 0.75,
    "orange": 0.98,
    "passionfruit": 2.50,
    "strawberries": 3.00,
    "mango": 1.99
}

while on:
    user_input = input("Name a fruit: ").lower()
    for fruit in fruit_dict:
        if user_input in fruit_dict:
            print((f"{user_input}: ${fruit_dict[user_input]}").title())
            break

        elif user_input == "quit":
            on = False

        else:
            print("Sorry, we don't have that fruit")
            break
 