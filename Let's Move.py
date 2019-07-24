import turtle
def up():
    turtle.goto(turtle.xcor(),turtle.ycor()+50)
def down():
    turtle.goto(turtle.xcor(),turtle.ycor()-50)
def left():
    turtle.goto(turtle.xcor()-50,turtle.ycor())
def right():
    turtle.goto(turtle.xcor()+50,turtle.ycor())
turtle.onkeypress(up,"w")
turtle.onkeypress(down, "s")
turtle.onkeypress(right, "d")
turtle.onkeypress(left, "a")
turtle.listen()
turtle.mainloop()
    
    
