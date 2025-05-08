import sys
input = sys.stdin.readline
 
# 전위 순회 (루트) (왼쪽 자식) (오른쪽 자식)
def preorder(tree, root):
    stack = []
    stack.append(root)
    result = ''
    while 0 < len(stack):
        data = stack.pop()
        result += data
 
        # 오른쪽 자식 노드 체크
        if tree[data][1] != '.':
            stack.append(tree[data][1])
 
        # 왼쪽 자식 노드 체크
        if tree[data][0] != '.':
            stack.append(tree[data][0])
    print(result) # ABDCEFG
 
 
# 중위 순회 (왼쪽 자식) (루트) (오른쪽 자식)
def inorder(tree, root):
    stack = []
    result = ''
    data = root
    stack.append(root)
    while True:
        # 왼쪽 자식 노드
        while tree[data][0] != '.':
            if data not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
 
        if 0 < len(stack):
            # 'D'
            data = stack.pop()
            result += data
            if tree[data][1] != '.':
                stack.append(tree[data][1])
                data = tree[data][1]
        else:
            break
    print(result) # DBAECFG
 
 
# 후위 순회 (왼쪽 자식) (오른쪽 자식) (루트)
def postorder(tree, root):
    stack = []
    result = ''
    stack.append(root)
    data  =root
 
    while True:
        # 왼쪽 자식 체크
        while tree[data][0] != '.':
            if tree[data][0] not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
 
        # 오른쪽 자식이 존재하는지를 먼저 체크하기 위해 pop() 하지 않고 값만 가져온다.
        last_data = stack[-1]
 
        # 오른쪽 자식이 존재하는지 체크
        if tree[last_data][1] == '.':
            # 오른쪽 자식이 없으면 그냥 출력
            result += stack.pop()
 
            # 다음 데이터를 지정해준다
            if stack:
                data = stack[-1]
            else:
                # stack이 비어 있으면 종료
                break
        else:
            # 오른쪽 자식이 있으면 다음의 규칙대로 해결
            #
            # 오른쪽 자식이 아직 나오지 않은 노드 -> stack에 추가
            if tree[data][1] not in result:
                stack.append(tree[data][1])
                data = tree[data][1]
            else:
                # 오른쪽 자식이 이미 나온 노드 -> 현재의 노드를 출력하고 start_index를 stack에 들어있는 노드로 바꿔준다.
                result += stack.pop()
                if 0 < len(stack):
                    data = stack[-1]
                else:
                    break
    print(result) # DBEGFCA
 
 
def solve(tree, root):
    preorder(tree, root) # ABDCEFG
    inorder(tree, root) # DBAECFG
    postorder(tree, root) # DBEGFCA
 
if __name__ == "__main__":
    n = int(input().strip())
    tree = {}
    root = None
    for i in range(n):
        info = input().strip().split(' ')
        tree[info[0]] = [info[1], info[2]]
 
    solve(tree, 'A')
