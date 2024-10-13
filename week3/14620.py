import sys
input =sys.stdin.readline

## 심을 수 있는지 체크하는 함수
def check(visit,i,j):
    for a,b in move:
        if [a+i,b+j] in visit:
            return False
    return True

# 탐색
def solve(visit,temp):
    global result
    if result<=temp:
        return
    elif len(visit)==15:
        result=min(result,temp)
        return 
    else:
        for i in range(1,n-1):
            for j in range(1,n-1):
                if check(visit,i,j) and (i,j) not in move:
                    ##혹시 해당 탐색이 최적이 아닐 수도 있기 때문에 따로 관
                    t=[]
                    t_c=0
                    for a,b in move:
                        ni=i+a; nj=j+b
                        t.append([ni,nj])
                        t_c+=flower[ni][nj]
                    solve(visit+t,temp+t_c)
    
move=[[0,1],[0,-1],[1,0],[-1,0],[0,0]]
n=int(input())
flower=[list(map(int,input().split())) for _ in range(n)]
MAX=3000
result=MAX

        
solve([],0)
print(result)
