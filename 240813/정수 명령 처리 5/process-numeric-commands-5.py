def f(X):
    listA = []
    
    for i in range(X):
        command = input().split()
        a = command[0]

        if a == "push_back":
            listA.append(int(command[1]))
        elif a == "pop_back":
            listA.pop()
        elif a == "size":
            print(len(listA))
        elif a == "get":
            k = int(command[1]) - 1
            print(listA[k])

N = int(input())
f(N)