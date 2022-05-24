import random
import json
import os
import sys
sys.path.append('../')
import culori

file = open('opere.json')
data = json.load(file)

print("1. Ani")
test = int(input("\nTipul de test: "))
nr = int(input("Numarul de teste: "))

if test == 1:
    while nr:
        opera = random.choice(data["opere"])
        an = int(opera["an"])
        culori.puts(opera["numeTitlu"] + culori.colors.blue)
        culori.puts("\nAnul aparitiei este: ", culori.colors.white)
        userAn = int(input())
        if an == userAn:
            culori.puts("\nRASPUNS CORECT", culori.colors.green) 
        else:
            culori.puts("\nRASPUNS GRESIT. MAI INVATA...", culori.colors.red)
        print("\nRaspunsul corect: " + str(an))
        print("Raspunusl tau: " + str(userAn))
        nr -= 1
