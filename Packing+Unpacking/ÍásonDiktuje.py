import json

#stvoření třídy Adresa
class Adresa():
    # inicializace instance
    def __init__(self, mesto, ulice, nump):
        self.city = mesto
        self.street = ulice
        self.apartment = nump

    # string adresy
    def __str__(self) -> str:
        return f"{self.city}{self.street}{self.apartment}"
    
    # konverze obj Adresa do slovníku
    def to_dick(self):
        return {
           "mesto": self.city,
            "ulice": self.street,
            "nump": self.apartment
            }
    
# Teď zrobím třídu Humanoida
class Hulman:
    # zas nejdřív instance
    def __init__(self, meno, primeni, adresa) -> None:
        self.name = meno
        self.last_name = primeni
        self.address = adresa

    # zrobím string zastupující instanci Hulmana
    def __str__(self) -> str:
        return f"{self.name}{self.last_name}{self.address}"
    
    # převod Hulmanova obj do slovníku
    def to_dick(self):
        return{
            "meno": self.name,
            "primeni": self.last_name,
            "adresa": self.address.to_dick()
        }

# stvoření obj Hulmana
st_obj = Hulman("Andrej ", "Babiš ", Adresa("Průhonice ","Tulipánová ", "983 "))
print(f"ahoj{st_obj}")

# sbalení toho Opičáka do prison str
serialized = json.dumps(st_obj.to_dick())
print(f"Naložený objekt\n{serialized}hovno\n")

# rozbalení JSONa do slovníku
deser = json.loads(serialized)
#print (deser)

# stvoření nové instance Hulmana z deser slovníku
nd_obj = Hulman(deser["meno"],deser["primeni"],Adresa(**deser["adresa"]))

# tisk deserializované instance Hulmana
print(f" Deserializovaný opičák\n{nd_obj}")
                