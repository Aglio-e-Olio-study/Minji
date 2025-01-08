import sys
input=sys.stdin.readline
from collections import Counter

n,m=map(int,input().split())
dna=list(input().rstrip() for _ in range(n))

def find(dna):
    index=list(zip(*dna))
    result=''
    for i in range(m):
        temp=index[i]
        counter=Counter(temp)

        sorting = sorted(counter.items(),key=lambda x: (-x[1], x[0]))
        result+=sorting[0][0]
    print(result)
    return result
