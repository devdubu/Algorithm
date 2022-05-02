'''
N*M 크기의 직사각형 미로
위치는 1,1 이며, 미로의 출구는 N,M의 위치에 존재함 한번에 한칸씩 이동 가능
괴물이 있는 부분 0, 괴물이 없는 부분 1로 표기
탈출하기 위해 움직여야하는 최소 칸의 개수를 구해라
'''
def bfs(x, y):
    #큐 구현을 위에 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌때 까지 반복
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네가지 방향 정의

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))