import random
import json
import os
import sys
sys.path.append('../')
import culori

file = open('opere.json')
data = json.load(file)

def ani(nrTeste):
    corecte = 0
    gresite = 0
    opereVerificate = []
    while nrTeste:
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
        nrTeste -= 1
    
    return corecte, gresite

def tema(nrTeste):
    culori.puts("\nDeoarece ai ales acest tip de test, verificarea va trebui facuta de tine\n", culori.colors.red)
    corecte = 0
    gresite = 0
    opereVerificate = []
    while nrTeste:
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
        nrTeste -= 1

        tip = int(input("CORECT(1), GRESIT(2): "))
        if tip == 1:
            corecte += 1
        else:
            gresite += 1
    
    return corecte, gresite

if __name__ == "__main__":
    iesire = False

    totalCorecte = 0
    totalGresite = 0

    while not iesire:
        print("1. Ani\n2. Tema")
        test = int(input("\nTipul de test: "))
        nrOpere = len(data["opere"])
        nr = int(input("Numarul de teste(maxim " + str(nrOpere) + " teste): "))
        if test == 1:
            corecteTest, gresiteTest = ani(nr)
            totalCorecte += corecteTest
            totalGresite += gresiteTest
        elif test == 2:
            corecteTest, gresiteTest = ani(nr)
            totalCorecte += corecteTest
            totalGresite += gresiteTest

        culori.puts("\nRapspunsuri corecte pentru acest test: " + str(corecteTest), culori.colors.green)
        culori.puts("\nRaspunsuri gresite pentru acest test: " + str(gresiteTest) + '\n', culori.colors.red)

        culori.puts("\nVrei sa continui cu alt test?(DA/NU)\n", culori.colors.cyan)
        continua = input()
        os.system('clear')

        if continua.upper() == "NU":
            iesire = True

        

    culori.puts("\nTotal raspunsuri corecte: " + str(totalCorecte), culori.colors.green)
    culori.puts("\nTotal raspunsuri gresite: " + str(totalGresite) + '\n', culori.colors.red)
