N = int(input())
cowLoc = list(map(int, input().split()))

num = 0
for i in range(N):
    for j in range(i+1, N):
        if cowLoc[i] <= cowLoc[j]:
            for k in range(j+1, N):
                if cowLoc[j] <= cowLoc[k]:
                    num += 1

print(num)