from collections import deque
# This is Depth First search (DFS).
# n: number of top
# m: number of edge
# g: adjacency list
# v: visited list

def dfs(node,n, g):
    stack = [node]
    visited = [False] * n
    visited[node] = True
    while stack:
        v = stack.pop()
        for i in g[v]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

def recursive_dfs(node, g, v):
    v[node] = True
    for i in g[node]:
        if not v[i]:
            recursive_dfs(i, g, v)
