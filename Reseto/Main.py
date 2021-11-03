N, K = map(int, input().split())
num = list(range(2, N + 1))
temp = []
count = 0
for i in num:
    if i not in temp:
        temp.append(i)
        j = 1
        while (j * i <= N):
            if (j * i not in temp):
                temp.append(j * i)
            j += 1
print(temp[K-1])