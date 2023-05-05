# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:13:35 2023

@author: nik1811
"""
#Importerer biblioteker
import csv
import numpy as np
import matplotlib.pyplot as plt

tekstfil = "oppgave11.csv"
#Lager en funksjon for å lese filen om vi skulle trenge det
def lesFil():
    with open(tekstfil, encoding="utf-8") as fil:
        fil = csv.reader(fil, delimiter=";")
        for i in fil:
            print(i)

#A
def matOgStrom():
    #Åpner filen
    with open(tekstfil, encoding="utf-8") as fil:
        #bruker csv biblioteket for å få verdiene i lister
        fil = csv.reader(fil, delimiter=";")
        #Henter overskriften
        overskrift = next(fil)
        
        #Summeerer opp alle beløpene (rad[2])
        total = 0
        for rad in fil:
            total += int(rad[2])
        
        print(f"Antall kroner brukt: {total}")
            

matOgStrom()
print("")

#B
def oversiktMaaneder():
    with open(tekstfil, encoding="utf-8") as fil:
        fil = csv.reader(fil, delimiter=";")
        
        overskrift = next(fil)
        januar = 0
        februar = 0
        mars = 0
        
        for rad in fil:
            #Vi splitter den første verdien i rad (datoen) får å få en ny liste
            dato = rad[0].split(".")
            
            #Sjekker hvilke måned som passer med hvem
            if dato[1] == "01":
                #Summerer opp beløpene for hver måned
                januar += int(rad[2])
            if dato[1] == "02":
                februar += int(rad[2])
            if dato[1] == "03":
                mars += int(rad[2])
        
        #printer ut oversikten
        print(f"Antall kroner brukt i Januar: {januar}")
        print(f"Antall kroner brukt i februar: {februar}")
        print(f"Antall kroner brukt i mars: {mars}")
        
oversiktMaaneder()


#C
def plottetOversikt():
    with open(tekstfil, encoding="utf-8") as fil:
        fil = csv.reader(fil, delimiter=";")
        
        overskrift = next(fil)
        
        #Angir x-verdiene
        maaneder = ["Januar", "Februar", "Mars"]
        
        #Siden strømregningen bare kommer 1 gang hver måned trenger vi ikke noe ekstra for den
        #Men for mat så må vi summere opp for hver måned
        utgiftMat = []
        matJanuar = 0
        matFebruar = 0
        matMars = 0
        utgiftStrom = []
        
        for rad in fil:
            #Om beløpet er relatert til mat, så splitter vi opp og summerer den for riktig måned
            #Samme system som i oppg B
            if rad[1] == "mat":
                dato = rad[0].split(".")
                
                if dato[1] == "01":
                    matJanuar += int(rad[2])
                if dato[1] == "02":
                    matFebruar += int(rad[2])
                if dato[1] == "03":
                    matMars += int(rad[2])
            #Strøm trenger vi ikke å tenke på, siden regningen kommer bare 1 gang i måneden
            elif rad[1]=="strøm":
                utgiftStrom.append(int(rad[2]))
        
        #Legger til månedsbeløpet for mat i total utgift listen
        utgiftMat.append(matJanuar)
        utgiftMat.append(matFebruar)
        utgiftMat.append(matMars)
        
        #Lager en plot
        fig, ax = plt.subplots(figsize=(10, 5))
        
        #lager en liste med tall
        x = np.arange(3)
        
        #plotter
        ax.bar(x+0.2, utgiftMat, width = 0.4, label="Mat")
        ax.bar(x-0.2, utgiftStrom, width = 0.4, label="Strom")
        ax.set_xticks(x, maaneder)
        ax.legend()
        plt.show()
        
plottetOversikt()
print("")

#D

def leggTilUtgift():
    with open(tekstfil, "a") as fil:
        #Henter input ifra brukeren
        print("Her kan du skrive inn ekstra utgifter, det er viktig at du skriver det i riktig format")
        dato = input("Skriv inn dato(Dag.måned.år (23.02.2023)): ")
        typen = input("Skriv hvilke type utgift det er (mat eller strøm): ")
        beløp = input("Skriv inn beløpet: ")
        kommentar = input("Legg til kommentar: ")
        
        #Legger all verdier, inkludert verdien som vi bruker for å separere andre verdier
        liste = [dato, ";", typen, ";", beløp, ";", kommentar]
        #Summerer alt sammen i en felles tekst
        tekst = ""
        for i in liste:
            tekst += i
        #Legger til en ny linje
        tekst += " \n"
        #"Appender" teksten inn i filen
        fil.write(tekst)
     
        
valg = input("Vil du legge til ekstra utgifter? (y/n): ")

if valg == "y":
    leggTilUtgift()
else:
    print("Den er grei :)")
        