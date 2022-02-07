n=int(input())
lis=[]
for i in range(n):
    word=input()
    if word in lis:
        pass
    else:
        lis.append(word)
lis.sort()
for w in lis:
    print(w)