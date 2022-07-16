# 1/27 15:00-17:00

# 자연수 n이 주어질 때, 임의의 수를 n으로 나눌 때, 몫과 나머지가 같은 수를 모두 더하여 return

n=int(input())

def solution(n):
    answer=0
    for i in range(1,n):
        answer=answer+n*i+i
    return answer
print(solution(n))