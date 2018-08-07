""" We created classes,defined functions inside of classes,we called a function
with a object, called a function with another function using self parameters. We also
also assigned different values to different object within the same class.We tested
different random ideas about what would happen changing order and placment of functions we
we called. We debugged multiple times finding fundamental,spelling and gramatic
typing errors. We had a lot of fun:) Completed chapter 8"""


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
        
        
class Giraffes:
    def __init__(self,spots):
        self.giraffe_spots = spots
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)



"""reginald = Giraffes()
harold =Giraffes()
reginald.move()
harold.eat_leaves_from_trees()


import turtle
avery = turtle.Pen()
kate = turtle.Pen()

jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)

reginald = Giraffes()
reginald.move()
reginald.breathe()
reginald.eat_food()
reginald.feed_young_with_milk()


reginald.find_food()
reginald.dance_a_jig()"""



"""animals
mammals
giraffe"""






