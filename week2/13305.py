import sys
input=sys.stdin.readline

n=int(input())
load=list(map(int,input().split()))
money=list(map(int,input().split()))
m=money[0]
result=0
for i in range(n-1):
    m=min(m,money[i])
    result+=load[i]*m

print(result)
    
