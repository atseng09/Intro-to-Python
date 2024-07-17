#%%
def area(x: float, y: float) -> float:
    '''This function calculates the area of a rectangle with dimensions x and y'''
    return x*y

def perimeter(x, y):
    return 2*x+2*y

def volume (x, y, z):
    return x*y*z

def feet_to_meters(feet):
    return feet*0.3048

def meters_to_feet(meters):
    return meters*3.28084

def miles_to_blocks(miles):
    return miles/20 
def blocks_to_miles(blocks):
    return blocks*20

def meters_to_miles(meters):
    return meters*1800

def miles_to_meters(miles):
    return miles/1800

def mph_to_mpm(mph):
    return mph/60

def mpm_to_mph(mpm):
    return mpm*60

def mpj_to_bph(mph):
    return mph*20

def bpm_to_mph(bph):
    return bph/20

def bph_to_mph(bph):
    RETURN