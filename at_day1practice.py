#%%
first_name = "Alison"
last_name = "Tseng"

height_feet = 5
height_inches = 5

total_height_in_inches = height_feet * 12 + height_inches

list_of_interests = ["drawing", "music", "volleyball"]

profile = {
    "First": "Alison",
    "Last": "Tseng",
    "Height (feet)": total_height_in_inches // 12,
    "Height (inches)": total_height_in_inches % 12,
    "Interests": list_of_interests,
    "Number of Interests": len(list_of_interests)
}

#%%
paragraph = f"""
    {profile["First"]} {profile["Last"]} is {profile["Height (feet)"]}\'
    {profile["Height (inches)"]}\". They have {profile["Number of Interests"]} interests.
"""