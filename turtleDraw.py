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
    for x in range(1,37):
        square.right(10)
        draw(square,4,90,"yellow", "turtle")
    #draw circle
##    circle = turtle.Turtle()
##    circle.shape("arrow")
##    circle.color("yellow")
##    circle.circle(100)
    #draw triangle
##    triangle = turtle.Turtle()
##    draw(triangle, 3, 120, "yellow", "turtle")
    window.exitonclick() #to exit

def draw_follower():
    window = turtle.Screen()
    window.bgcolor("green")
    square = turtle.Turtle()
    #draw triangle
    triangle = turtle.Turtle()
    for x in range(1,37):
        triangle.right(20)
        draw(triangle, 3, 120, "yellow", "turtle")
    window.exitonclick() #to exit
    
#draw_art()
draw_follower()



    
