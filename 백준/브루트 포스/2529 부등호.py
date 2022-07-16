### 부르트포스 - 조합 가능한 모든 것을 하나씩 대입해보는 방법
### 백트래킹 - 답이 될 만한 상황이면 탐색 중단, 모든 경우의 수 중에서 특정한 조건의 경우만 살피는 것

# < 와 >가 k개 나열된 A가 있다.
# 이 부등호의 앞 뒤에 한자리 숫자를 넣어 만족시키려고 한다.
# 이 부등호의 순서를 만족하는 정수 중 최대와 최소를 return

n=int(input())
A=list(map(str, input().split()))
mn=''
mx=''
visited=[0]*10

def check(i,j,k):
    if k=='<':
        return i<j
    if k=='>':
        return i>j

def back(cnt,s):
    global mx, mn

    if cnt==n+1: # n+1의 수만큼 뽀았
        if len(mn)==0:
            mn=s
        else:
            mx=s
        return
    for i in range(10):
        if visited[i]==0:
            if cnt==0 or check(s[-1],str(i),A[cnt-1]):
                visited[i]=1
                back(cnt+1,s+str(i))
                visited[i]=0


back(0,'')
print(mx)
print(mn)