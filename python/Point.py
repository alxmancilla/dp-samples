#!c:/Python34/python.exe -u
# -*- coding: utf-8 -*-

import math

class Point:
    """Clase Point define objeto bidimensional en el plano cartesiano"""
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        return math.sqrt(dx*dx+dy*dy)
    
    def equals(self, aPoint):
        return (self.x == aPoint.x) and (self.y == aPoint.y)


if __name__=='__main__':
    print(type(Point))
    p1 = Point()
    p2 = Point()
    
    print(type(p1))
    print(p1 == p2)
    print(p1.equals(p2))
    
    p1.move(2,3)
    p2.move(5,7)
    print( p1.distance(p2) )
    