a=[[9,8,7],[6,7,5],[4,3,2]]
z="1 2 3 3".split(" ")
z=list(map(int,z))
add=0
for row in range(z[0]-1,z[2]):
    for col in range(z[1]-1,z[3]):
        add=add+a[row][col]
print(add)
