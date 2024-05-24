# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:27:16 2024

@author: jonat
"""
# =============================================================================
# ==> Strg 4  ==> Strg 5

# import numpy as np
# 
# def main():
#     array = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10])
#     print(array)
# 
# main()
# 
# =============================================================================

# =============================================================================
# import numpy as np
# array_example = np.array([[[0, 1, 2, 3],
#                            [4, 5, 6, 7]],
# 
#                           [[0, 1, 2, 3],
#                            [4, 5, 6, 7]],
# 
#                           [[0 ,1 ,2, 3],
#                            [4, 5, 6, 7]]])
# new_array = np.reshape(array_example,(4,6),order="F")
# 
# print (array_example)
# print (new_array)
# =============================================================================
# =============================================================================
# import numpy as np
# 
# a = np.arange(1,13,1)
# 
# a2= a.reshape(3, 4)
# 
# print (a2)
# 
# ============================================================================
import numpy as np

aba= np.arange (1,13)
B= np.reshape(aba,(4,3))

print (aba[1:3])
print (aba[:-1])
print(aba[::2]) # [startIndex:endIndex:Schritt]


    

    