from collections import deque
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited =[]

def bfs(visited,graph,node):
    visited.append(node)
    dq = deque()
    dq.append(node)
        
    while dq:
        current_node = dq.popleft()
        print(current_node,end= ' ')
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                dq.append(neighbour)
    
    
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling