'''days=3
N_cluster=4
clusters=[['c1',100,300],['c2',100,300],['c3',100,200],['c4',100,400]]
fedral=[['F','c1'],['f','c2'],['c2','c3'],['c3','c4']]
'''
days=int(input())
N_cluster=int(input())
clusters=[input().split(" ") for i in range(N_cluster)]
N_fedral=int(input())
fedral=[input().split("_") for i in range(N_fedral)]


pipe=[]
#seperation of fed
for i in range(len(fedral)-1):
    for j in range(i+1,len(fedral)):
        if(fedral[i][-1]==fedral[j][0]):
            fedral[i].append(fedral[j][1])
for i in range(len(fedral)):
    if(fedral[i][0]=='f' or fedral[i][0]=='F'):
        pipe.append(fedral[i])
'''-------------------'''
limit=[]
for i in range(len(clusters)):
    limit.append(int(clusters[i][1]))

indicator=[]
for i in range(len(clusters)):
    indicator.append(int(clusters[i][2]))
'''-------------------'''

total=sum(indicator)
print('filled    {}'.format(indicator))
for q in range(1,days+1):
    l=[]

    for i in range(len(indicator)):
        if indicator[i]<limit[i]:
            l.append(i)
    
    if len(l)==0:
        for i in range(len(indicator)):
            indicator[i]-=int(clusters[i][1])
    else:
        lpipe=[]
        for i in range(len(pipe)):
            lpipe.append(0)
        
        for k in l:
            for i in range(len(pipe)):
                if clusters[k][0] in pipe[i]:
                    b=pipe[i].index(clusters[k][0])
                    lpipe[i]=b
        for o in range(len(lpipe)):
            for i in range(1,lpipe[o]+1):
                for j in range(len(clusters)):
                    if pipe[o][i] in clusters[j]:
                        indicator[j]=int(clusters[j][2])
                        total+=int(clusters[j][2])      
        print('filled    {}'.format(indicator))
        for i in range(len(indicator)):
            indicator[i]-=int(clusters[i][1])       

    print('day after {}'.format(indicator))     
print(total)


'''
================ Testcase 1 ===============
3
4
c1 200 400
c2 200 300
c3 100 100
c4 150 300
4
f_c1
f_c3
c1_c2
c3_c4

filled    [400, 300, 100, 300]
day after [200, 100, 0, 150]
filled    [400, 300, 100, 150]
day after [200, 100, 0, 0]
filled    [400, 300, 100, 300]
day after [200, 100, 0, 150]
3000
>>> 
================ Testcase 2 ===============
2
3
c1 100 300
c2 150 300
c3 100 100
3
f_c1
f_c2
c2_c3

filled    [300, 300, 100]
day after [200, 150, 0]
filled    [200, 300, 100]
day after [100, 150, 0]
1100
>>> 
================ Testcase 3 ===============
3
4
c1 100 300
c2 100 300
c3 100 200
c4 100 400
4
f_c1
f_c2
c2_c3
c3_c4

filled    [300, 300, 200, 400]
day after [200, 200, 100, 300]
day after [100, 100, 0, 200]
filled    [100, 300, 200, 200]
day after [0, 200, 100, 100]
1700
>>>
'''
