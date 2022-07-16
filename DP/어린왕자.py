case=int(input())
for i in range(case):
    count=0
    x1, y1, x2, y2=map(int, input().split())
    n=int(input())
    for j in range(n):
        x,y,r=map(int, input().split())
        if (x-x1)*(x-x1)+(y-y1)