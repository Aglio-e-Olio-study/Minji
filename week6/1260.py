import sys
input=sys.stdin.readline

def dfs(i):
    print(i,end=' ')
    for nxt in graph[i]:
        if not visit[nxt]:
            visit[nxt]=1
            dfs(nxt)

def bfs(i):
    que=[i]
    while que:
        q=que.pop(0)
        print(q,end=' ')
        for nxt in graph[q]:
            if not visit[nxt]:
                visit[nxt]=1
                que.append(nxt)
        
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

#인접리스트로 구현
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

### 초기화
visit=[0]*(n+1)
visit[v]=1
### dfs 호출
dfs(v)
print()

### 초기화
visit=[0]*(n+1)
visit[v]=1
### bfs 호출
bfs(v)
#print(graph)
