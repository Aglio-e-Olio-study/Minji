import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
cnt=0
def solve(i,com,virous):
    global cnt
    for next in com[i]:
        if next not in virous:
            cnt+=1
            virous.append(next)
            solve(next,com,virous)
    return
# dfs -> 1과 연결된 노드 수
com=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    com[x].append(y)
    com[y].append(x)

solve(1,com,[1])
print(cnt)