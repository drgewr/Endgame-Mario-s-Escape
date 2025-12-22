import heapq
from collections import deque

# Challenge 1: Missionaries & Cannibals Problem

# State representation: (missionaries_left, cannibals_left, boat_position)
# boat_position: 0 = left bank, 1 = right bank
START = (3, 3, 0)
GOAL = (0, 0, 1)
# Allowed moves respecting boat capacity (max 2 people)
MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] 

def isValid(state):
    #Check whether a state satisfies problem constraints
    mL, cL, _ = state
    mR, cR = 3 - mL, 3 - cL

    if mL < 0 or mL > 3 or cL < 0 or cL > 3:
        return False
    # Left bank constraint
    if mL > 0 and cL > mL:
        return False
    # Right bank constraint
    if mR > 0 and cR > mR:
        return False
    
    return True

def successorState(state):
    #Generate all valid successor states
    m, c, boat = state

    # Direction depends on boat location
    direction = -1 if boat == 0 else 1
    successors = []
    
    for dm, dc in MOVES:
        new_state = (m + direction * dm, c + direction * dc, 1 - boat)
        if isValid(new_state):
            successors.append(new_state)
    
    return successors

def heuristic_mc(state):
    #Admissible heuristic for A*: Number of people remaining on the left bank
    m, c, _ = state
    
    return m + c

def missionaries_cannibals_problem():
    #Solve the problem using A* search
    frontier = []
    heapq.heappush(frontier, (heuristic_mc(START), 0, START, [START]))
    visited = set()

    while frontier:
        f, g, state, path = heapq.heappop(frontier)

        if state in visited:
            continue
        
        visited.add(state)
        print(f"Expanding {state}")

        if state == GOAL:
            return path

        for successor in successorState(state):
            if successor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic_mc(successor)
                heapq.heappush(frontier, (new_f, new_g, successor, path + [successor]))

    return None

def challenge_1():
    #Wrapper for Missionaries & Cannibals Challenge
    path = missionaries_cannibals_problem()

    print("-"*40)
    print("Solution path:")
    print(" -> ".join(str(state) for state in path))
    print("-"*40)
    
    return True

# Challenge 2: Finding Luigi in a Maze and Escape
def parse_maze(file_text):
    #Parse maze structure, coordinates, Luigi and Exit.
    graph = {}
    pos = {}
    luigi = None
    exit_room = None

    for line in file_text.strip().splitlines():
        parts = line.strip().split()
        
        if not parts:
            continue
        if parts[0] == "Luigi":
            luigi = parts[1]
            continue
        if parts[0] == "Exit":
            exit_room = parts[1]
            continue

        room = parts[0]
        x, y = int(parts[1]), int(parts[2])
        neighbors = parts[3:]
        pos[room] = (x, y)
        graph[room] = neighbors

    return graph, pos, luigi, exit_room

def manhattanDistance(p1, p2):
    #Manhattan distance heuristic
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def greedy_best_first_search(graph, pos, start, goal):
    #Greedy Best-First Search with graph search
    frontier = []
    heapq.heappush(frontier, (manhattanDistance(pos[start], pos[goal]), start, [start]))
    visited = set()

    while frontier:
        _, node, path = heapq.heappop(frontier)

        if node in visited:
            continue
        
        visited.add(node)   
        print(f"Expanding {node}")

        if node == goal:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                h = manhattanDistance(pos[neighbor], pos[goal])
                heapq.heappush(frontier, (h, neighbor, path + [neighbor]))
    
    return None

def challenge_2():
    #Wrapper for Finding Luigi in a Maze and Escape Challenge
    with open("maze_structure.txt", "r") as file:
        inFile = file.read()

    graph, pos, luigi, exit_room = parse_maze(inFile)

    print("Finding Luigi...")
    path_to_luigi = greedy_best_first_search(graph, pos, "A2", luigi)
    
    if not path_to_luigi:
        print("Failed to find Luigi.")
        return False
    
    print("Path to Luigi:", " ".join(path_to_luigi))
    print("Luigi was found! Escaping to Exit...")
    path_to_exit = greedy_best_first_search(graph, pos, luigi, exit_room)
    
    if not path_to_exit:
        print("Failed to reach Exit.")
        return False

    return True

def move_to_challenge(challenge):
    #Dispatch to the corresponding challenge
    if challenge == "C1":
        return challenge_1()
    if challenge == "C2":
        return challenge_2()
    
    return True

def uniform_cost_search(graph, start, goal):
    #Uniform Cost Search on survival game map
    frontier = [(0, start)]
    heapq.heapify(frontier)
    visitedNode = set()
    totalCost = {start: 0}
    previousNode = {start: None}

    while frontier:
        currentCost, currentNode = heapq.heappop(frontier)

        if currentNode in visitedNode:
            continue
        
        visitedNode.add(currentNode)
        
        if currentNode == "C1":
            print("Expanding C1.. Moving to challenge 1")
            print("-"*40)
            move_to_challenge(currentNode)
        elif currentNode == "C2":
            print("Expanding C2.. Moving to challenge 2")
            print("-"*40)
            move_to_challenge(currentNode)
        else:
            print(f"Expanding {currentNode}")
        
        if currentNode == goal:
            break
        
        for neighbor, neighborCost in graph[currentNode]:
            newCost = currentCost + neighborCost
            if neighbor not in totalCost or newCost < totalCost[neighbor]:
                totalCost[neighbor] = newCost
                heapq.heappush(frontier, (newCost, neighbor))
                previousNode[neighbor] = currentNode

    path = []
    node = goal
    
    while node is not None:
        path.append(node)
        node = previousNode.get(node)
    
    path.reverse()
    print("-"*40)
    print("Solution path:", " ".join(path))
    print("-"*40)

def breadth_first_search(graph, start, goal):
    #Breadth-First Search on survival game map
    queue = deque([start])
    visitedNode = set()
    previousNode = {start: None}

    while queue:
        currentNode = queue.popleft()

        if currentNode in visitedNode:
            continue
        
        visitedNode.add(currentNode)
        
        if currentNode == "C1":
            print("Expanding C1.. Moving to challenge 1")
            print("-"*40)
            move_to_challenge(currentNode)
        elif currentNode == "C2":
            print("Expanding C2.. Moving to challenge 2")
            print("-"*40)
            move_to_challenge(currentNode)
        else:
            print(f"Expanding {currentNode}")
        
        if currentNode == goal:
            break
        
        for neighbor, _ in graph[currentNode]:
            if neighbor not in visitedNode and neighbor not in queue:
                queue.append(neighbor)
                previousNode[neighbor] = currentNode

    path = []
    node = goal
    
    while node:
        path.append(node)
        node = previousNode.get(node)
    
    path.reverse()
    print("-"*40)
    print("Solution path:", " ".join(path))
    print("-"*40)

def main():
    #Main menu
    graph = {
        "S": [("F", 80), ("C1", 99)],
        "F": [("C2", 97)],
        "C1": [("E", 211)],
        "C2": [("E", 101)],
        "E": []
    }
    start = "S"
    goal = "E"

    while True:
        print("Choose the Algorithm to Apply:")
        print("1) UCS")
        print("2) BFS")
        choice = input("Choice: ")

        if choice == "1":
            uniform_cost_search(graph, start, goal)
        elif choice == "2":
            breadth_first_search(graph, start, goal)
        else:
            print("Invalid choice!")

        choose = input("Do you want to continue? (y/n): ")
        print("="*40)
        
        if choose not in ("y", "Y"):
            break

if __name__ == "__main__":
    main()