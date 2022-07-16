# N개의 문자열 데이터를 입력받아 앞, 뒤에서 읽을 때 같을 경우 YES 출력
# 아니면 NO출력

# N=int(input())
#
# for i in range(N):
#     count = 0
#     ch=list(map(str,input()))
#     for j in range(len(ch)//2):
#         if ch[j]==ch[-1-j] or ch[j]==ch[-1-j].upper() or ch[j]==ch[-1-j].lower():
#             count=count+1
#     if len(ch)//2==count:
#         print("#",i+1, "YES")
#     else:
#         print("#",i+1,"NO")

# 선생님 풀이
N=int(input())
for i in range(N):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#",i+1,"YES")
    else:
        print("#",i+1,"NO")