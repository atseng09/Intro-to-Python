#%%
# Load the dataset into a pandas dataframe.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cereal = pd.read_csv(r"cereal.csv")
# %%
# Print the first 5 rows of the dataset.
print(cereal.head())


#%%
# Use pandas to generate a description of the dataset.
cereal.describe()

#%%
#Print the correlation matrix of the dataset. Which two columns have the highest correlation? Which two columns have the lowest correlation? Generate a correlation matrix plot using pandas.
cereal_corr = cereal[["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "potass", "vitamins", "shelf", "weight", "cups", "rating"]].corr()*100
print(cereal_corr)

high_corr = cereal_corr.unstack().sort_values(ascending = False).head(1)
lowest_corr = cereal_corr.unstack().sort_values(ascending = True).head(1)
print("\nColumn pair with highest correlation:", high_corr)
print("\nColumn pair with lowest correlation:", lowest_corr)

#%%
#Generate a correlation matrix plot using pandas.
K=cereal_corr.plot(kind = "bar")

K.set_facecolor("aliceblue")
plt.gcf().set_facecolor("steelblue")
plt.xticks(color="white")
plt.yticks(color="k")

#%%
# Use pandas to plot a scatter matrix of the dataset.
from pandas.plotting import scatter_matrix
scatter_matrix(cereal, alpha = 0.7, color="grey", figsize=(12, 12))
plt.gcf().set_facecolor("steelblue")
plt.xticks(color="white")
plt.yticks(color="white")

#%%
 #Create a bar chart of the number of cereals in each manufacturer using the graphing library of your choice.

manu = cereal["mfr"].value_counts()

M = manu.plot(kind = "bar", color= "silver")
M.set_facecolor("aliceblue")
plt.gcf().set_facecolor("steelblue")
plt.xticks(color="white")
plt.yticks(color="k")

#%%
# Generate a scatter plot of the calories vs. the rating of the cereal using the graphing library of your choice.
cal_rat = ["calories", "rating"]
scatter_matrix(cereal[cal_rat], alpha = 0.7, color="grey", figsize=(8, 8))
plt.gcf().set_facecolor("steelblue")
plt.xticks(color="white")
plt.yticks(color="white")

#%%
# Select a few interesting looking graphs from the scatter matrix generated in problem 6 and make them visually appealing using the graphing library of your choice.
#??
#%%
# Create a histogram of the ratings of the cereals using the graphing library of your choice.
fig, ax = plt.subplots()
ax.hist(cereal["rating"], bins = 100, color = "silver")
fig.patch.set_facecolor("steelblue")

# Describe any conclusions you can make about the dataset.
#??
# major manufacturers : Kelloggs and Quakers
# All-Bran with Extra Fiber is apparently the best rated
# Potassium and Fiber have the biggest correlation [besides just the categories set against their own categories]
#surprisingly, sugar and rating have the lowest correlation, meaning the rating may factor in sugar but isnt mostly driven by it
# %%
