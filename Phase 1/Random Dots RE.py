import turtle
import random
# list of colors
turtle.speed(0)
colors = [ 'red' , 'green' , 'blue' , 'yellow' , 'orange' , 'black' , 'purple' ]
for i in range(50):
    x = random.randint(-100, 100)
    y =  random.randint(-100, 100)
    # set a random position
    turtle.setposition(x, y)
    # set a random color
    i = random.randint(0, len(colors)-1)
    turtle.dot(colors[i])
turtle.done()
