from sys import getrecursionlimit, setrecursionlimit

print(getrecursionlimit())
setrecursionlimit(1000000000)
print(getrecursionlimit())
