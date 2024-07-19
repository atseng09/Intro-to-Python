#%%

import pandas as pd

data = pd.read_csv(r"day4.py")
# %%
data = data.drop(columns=["First Name", "Last Name"])

#%%
data["Timestamp"] = pd.to_datetime(data["Timestamp"])