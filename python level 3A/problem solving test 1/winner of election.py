from collections import Counter as c
l=['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']
l=c(l)
Max=max(l.values())
l1,l2=[],[]
for i,j in l.items():
    if Max==j:
        l1.append(i)
        l2.append(len(i))
print(l1[l2.index(min(l2))])
