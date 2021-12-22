
import math
class TRectangle:
    def __init__(self,*args) :
        if   len(args)==0:
#v=TRectangle()
              self.x=0
              self.y=0

        elif len(args)==2:
#v2=TRectangle(2,4)
              self.x=args[0]
              self.y=args[1]
        elif len(args)==1 and isinstance(args[0],TRectangle):
#v3=TRectangle(V2)
               self.x=args[0].x
               self.y=args[0].y

    def input_coordinates(self):
          self.x=float(input('x='))
          self.y = float(input('y='))
    def __str__(self):
          return 'TRectangle ({0},{1})'.format(self.x,self.y)

    def square(self):
        return self.x * self.y
    def perimeter(self):
        return 2*(self.x+self.y)

    def is_equal(self,other_rectangle):
        eps=0.00001
        return math.fabs(self.x-other_rectangle.x)<eps and math.fabs(self.y-other_rectangle.y)<eps
    def __add__(self,other_rectangle):
        return TSquare(self.x+other_rectangle.x,self.y+other_rectangle.y)
    def __sub__(self,other_rectangle):
        return TSquare(self.x-other_rectangle.x,self.y-other_rectangle.y)
    def __mul__(self,other_rectangle):
        return self.x*other_rectangle.x+self.y*other_rectangle.y






v=TRectangle()
v.input_coordinates()
v.__str__()
print('S прямокутника ={0} '.format(v.square()))
print('P прямокутника ={0} '.format(v.perimeter()))

