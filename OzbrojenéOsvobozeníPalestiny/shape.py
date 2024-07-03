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

animal=Animal("kapr",49,"p")

animal.make_sound()

class Cat(Animal):
    def __init__ (self, name, age):
        super().__init__(name,age,"mňau")
        

   
class Doga(Animal):
    def __init__ (self, name, age):
        super().__init__(name,age,"buf")
       
cat=Cat("Kašpar",12)
čokl=Doga("Rek",15)

cat.make_sound()
čokl.make_sound()