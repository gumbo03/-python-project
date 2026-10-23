# print("hello solomon")
import turtle
import time

delay = 0.1

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by geey")
wn.bgcolor("red")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen update

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction ="up"


# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

#Main game loop
while True:
    wn.update() 

    move()

    time.sleep(delay)



wn.mainloop()