m,n=input().split()
m=int(m)
n=int(n)
lis1=[]
lis2=[]
for i in range(m):
    inp=input().split()
    lis=[]
    for y in range(n):
        lis.append(int(inp[y]))
    lis1.append(lis)
for i in range(m):
    inp=input().split()
    lis=[]
    for y in range(n):
        lis.append(int(inp[y]))
    lis2.append(lis)
lis=[]
for i in range(m):
    end=""
    for y in range(n):
        add=lis1[i][y]+lis2[i][y]
        end+=str(add)+" "
    end=end.rstrip(" ")
    lis.append(end)
for l in lis:
    print(l)
        
