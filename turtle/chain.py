import turtle

links = [1,2,3,4,5,6,7,8]
sides = [1,2,3,4,5,6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# move back so chain is centered
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    # draw a hexagon
    for side in sides:
        weaver.forward(10)
        weaver.right(60)

        #scoot over to the next line
        weaver.penup()
        weaver.forward(20)
        weaver.pendown()

weaver.hideturtle()