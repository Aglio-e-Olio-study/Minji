import sys,heapq
input=sys.stdin.readline

n=int(input())
time=[list(map(int,input().split())) for _ in range(n)]
time.sort()

result=[]
heapq.heappush(result,time[0][1])

for i in range(1,n):
    if result[0]<=time[i][0]:
        heapq.heappop(result)
    heapq.heappush(result,time[i][1])
print(len(result))    
