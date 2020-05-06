d={'{':'}','[':']','(':')'}
x=int(input())
for i in range(x):
    l1=[]
    y=list(input())
    for j in range(len(y)):
        if y[j] in d:
            if d[y[j]] in y[j:]:
                l1.append(y[j])
                l1.append(d[y[j]])
    print(l1)
    if len(l1)==len(y):
        print('True')
    else:
        print('False')
