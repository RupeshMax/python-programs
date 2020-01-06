from collections import Counter as cs
x=cs(list(input()))
a=list(sorted(x.items(),key=lambda x:x[1]),reverse=True)
print(a)
