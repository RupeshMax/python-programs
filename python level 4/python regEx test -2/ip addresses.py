import re
for i in range(int(input())):
    a=input()
    txt=re.findall('[.]|[:]',a)
    if txt:
        if txt[0]=='.':
            x=re,split('[.]',a)
            for i in x:
                if int(i)>=0 and int(i)<256:
                    count=1
                else:
                    count=0
                    print('Neither')
                    break
            if count==1:
                print('Ipv4')
        elif txt[0]==':':
            x=re,split('[:]',a)
            for i in x:
                if len(i)==4:
                    count=1
                else:
                    count=0
                    print('Neither')
                    break
            if count==1:
                print('Ipv6')
        else:
            print('Neither')
    else:
        print('Neither')
        
