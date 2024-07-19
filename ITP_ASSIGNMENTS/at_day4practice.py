#%%
#import the name
import numpy
#import the name and change it
import numpy as np
#import specific functions or modules from the package
from numpy import sin

#%%
import numpy as np

a_deg = np.linspace(0, 10 ,1000)
a_rad = np.deg2rad(a_deg)
b = np.sin(a_rad)
c = np.cos(a_rad)

# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(a_deg, b, label="sin")
ax.set_title("Trig Plot")
ax.set_xlabel("Degrees")
ax.set_ylabel("Magnitude")
ax.set_xlim(0, 360)
ax.set_xticks(np.arange(0, 361,30))
ax.set_ylim(-1,1)
ax.legend(loc="upper right", ncols=2)

#%%
res = [1, 10, 30]
fig, ax = plt.subplots()

for r in res:
    a_deg = np.arange(0, 361, r)
    a_rad = np.deg2rad(a_deg)
    b = np.sin(a_rad)

    ax.scatter(a_deg, b, label=f"{r}-deg")

ax.set_title("Trig Plot")
ax.set_xlabel("Degrees")
ax.set_ylabel("Magnitude")
ax.set_xlim(0, 360)
ax.set_xticks(np.arange(0, 361,30))
ax.set_ylim(-1,1)
ax.legend(loc="upper right", ncols=2)

#%%
frequency = [1, 10, 30]
fig, ax = plt.subplots()

for f in frequency:
    b = np.sin(f * a_rad)

    ax.plot(a_deg, b, label=f"{f} Hz")

ax.set_title("Trig Plot")
ax.set_xlabel("Degrees")
ax.set_ylabel("Magnitude")
ax.set_xlim(0, 360)
ax.set_xticks(np.arange(0, 361,30))
ax.set_ylim(-1,1)
ax.legend(loc="upper right", ncols=2)

fig.savefig("figure4.png")

#%%
