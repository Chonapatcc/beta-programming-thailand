Adrian="ABC"
Bruno="BABC"
Goran="CCAABB"
n=input()
word=input()


A=0
B=0
G=0
def Ad(x):
    i=x
    num=i%3
    if word[i]==Adrian[num]:
        return 1
    else:
        return 0
def Br(x):
    i=x
    num=i%4
    if word[i]==Bruno[num]:
        return 1
    else:
        return 0
def Go(x):
    i=x
    num=i%6
    if word[i]==Goran[num]:
        return 1
    else:
        return 0
for i in range(len(word)):
    ad=Ad(i)
    br=Br(i)
    go=Go(i)
    if ad==1:
        A+=1
    if br==1:
        B+=1
    if go==1:
        G+=1

if A>B and A>G:
    print(A)
    print("Adrian")
elif B>A and B>G:
    print(B)
    print("Bruno")
elif G>A and G>B:
    print(G)
    print("Goran")
elif A==B and A==G:
    print(A)
    print("Adrian\nBruno\nGoran")
elif A>G and A==B:
    print(A)
    print("Adrian\nBruno")
elif A>B and A==G:
    print(A)
    print("Adrian\nGoran")
else:
    print(B)
    print("Bruno\nGoran")