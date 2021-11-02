a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
num1=b-a-1
num2=c-b-1
if num2 >num1:
    print(num2)
else:
    print(num1)