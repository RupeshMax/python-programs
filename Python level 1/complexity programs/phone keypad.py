l1=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
for i in range(int(input())):
    for j in input():
        for k in range(len(l1)):
            if j in l1[k]:
                print(k+2,end="")

        
            
        
