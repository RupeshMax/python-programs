from collections import Counter as c,OrderedDict as od
for i in range(int(input())):
    d=od(sorted(c(input().split(" ")).items(),key=lambda x:x[0]))
    for k,v in sorted(d.items(),key=lambda x:x[1],reverse=True):
        print((k+" ")*v,end='')
    print()
    
    
