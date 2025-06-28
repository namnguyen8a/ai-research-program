class Shape:
    def draw(self):
        print("Drawing a shape")
        return None

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
        return None

class Square(Shape):
    def draw(self):
        print("Drawing a square")
        return None

def render(shape):
    shape.draw()

shapes = [Circle(), Square()]
for shape in shapes:
    render(shape)