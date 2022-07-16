# 문자와 숫자가 섞인 문자열이 주어질 때, 숫자만 추출해서 순서대로 자연수를 만든다.
# 만들어진 자연수와 그 자연수의 약수 갯수를 출력

# 숫자 판별 함수
# isdeximal(): 0~9 사이 숫자 판별, isdigit()
a=list(input())
res=0
for i in a:
    if i.isdecimal():
        res=res*10+int(i)
print(res)
count=0
for j in range(1,res+1):
    if res%j==0:
        count=count+1
print(count)
