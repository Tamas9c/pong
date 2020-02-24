import turtle
w = turtle.Screen()
bü = turtle.Turtle()

# bal ütő
bü.shape("square")
bü.shapesize(5,1)
bü.color("brown")
bü.penup()
bü.goto(-460,0)

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
    y = bü.ycor()
    if y < 330:
        y = y + 100
    bü.sety(y)
   
def b_le():
    y = bü.ycor()
    if y > -330:
        y = y - 100
    bü.sety(y)  

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
        b=b*-1
    
    if l.ycor() < -300:
        l.sety(-300)
        b=b*-1
    if j.xcor()-30 < l.xcor() < j.xcor() and j.ycor()-50 < l.ycor() < j.ycor()+50: 
        l.setx(j.xcor()-30)
        x2=x2*-1
    
    if bü.xcor()+30 > l.xcor() > bü.xcor() and bü.ycor()-50 < l.ycor() < bü.ycor()+50: 
        l.setx(bü.xcor()+30)
        x2=x2*-1
