# =====================================
# BFS & DFS Graph Traversal
# Python Implementation
# =====================================


from collections import deque



# Breadth First Search

def bfs(graph, start):

    visited = set()

    queue = deque([start])

    visited.add(start)


    print("BFS Traversal:", end=" ")


    while queue:

        node = queue.popleft()

        print(node, end=" ")


        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)



    print()



# Depth First Search

def dfs(graph, start, visited=None):

    if visited is None:

        visited = set()

        print("DFS Traversal:", end=" ")



    visited.add(start)

    print(start, end=" ")



    for neighbor in graph[start]:

        if neighbor not in visited:

            dfs(graph, neighbor, visited)



# Example Graph (City Map)

graph = {


    'A': ['B', 'C'],

    'B': ['D', 'E'],

    'C': ['F'],

    'D': [],

    'E': [],

    'F': []

}



# Starting Node

start_node = 'A'



# Function Calls

bfs(graph, start_node)

dfs(graph, start_node)
