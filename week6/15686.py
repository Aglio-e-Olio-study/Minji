import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
result = 10**6
h = []      
c = []      

#인접행렬
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            h.append([i, j])
        elif graph[i][j] == 2:
            c.append([i, j])
            
## 내장 combinations 사용
for chi in combinations(c, m): 
    temp = 0            
    for house in h: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(house[0] - chi[j][0]) + abs(house[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)