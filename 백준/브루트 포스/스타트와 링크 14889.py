from itertools import combinations as com

N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))

ele=[]
for i in range(1,N+1):
    ele.append(i)


result=[]
for x in com(ele,int(N/2)):
    start_re,link_re=0,0
    start=x
    link=list(set(ele)-set(start))
    for a in com(start,2):
        start_re+=arr[a[0]-1][a[1]-1]
        start_re+=arr[a[1]-1][a[0]-1]
    for a in com(link,2):
        link_re+=arr[a[0]-1][a[1]-1]
        link_re+=arr[a[1]-1][a[0]-1]
    result.append(abs(start_re-link_re))
print(min(result))