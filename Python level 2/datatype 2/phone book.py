d={}
x=int(input())
for i in range(x):
    a=input().split(" ")
    d[a[0]]=a[1]
while True:
    try:
        y=input()
        if y in d:
            print("{}={}".format(y,d[y]))
        else:
            print("Not found")
    except EOFError as err:
        time.sleep(1)
        break
     
    
