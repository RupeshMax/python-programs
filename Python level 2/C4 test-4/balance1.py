d={'}':'{',']':'[',')':'('}
for i in range(int(input())):
    y=list(input())
    while len(y)>0:
        if y[0] in d:
            if d[y[0]] in y:
                y.remove(d[y[0]])
                y.remove(y[0])
            else:
                break
        else:
            break
    print(y)
    if len(y)>0:
        print("False")
    else:
        print("True")

                        
    
    
