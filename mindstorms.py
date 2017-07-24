import turtle   #this is the thing that moves around on the screen and actually draws the things

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('yellow')
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()


def draw_square():
    brad = turtle.Turtle()  # our turtle is called 'Brad'^^
    brad.shape('turtle')
    brad.color('red')
    brad.speed(2)
    #draw the rectangle
    for i in range(4):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    # create another class instance
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)


def draw_triangle():
    # create another class instance
    mike = turtle.Turtle()
    mike.shape('classic')
    mike.color('black')
    for i in range(3):
        mike.backward(200)
        mike.left(120)

