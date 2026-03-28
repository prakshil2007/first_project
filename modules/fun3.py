import turtle

screen = turtle.Screen()

# Define the shape using (x, y) points
# This shape looks like a boomerang or an arrow
boomerang_shape = ((0, 0), (10, 20), (30, 0), (10, 5))

# Register the shape with a name
screen.register_shape("boomerang", boomerang_shape)

t = turtle.Turtle()
t.shape("boomerang") # Use the name you gave it
t.color("purple")
t.pensize(3)

# Spin it!
t.speed(1)
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()