N,K=map(int, input().split())
n=[i for i in range(1,N+1)]
ans=[]
x=0
for j in range(N):
    x=x+(K-1)
    x=x%len(n)
    ans.append(n.pop(x))
print(f"<{', '.join(map(str,ans))}>")