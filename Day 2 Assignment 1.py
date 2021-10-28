'''
Assignment 1 Day 3
You all are pilots, you have to land a plane,
the altitude required for landing a plane is 1000ft,
if it is less than that tell pilot to land the plane, 
or it is more than that but less than 5000 ft ask the pilot to “come down to 1000 ft”, 
else if it is more than 5000ft ask the pilot to “go around and try later”
'''
import random

pilot = input("Please Identify Yourself who are you -")
print("Please wait a sec we are checking your details!!!")
print("Hello Mr.", pilot, "!  Sorry for inconvenience sir")
height = int(input("Sir can you Please tell us your height, so that we can grant you permission to land."))

if height <= 1000 :
    print("Thank you sir")
    lst = [1,2,3,4,5,6,7,8,9]
    hanger = random.choice(lst)
    print("Now you can land your plane on hanger no.",hanger)
elif height <= 5000 :
    print("Sir you have to wait till you get to 1000 feet.")
else :
    print("Sorry Sir as you are above 5000 feet you have to go around and try again later.")        