from turtle import Turtle

class Turtles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=10, stretch_len=2)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)



