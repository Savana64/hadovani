# Na základě tadyhle vzorového příkladu od ejaj
def pruzkum(hloubka):
    print(f'Rozhlížím se v hloubce {hloubka} m')
    if hloubka >= 30:
        print('Už toho bylo dost!')
    else:
        print(f'Zanořuju se (z {hloubka} m)')
        pruzkum(hloubka + 10)
        print(f'Vynořuju se (na {hloubka} m)')

pruzkum(0)
# jsem napsala tady tenhle prográmek, aniž bych pochopila, jak to funguje
def řada(číslo):
    print(f"přičítám číslo {číslo}")
    if číslo == 0:
        print("jdem to vypsat")
    else:
        print(f"nejdřív vezmu {číslo} ")
        řada(int(input("a dál?")))
        print(f"že by pozpátku?{číslo}")
    
řada(číslo=int(input("tu to piš\n")))
print(0)
# zkrácená verze
def řada(číslo):
    if číslo == 0:              
        print(0)
    else:
        řada(int(input("a dál?")))
        print(číslo)
        
řada(číslo=int(input()))

# a jejich verze
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()


