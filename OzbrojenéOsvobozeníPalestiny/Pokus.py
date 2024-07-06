import re
class myOperátor:
    @staticmethod
    def exkrementer(str):
        numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*',str)]
        result = []
        for guvno in numbers:
            result.append(guvno+11)
        return result
    @staticmethod
    def odkrementer(str):
        numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*',str)]
        result = []
        for guvno in numbers:
            result.append(guvno-7)
        return result

lůzrSting = "Najdi v tomhle textu čísla 55 a 47.8, taky 66.2 a 12 a zpracuj"
print(myOperátor.exkrementer(lůzrSting))
print(myOperátor.odkrementer(lůzrSting))