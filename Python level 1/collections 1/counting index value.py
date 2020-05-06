from collections import Counter as cs
from collections import defaultdict as dc
x=input().split(" ")
x=list(map(int,x))
for i in range(len(x)):
      l1=[]
      d=dc()
      for j in range(x[i]):
            y=input()
            d[j+1]=y
            l1.append(y)
      print(l1)
      print(d)
      print(cs(l1))
      a=cs(l1)
      for k,v in a.items():
            if v!=1:
                  for i in d.keys():
                        if d[i]==k:
                              print(i,end="")
            print()
'''5 2
a
b
a
a
b
['a', 'b', 'a', 'a', 'b']
defaultdict(None, {1: 'a', 2: 'b', 3: 'a', 4: 'a', 5: 'b'})
Counter({'a': 3, 'b': 2})
134
25
a
b
['a', 'b']
defaultdict(None, {1: 'a', 2: 'b'})
Counter({'a': 1, 'b': 1})
'''
