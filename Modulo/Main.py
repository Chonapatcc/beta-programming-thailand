x=42
lis=[]
num=0
for i in range(10):
    n=int(input())
    so=n%x
    if so in lis:
        pass
    else:
        num+=1
        lis.append(so)
print(num)

