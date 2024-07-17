#%%
import mymath

mymath.area

from mymath import area

area (10,10)

# %%
from mymath import*

area(10, 10)
perimeter(10,10)

#%%
#Miles Per Hour, how many miles do I go in one hour
#How fast do I have to bike to reach somewhere in time

block = 1/20
speed_mph = 10 # s = d / t

block_mph = speed_mph # d (miles)/ t * 20(blocks) / 1 mile

speed_mpm = speed_mph / 60 # d(miles) / t (hours)* t (hours)/ 60 (seconds)
block_mpm = speed_mpm * 20

distance = 50
time = distance / block_mpm  # t = d/s

#Based on my speed, how far can I get in an amount of time
def navigator(speed=None, time=None, distance=None, units = {
     "distance": "miles",
     "time": "hour",
     "speed": "mph"
}):
    
    #speed = distance/ time
    #distance = speed * time
    #times = distance/ speed
        
    #if speed, if time -> distance
        if speed and time:
            distance = speed * time
    
    #if time, distance -> speed necessary to get to destination on time
        if time and distance:
            speed = distance/ time

    #if distance, speed -> time to destination
        if distance and speed:
             time = distance/speed

        # if distance_units == "miles":
        #     if time_units == "hour":
        #          speed_units = "mph"
        #     if time_units == "minute":
        #          speed_units = "mpm"
        
        # if distance_units == "blocks":
             

        print("You need to go {speed:.{2}f} {speed_units} to get {distance:.{2}f} {distance_units} in {time:.{2}f} {time_units}")
        return distance, time, speed

distance, time, speed = navigator(speed=3, distance=40)
# %%
