from turtle import Turtle, Screen
from itertools import cycle
from time import  sleep

class App:
    def __init__(self, master):
        self.master = master
        colors = ['blue', 'yellow']
        self.color = iter(cycle(colors))
        
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(2)
        self.turtle.pensize(4)
        
    def start(self):
        times = int(self.master.numinput('X Polygon', 'Several times? '))
        
        for time in range(times):
            sides = int(self.master.numinput('X Polygon', f'Number of sides for polygon{time+1}: ', minval=3, maxval=15))
            angle = 180-((180*(sides-2))/sides)
            length = 150 - (sides*2)
            self.go(50, -180+((10-sides)*25))
            
            for side in range(sides):
                if sides%2 and side==sides-1:
                    self.turtle.color('gray')
                else:
                    self.turtle.color(next(self.color))
        
                self.turtle.left(angle)
                self.turtle.forward(length)
                
            sleep(1.5)
            self.turtle.clear()
            
        self.exit()
        
    def go(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x=x, y=y)
        self.turtle.pendown()
        
    def exit(self):
        self.go(-70, 0)
        self.turtle.color('white')
        self.turtle.write('Click for exit', font='arial 20')
        self.master.exitonclick()

if __name__ == "__main__":
    root = Screen()
    root.bgcolor('black')
    root.title('X Polygon')
    root.setup(width=700, height=700, startx=350, starty=70)
    
    app = App(root)
    app.start()
