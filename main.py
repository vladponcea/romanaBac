import random
import json
import os
import sys
sys.path.append('../')
import culori

file = open('opere.json')
data = json.load(file)

print("1. Ani\n2. Tema")
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
elif test == 2:
    culori.puts("\nDeoarece ai ales acest tip de test, verificarea va trebui facuta de tine\n", culori.colors.red)
    corecte = 0
    gresite = 0
    opereVerificate = []
    while nr:
        opera = random.choice(data["opere"])
        while opera in opereVerificate:
            opera = random.choice(data["opere"])
        opereVerificate.append(opera)
        
        tema = opera["tema"]
        culori.puts("\n" + str(opera["numeTitlu"]), culori.colors.blue)
        culori.puts("\nTema este: ", culori.colors.white)
        userTema = str(input())
        
        print("\nRaspunsul corect: ")
        for x in tema:
            culori.puts(str(x) + '\n', culori.colors.green)
        print("Raspunusl tau: " + userTema)
        nr -= 1

        tip = input("CORECT(1), GRESIT(2): ")
        if tip == 1:
            corecte += 1
        else:
            gresite += 1

culori.puts("\nTotal raspunsuri corecte: " + str(corecte), culori.colors.green)
culori.puts("\nTotal raspunsuri gresite: " + str(gresite) + '\n', culori.colors.red)
