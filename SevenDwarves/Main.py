
lis=[]
for i in range(9):
    n=int(input())
    lis.append(n)
score=0
for n in lis:
    score+=n

score-=100
def solve(x,y):
    lis=x
    score=y
    for num1 in lis:
        for num2 in lis:
            sc=0
            if lis.count(num1)>0:
                sc=num1+num2
            elif num1!=num2:
                sc=num1+num2
            if sc==score:
                return [num1,num2]



s=solve(lis,score)
end=[]
for numlis in lis:
    if numlis in s:
        pass
    else:
        end.append(numlis)
for dw in end:
    print(dw)
