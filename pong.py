import turtle
import time 
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(2)

# Boundary Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-390, -290)
border.pendown()
border.pensize(3)

for i in range(2):
    border.forward(780)   
    border.left(90)
    border.forward(580)   
    border.left(90)

border.hideturtle()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = -.89
ball.dy = .78
time.sleep(0.016)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    if paddle_a.ycor() < 240:
        paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    if paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    if paddle_b.ycor() < 240:
        paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    if paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 20)


# Controls
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Loop
while True:
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ASSETS/WALL.wav", winsound.SND_ASYNC) 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ASSETS/WALL.wav", winsound.SND_ASYNC) 
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ASSETS/HIT.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1   
        winsound.PlaySound("ASSETS/HIT.wav", winsound.SND_ASYNC)

# AI Player
    # if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor() > 10):
    #         paddle_b_up()
    # elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor() > 10):
    #         paddle_b_down()