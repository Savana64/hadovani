class Vehikl:
    def __init__(self,sajna,model,vintáž,kmage,sound):
        self.brand=sajna
        self.model=model
        self.year_of_production=vintáž
        self.mileage=kmage
        self.sound=sound

    def get_brand(self):
        return(self.brand)
    
    def get_model(self):
        return(self.model)
    
    def get_year_of_production(self):
        return(self.year_of_production)
    
    def get_mileage(self):
        return(self.mileage)
    
    def add_mileage(self,new_miles):
        self.mileage=self.mileage+new_miles

    def get_sound(self):
        return(self.sound)
    
    def info(self):
        print(car.brand, car.model,car.year_of_production,car.mileage,car.sound)

car=Vehikl("honda","stream",2001,382562,"kadlekadle")

car.add_mileage(564)
car.info()