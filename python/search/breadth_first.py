from collections import deque
# This is Breath First search (BFS).
# n: number of top
# m: number of edge
# g: adjacency list
def bfs(node, n, g):
    queue = deque([node])
    distance = [None] * n # Inisialize distance from node 
    distance[node] = 0 # The distance from itself 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if distance[i] is None:
                distance[i] = distance[v] + 1
                queue.append(i)
    return distance