import sys

n = int(sys.stdin.readline())
d = 2

while( n != 1):
    if n % d != 0:
        d+=1
    else:
        n = n //d
        print(d)
    