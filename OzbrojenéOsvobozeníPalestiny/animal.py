class Animal:
    def __init__(self,name,age,sound):
        self.name=name
        self.age=age
        self.sound=sound

    def get_name(self):
        return(self.name)
    
    def get_age(self):
        return(self.age)
    
    def get_sound(self):
        return(self.sound)
    
    def make_sound(self):
        print(self.sound)

animal=Animal("Fík",49,"ahój")

animal.make_sound()