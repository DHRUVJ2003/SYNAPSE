modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']
indices=[]
characters=[]
temp=[]
phew_finally={}
for i, y in enumerate(modern_family):
    indices.append(i)
    characters.append(y.lower().replace("_","-"))
x=lambda a:len(a)
temp=list(map(x,characters))
indices=list(zip(indices,temp))
for j in range(len(indices)):
    indices[j]=sum(indices[j])
indices.sort(reverse=True)
for k in range (len(characters)):
    phew_finally.update({indices[k]:characters[k]})
print (dict(phew_finally))