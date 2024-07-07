class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."
    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."

class Developer (Person):
    def __init__(self, firstName, lastName, age, jobTitle):
        super().__init__(firstName, lastName, age)
        self.jobTitle = jobTitle
        self.__salary = 0
    
    def setBasicSalary(self):
        if self.__rung == 'Junior':
            self.__salary = 1000
        elif self.__rung == 'Middle':
            self.__salary = 3000
        elif self.__rung == 'Senior':
            self.__salary = 5000
        elif self.__rung == 'Lead':
            self.__salary = 10000
    
    @classmethod
    def setRung(cls, rungName):
        cls.__rung = rungName
    def calculateSalary(self, perc):
        return  self.__salary+self.__salary*perc    
    def getInfo(self):
        return super().getInfo() + f"\njobTitle -  {self.jobTitle};\nrung - {self.__rung};\nbasic salary - {self.__salary}."

Developer.setRung("Junior")
jun1 = Developer("Kate", "Smith", 22,"UI (user interface) designer")
jun2 = Developer("Joe", "Smith", 25, "Back-end developer")
# tadyhle takhle se zipuje, všímej
for juno in zip((jun1, jun2, jun1, jun2), (0.25, .3, 5, 66)):
    juno[0].setBasicSalary()
    print(juno[0].getInfo())
    print(f"expexted salary:{juno[0].calculateSalary(juno[1])}")
    