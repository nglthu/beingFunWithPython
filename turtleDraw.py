import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    draw = turtle.Turtle()
    draw.shape("turtle")
    draw.color("yellow")
    draw.speed(4)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)

    window.exitonclick()


draw_square()
