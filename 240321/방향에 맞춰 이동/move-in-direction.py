x, y = 0, 0
N = int(input())

dx, dy = 0, 0

for i in range(N):
    loc, dis = input().split()
    dis= int(dis)
    if loc == 'E':
        dx += dis
    elif loc == 'W':
        dx -= dis
    elif loc == 'S':
        dy -= dis
    else:
        dy += dis
        
print(dx, dy)