import math
from telnetlib import WILL

class Circle():
    PI=3.142
    def __init__(self,radius,circumference):
        self.radius=radius
        self.circumference=circumference
        
    def area(self):
        return Circle.PI*self.radius*self.radius
    
    def circumference(self):
        return 2*Circle.PI*self.radius
    
    
class Square():
    def __init__(self,a,):
        self.a=a
        
    def area(self):
        return Square.a*self.a*self.a
    
    def perimeter(self):
        return 4*self.a
    
class Rectangle():
    def __init__(self,l, w):
        self.w = w
        self.l = l

    def area(self):
        return self.w*self.l

    def perimeter(self):
        return 2(self.w + self.l)
    
class Spheres():
    def __init__(self, r):
        self.radius = r
        self.area = 0
        self.volume = 0

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r=self.radius
        self.area = 4 * 3.14 * (r*r)
        return (self.area)

    def getVolume(self):
        r=self.radius
        self.volume = (4/3) * 3.14 * (r * r * r)
        return (self.volume)
        
          
    
        
    
        
 
    
    
    