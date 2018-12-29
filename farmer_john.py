# Use turtle to draw four circles at the corners of a center circle that is decided 
# by user input being the length of one side of the square
import turtle
import math

wn = turtle.Screen()

sprinkler = turtle.Turtle()
sprinkler.color("lightblue")

field = turtle.Turtle()
field.color("green")

shader = turtle.Turtle()
shader.color("yellow")

squarelength = int(input("How long is one side of the square field?"))
#Fruitful function to take in the user input of the length of one side of the square and return the area missed 
def findArea(squarelength):
    squareArea = squarelength * squarelength
    circleArea = math.pi * squarelength/2 ** 2
    areaMissed = squareArea - circleArea
    return areaMissed

#Draw the field with centers of sprinklers on each of the corners of the perfect square field
def drawField(squarelength):
    shader.begin_fill()
    for i in range(4):
        shader.fd(squarelength)
        shader.left(90)
    shader.end_fill()
    #Make the sprinklers at each square 
    for i in [[squarelength,-squarelength/2],[squarelength,squarelength/2],[0,squarelength/2],[0,-squarelength/2]]:
        sprinkler.penup()
        sprinkler.goto(i[0],i[1])
        sprinkler.pendown()
        sprinkler.begin_fill()
        sprinkler.circle(squarelength/2)
        sprinkler.end_fill()
        sprinkler.penup()

    field.pensize(2)
    field.pendown()

    field.begin_fill()
    for i in range(4):
        field.pendown()
        field.fd(squarelength)
        field.left(90)

drawField(squarelength)
#Print answer of the area missed in the center of square to the command line
print("The area missed by sprinklers is {:6.2f} ft^2".format(findArea(squarelength)))

wn.exitonclick()