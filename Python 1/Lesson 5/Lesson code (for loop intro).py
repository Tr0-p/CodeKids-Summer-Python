import turtle

bob = turtle.Turtle() # creates and names our own turtle
bob.speed(0) # max speed
bob.color("red") # change the color of bob to be yellow

for side in range(200): # repeat the following lines 200 times
    bob.forward(side) 
    bob.left(97)
    bob.dot(10)



turtle.done() # makes our code work!

# DRY - Don't Repeat Yourself
