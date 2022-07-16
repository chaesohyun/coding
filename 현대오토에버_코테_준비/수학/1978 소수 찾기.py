import sys

N=int(input())
num=sys.stdin.readline().split()
sosu=0
for i in range(N):
    count=0
    for j in range(1,int(num[i])+1):
        if int(num[i])%j==0:
            count=count+1
    if count==2:
        sosu=sosu+1
print(sosu)