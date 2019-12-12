d={'ram':{'eng':40,'sci':60},'arun':{'eng':70,'sci':50},'joy':{'eng':10,'sci':40}}
l1,l3=[],[]
print(d)
for i,j in d.items():
    #print("name:",i)
    for key in j:
        if key=='eng':
            l1.append(j[key])
    for key in j:
        if key=='sci':
            l3.append(j[key])
#print(l1)
for i in range(len(l1)):
    for j in range(i,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
            l3[i],l3[j]=l3[j],l3[i]
#print(l1)
l2=[]
for i in range(len(l1)):
    for k,v in d.items():
        if l1[i]==v['eng']:
            l2.append(k)
            #print(l1[i],':',v['eng'])

#print(l2)
d1={}
for i in range(len(l2)):
    for k,v in d.items():
        if l2[i]==k:
            d1[k]={}
            d1[k]['eng']=l1[i]
            d1[k]['sci']=l3[i]
print(d1)

