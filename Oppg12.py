# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:23:16 2023

@author: nik1811
"""

class Person:
    def __init__(self, navn):
        #Konstruktøren
        self.navn = navn
        self.ektefelle = ""
        
    def visStatus(self):
        #Sjekker om personen er gift eller singel
        if self.ektefelle:
            print(f"Jeg er gift med {self.ektefelle}")
        else:
            print("Jeg er singel")
            
    def gifteMeg(self, person):
        #sjekker om personen er singel eller gift
        if self.ektefelle:
            print(f"Beklager {person.navn}, jeg er allerede gift med {self.ektefelle}")
        else:
            #Om man ikke er gift så gjør endrer man navnet på ektefellen
            self.ektefelle = person.navn
            person.ektefelle = self.navn
            
#Svar på oppg D:

"""
For å unngå en feil som i koden ovenfor så må vi sjekke om personen i parameteren har en ektefelle
det kan vi gjøre ved å enten utvide If setningen, eller legge til en "or" i den første.
Her er et eksempel man kan gjøre for å utvide if setningen:

def gifteMeg(self, person):
    if self.ektefelle:
        print(f"Beklager {person.navn}, jeg er allerede gift med {self.ektefelle}")
    elif person.ektefelle:
        print(f"Oida, ser ut som om du er gift med {person.ektefelle}")
    else:
        self.ektefelle = person.navn
        person.ektefelle = self.navn
"""
def hovedprogram():
    brad = Person("Brad Pitt")
    brad.visStatus()
    
    angie = Person("Angelina Jolie")
    brad.gifteMeg(angie)
    brad.visStatus()
    
    jo = Person("Jo By")
    brad.gifteMeg(jo)
    jo.gifteMeg(brad)
    jo.visStatus()


hovedprogram()