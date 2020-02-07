import turtle
w = turtle.Screen()
b = turtle.Turtle()

# bal ütő
b.shape("square")
b.shapesize(5,1)
b.color("brown")
b.penup()
b.goto(-460,0)

#jobb ütő
j = turtle.Turtle()
j.shape("square")
j.shapesize(5,1)
j.color("brown")
j.penup()
j.goto(460,0)

#labda
l = turtle.Turtle()
l.shape("circle")
l.shapesize(1,1)
l.color("brown")
l.penup()
l.goto(0,0)

def b_fel():
    y = b.ycor()
    if y < 330:
        y = y + 100
    b.sety(y)
   

def b_le():
    y = b.ycor()
    if y > -330:
        y = y - 100
    b.sety(y)

def j_fel():
    y = j.ycor()
    if y < 330:
        y = y + 100
    j.sety(y)
   

def j_le():
    y = j.ycor()
    if y > -330:
        y = y - 100
    j.sety(y)    


w.onkey(b_le,"s")    
w.onkey(b_fel,"w")
w.onkey(j_le,"Down")    
w.onkey(j_fel,"Up")

a=1
b=1
w.listen()
while True:
    w.update()
    
    l.setx(l.xcor()+a)
    l.sety(l.ycor()+b)
    
    if l.ycor() > 100:
        l.sety(100)
        b=b*-1
    
    if l.ycor() < -100:
        l.sety(-100)
        b=b*-1
