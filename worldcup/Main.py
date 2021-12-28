names=[]
namesdic={}
scoreskick={}
scoreswaskick={}
for i in range(4):
    name=input()
    names.append(name)
    namesdic[name]=0
    scoreskick[name]=0
    scoreswaskick[name]=0  
scores=[]
for y in range(4):
    score=input().split(" ")
    score=[int(anum) for anum in score]
    scores.append(score)

for i in range(4):
    for y in range(4):
        if i==y:
            continue
        scoreskick[names[i]]+=scores[i][y]
        scoreswaskick[names[y]]+=scores[i][y]
        teamA=scores[i][y]
        teamB=scores[y][i]
        if teamA>teamB:
            namesdic[names[i]]+=3
        elif teamA==teamB:
            namesdic[names[i]]+=1
        else:
            pass


sorted_dict = {}
sorted_keys = sorted(namesdic, key=namesdic.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = namesdic[w]

for key,value in reversed(list(sorted_dict.items())):
    print(key,value)