class Animal:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color

my_dog = Animal("brown")

my_dog.set_color("black")