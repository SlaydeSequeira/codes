from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            print(visited)
            for neighbour in graph[node]:
                queue.append(neighbour)

graph ={
    'A':['B','C'],
    'B':['A','D'],
    'D':['C']
}

bfs(graph,'A')