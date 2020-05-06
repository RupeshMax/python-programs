x="...222431666"
x="46112W1O166O.21143O"
balls=0
total=0
strike=['P1','P2']
players={'P1':0,'P2':0}
extra=0
for i in x:
    if i == '.':
        balls+=1
        
    elif i=='1':
        players[strike[0]]+=1
        total+=1
        balls+=1
        strike[0],strike[1]=strike[1],strike[0]
        
    elif i=='2':
        total+=2
        players[strike[0]]+=2
        balls+=1

    elif i=='3':
        total+=3
        players[strike[0]]+=3
        balls+=1
        strike[0],strike[1]=strike[1],strike[0]
        
    elif i=='4':
        total+=4
        players[strike[0]]+=4
        balls+=1
        
    elif i=='6':
        total+=6
        players[strike[0]]+=6
        balls+=1
        
    elif i=='W':
        total+=1
        extra+=1
        

    elif i=='O':
        strike.pop(0)
        strike.insert(0,'P'+str(len(players)+1))
        players['P'+str(len(players)+1)]=0
        balls+=1

    if balls%6==0:
        strike[0],strike[1]=strike[1],strike[0]

for i,j in players.items():
    print("{}-{}(runs)".format(i,j))

print("Strike-{}".format(strike[0]))

print("Non-Strike-{}".format(strike[1]))

print("Total-{}".format(total))

overs=balls//6

print("Overs-{}.{}".format(overs,balls-(6*overs)))

print("Extra-{}".format(extra))

print("Wicket(s)-{}".format(len(players)-2))

print("Remaining Wicket(s)-{}".format(10-(len(players)-2)))





        
        
