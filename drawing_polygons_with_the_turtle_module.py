# Description
# Drawing Polygons with the turtle module
'''The user is prompted to enter the dimensions of a polygon before the application utilizes the turtle module to draw
the polygon on a graphics window. The polygon is drawn using a for loop after the computer utilizes a formula to determine
the angle between each side of the polygon. The program utilizes an if-elif-else statement (or dictionary) to label the
polygon based on the number of sides after it has been drawn, and then uses the turtle module's write method to display
the label on the graphics window. Using the turtle module's numinput method, the default, minimum, and maximum values
are also set for the number of sides and the length of each side.'''
import turtle

# Takes the number of sides of the polygon from the user
num_sides = turtle.numinput("Number of sides", "Enter the number of sides of the polygon (3-12): ", default=3, minval=3, maxval=12)
num_sides = int(num_sides)

# Takes the length of each side of the polygon from the user
side_length = turtle.numinput("Length of sides", "Enter the length of each side of the polygon (50-250): ", default=50, minval=50, maxval=250)

# Now it calculate the angle between each side
angle = 180 * (num_sides - 2) / num_sides

# Now it calculates the angle at which the turtle should turn to draw the polygon
turn_angle = 180 - angle


t = turtle.Turtle()
t.speed(0)

# it uses a for loop to draw the polygon
for i in range(num_sides):
    t.forward(side_length)
    t.right(turn_angle)

#  Now it label the polygon based on the number of sides
if num_sides == 3:
    t.write("Triangle", align="left")
elif num_sides == 4:
    t.write("Square", align="left")
elif num_sides == 5:
    t.write("Pentagon", align="left")
elif num_sides == 6:
    t.write("Hexagon", align="left")
elif num_sides == 7:
    t.write("Heptagon", align="left")
elif num_sides == 8:
    t.write("Octagon", align="left")
elif num_sides == 9:
    t.write("Nonagon", align="left")
elif num_sides == 10:
    t.write("Decagon", align="left")
elif num_sides == 11:
    t.write("Hendecagon", align="left")
else:
    t.write("Dodecagon", align="left")

 
turtle.done()
