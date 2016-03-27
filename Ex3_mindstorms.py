import turtle


window = turtle.Screen()
window.bgcolor("white")

def draw_flower(n):
    ff = turtle.Turtle()
    ff.shape("turtle")
    ff.color("blue")
    ff.speed(10)

    for j in range(n/2):

        for i in range(2):
            ff.forward(100)
            ff.right(60)
            ff.forward(100)
            ff.right(120)

        ff.right(240)

        for i in range(2):
            ff.forward(100)
            ff.left(60)
            ff.forward(100)
            ff.left(120)
            
        ff.left(240)
        ff.right(360/n)

    ff.left(90)
    ff.forward(200)
    window.exitonclick()        

def draw_square(n):
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)

    for j in range(n):
       
        for i in range(4):
            brad.forward(100)
            brad.right(90)

        brad.right(360/n)


    window.exitonclick()

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)    


def draw_triangle():
    kk = turtle.Turtle()
    kk.shape("circle")
    kk.color("purple")

    for i in range(3):
        kk.left(120)
        kk.forward(100)
    
    window.exitonclick()

draw_flower(60)
#draw_square(50)
#draw_circle()
#draw_triangle()
