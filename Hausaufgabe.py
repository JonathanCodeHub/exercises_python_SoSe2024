
i=1
lz=10
AK=10000
SR=1000
end=[]

for t in range (0,lz):
    def sparfunktion(AK,SR,i):
        AKn=AK*i
        sparfunktion += AKn+SR + (AKn+SR)*i
        end.append(sparfunktion)
print(end)