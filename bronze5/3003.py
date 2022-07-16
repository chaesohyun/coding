n=list(map(int, input().split()))
std=[1,1,2,2,2,8]
for i in range(len(std)):
    print(std[i]-n[i],end=' ')