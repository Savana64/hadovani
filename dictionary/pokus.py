my_dict = {
    "jméno":"Adolf",
    "příjmení":"Hitler",
    "narozen":"20,4,1889",
    "rodiště":"Braunau am Inn",
    "národnost":"Skopčák",
    "dílo":"Mein Kampf",
}
print("vypíše slovník zasebou")
print(my_dict)
print("vypíše hodnotu klíče")
for key in my_dict:
    print(my_dict[key])
print("vypíše slovník podsebou")
for key in my_dict:
    print(key,my_dict[key])
print("vypíše klíče, ale nepiš i, toto je pokus")
for i in my_dict:
    print(i)
print("HDP_PPP")
country_HDP_PPP = {
    "Kongo": 1552,
    "Mongolsko": 15088,
    "Česko": 49025,
    "Polsko": 45538,
    "Nigérie": 6148,
}
print(country_HDP_PPP["Nigérie"],"tady sem")
# to je v dupě=pod 2500
# to je bída= pod 10000
# idealos = pod 25000
# jen se neposerte nad 25000
country_HDP_PPP["Lucembursko"]=112053
hodnocení={"cosi",}
for key in country_HDP_PPP:
    if country_HDP_PPP[key]>25000:
        print(key, "jen se neposerte")
    elif country_HDP_PPP[key]>10000:
        print(key,"idealos")
    elif country_HDP_PPP[key]>2500:
        print(key, "to je bída")
    else:
        print(key,"je to v dupě")
