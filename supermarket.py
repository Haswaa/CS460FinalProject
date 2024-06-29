import heapq

def dijkstra(graph, start):
    #dictionary will store the shortest path to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    #priority queue to store nodes to be explored and initialized with the start node
    priority_queue = [(0, start)]
    
    while priority_queue:
        #gets the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        #nodes can be pushed multiple times with different distances
        #only process a vertex the first time we remove it from the priority queue
        if current_distance > shortest_paths[current_node]:
            continue
        
        #explores each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            #only consider this new path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

#example supermarket layout as a graph
supermarket_graph = {
    'Entrance': {'Produce': 5, 'Bakery': 2},
    'Produce': {'Dairy': 2, 'Meat': 3},
    'Bakery': {'Dairy': 3},
    'Dairy': {'Checkout': 1},
    'Meat': {'Checkout': 5},
    'Checkout': {}
}

#starting at the entrance, find the shortest path to all other sections
shortest_paths_from_entrance = dijkstra(supermarket_graph, 'Entrance')
print("Shortest paths from Entrance:", shortest_paths_from_entrance)