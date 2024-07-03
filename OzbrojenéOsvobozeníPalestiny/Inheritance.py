class Mendel:
    def __init__(self):
        self.city = "Brno"
        self.age = 50

    def get_food(self):
        return "hrach"
    
class Synacek (Mendel):
    def speak(self):
        return "UAAAA"
    
m = Mendel()
s = Synacek()

print(m.age)
print(s.age)

print(s.speak())
print(m.speak())