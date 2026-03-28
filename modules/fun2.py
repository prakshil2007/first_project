import turtle

t = turtle.Turtle()
t.shape("circle")
t.speed(0)          # Fastest speed
t.penup()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "black", "magenta", "indigo"]

for i in range(50):
    t.color(colors[i % 10])  # Cycle through colors
    t.forward(i * 3)        # Move forward a little more each time
    t.stamp()               # Leave a stamp
    t.right(45)             # Turn

turtle.done()