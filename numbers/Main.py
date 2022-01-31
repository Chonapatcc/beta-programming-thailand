n=int(input())
lis=input().split(" ")
lis1=[]
lis2=[]
for i in lis:
    if i=="0":
        lis1.append(int(i))
    else:
        lis2.append(int(i))

num=""
num0=""
lis1.sort()
for y1 in lis1:
    num0+=str(y1)
    
lis2.sort()
for y2 in lis2:
    num+=str(y2)
num=num[0]+num0+num[1:]
print(int(num))