import pickle
slovník = {
    "František Nepil":"Střevíce z lýčí",
    "Douglas Adams":"Převážně neškodná",
    "James Herriot":"Wet in a spin"
}
with open("pickle.bin","wb") as file:
    pickle.dump(slovník,file)


with open("pickle.bin","rb") as file:
    data = pickle.load(file)

for x in data:
    print(x)