# 쇠막대기 절단하려고 한다.
# 끝점은 겹치지 않게 놓는다.
# 각 쇠막대기를 자르는 레이저는 적어도 한 개 존재
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수 구하는 프로그램
# 레이저는 () 쌍으로 표현되고, 쇠막대기의 끝은 ( , ) 으로 표현된다.
arr=input()
arr=list(map(str,arr))

stack=[arr[0]]
tmp=0
for i in range(1,len(arr)):
    print(i,stack)
    if arr[i-1]=='(' and arr[i]==')':
        stack.pop()
        tmp=tmp+len(stack)
    elif arr[i-1]==')' and arr[i]==')':
        tmp=tmp+1
        stack.pop()
    else:
        stack.append(arr[i])

print(tmp)
