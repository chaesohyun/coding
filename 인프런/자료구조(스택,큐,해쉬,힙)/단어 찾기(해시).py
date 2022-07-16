#N개의 단어를 적었는데 시에 쓰지 않은 단어가 하나 있다. 찾기

# N개의 단어가 입력되고, 시에 입력된 N-1개의 단어가 입력된다.
# 해시 사용(딕셔너리)
N=int(input())
p=dict()
for i in range(N):
    x=input()
    p[x]=1

for i in range(N-1):
    x=input()
    p[x]=0
print(p.values())
for key,val in p.items():
    if val==1:
        print(key)

# N=int(input())
# tmp=[]
# for i in range(N):
#     x=input()
#     tmp.append(x)
#
# tmp2=[]
# for i in range(N-1):
#     x=input()
#     tmp2.append(x)
#
# for i in tmp:
#     if i not in tmp2:
#         print(i)
#         break