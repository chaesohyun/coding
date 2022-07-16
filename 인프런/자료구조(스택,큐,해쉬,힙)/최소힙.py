# 완전이진트리로 구현된 자료구조인 최소힙
# 부모 노드값이 왼쪽 자식, 오른쪽 자식의 값보다 작게 트리를 구성하는 것
# 자연수 입력되면 최소힙에 입력, 0입력되면 최소힙에서 최솟값 출력, -1 입력되면 프로그램 종료

# ## 최소힙 - 부모가 자식보다 작아야하는 자료구조 ## #
import sys
import heapq # 생성되는 list가 heapq에서 제공하는 heap의 자료구조처럼 조작이 된다.
a=[]
while True:
    N=int(input())
    if N==-1:
        break
    if N==0:
        if len(a)==0:
            print(-1)
        else:
            print(heapq.heappop(a))
    else:
        heapq.heappush(a,N)