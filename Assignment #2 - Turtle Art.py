#------------------------------------------------------------------------------------
# Program: Assignment #2: Turtle Art
# Author: Erik Floyd
# Date: Feb 28, 2020
# Description: User inputs the kind of shape and how many they want
#              to draw, turtle then draws the shapes inside each other
#              in multi color.
# Input: User Inputs the number of sides the shape should have,
#        Then the user inputs the size of gap they wish to have as
#        well as the number of shapes that should be printed
#--------------------------------------------------------------------------------------

import turtle, random

#Claiming The Code
print('Program: Assignment #2: Turtle Art --- Author: Erik Floyd')

#User inputs for how the shape will look and how many will be on the screen
numberSides = int(input('Enter Number Of Sides: '))
gapSize = int(input('Enter Gap Size: '))
numberShapes = int(input('Enter the Number of Shapes To Draw: '))


#Creates the Turtle
turtle.shape('turtle')

#The loop that draws progressively bigger shapes until the number of shapes is reached.
for i in range(numberShapes):
    turtle.pensize(i + 1) #Adds one to the size of the lines each time a shape is drawn
    randomColor = (random.random(), random.random(), random.random()) #Stores a random color in randomColor
    turtle.color(randomColor) #Sets the turtle to the random color chosen and stored in the Variable randomColor
    turtle.forward(gapSize / 2) #Makes the gap size half as big for the bottom part of the shape, only half is drawn at the beginning
    turtle.left(360 / numberSides) #Divide the number of sides to determine how much the turtle should turn

    #Loop for actually drawing the individual shapes
    for y in range(numberSides - 1):
        turtle.color(random.random(), random.random(), random.random()) #sets the color of the turtle to be random once again
        turtle.forward(gapSize) #the turtle moves forward by the size determined by what shape its drawing to create a uniform shape
        turtle.left(360 / numberSides) #Turns the turtle at the right angle so that the shape closes once all the sides have been drawn


    turtle.color(randomColor) #choses the random color from earlier so that it can finish the bottom of the shape
    turtle.forward(gapSize / 2) #only draws half of the bottom to finish it off
    gapSize += gapSize #Doubles the gap size for the next shape to be drawn

#Code below resets the turtle position to the middle at the end of the program/finishes the final shape
turtle.left(90)
turtle.forward(10)
