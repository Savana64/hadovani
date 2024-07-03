class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price_eur(self):
        return self.price / 25
    
p = Product("banan", 30)

print(p.name)
print(p.price)
print(p.price_eur)