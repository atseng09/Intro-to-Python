#%%
print(" ")

#PROBLEM 1
def is_palindrome(i):
    # word = "panda"
    i = i.lower()
    reverse = i[::-1]

    print("Word: " + i) 
    print("Word reversed: "+ reverse)

    
    left = 0
    right = len(i)-1

    while right > 0:
        if right > 0:
            left += 1
            right -= 1

        if i[left] != i[right]:
            print("This is isn't a palindrome!")
            print("")
            return False 

        else:
            left += 1
            right -= 1 
            print("This is a palindrome!")
            print("")
            return True 

print(is_palindrome("Racecar"))

print(" ")

# %%

#PROBLEM 2
class Rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width)*2
    
    def area (self):
        return self.length * self.width
    
r = Rectangle (9,12)

print("P: ", r.perimeter())
print("A: ", r.area())

print(" ")

# %%

#PROBLEM 3

def count_words(list):

    word_amnt = {}
    for word in list:
        if word in word_amnt:
            word_amnt[word] += 1
        else:
            word_amnt[word] = 1
    return word_amnt
        
wordlist = ["star", "pillow", "moon", "star", "moon", "light", "pillow", "dream", "moon", "star", "star", "blue"]
counting = count_words(wordlist)
print("Word list: ", wordlist)
print("Count: ", counting)

print(" ")
# %%
