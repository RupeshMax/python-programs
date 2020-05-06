import re
for i in range(int(input())):
    x=input()
    a=re.findall("[0-9][0-9]",x)
    if a:
        print(min(a))
    else:
        a=re.findall("[0-9]",x)
        print(min(a))
