from collections import Counter,OrderedDict as dd
l1=[9,4,5,4,4,5,9,5,4]
a=Counter(l1)
a=dd(sorted(a.items(),key=lambda kv:kv[1]))
print(a)
b=list(a.keys())
print(b[-1])
