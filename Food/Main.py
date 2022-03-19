from itertools import permutations
all=int(input())
dislike=int(input())
#dislike
dislikelis=input().split(" ")
lis=[]
for i in range(1,all+1):
    lis.append(i)
perm = permutations(lis)
for aperm in perm:
    text=""
    for rm in aperm:
        text+=str(rm)+" "     
    text=text.rstrip(" ")
    if str(aperm[0]) in dislikelis:
            pass
    else:
        print(text)


 