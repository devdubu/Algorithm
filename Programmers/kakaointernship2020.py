'''
왼쪽열 1,4,7 -> 왼쪽 엄지로 누름
가운데 2, 5, 8, 0은 현재 엄지 위치 중 가까운 엄지
오른열 3, 6, 9 -> 오른쪽 엄지로 누름

만약 엄지까지의 거리가 같다면, 오른손 잡이는 오른쪽 엄지, 왼손잡이는 왼쪽 엄지로 누른다

왼손 위치, 오른손 위치
현재 위치..거리비교는 BFS를 이용해야할듯 한데


1 2 3
4 5 6
7 8 9
  0
[ [], [2,4], [1, 3, 5], [2, 6], [1, 5], [2, 4, 6], [3, 5], [4, 8], [5, 7, 9], [6, 8],[8]]


'''
from collections import deque

def dfs(graph,visited,start, end):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(graph,visited,start, end):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if graph[v] == end:
                return
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def solution(numbers, hand):
    numberpad = [ [], [2,4], [1, 3, 5], [2, 6], [1, 5], [2, 4, 6], [3, 5], [4, 8], [5, 7, 9], [6, 8],[8]]
    visited = [False]*10

    print(bfs(numberpad, visited, 1, 7))
    print(dfs(numberpad,visited,1,4))
    answer = ''
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

solution(numbers, hand)