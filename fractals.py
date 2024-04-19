import turtle

t = turtle.Turtle ()
t.setheading (90)
t.speed (0)
turtle.colormode(255)

#Koch normal =========================================================
        
def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(size)
    else:
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        t.rt(120)
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)

#I didn't get this one so my solution wouldn't work here -> used hw solution
        
#Koch weird
def newkoch(t, depth, size):
    if (depth == 1):
        t.fd(size)
    else:
        t.fd(size)
        newkoch(t, depth-1, size * 0.8)
        t.lt(90)
        newkoch(t, depth-1, size * 0.8)
        t.rt(90)
        newkoch(t, depth-1, size * 0.8)
        t.rt(90)
        newkoch(t, depth-1, size * 0.8)
        t.lt(90)
        t.fd(size)
        newkoch(t, depth-1, size * 0.8)

def newkoch_full (depth, size):
    x = 0
    while x < 4:
        newkoch(t, depth, size)
        t.rt (90)
        x = x + 1

#newkoch_full (3, 10)

#square instead of triangle fractals
#size mod
#'squareflake' instead of snowflake
        

#Sierpinski normal =========================================================
    
def draw_sierpinski(t, depth, length):
    if depth == 1:
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
    else:
        draw_sierpinski(t, depth - 1, length / 2)
        t.fd (length / 2)
        draw_sierpinski(t, depth - 1, length / 2)
        t.bk (length / 2)
        t.lt (60)
        t.fd (length / 2)
        t.rt (60)
        draw_sierpinski(t, depth - 1, length / 2)
        t.lt (60)
        t.bk (length / 2)
        t.rt (60)

#Sierpinski weird
def newsierpinski(t, depth, length):
    color = ["blue", "teal", "cyan", "aqua", "blue", "teal", "cyan", "aqua","blue", "teal", "cyan", "aqua", "blue", "teal", "cyan", "aqua"]
    if depth == 1:
        t.pensize (depth * 0.6)
        t.fillcolor (color[depth])
        t.begin_fill()
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
        t.end_fill()
    else:
        newsierpinski(t, depth - 1, length / 2)
        t.fd (length / 2)
        newsierpinski(t, depth - 1, length / 2)
        t.fillcolor (color[depth + 1])
        t.bk (length / 2)
        t.lt (90)
        t.fd (length / 2)
        t.rt (90)
        newsierpinski(t, depth - 1, length / 2)
        t.fillcolor (color[depth])
        t.lt (90)
        t.bk (length / 2)
        t.rt (90)
        

#newsierpinski(t, 3, 100)

#color fill changes depending on depth
#a version using 90 degree angles, which creates a flat triangle made of smaller triangles.

#Tree normal  =========================================================
def tree (t, depth, length, angle):
    if depth == 1:
        t.fd (length)
        t.bk (length)
    else:
        t.fd (length)
        t.rt (angle / 2)
        tree (t, depth - 1, length, angle)
        t.lt (angle)
        tree (t, depth - 1, length, angle)
        t.rt (angle / 2)
        t.bk (length)

#tree modded
def newtree (t, depth, length, angle, width):
    t.pensize(width)
    if depth == 0:
        t.fd (length)
        t.pencolor("green")
        t.fillcolor ("green")
        t.stamp()
        t.fillcolor ("black")
        t.pencolor("black")
        t.bk (length)
    else:
        t.pencolor("black")
        t.fd (length)
        t.rt (angle / 3)
        newtree (t, depth - 1, length - 5, angle - (.1 * angle), width -1)
        t.lt ((angle / 3) * 2)
        newtree (t, depth - 1, length - 5, angle - (.1 * angle), width -1)
        t.rt (angle / 3)
        newtree (t, depth - 1, length - 5, angle - (.1 * angle), width -1)
        t.bk (length)
 
newtree (t, 3, 60, 80, 5)
 
#added a small length mod so it didn't go in circles for higher depths and also since it looks better
#Turned 2 branches into 3
#Angle of brnach split decreases as depth increases
#stamp green 'leaves' at the ends of the branches 

turtle.exitonclick()

