"""
Assignment 2 Day 3(Optional)
Ankit is in maze. The command center sent him a string which decodes to come out from the maze. 
He is initially at (0, 0).
String contains L, R, U, D denoting left, right, up and down.
In each command he will traverse 1 unit distance in the respective direction.


For example if he is at (2, 0) and the command is L he will go to (1, 0).

You guys just need to make the flow of the logic which updates the position after taking input from u L, R, U, D"""

print("Hello !! Hello!!")
print("Sir I am Ankit. I am traped in a maze. please tell me the right direction to go out.")

x = 0
y = 0
while True:

    dir = input("Sir! Please tell we where I have to go.")
    if dir == "L":
        x -= 1
    elif dir == "R":
        x += 1
    elif dir == "U":
        y += 1
    elif dir == "D":
        y -= 1 
    else:
        print("Please Enter a Correct Value.I am in Danger!!")
  
    print((x,y))