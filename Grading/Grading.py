a=int(input())
b=int(input())
c=int(input())
score=a+b+c
if score<=100 and score>=80:
    print("A")
elif score<80 and score >=75:
    print("B+")
elif score<75 and score>=70:
    print("B")
elif score<70 and score >=65:
    print("C+")
elif score<65 and score>=60:
    print("C")
elif score<60 and score>=55:
    print("D+")
elif score<55 and score>=50:
    print("D")

else:
    print("F")