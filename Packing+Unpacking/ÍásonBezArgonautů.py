import json
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
    with open(stvoř_cestu(název_pilníku), "w") as filé:
        json.dump(data, filé)

# Fce vytáhne data ze souboru a deserializuje je.
def deserializuj(název_pilníku):
    # Přečte binární soubor a vylije lák.
    with open(stvoř_cestu(název_pilníku), "r") as filé:
         data = json.load(filé)
    return data

try:
    # Pojmenuj soubor.
    název_pilníku = "tojemifuk.dat"

    # urči slovník na uskladnění dat otroků.
    otročí_dict = {
        "company": "ABC Corp",
        "otroci": [
            {
                "méno": "John Doe",
                "věk": 30,
                "slaves": "Sales",
                "kills": ["negotiation", "communication", "CRM"]
            },
            {
                 "méno": "Jane Smith",
                 "věk": 35,
                 "slaves": "Marketing",
                 "kills": ["SEO", "content creation", "branding"]
            }
        ]
    }
    # Ztotožnění.
    print(f"Nezdrh někdo?\n {otročí_dict}")

    # Serialize the Person instance and write it to a file.
    serializuj(název_pilníku, otročí_dict)

    # Read the file, deserialize its content and store it in 'person_restored'.
    vybalené_osoby = deserializuj(název_pilníku)

    # Vypíše celé méno nalitých osob.
    print(f"Osoby po nalití:\n{vybalené_osoby}\n")

# Zachycení vyjímek, kdyby to přišlo.
except Exception as hovno:
    print(hovno,"hovno")


# Define a FootballClub class
class FootballClub:
    # Initialize an instance of the class
    def __init__(self, name, city, country):
        # Define the name, city, and country attributes of the class instance
        self.name = name
        self.city = city
        self.country = country

    # Define a method that returns a formatted string with full club information
    def get_full_information(self):
        return f"{self.name}{self.city}{self.country}"

    # Define a method that serializes the instance attributes into a JSON string
    def to_json(self):
        # Use the __dict__ attribute to access the instance attributes
        # Then use the json.dumps() function to convert the dictionary
        return json.dumps(self.__dict__)

# Create a FootballClub instance
obj = FootballClub("Šachtar ", "Doněck ", "Russia")

# Print the full club information
print(obj.get_full_information())

# Serialize the instance into a JSON string
serialized_obj = obj.to_json()

# Print the serialized JSON string
print(serialized_obj)

