import random
from art import logo, door
from os import system, name

# Eetun python clear
def clear():
 
    # Jos käyttöjärjestelmänä Windows
    if name == 'nt':
        _ = system('cls')
 
    # Jos käyttöjärjestelmänä Mac/Linux
    else:
        _ = system('clear')


ovet = [1,2,3]
score = 0

clear()
print(logo)
print("Valitse ovi. Oven takana on koira tai keksi.")

def jatka():
    jatkuu = input("jatketaanko peliä? j/e: ")
    if jatkuu == "j":
        peli()
    elif jatkuu == "e":
        print(f"keksisi: {score}🍪")
        exit()
    else:
        print("en ymmärrä")
        jatka()
        
def sokerihumala():
    if score >= 3:
        print("Saavutit sokerihumalan. Voitit! 🍪🍪🍪🍴")
        exit()

def peli():
    keksi = random.choice(ovet)
    
    sokerihumala()
    
    print(door)
    possu = int(input("valitse ovi (1, 2, 3) tai koira syö sinut: ")) 
    
    if possu == keksi:
        print("oikein! 🥳 sait keksin. 🍪")
        globals()['score'] += 1
        sokerihumala()
        jatka()
        
    else:
        print("väärin! koira söi sinut silti. nam nam.🍴🐶")
        print(f"keksisi: {score}🍪")

peli()