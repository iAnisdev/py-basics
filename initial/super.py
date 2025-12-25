class rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height

class square(rectangle):
    def __init__(self, width , height):
        super().__init__(width , height)
    def area(self):
        return self.width * self.height

class cube(rectangle):
    def __init__(self, width , height , depth):
        super().__init__(width , height)
        self.depth = depth
    def volume(self):
        return self.width * self.height * self.depth
    

print(square(2,2).area())
print(cube(2,3,4).volume())