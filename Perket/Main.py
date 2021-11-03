n=int(input())
Sbar=1
Bbar=0
dif=[]
for i in range(n):
    s,b=input().split()
    s,b=int(s),int(b)
    Sbar*=s
    Bbar+=b
    d=abs(Sbar-Bbar)
    dif.append(d)

dif.sort()
print(0)