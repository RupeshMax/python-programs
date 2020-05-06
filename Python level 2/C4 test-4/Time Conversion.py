x=int(input())
for i in range(x):
    y=input().split(":")
    if 'P' in y[-1]:
        print("{}:{}:{}".format(int(y[0])+12,y[1],y[2][:2]))
    else:
        print("{}:{}:{}".format((y[0]),y[1],y[2][:2]))
'''   
1
01:00:00PM

=>13:00:00

1
10:20:23PM

=>22:20:23

1
12:00:00AM

=>12:00:00
'''
