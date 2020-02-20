'''
                                  ================== CHEMIST QUESTION ==================

You have been hired as a software consultant at a chemist. The chemist shop sells various types of compounds and mixture to their customers. They have a research team that put together various formulas for the chemist of sell. The owner of the shop is a bit of stickler for cleanliness and is also afraid of unforeseen reactions when creating the compounds. So,she has created a rule where a new mixing can is to used for creating a new compound (whether the compound is made of the base elements or from another set of pre-made compounds). Your job as a consultant is to determine the minimal number of bowls that are required to make them. Any compound/element that is part of a definition, without its own definition can be assumed to be a base element. base elements don’t need any preparation.


Multiline input. Where first line N specifies the number of compound definitions followed by N definitions. Followed. Followed by integer M specifies the number of compounds to prepare and M compounds to prepare.


Calculate the minimum number of bowls required to prepared the given compounds.


Test case 1


Input
2
H2O = H + O
NaCL= Na + CL
1
NaCL
Output
1
 
Test case 2
Input 
2
H2O = H + O
NaCL= Na + CL
2
NaCL
NaCL
Output
1
Test case 3
Input 
4
H2O = H + O
NaCL = Na + CL
H2SO4 = H2O + S03
S03 = S + O
1
H2SO4


Output
3



'''

c,value2=0,[]
def solvecal_bowl(i):
    global c
    value=d[i]
    c+=1
    #print(d[i])
    for j in range(len(value)):
        if value[j] in d:
            c+=1
            value2=d[value[j]]
            #print(value2)
            for k in range(len(value2)):
                if value2[k] in d:
                    c+=1
    #print (c)
    return c 
 
compounds=int(input())
d={}
for i in range(compounds):
    element=input().replace(' ','').split("=")
    base=element[1].split("+")
    d[element[0]]=base
#print(d)
requested=int(input())
mixing=[]
for j in range(requested):
    chemical=input()
    if chemical not in mixing:
        mixing.append(chemical)

for i in mixing:
    result=solvecal_bowl(i)
    
print("Output: ",result)

'''
================== Testcase 1 ==================
5
H2SO4NaCL = H2SO4 + NaCL
H2SO4 = H2O + SO3
H2O = H + O
SO3 = S + O
NaCL = Na + CL
2
H2SO4NaCL
SO3
Output:  6
>>> 
================== Testcase 2 ==================
2
H2O = H + O
NaCL= Na + CL
1
NaCL
Output:  1
>>> 
================== Testcase 3 ==================
2
H2O = H + O
NaCL= Na + CL
2
NaCL
NaCL
Output:  1
>>> 
================== Testcase 4 ==================
4
H2O = H + O
NaCL = Na + CL
H2SO4 = H2O + S03
S03 = S + O
1
H2SO4
Output:  3
>>> 
================== Testcase 5 ==================
5
H2O = H + O
NaCL = Na + CL
H2SO4NaCL = H2OSO4 + NaCL
H2SO4 = H2O + SO3
H2Na = H2 + Na
2
H2SO4NaCL
H2Na
Output:  3
'''
