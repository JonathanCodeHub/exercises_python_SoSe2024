# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:29:19 2024

@author: jonat
"""

#Buchstaben Häufigkeiten

#Schreiben Sie eine Funktion buchstaben_häufigkeit(), 
#die eine String annimmt und die Anzahl der einzelnen Buchstaben in der String zurückgibt.
# Mit anderen Worten, die Funktion berechnet die Häufigkeit jedes Buchstabens in der String. 
#Die Funktion berücksichtigt nur Buchstaben und keine Zahlen oder Sonderzeichen.
# Groß- und Kleinbuchstaben werden als der gleiche Buchstabe betrachtet. 
#Die Funktion gibt ein Dictionary mit Buchstaben als Schlüssel (key) die Buchstabenhäufigkeit als Wert (value) zurück. 
#Achtung! Das von der Funktion zurückgegebene Dictionary ist alphabetisch geordnet.

#buchstaben_häufigkeit("123Wie g&eht es Ihnen%$?")

#{'e': 4, 'g': 1, 'h': 2, 'i': 2, 'n': 2, 's': 1, 't': 1, 'w': 1}
#PS. Wenn Sie noch etwas Zeit haben, plotten Sie ein Histogramm mit den Schlüsseln (die Buchstaben
#) auf der horizontalen Achse und den Werten (die Häufigkeit) auf der vertikalen Achse, plt.bar(). 
#Zuerst müssen Sie matplotlib importieren.

import numpy as np

def neue_alphabet_Matrix():
    alphabet= "abcdefghaijklmnopqrstuvwxyz"
    alphabet_matrix = np.array(list(alphabet))
    return alphabet_matrix

def zähle_buchstaben(text):
    alphabet_matrix=neue_alphabet_Matrix()
    Zähler = {char: 0 for char in alphabet_matrix.flatten()}
    for char in text.lower():
        if char in Zähler:
            Zähler[char]+=1
    buchstaben_häufigkeit = {char: count for char, count in Zähler.items() if count > 0}
   
    return buchstaben_häufigkeit

text= "hier könnte ihre Werbung stehen"

buchstaben_häufigkeit = zähle_buchstaben(text)
print(buchstaben_häufigkeit)