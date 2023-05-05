# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:53:06 2023

@author: nik1811
"""
import random as rd

class Butikk:
    def __init__(self, utvalg: list):
        self.utvalg = utvalg
    
    def visUtvalg(self):
        j = 0
        for i in self.utvalg:
            print(f"{j}. {i.navn}")
            j += 1
    
    def leggTilUtvalg(self, objekt: object):
        self.utvalg.append(objekt)
    def slettUtvalg(self, objekt: object):
        self.utvalg.remove(objekt)
        
    def visRoseAvType(self):
        print("Velg hvilken rose du vil ha")
        print("")
        print("1, Klatrerose")
        print("2, Stilkrose")
        print("3, Buskrose")
        print("")
        valg = input("Velg hvilken rose (1, 2, 3): ")
        
        for i in self.utvalg:
            if valg == "1":
                if i.navn == "Klatrerose":
                    i.visInfo()
            if valg == "2":
                if i.navn == "Stilkrose":
                    i.visInfo()
            if valg == "3":
                if i.navn == "Buskrose":
                    i.visInfo()

    def visRoseAvFarge(self):
        print("Velg hvilken farge du vil ha")
        print("")
        print("1, Blå")
        print("2, Lilla")
        print("3, Rød")
        print("")
        valg = input("Velg hvilken farge (1, 2, 3): ")
        
        for i in self.utvalg:
            if valg == "1":
                if i.farge == "Blå":
                    i.visInfo()
            if valg == "2":
                if i.farge == "Lilla":
                    i.visInfo()
            if valg == "3":
                if i.farge == "Rød":
                    i.visInfo()
        
class Rose:
    def __init__(self, navn, høyde, farge, pris):
        self.butikk = ""
        self.navn = navn
        self.høyde = høyde
        self.farge = farge
        self.pris = pris
    
    def visInfo(self):
        print(f"Navn: {self.navn}, høyde: {self.høyde}, farge: {self.farge}, pris: {self.pris}")
        

class Klatrerose(Rose):
    def __init__(self, navn, høyde, farge, pris, lengdeRankene, støttekrav, voksemønster):
        super(). __init__(navn, høyde, farge, pris)
        self.lengdeRankene = lengdeRankene
        self.støttekrav = støttekrav
        self.voksemønster = voksemønster
    
    def planteGuide(self):
        print("blablabla")  

class Stilkrose(Rose):
    def __init__(self, navn, høyde, farge, pris, stilkLengde, antallBlomster, duft):
        super().__init__(navn, høyde, farge, pris)
        self.stilkLengde = stilkLengde
        self.antallBlomster = antallBlomster
        self.duft = duft
    
    def bukettGuide(self):
        print("blablablalala")
        

class Buskerose(Rose):
    def __init__(self, navn, høyde, farge, pris, voksehøyde, breddeKrone, blomstringstidspunkt):
        super().__init__(navn, høyde,farge,pris)
        self.voksehøyde = voksehøyde
        self.breddeKrone = breddeKrone
        self.blomstringstidspunkt = blomstringstidspunkt
        
    def planteGuide(self):
        print("WOWOWOW")

class handlevogn:
    def __init__(self, butikk: object):
        self.butikk = butikk
        self.antallVarer = []
    def visInfo(self):
        j = 0
        for i in self.antallVarer:
            print(f"{j}. {i.navn}")
            j += 1
    def leggTilVare(self, index):
        vare = self.butikk.utvalg[index]
        self.antallVarer.append(vare)
        print("Vare lagt til")
    def fjernVare(self):
        self.visInfo()
        valg = input("Skriv inn hvilke vare du vil slette: ")
        self.antallVarer.pop(int(valg))
        
    def beregnPris(self):
        total = 0
        for i in self.antallVarer:
            total += i.pris
        return total
    
liste_med_roser = []
for i in range(10):
    random = rd.randint(1, 3)
    if random == 1:
        blomst = Klatrerose("Klatrerose", "35cm", "Blå", 76, "75cm", "Plank", "Sprial")
        liste_med_roser.append(blomst)
    if random == 2:
        blomst = Stilkrose("Stilkrose", "130cm", "Lilla", 330, "100cm", "30", "Lavender")
        liste_med_roser.append(blomst)
    if random == 3:
        blomst = Buskerose("Buskerose", "45cm", "Rød", 34, "105cm", "40cm", "kl 2 på natta")
        liste_med_roser.append(blomst)


kunde = True
ansatt = False
butikk = Butikk(liste_med_roser)

if kunde == True:
    valg1 = input("Hei, velkommen til Rosehagen.no, se utvalg? (y/n): ")
    
if valg1 == "y":
    butikk.visUtvalg()
    
if kunde == True:
    valg2 = input("Har du lyst til å se på roser etter farge? (y/n)")
if valg2 == "y":
    butikk.visRoseAvFarge()

if kunde == True:
    valg2 = input("Har du lyst til å se på roser etter type? (y/n)")
if valg2 == "y":
    butikk.visRoseAvType()
handletur = False
valg = input("Starte handletur eller stoppe her? (y/n): ")

if valg == "y":
    handletur = True

if handletur == True:
    vogn = handlevogn(butikk)
    butikk.visUtvalg()
    
    valg = input("Vil du legge varer i handlevognen din? (y/n): ")
    if valg == "y":
        gyldig = False
        while not(gyldig):
            valg = input("Skriv inn tallet til varen du vil legge inn: ")
            vogn.leggTilVare(int(valg))
            valg = input("Stoppe her? (y/n): ")
            if valg == "y":
                gyldig = True
                
    vogn.visInfo()
    valg = input("Vil du slette noen varer ifra handlevognen din? (y/n): ")
    if valg == "y":
        fortsett = False
        while not(fortsett):
            vogn.fjernVare()
            valg = input("Stoppe her? (y/n): ")
            if valg == "y":
                fortsett = True
            else:
                continue
            
    print("Her er en oversikt over varene dine:")
    vogn.visInfo()
    print(f"Totale Prisen: {vogn.beregnPris()}")
   
    
    
    
