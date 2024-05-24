# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:34:56 2024

@author: jonat
"""
# =============================================================================
# 
# 1) Erstellen Sie ein 2D-Array genannt D mit zehn Zeilen, wobei jede Zeile von 1 bis 10 geht. 
#Verwenden Sie dazu die Funktion np.arange() and np.tile(). 
#Berechnen Sie die Summe über die Zeilen und den Mittelwert über die Spalten.
# 
# Datei H:\exercises_python\exercise10.py. Nutzen Sie spyder.
# 
# 2) Berechnen Sie die Summe entlang der zweiten und der dritten Achse des folgenden 3D-Array.
# 
# E = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[9,8,7], [6,5,4], [3,2,1]], [[9,8,7], [3,2,1], [6,5,4]]])
# Datei H:\exercises_python\exercise11.py. Nutzen Sie spyder.
# =============================================================================

import numpy as np

M_liste=[]
for i in range (10):
    Matrix= np.arange(1,11 )
    M_liste.append(Matrix)
    
M=np.vstack(M_liste)

print(M)

print (M.sum(axis= 0))
print (M.mean(axis=0))