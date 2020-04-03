import re
x=input()
a=re.findall("[@,!,#,:,.,:,/,R]\w*",x)
print(a)
