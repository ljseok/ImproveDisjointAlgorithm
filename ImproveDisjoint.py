def find_parent(parent, x): # 특정 원소가 속한 집합을 찾기

    if parent[x] != x: #루트 노드가 아니면
        parent[x] = find_parent(parent, parent[x]) #루트 노드를 찾을 때까지 재귀적으로 호출
    return parent[x]

def union_parent(parent, a, b):  #두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # 노드의 개수와 간선의 개수 입력 받기
parent = [0] * (v + 1) # 부모 테이블 초기화

for i in range(1, v + 1): # 부모 테이블상에서
    parent[i] = i # 부모를 자기 자신으로 초기화

for i in range(e): # Union 연산
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='') # 각 원소가 속한 집합 출력하기
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='') # 부모 테이블 내용 출력하기
for i in range(1, v + 1):
    print(parent[i], end=' ')