#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"adult.csv.zip")
# %%

data = data.rename(columns={"fnlwgt": "salary"})

data.columns = data.columns.str.replace(".", "")


# %%
fig, ax = plt.subplots()
ax.hist(data.salary, bins = 100)
ax.set_xticks(np.linspace(0, 1500000, 4))
ax.set_xlim(0, 1500000)
ax.ticklabel_format(useOffset=False)
ax.ticklabel_format(style='plain')
ax.set_xlabel("Salary [$]")
ax.set_ylabel("Count")
ax.set_title("Amount of Earners")
    
# %%
fig, ax = plt.subplots()
ax.hist(data["educationnum"], bins = 100)
ax.set_xlabel("Years of Education")
ax.set_ylabel("Count")
ax.set_title("Years of Education")
# %%
data["sex_factorized"] = data.sex.factorize()[0]
data["nativecountry_factorized"] = data.nativecountry.factorize()[0]
data["race_factorized"] = data.race.factorize()[0]

#%%
correlation = data[["salary", "sex_factorized", "race_factorized", "age", "educationnum"]].corr()*100

# %%
# data["race"] = data.str.lower()

males = data[data.sex == "Male"]
females = data[data.sex == "Female"]

black_males = data[(data.sex == "Male") & (data.race == "Black")]

gens ={
    "silent": 79,
    "boomers": 60,
    "genx": 44,
    "millennials": 28,
    "genz":12,
    "alpha":0
}

def gen(x):
    if x >= 79:
        return "gen v"
    elif x>=60:
        return "gen w"
    elif x >= 44:
        return "gen x"
    elif x>=28:
        return "gen y"
    elif x>=12:
        return "gen z"
    else:
        return "gen a"
    

data["gens"] = data.age.apply(lambda x: gen(x))
# %%
