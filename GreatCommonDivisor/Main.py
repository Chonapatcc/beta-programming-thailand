a,b=input().split()
a,b=int(a),int(b)
lis=[]
solve=0
if a>b:
    solve=b
else:
    solve=a

for i in range(1,2000000000):
    if i>solve:
        break
    if a%i==0 and b%i==0:
        lis.append(i)
    

print(lis[-1])