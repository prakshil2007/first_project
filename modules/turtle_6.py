import turtle

t = turtle.Turtle()

# Setup
t.speed(2)
t.pensize(5)         # Thick lines
t.pencolor("blue")   # Blue outline
t.fillcolor("red")   # Red inside

# Move without drawing (centering the circle a bit)
t.penup()
t.goto(0, -100)
t.pendown()

# Draw and fill
t.begin_fill()       # Start "recording" the shape for filling
t.circle(100)        # Draw circle with radius 100
t.end_fill()         # Stop "recording" and fill it in

turtle.done()