data=input()
days=data.replace(' ','').split("Day")
days.pop(0)
print(days)
d,output={},0
for i in range(len(days)):
    attack=days[i].split(':')
    #print(attack)
    if len(attack)>1:
        for j in range(len(attack)):
            index=attack[j].index('X')
            side=attack[j][index-2]
            height=attack[j][index+2]
            #print(side,height)
            if side not in d:
                output+=1
                d[side]=height
            elif d[side]<height:
                output+=1
                d[side]=height
            
    else:
        #print(days[i])
        index=days[i].index('X')
        side=days[i][index-2]
        height=days[i][index+2]
        #print(side,height)
        if side not in d:
                output+=1
                d[side]=height
        elif d[side]<height:    
            output+=1
            d[side]=height
print(output)
print(d)
