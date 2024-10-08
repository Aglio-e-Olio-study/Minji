import sys
input=sys.stdin.readline

n=int(input())
time=[]
for _ in range(n):
    time.append(map(int.input().split()))
print(time)