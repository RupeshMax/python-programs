import re
for i in range(int(input())):
    print(*re.findall('\d+',input()))
