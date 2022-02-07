from math import factorial
N = int(input())
if N%2 == 1:
    N = N+1
print(factorial(N)//(factorial(N//2)*factorial(N//2)))