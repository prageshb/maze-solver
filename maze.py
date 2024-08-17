import heapq
from collections import deque

# Helper function to get valid neighbors in the maze LC00017001987
def get_neighbors(maze, position):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []
    for d in directions:
        new_row = position[0] + d[0]
        new_col = position[1] + d[1]
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
            neighbors.append((new_row, new_col))
    return neighbors

# Heuristic function for A* and Best-First Search LC00017001987
def maze_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

# Depth-First Search (DFS) LC00017001987
def depth_first_search(maze, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (current, path) = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in get_neighbors(maze, current):
            stack.append((neighbor, path + [neighbor]))

    return None

# Breadth-First Search (BFS) LC00017001987
def breadth_first_search(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (current, path) = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in get_neighbors(maze, current):
            queue.append((neighbor, path + [neighbor]))

    return None

# Uniform Cost Search (UCS) LC00017001987
def uniform_cost_search(maze, start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        (cost, current, path) = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in get_neighbors(maze, current):
            new_cost = cost + 1  # Assuming each move has a cost of 1
            heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))

    return None

# A* Search LC00017001987
def a_star_search(maze, start, goal):
    queue = [(maze_distance(start, goal), start, [start])]
    visited = set()

    while queue:
        (_, current, path) = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in get_neighbors(maze, current):
            priority = len(path) + maze_distance(neighbor, goal)
            heapq.heappush(queue, (priority, neighbor, path + [neighbor]))

    return None

# Best-First Search LC00017001987
def best_first_search(maze, start, goal):
    queue = [(maze_distance(start, goal), start, [start])]
    visited = set()

    while queue:
        (_, current, path) = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor in get_neighbors(maze, current):
            priority = maze_distance(neighbor, goal)
            heapq.heappush(queue, (priority, neighbor, path + [neighbor]))

    return None

# Function to visualize the maze and path LC00017001987
def visualize_maze(maze, path=None, start=None, goal=None):
    maze_copy = [row[:] for row in maze]
    if path:
        for position in path:
            maze_copy[position[0]][position[1]] = '.'
    if start:
        maze_copy[start[0]][start[1]] = 'S'
    if goal:
        maze_copy[goal[0]][goal[1]] = 'G'

    for row in maze_copy:
        print(' '.join(str(cell) for cell in row))
    print()

# Main function to run the Maze Solver LC00017001987
def main():
    print("\n\nWelcome to the Maze Solver! \nBy Pragesh Bhandari")

    # Initial 2D Maze Representation LC00017001987
    new_maze = [
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
    ]
    start = (0, 0)
    goal = (7, 7)

    algorithms = {
        '1': ('Depth-First Search', depth_first_search),
        '2': ('Breadth-First Search', breadth_first_search),
        '3': ('Uniform Cost Search', uniform_cost_search),
        '4': ('A* Search', a_star_search),
        '5': ('Best-First Search', best_first_search),
    }

    while True:
        print("\nChoose a search algorithm:")
        for key, (name, _) in algorithms.items():
            print(f"{key}. {name}")

        choice = input("Enter your choice (1-5): ")
        if choice not in algorithms:
            print("Invalid choice. Please try again.")
            continue

        _, algorithm = algorithms[choice]

        print("\nInitial Maze:")
        visualize_maze(new_maze, start=start, goal=goal)

        path = algorithm(new_maze, start, goal)

        if path:
            print(f"Path found using {algorithms[choice][0]}:")
            visualize_maze(new_maze, path=path, start=start, goal=goal)
        else:
            print("No path found.")

        repeat = input("Solve another maze? (y/n): ")
        if repeat.lower() != 'y':
            break

if __name__ == "__main__":
    main()