import operator
ops = { "+": operator.add, "-": operator.sub,"*": operator.mul, '//' : operator.floordiv} # etc.

#print (ops["+"](1,1))
#x='10 + 2 * 6 '
x='100 * ( 2 + 12 )'
x=x.split()
pro={'*':2,'/':2,'-':1,'+':1,'^':3}
d={')':'('}
string=[]
stack=[]
pro1=[]
a=''
for i in x:
    if i in d or i in d[')']:
        stack.append(i) 
    elif i in pro:
        stack.append(i)
        pro1.append(pro[i])
    else:
        string.append(i)
        
    

print(stack)
print(pro1)
print(string)
