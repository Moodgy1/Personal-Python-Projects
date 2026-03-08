#!/usr/bin/env python
# coding: utf-8

# In[2]:


from turtle import *

speed(0.1)

for i in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    for j in range(2):
            fd(i)
            lt(71)
            rt(120)
    rt(120)
    lt(51)
    
done()
    


# In[3]:


# import turtle
import turtle

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(1000)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(200):
	t.pencolor(colors[x%6]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()
t.speed(1000)

turtle.bgcolor("black") # changes the background color

# make spiral_web
for x in range(20):
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()


# In[5]:


# Python program to draw star
# using Turtle Programming
import turtle
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
	star.right(144)
	star.forward(100)
	
turtle.done()


# In[ ]:


# Python program to draw square
# using Turtle Programming
import turtle
skk = turtle.Turtle()

for i in range(4):
	skk.forward(50)
	skk.right(90)
	
turtle.done()


# In[1]:


# Draw a Panda using Turtle Graphics
# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining method to draw a colored circle
# with a dynamic radius
def ring(col, rad):

	# Set the fill
	pen.fillcolor(col)

	# Start filling the color
	pen.begin_fill()

	# Draw a circle
	pen.circle(rad)

	# Ending the filling of the color
	pen.end_fill()

##########################Main Section#############################

# pen.up			 --> move turtle to air
# pen.down		 --> move turtle to ground
# pen.setpos		 --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
###################################################################

##### Draw ears #####
# Draw first ear
pen.up()
pen.setpos(-35, 95)
pen.down
ring('black', 15)

# Draw second ear
pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

##### Draw face #####
pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

##### Draw eyes black #####

# Draw first eye
pen.up()
pen.setpos(-18, 75)
pen.down
ring('black', 8)

# Draw second eye
pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

##### Draw eyes white #####

# Draw first eye
pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

# Draw second eye
pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

##### Draw nose #####
pen.up()
pen.setpos(0, 55)
pen.down
ring('black', 5)

##### Draw mouth #####
pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)
pen.hideturtle()


# In[2]:


import turtle


screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('Green')

# tell screen to not 
# show automatically
screen.tracer(0)            

t = turtle.Turtle()
t.speed(0)
t.width(3)

# hide donatello, we
# only want to see the drawing
t.hideturtle()            

def draw_square() :
    t.fillcolor("Orange")
    t.begin_fill()
    for side in range(4) :
        t.forward(100)
        t.left(90)
    t.end_fill()
t.penup()
t.goto(-350, 0)
t.pendown()

while True :
    t.clear()
    draw_square()
    
    # only now show the screen,
    # as one of the frames
    screen.update()         
    t.forward(0.02)
    


# In[2]:


# Import the turtle library for
# drawing the required curve
import turtle

# Set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(10)

# Iterate six times in total
for i in range(6):

	# Choose your color combination
	for color in ('red', 'magenta', 'blue',
				'cyan', 'green', 'white',
				'yellow'):
		turtle.color(color)
		
		# Draw a circle of chosen size, 100 here
		turtle.circle(100)
		
		# Move 10 pixels left to draw another circle
		turtle.left(10)
	
	# Hide the cursor(or turtle) which drew the circle
	turtle.hideturtle()


# In[1]:


# Import required module
import turtle



# Create turtle object
t = turtle.Turtle()

# Create a screen
screen =turtle.Screen()

# Set background color
screen.bgcolor("sky blue")



# Function to draw body of snowman
def draw_circle(color, radius, x, y):
	t.penup()
	t.fillcolor (color)
	t.goto (x, y)
	t.pendown()
	t.begin_fill()
	t.circle (radius)
	t.end_fill()


	
# Illustrating snowman
# Drawing snowman body
draw_circle ("#ffffff", 30, 0, -40)
draw_circle ("#ffffff", 40, 0, -100)
draw_circle ("#ffffff", 60, 0, -200)

# Drawing left eye
draw_circle ("#ffffff", 2, -10, -10)

# Drawing right eye
draw_circle ("#ffffff", 2, 10, -10)

# Drawing nose
draw_circle ("#FF6600", 3, 0, -15)

# Drawing buttons on
draw_circle ("#ffffff", 2, 0, -35)
draw_circle ("#ffffff", 2, 0, -45)
draw_circle ("#ffffff", 2, 0, -55)



# Function to draw arms
def create_line(x, y, length, angle):
	t.penup()
	t.goto(x, y)
	t.setheading(angle)
	t.pendown()
	t.forward(length)
	t.setheading(angle + 20)
	t.forward(20)
	t.penup()
	t.back(20)
	t.pendown()
	t.setheading(angle - 20)
	t.forward(20)
	t.penup()
	t.home()
	

	
# Drawing left arm
create_line(-70, -50, 50, 160)

# Drawing right arm
create_line(70, -50, 50, 20)



# Drawing hat
t.penup()
t.goto (-35, 8)
t.color ("black")
t.pensize (6)
t.pendown()
t.goto (35, 8)

t.goto (30, 8)
t.fillcolor ("black")
t.begin_fill()
t.left (90)
t.forward (15)
t.left (90)
t.forward (60)
t.left (90)
t.forward (15)
t.end_fill()


# In[ ]:




