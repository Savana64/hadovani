class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._grades = []

    #def print_age(self):
    #    print(self._age)

    def add_grade(self, grade):
        self._grades.append(grade)

    def grade_avg(self):
        return sum(self._grades) / len(self._grades)
    
    def get_name(self):
        return self._name
    
    def get_age(self, offset = 0):
        return self._age + offset


#student = Student()
student = Student("Petr", 10)

print(type(student))
#print(student._name)
print(student.get_name())
#student._age = 20
#student._grades.append("1-")
#print(student._age)
print(student.get_age())
print(student.get_age(-40))


grade = int(input("Zadej ctyřku: "))
student.add_grade(grade)
student.add_grade(int(input("Zadej trojku")))
print(F"{student.get_name()} má průměrnou známku {student.grade_avg()}")
