# =============================================================================
# 
# i=1
# lz=10
# AK=10000
# SR=1000
# end=[]
# 
# for t in range (0,lz):
#     def sparfunktion(AK,SR,i):
#         AKn=AK*i
#         sparfunktion += AKn+SR + (AKn+SR)*i
#         end.append(sparfunktion)
# print(end)
# =============================================================================

import matplotlib.pyplot as plt

def spar_funktion (AK, SR, r, lz):
    kapital= AK
    gesammt_kapital = []
    for k in range (1, lz+1):
        kapital = SR + kapital * (1+r)
        gesammt_kapital.append(kapital)
    return gesammt_kapital
   

end_kapital=(spar_funktion(AK = 10000, SR=1000 , r=0.1, lz=30))
             
plt.plot(end_kapital)




    