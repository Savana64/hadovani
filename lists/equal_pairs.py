#a = [int(s) for s in input().split()] a = [int(s) for s in input().split()]
# print(' '.join([str(i) for i in a]))
import math
b = [0 1 43 10 13 33 15 8 18 21]
c = b.append(sum(b))
a = sorted(c)
cow = 0
suma = 0
kombi = 0
for i in range (len(a)+1):
    if a[i] == a[i+1]:
       continue
    cow=(a.count(a[i]))
    suma +=cow
    if cow >1:
        kombi +=(math.factorial(cow)/(math.factorial((cow-2))*2)) 
    if suma >=(len(a))-1:
        break
    #if a[i] != a[i+1]:
print(int(kombi))

print ("Generátor seznamu faktoriálů")
import math
n = 5
b = [math.factorial(i) for i in range (n+1)]
print(b)

print ("print(' '.join(a)) lze použít jen pro str, pro int vyvolá chybu")
#print(' '.join(a))
print(' '.join([str(i) for i in a]))

print ("Ternární operátor")
muz = False # nějaká proměnná udávající pohlaví
nazev_pohlavi = ""
if muz:
    nazev_pohlavi = "muž"
else:
    nazev_pohlavi = "žena"
print(nazev_pohlavi)
# obecná syntaxe:  prvni_hodnota if (vyraz) else druha_hodnota

muz = True # nějaká proměnná udávající pohlaví
nazev_pohlavi =  "muž" if (muz) else "žena"
print(nazev_pohlavi)

customers = ['Bob','Anna','Joe','Bob','Nick']
if ('Bob' in customers):
    print("Bob is our customer")
else:
    print("Sorry")

a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)
