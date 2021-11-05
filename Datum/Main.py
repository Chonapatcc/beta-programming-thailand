day,month=input().split()
day,month=int(day),int(month)
n=0
lisd=["Wednesday", "Thursday", "Friday", "Saturday","Sunday","Monday","Tuesday",]
lism=[0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(month):
    n+=lism[i]
n+=day
n%=7
print(lisd[n])