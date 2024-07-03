class Animal:
    def __init__(self):
        self.name = "Rek"
        self._age = 10
        self.__color = "brown"

    def get_color(self):
        return self.__color

a = Animal()

print(a.name)
print(a._age)
#print(a.__color) -- nefunguje, bo jsou před ním dvě podtržítka, tak je to tajne
print(a.get_color())  # a vytáhneš to z kódu jen pomocí fce