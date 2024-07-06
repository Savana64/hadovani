import random
class Sportsman:
    hobby = "cooking meth"
    def __init__(self, nick, height, weight):
        # public properties
        self.nick = nick
        self.height = height
        #protecte properties
        self._weight = weight
        #private properties
        self.__personID = random.randint(1,100)

    #private methods
    def __showID(self):
        print(self.__personID)
    
    #public methods
    def getInfo(self):
        self.__showID()
        return f"Sportsman's nick- {self.nick}, height- {self.height} and weight- {self._weight}."
    
    def sayHi(self, mesič):
        print(self.getInfo())
        return f"{mesič}! I am {self.nick}."
    
    #static methods
    @staticmethod
    def sayGreetings():
        print("Nice to meth you")
    
    #class methods
    @classmethod
    def defaultHobby(cls):
        cls.hobby = "drinking beer"

sportsman1 = Sportsman("Kyklop", 164, 72)
print(sportsman1.hobby)
Sportsman.defaultHobby()
sportsman2 = Sportsman("Číňan",166, 65)
print(sportsman2.hobby)
sportsman3 = Sportsman("Páťa", 189, 96)
print(sportsman3.hobby)