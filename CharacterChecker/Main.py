word=input()
up=0
low=0
for i in word:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1

if up>0 and low>0:
    print("Mix")
elif up>0 and low==0:
    print("All Capital Letter")
elif low>0 and up==0:
    print("All Small Letter")
