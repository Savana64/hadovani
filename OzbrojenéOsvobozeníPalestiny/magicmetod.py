class Class1:

    def __init__(self):
        print("Hi! I am __init__ magic method.")

    def __new__(cls):
        print("Hi! I am __new__ magic method.") 
        return super(Class1, cls).__new__(cls)   
        
obj1=Class1()

junak1 = "Ferda"
junak2 = "Pytlík"

for jun in zip((junak1, junak2),(0.25,0.3)):
    
    print(f"expexted salary:{jun[0],(jun[1])}")