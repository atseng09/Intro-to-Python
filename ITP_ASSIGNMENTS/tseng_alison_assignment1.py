#%%
#BASICS
name = "Alison Tseng"
print(name)

age = 17
print(age)

#just for organization
print()


#*height is in meters*
height = 1.651 
print(height)

print(age + height)
print(age * height)
print(height / age)

print()

#INTRO
intro = name + ' ' + str(age)
print(intro)

print(intro.upper())
print(intro.lower())
print(intro.title())
print(intro.swapcase())

print()


#testing
age0 = age + 1
print(age0)
intro0 = name + ' ' + str(age0)
print(intro0)
print(intro0.swapcase())

print()


#HOBBIES
hobbies_list = ["decorating", "drawing", "listening to music", "playing volleyball", "sleeping"]
print((', ').join(hobbies_list))

hobbies_list.append("watching movies/shows")
print((', ').join(hobbies_list))
hobbies_list.remove("decorating")
print((', ').join(hobbies_list))
hobbies_list.reverse()
print((', ').join(hobbies_list))

#testing
hobbies_list.pop()
print((', ').join(hobbies_list))
hobbies_list.insert(0, "drawing")
print((', ').join(hobbies_list))

print()


#PROFILE
profile = {
    "name": name,
    "age": age,
    "height": height,
    "hobbies": hobbies_list
}

profile.update({"favorite color": "blue"})
print(profile)
profile.pop("height")
print(profile)
print(profile.get("hobbies"))
profile["age"] = 18
print(profile)

print(profile.values())

# %%
