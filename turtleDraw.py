import turtle

def draw(draw, n, angle, color, shape):
    draw.color(color)
    draw.shape(shape)
    for x in range(0,n):
        draw.forward(100)
        draw.left(angle)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    square = turtle.Turtle()
    #draw square
    draw(square,4,90,"yellow", "turtle")
    #draw circle
    circle = turtle.Turtle()
    circle.shape("arrow")
    circle.color("yellow")
    circle.circle(100)
    #draw triangle
    triangle = turtle.Turtle()
    draw(triangle, 3, 120, "yellow", "turtle")
    window.exitonclick() #to exit
    
draw_art()
