#  \file:    pong.py
#  \author:  @4497cv
#  \date:    June 8th 2020
#  \brief:   Python Game: Pong

# libraries
import turtle
import time

# Window
window = turtle.Screen()                            # create window object
window.title("Pong game")                           # assign window's title
window.bgcolor("black")                             # assign window's background color
window.setup(width=800, height=600)                 # set window's dimensions
window.tracer(0)                                    # turn off drawing animation

# Paddle for player A
paddle_a = turtle.Turtle()                          # create paddle_a object
paddle_a.speed(0)                                   # set paddle's drawing speed to be the fastest
paddle_a.shape("square")                            # set paddle's shape as a square
paddle_a.color("white")                             # set paddle's color to be white
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # set paddle's shape size
paddle_a.penup()                                    # no drawing when moving
paddle_a.goto(-350,0)                               # move paddle to coordinates(-350,0)

# Paddle for player B
paddle_b = turtle.Turtle()                          # create paddle_b object
paddle_b.speed(0)                                   # set paddle's drawing speed to be the fastest
paddle_b.shape("square")                            # set paddle's shape as a square
paddle_b.color("white")                             # set paddle's color to be white
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    # set paddle's shape size
paddle_b.penup()                                    # no drawing when moving
paddle_b.goto(350,0)                                # move paddle to coordinates(350,0)

ball = turtle.Turtle()                              # create ball object
ball.speed(0)                                       # set ball's drawing speed to be the fastest
ball.shape("square")                                # set ball's shape as a square    
ball.color("white")                                 # set ball's color to be white
ball.penup()                                        # no drawing when moving
ball.goto(0,0)                                      # move ball to the center of the screen
ball.dx = -2                                        # set dx value (horizontal change)
ball.dy = 2                                         # set dy value (vertical change)

def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")

window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

while True:
    window.update()
    
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
        
    time.sleep(1/120)

    if((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40) and (ball.ycor() > paddle_b.ycor()-40)):
        ball.setx(340)
        ball.dx *= -1
    
    if((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40) and (ball.ycor() > paddle_a.ycor()-40)):
        ball.setx(-340)
        ball.dx *= -1
