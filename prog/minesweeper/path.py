from websockets.sync.client import connect
import json
import numpy as np
import heapq

def find_path(status, start, end):
    board = define_inputs(status, end)
    path = dijkstra(board, start, end)
    return path

def convert_path_to_directions(coords):
    directions = []
    for i in range(len(coords) - 1):
        y1, x1 = coords[i]
        y2, x2 = coords[i + 1]
        if y2 > y1: directions.append('down')
        elif y2 < y1: directions.append('up')
        elif x2 > x1: directions.append('right')
        else: directions.append('left')

    return directions

def dijkstra(maze, start, end):
    # Create a priority queue to store the distances
    distances = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] != 0:
                distances[(i, j)] = float('inf')
    distances[start] = 0

    # Create a dictionary to store the previous nodes
    previous_nodes = {}

    # Create a priority queue to store the nodes
    pq = [(0, start)]
    while pq:
        # Get the node with the minimum distance
        current_distance, current_node = heapq.heappop(pq)

        # Check if we have reached the end
        if current_node == end:
            # Reconstruct the path
            path = []
            while current_node in previous_nodes:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()

            #conversions
            # converted_path = [(y, x) for x, y in path]
            converted_path = convert_path_to_directions(path)
            return converted_path

        # Update the distances of the neighbors
        i, j = current_node
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            if neighbor in distances:
                new_distance = current_distance + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (new_distance, neighbor))

    # If we haven't reached the end, return an empty list
    return []

def define_inputs(status, end):
    board = np.array(status['map'])
    mapping = {'c0': 1, 'c1': 1, 'c2': 1, 'c3': 1, 'c4': 1, 'c5': 1, 'c6': 1, 'c7': 1, 'covered': 0, 'key': 1, 'bomb': 0}
    board = np.vectorize(mapping.get)(board)
    board[end[0],end[1]] = 1

    return board

if __name__ == '__main__':
    with connect("ws://mikusweeper.chals.sekai.team/socket") as websocket:
        status = json.loads(websocket.recv())
        start = (1,1)
        end = (10,10)
        print(find_path(status, start, end))

