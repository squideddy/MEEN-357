# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kasey Villarreal
# Section:      357-501
# Assignment:   Project Phase 1
# Date:         8/27/2025

rover = {}
rover['wheel_assembly'] = {
    'wheel':{
        'radius':.30,'mass':1.0},
    'speed_reducer':{
        'type':'reverted','diam_pinion':0.04,'diam_gear':0.07,'mass2':1.5}}

    


#rover['chassis']
#rover['science_payload']
#rover['power_subsys']
 
print(rover['wheel_assembly']['speed_reducer']['mass2'])

def divide(a, b):
    if b == 0:
        # Raise a ValueError if the denominator is zero
        raise ValueError("Denominator cannot be zero.")
    return a / b

try:
    result = divide(10, 2)
    print(result)
except ValueError as e:
    print(f"Error: {e}")