a, b = map(int, input().split())

for i in range(a):
    for j in range(b):
        print((j + 1) * (i + 1), end=" ")
    print()