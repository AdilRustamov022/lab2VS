#1414	B(n) ədədi massivinin(siyahının) 9-dan böyük elementlərinin 
#hasilini hesablayan alqoritm tərtib etməli.
import random
B=[]
hasil=1
for i in range(0,10):
    n = random.randint(0,200)
    B.append(n)


for x in B:
    if int(x)>9:hasil*=int(x)
    
print(hasil)