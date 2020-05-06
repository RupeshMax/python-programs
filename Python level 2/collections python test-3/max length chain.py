for i in range(int(input())):
    l1=sorted([[int(input()),int(input())] for j in range(int(input()))],key=lambda x:x[1])
    print(l1)
    b=l1[0][1]
    count=1
    for k in range(1,len(l1)):
        if b<l1[k][0]:
            count+=1
            b=l1[k][1]
    print(count)
            
            
                   
'''
2
5
5
24
39
60
15
28
27
40
50
90
[['5', '24'], ['39', '60'], ['15', '28'], ['27', '40'], ['50', '90']]
3
2
5
10
1
11
[['5', '10'], ['1', '11']]
1
'''
