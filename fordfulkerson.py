
import sys
from collections import deque

def bfs(source, sink, parent, capacity_matrix, adj_list, V):
    # Reset visited array
    visited = [False] * V
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        
        for v in adj_list[u]:
          
            if not visited[v] and capacity_matrix[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
                    
    return False

def solve():
   
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    V = int(input_data[0])
    E = int(input_data[1])
    
    
    adj_list = [[] for _ in range(V)]
    # 2D capacity matrix to track residual capacities between nodes
    capacity_matrix = [[0] * V for _ in range(V)]
    
    idx = 2
    for _ in range(E):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        cap = int(input_data[idx+2])
        idx += 3
        
        # If there are duplicate edges, accumulate the capacities
        if capacity_matrix[u][v] == 0 and capacity_matrix[v][u] == 0:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        capacity_matrix[u][v] += cap

    source = 0
    sink = V - 1
    max_flow = 0
    parent = [-1] * V
    
    
    while bfs(source, sink, parent, capacity_matrix, adj_list, V):
  
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity_matrix[parent[s]][s])
            s = parent[s]
            
        
        v = sink
        while v != source:
            u = parent[v]
            capacity_matrix[u][v] -= path_flow
            capacity_matrix[v][u] += path_flow
            v = parent[v]
            
        max_flow += path_flow
        
    print(max_flow)

if __name__ == '__main__':
    solve()
