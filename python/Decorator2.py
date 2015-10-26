from abc import ABCMeta

class Shape(metaclass=ABCMeta):
	def draw(self): pass

class Rectangle(Shape):
	def draw(self):
		print("shape rectangle")
		
		
class Circle(Shape):
	def draw(self):
		print("shape circle")
		
class ShapeDecorator(Shape):
	def __init__(self, decoratedShape):
			self.decoratedShape = decoratedShape
	
	def draw(self):
		self.decoratedShape.draw()
		
class RedShapeDecorator(ShapeDecorator):
	def draw(self):
		self.decoratedShape.draw()
		self.doSomething(self.decoratedShape)
		
	def doSomething(self, decoratedShape):
		print("decorated shape in RED")
		
if __name__ == "__main__":
	circle = Circle()
	redCircle = RedShapeDecorator(Circle())
	
	circle.draw()
	
	redCircle.draw()
	
