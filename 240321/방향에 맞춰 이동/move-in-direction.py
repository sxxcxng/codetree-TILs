x, y = 0, 0
N = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    loc, dis = input().split()
    dis= int(dis)
    if loc == 'E':
        a = 0
    elif loc == 'W':
        a = 1
    elif loc == 'S':
        a = 2
    else:
        a = 3

    x += dx[a] * dis
    y += dy[a] * dis
        
print(x, y)