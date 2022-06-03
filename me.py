
import math 

class Circle():
    def __init__(self, r, a):
        self.radius = r
        self.area = a
    
    def point_distance(x1, y1, x2, y2):
        r = math.sqrt(((y2-y1)**2) + ((x2-x1)**2))
        return r
    
    def area(self):
        a = 2*math.pi*self.radius**2
        return a
