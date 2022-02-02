import math
A,B,C=list(map(int, input().split(" ")))
#A = ac, B =ad + bc, C = bd
found=False
if C==0 and B>=0 and not found:
    b=0
    for a in range(1,A+1):
        if A%a==0 and not found:
            c=A//a
            for d in range(1,B+1):
                if B%d==0 and not found:
                    if a*d==B:
                        print(a,b,c,d)
                        found = True
                        break
elif C==0 and B<0:
    d=0
    for a in range(1,A+1):
        if A%a==0 and not found:
            c=A//a
            for b in range(1,B+1):
                if B%b==0 and not found:
                    if c*b==B:
                        print(a,b,c,d)
                        found = True
                        break
else:
    for a in range(1,A+1):
        if A%a==0 and not found:
            for b in range(-1*abs(C),abs(C)+1):
                if b!=0 and not found:
                    if C%b==0:
                        c,d=A//a,C//b
                        if a*d+b*c==B:
                            print(a,b,c,d)
                            found=True
                            break
if not found:
    print("No Solution")

    