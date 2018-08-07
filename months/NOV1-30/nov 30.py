""" Added onto Class program from yeterday, made a dance for reginald. We
retouched on using the turtle module and Pen class. We made several pictures to practice
the commands A.M session, will be resumed later"""

class Things:
    pass
class Inanimate(Things):
    pass
class Animate (Things):
    pass
#class Sidewalks(inanimate):
    #pass
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
            
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        #print('eating leaves')
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def find_food(self):
        self.move()
        print("I've found food")
        self.eat_food()
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_back(self):
        print('left foot back')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_back(self):
        print('right foot back')
    def spin(self):
        print('Spin three times and do the splits')
    def dance(self):
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_forward()
        self.left_foot_back()
        self.spin()

reginald = Giraffes()
reginald.dance()

import turtle
t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()

t1.forward(100)
t1.left(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t2.forward(110)
t2.left(90)
t2.forward(25)
t2.right(90)
t2.forward(25)
t3.forward(110)
t3.right(90)
t3.forward(25)
t3.left(90)
t3.forward(25)
t4.forward(100)
t4.right(90)
t4.forward(50)
t4.left(90)
t4.forward(50)

"""t1.forward(70)
t2.right(80)
t2.forward(50)
t3.backward(250)
t4.left(110)
t4.forward(150)

t1.left(90)
t1.forward(300)
t2.left(90)
t2.forward(150)
t2.right(90)
t2.forward(100)
t3.up()
t3.forward(100)
t3.down()
t3.left(90)
t3.forward(300)"""



    
    
        
        
