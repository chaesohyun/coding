# 이진트리를 전위순회, 중위순회, 후위순회 출력

## 깊이우선탐색 - 루투에서 시작해서 다음 레벨로 넘어가기 전에 완벽하게 탐색하는 방법

# 전위 순회
def pre_DFS(x):
    if x>7:
        return
    else:
        # print(x, end='') # 선위순회
        pre_DFS(2*x)
        # print(x, end='') # 중위순회
        pre_DFS(2*x+1)
        # print(x, end='') # 후위순회




pre_DFS(1)