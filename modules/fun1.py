import turtle

t = turtle.Turtle()
t.shape("turtle")   # Change the cursor shape to a turtle
t.color("black")
t.speed(3)
t.penup()           # We don't want to draw lines, just stamp

for _ in range(12):
    t.forward(100)  # Move out from center
    t.stamp()       # Leave a copy of the turtle here
    t.backward(100) # Go back to center
    t.right(30)     # Turn 30 degrees (360 / 12 = 30)

turtle.done()