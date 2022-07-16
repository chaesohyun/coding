import heapq
import sys
import heapq
a=[]
while True:
    N=int(input())
    if N==-1:
        break
    if N==0:
        if len(a)==0:
            print(-1)
        else:
            print(-heapq.heappop(a))
    else:
        heapq.heappush(a,-N)