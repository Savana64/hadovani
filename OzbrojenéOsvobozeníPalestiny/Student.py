class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._grades = []

    def print_age(self):
        print(self._age)

    def add_grade(self, grade):
        self._grades.append(grade)

    def grade_avg(self):
        return sum(self._grades) / len(self._grades)
    
    def get_name(self):
        return self._name
    
    def get_age(self, hovno = 60):
        return self._age + hovno


#student = Student()
student = Student("Petr", 10)

print(type(student))
#print(student._name)
print(student.get_name())
student._age = 21
#student._grades.append("1-")
#print(student._age)
print(student.get_age())
print(student.get_age(-4))


student.add_grade(4)
student.add_grade(3)
print(student.grade_avg())
class Pičus(Student):
    def __init__(self,_name, _age, skóre):
        super().__init__ (_name, _age) 
        self.skóre = skóre

    def jeÚspěch(self, skóre):
        return True if skóre > 1 else False

zmrd = Pičus("Zunka", 66, 0)
print(f"Je {zmrd._name} úspěšný hráč? {zmrd.jeÚspěch(0)}. Je to prostě sráč.")



