import pickle
import os

# fce vytvoří cestu k souboru.
def stvoř_cestu(název_pilníku):
    # Adresář výskytu.
    skříp_adresáře = os.path.dirname(os.path.realpath(__file__))
    # vrátí celou cestu.
    return os.path.join(skříp_adresáře, název_pilníku)

# fce serializuje data do pilníku.
def serializuj(název_pilníku, data):
    # Otevře soubor a nasype do něj data.
    with open(stvoř_cestu(název_pilníku), "wb") as filé:
        pickle.dump(data, filé)

# Fce vytáhne data ze souboru a deserializuje je.
def deserializuj(název_pilníku):
    # Přečte binární soubor a vylije lák.
    with open(stvoř_cestu(název_pilníku), "rb") as filé:
         data = pickle.load(filé)
    return data

# stvoření třídy pro osobnost.
class Osoba:
    # konstruktor třídy? Asi,hovno se v tom vyznám.
    def __init__(self, jméno, přímení):
        self.jméno = jméno
        self.přímení = přímení

    # vrátí celé méno.
    def identifikuj_se(self):
        return f"{self.jméno}{self.přímení}"

try:
    # stvoření instance třídy.
    sh = Osoba("Štěpán", " Jestřábník")
    # Ztotožnění.
    print(f"Největší fyzik:\n{sh.identifikuj_se()}\n originál")

    # Pojmenuj soubor.
    název_pilníku = "tojefuk.dat"

    # Serialize the Person instance and write it to a file.
    serializuj(název_pilníku, sh)
    # Read the file, deserialize its content and store it in 'person_restored'.
    vybalená_osoba = deserializuj(název_pilníku)

    # Vypíše celé méno vylité osoby.
    print(f"Osoba po teleportu:\n{vybalená_osoba.identifikuj_se()}\n")

# Zachycení vyjímek, kdyby to přišlo.
except Exception as hovno:
    print(hovno,"hovno")