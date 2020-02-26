for i in range(int(input())):
    y,l2=(list(map(int,input().split()))),[]
    for i in range(1,len(y)):
        l2.append(max(y[i:]))
    print(*(l2+[-1]))
        
    
    
    
    
