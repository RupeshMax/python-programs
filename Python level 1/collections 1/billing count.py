
from collections import OrderedDict as od  
x=int(input())
d=dict()
for i in range(x):
      y=input().split()
      a=" ".join(y[:-1]) 
      #print(a)
      if a not in d.keys():
            d[a]=y[-1]
      else:
            d[a]=int(d[a])+int(y[-1])
            
print(d)
q=od(sorted(d.items()))
print(q)
for k,v in q.items():
      print(k,v)
'''
ouput:
9
potato chips 20
coffee 10
potato chips 23
tea 60
tea 10
coffee 50
fish finger 10
fish finger 15
coffee 5
{'potato chips': 43, 'coffee': 65, 'tea': 70, 'fish finger': 25}
OrderedDict([('coffee', 65), ('fish finger', 25), ('potato chips', 43), ('tea', 70)])
coffee 65
fish finger 25
potato chips 43
tea 70'''
