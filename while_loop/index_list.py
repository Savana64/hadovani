i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)
    
a = int(input())
b = 0
cisla = []
while a !=0:
    cisla.append(a)
    a = int(input())
print(cisla.index(max(cisla)))
customers = ['Bob','Anna','Joe','Bob','Nick']
list5 = [i for i in customers if i != 'Bob' and i != 'Joe']
print(list5) #['Anna', 'Nick']
category = ["Drama", "Comedy", "Mystery","Romance","Comedy"]
print(category.index("Mystery")) #2
print(category.index("Comedy")) #1