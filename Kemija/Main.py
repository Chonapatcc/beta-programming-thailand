word=input()
realword=""
vowel="a,e,i,o,u".split(",")
num=0
for let in word:
    if num==0:
        if let in vowel:
            realword+=let
            num=2
        else:
            realword+=let
    elif num>0:
        num-=1
print(realword)