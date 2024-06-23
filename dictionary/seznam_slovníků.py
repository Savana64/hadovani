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

print(cestovní_deník_list[2]["projitá města"])
print(cestovní_deník_list[2]["projitá města"][-2])