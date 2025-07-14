from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_bits = []
        self.snake_length_unit = 0
        self.start_x = 0
        self.create_snake()
        self.first_bit = self.snake_bits[0]
        
    def create_snake(self):
        for _ in range(3):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(self.start_x, 0)
            self.start_x -= 20
            self.snake_bits.append(t)    
        
    def move_forward(self):
        for bit in range(len(self.snake_bits) - 1, 0, -1):
            coords = self.snake_bits[bit-1].pos()
            self.snake_bits[bit].setpos(coords)
            
        self.snake_bits[0].forward(20)
    
    def add_snake_bit(self):
        t = Turtle("square")
        t.penup()
        t.color("white")
        self.snake_bits.append(t)
    
    def up(self): #90
        if self.first_bit.heading() != 270:
            self.snake_bits[0].setheading(90)

    def down(self): #270
        if self.first_bit.heading() != 90:
            self.snake_bits[0].setheading(270)                

    def left(self): #180
        if self.first_bit.heading() != 0:
            self.snake_bits[0].setheading(180)

    def right(self): #0
        if self.first_bit.heading() != 180:
            self.snake_bits[0].setheading(0)