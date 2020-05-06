def fun2(no):
    ctr=0
    for i in range(1,20):
        toadd=int(no/(5**i))
        if toadd==0:
            return ctr
        else:
            ctr+=toadd
    return ctr
import time
 
def main():
    x=int(input())
    a=time.clock()
    lowerbound=x*4
    upperbound=x*5
    low=fun2(lowerbound)
    upp=fun2(upperbound)
    if low==x:
        return lowerbound
    elif upp==x:
        return upperbound
    while True:
        mid=(lowerbound+upperbound)//2
        low=fun2(lowerbound)
        upp=fun2(upperbound)
        midval=fun2(mid)
        if midval==x:
            return mid
        elif midval>x:
            upperbound=mid
        elif midval<x:
            lowerbound=mid
        if (time.clock()-a>0.00021):
            return 0
t=int(input())
for i in range(t):
    ans=main()
    if ans!=0:
        print(5)
        if ans%10>=5:
            ans=ans-(ans%10-5)
            for j in range(ans,ans+5):
                print(j,end=" ")
            print()
        else:
            ans=ans-ans%10
            for j in range(ans,ans+5):
                print(j,end=" ")
            print()
    else:
        print(0)
