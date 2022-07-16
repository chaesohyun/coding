# N개의 단어로 이루어져 있고, 알파벳 대문자로 이루어져있다.
# 각 알파벳 대문자를 0~9의 수 중 하나로 바꿔서 N개의 수를 합하는 문제
# 같은 알파벳은 같은 수로 바뀌고, 두 개 이상의 알파벳이 같은 숫자로 바뀌면 안됨
# N개의 단어가 주어질 때, 그 수의 합을 최대로 만드는 프로그램
import operator

N=int(input())
arr=[]
for i in range(N):
    arr.append(input())

dic={}
for i in range(N):
    for j in range(len(arr[i])):
        if arr[i][j] in dic:
            dic[arr[i][j]]=dic[arr[i][j]]+10**(len(arr[i])-1-j)
        else:
            dic[arr[i][j]]=10**(len(arr[i])-1-j)

x=sorted(dic.values())

result=0
n=9
for i in range(len(x)-1,-1,-1):
    result=result+x[i]*n
    n=n-1
print(result)