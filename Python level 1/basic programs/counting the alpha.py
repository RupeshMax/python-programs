from collections import Counter as cs,defaultdict as dd,OrderedDict
x=cs(list(input()))
d=dd()
x=(OrderedDict(sorted(x.items(),key=lambda kv:kv[1] ,reverse=True)))
for k,v in x.items():
    if v>1:
        print(k,v)
