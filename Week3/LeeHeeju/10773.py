import sys

n = int(sys.stdin.readline())
numbers=[]
for _ in range(n):
    m = int(sys.stdin.readline())
    if (m != 0 ):
        numbers.append(m)
    elif (m == 0):
        numbers.pop()

print(sum(numbers))
