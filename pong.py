import turtle
w = turtle.Screen()
bü = turtle.Turtle()

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


# ütő mozgatás definíciója
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

#mozgás billentyűre tétele
w.onkey(b_le,"s")    
w.onkey(b_fel,"w")
w.onkey(j_le,"Down")    
w.onkey(j_fel,"Up")

y2=1
x2=1
w.listen()
while True:
    
    l.setx(l.xcor()+x2)
    l.sety(l.ycor()+y2)
    
    if l.ycor() > 300:
        l.sety(300)
        y2=y2*-1
    
    if l.ycor() < -300:
        l.sety(-300)
        y2=y2*-1
    if j.xcor()-30 < l.xcor() < j.xcor() and j.ycor()-50 < l.ycor() < j.ycor()+50: 
        l.setx(j.xcor()-30)
        x2=x2*-1
    
    if b.xcor()+30 > l.xcor() > b.xcor() and b.ycor()-50 < l.ycor() < b.ycor()+50: 
        l.setx(b.xcor()+30)
        x2=x2*-1
