def minimum_no_of_coins(N,l):
    if N==0:
        return ans
    else:
        for i in range(0,l):
            if deno[i]>N:
                l=i
                break
        ans.append(deno[l-1])
        N=N-deno[l-1]
    return minimum_no_of_coins(N,l)
            
                

for i in range(int(input())):
    deno=[1,2,5,10,20,50,100,200,500,2000]
    l=len(deno)
    ans=[]
    N=int(input())
    print(minimum_no_of_coins(N,l))
