import random
import json
import os

f = open('opere.json')
data = json.load(f)

print("1. Ani\n")
test = int(input("\nTipul de test: "))
nr = int(input("\nNumarul de teste: "))

if test == 1:
    while nr:
        opera = random.choice(data["opere"])
        an = opera["an"]
        userAn = input("\n" + opera["numeTitlu"] + "\nAnul aparitiei este: ")
    
        print("\nRaspunsul corect: " + an)
        print("Raspunusl tau: " + userAn)
        nr -= 1