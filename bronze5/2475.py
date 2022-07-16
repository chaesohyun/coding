n=list(map(int, input().split()))
count=0
for i in n:
    count=count+(i*i)
print(count%10)