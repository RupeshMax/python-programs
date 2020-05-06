import sys
 
def numFab(arr, n):
    rights = [-1] * n
    lefts = [-1] * n
    
    st = [n - 1]
    for i in range(n - 2, -1, -1):
        while st and arr[st[-1]] < arr[i]:
            st.pop()
        
        if st:
            rights[i] = st[-1]
        
        st.append(i)
    
    st =[0]
    
    for i in range(1, n, 1):
        while st and arr[st[-1]] < arr[i]:
            st.pop()
        
        if st:
            lefts[i] = st[-1]
        
        st.append(i)
 
    res = [0] * n
 
    for i in range(n):
        if rights[i] != -1:
            res[rights[i] - i] = max([res[rights[i] - i], i - lefts[i]])
    
    return sum(res)
 
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
 
sif n <= 1:
    print(0)
    
else:
    count = numFab(arr, n)
    print(count)
