cities = {
    "Venezuela":"Buenos Aires",
    "Vietnam":"Hanoj",
    "Aljaška":"Juneau",
}
print(cities["Aljaška"])

travel_diary ={
    "Venezuela": ["Caracas","Maracaibo", "Valencia"],
    "Vietnam": ["Hanoj","Ho Či Minovo Město","Haiphong"],
    "Aljaška":["Juneau","Anchorage","Valdez"]
}




print(travel_diary["Vietnam"][1])
print ("\t\tSlovník ve slovníku")
cestovní_deník={
    "Venezuela": {"projitá města":["Caracas","Maracaibo", "Valencia"],"počet návštěv":3},
    "Vietnam": {"projitá města":["Hanoj","Ho Či Minovo Město","Haiphong"],"počet návštěv":2},
    "Aljaška":{"projitá města":["Juneau","Anchorage","Valdez"], "počet návštěv":0}
}
print(cestovní_deník)
print(cestovní_deník["Vietnam"])
print(cestovní_deník["Vietnam"]["projitá města"] )
print(cestovní_deník["Vietnam"]["projitá města"][2])

print("\t\tslovník v seznamu")
cestovní_deník_list = [
    {
       "Země":"Venezuela",
       "projitá města":["Caracas","Maracaibo", "Valencia"],
       "počet návštěv":3, 
    },
{
    "Země":"Vietnam", 
 "projitá města":["Hanoj","Ho Či Minovo Město","Haiphong"],
 "počet návštěv":2,
 },
 {
     "Země": "Aljaška",
     "projitá města":["Juneau","Anchorage","Valdez"],
       "počet návštěv":0
 },
]
print(cestovní_deník_list[2])

print(cestovní_deník_list[1]["projitá města"])
print(cestovní_deník_list[0]["projitá města"][-2])

def add_countries(country_name,town_list, visits):
    new_dictionary= {}
    new_dictionary["Země"]=country_name
    new_dictionary["projitá města"]=town_list
    new_dictionary["počet návštěv"]=visits
    cestovní_deník_list.append(new_dictionary)
add_countries("Itoška", ["Řím","Milano","Livorno"],6)
print(cestovní_deník_list,"\nasdf")
print(cestovní_deník_list[3]["počet návštěv"])