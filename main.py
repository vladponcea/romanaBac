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
    corecte = 0
    gresite = 0
    opereVerificate = []
    while nr:
        opera = random.choice(data["opere"])
        while opera in opereVerificate:
            opera = random.choice(data["opere"])
        opereVerificate.append(opera)
        
        an = int(opera["an"])
        culori.puts("\n" + str(opera["numeTitlu"]), culori.colors.blue)
        culori.puts("\nAnul aparitiei este: ", culori.colors.white)
        userAn = int(input())
        
        if an == userAn:
            corecte += 1
            culori.puts("\nRASPUNS CORECT", culori.colors.green) 
        else:
            gresite += 1
            culori.puts("\nRASPUNS GRESIT. MAI INVATA...", culori.colors.red)
        
        print("\nRaspunsul corect: " + str(an))
        print("Raspunusl tau: " + str(userAn))
        nr -= 1

    culori.puts("\nTotal raspunsuri corecte: " + str(corecte), culori.colors.green)
    culori.puts("\nTotal raspunsuri gresite: " + str(gresite), culori.colors.red)
