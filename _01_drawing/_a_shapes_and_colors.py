import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
turtle= turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
turtle.speed()
# Set your turtle's color using .color('green') and .pencolor('blue')
turtle.color('pink')
turtle.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
turtle.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
turtle.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
turtle.goto(x.y)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
turtle.circle(1, steps=30)
turtle.hideturtle()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
turtle.begin_fill("blue")
# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.screen.mainloop()
