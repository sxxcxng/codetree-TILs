n = int(input())
num = list(map(int, input().split()))


minSum = 0

for i in range(n):
    sum = 0
    for j in range(n):
        sum += num[j] * abs(i-j)
    if minSum == 0:
        minSum = sum
    elif minSum > sum:
        minSum = sum
    else:
        minSum = minSum

print(minSum)