num=int(input("No of entries"))
entry=[]
total_entry=[]
inside=0
insidelist=[]
insidetime=[]
outsidetime=[]
#total_entry=[[1,3,'enter'],[2,2,'exit'],[3,6,'enter'],[4,1,'exit'],[5,2,'enter'],[6,8,'exit']]
total_entry=[[830,2,'enter'],[900,3,'enter'],[930,4,'enter'],[1000,0,'exit'],[1030,2,'exit'],[1100,7,'exit']]
'''for i in range(num):
    time=int(input("Enter timestamp"))
    ppl=int(input("Enter people"))
    path=input("Enter enter/exit")
    entry.extend([time,ppl,path])
    print(entry)
    total_entry.append(entry)
    entry=[]
    print("")'''
list1=[]
list2=[]
add=0
print(total_entry)
for i in range(num):
    if(total_entry[i][2]=="enter"):
        inside+=total_entry[i][1]
        timestamp=total_entry[i][0]
        insidetime.append(timestamp)
        list1.append(inside)
        add=inside
    else:
        insidelist.append(inside)
        timestamp=total_entry[i][0]
        outsidetime.append(timestamp)
        inside-=total_entry[i][1]
        if(add!=inside):
            list2.append(timestamp)
            #print(list2)
maximum=max(insidelist)
mx=insidelist.index(maximum)
max=list1.index(maximum)
print(insidelist[mx])
print(insidetime[max])
print(list2[mx])
