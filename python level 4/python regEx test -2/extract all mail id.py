import re
s=input()
match=re.findall(r'[\w\.-]+@[\w\.-]+',s)
if len(match)==0:
    print("mail id in not present")
else:
    for i in match:
        print(i)

'''
= testcase -1 =
ram is my name and ram@gmail.com and ram@yahoo.com
ram@gmail.com
ram@yahoo.com
>>>
