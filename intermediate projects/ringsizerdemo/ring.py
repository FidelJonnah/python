import turtle

def increase_radius():
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(turtle.radius+10)
    turtle.radius+=10
    turtle.goto(0, -20)
    turtle.write("Size: "+ str(turtle.radius*2) + "mm", align="center", font=("Arial", 16, "bold"))

def decrease_radius():
    if turtle.radius >= 10:
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.circle(turtle.radius-10)
        turtle.radius-=10
        turtle.goto(0, -20)
        turtle.write("Size: "+ str(turtle.radius*2) + "mm", align="center", font=("Arial", 16, "bold"))

turtle.radius = 50
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(turtle.radius)
turtle.goto(0, -20)
turtle.write("Size: "+ str(turtle.radius*2) + "mm", align="center", font=("Arial", 16, "bold"))
screen = turtle.Screen()
screen.listen()
screen.onkey(increase_radius, 'Up')
screen.onkey(decrease_radius, 'Down')

turtle.mainloop()
