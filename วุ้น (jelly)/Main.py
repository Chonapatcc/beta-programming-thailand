a,b,c=map(int,input().split())

def check(x):
    if x%2==0 and x!=1:
        x/=2
    else:
        x-=1
        x/=2
    return int(x)
n=0
while a!=1:
    a=check(a)
    n+=1
while b!=1:
    b=check(b)
    n+=1
while c!=1:
    c=check(c)
    n+=1
print(n)    
    
    

