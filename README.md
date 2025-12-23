# Endgame: Mario's Escape

## Overview
This project focuses on applying classical search algorithms to solve a multi-stage problem.
Mario must escape a survival island by navigating a map and successfully completing two embedded challenges.
The goal is to correctly model the problems, apply appropriate search strategies, and clearly show node expansion order and solution paths.

The project consists of three main parts:
	1.	Island navigation using UCS and BFS
	2.	Challenge 1: Missionaries and Cannibals solved using A* Algorithm
	3.	Challenge 2: Maze navigation solved using Greedy Best-First Search Algorithm

## Survival Game Island (Main Map)

### Graph Representation
The island is represented as a weighted graph

  <img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/71ef8b07-5d7a-4bee-b063-6126840f881c" />

	•	Nodes: S, F, C1, C2, E
	•	Edges: (neighbor, cost)

### Algorithms Applied:
- Uniform Cost Search (UCS)
Expands nodes in increasing path-cost order.

- Breadth-First Search (BFS)
Expands nodes level by level, ignoring edge costs.

### Required Output Behavior
	•	Each expanded node is printed.
	•	When a challenge node is expanded, a message indicates moving to the challenge.
	•	A valid solution path is printed after reaching the exit.

## Challenge 1: Missionaries and Cannibals Problem

Problem Formulation
	•	State Representation:
(M, C, B)
	•	M: missionaries on the left bank
	•	C: cannibals on the left bank
	•	B: boat position (0 = left, 1 = right)
	•	Initial State:
(3, 3, 0)
	•	Goal State:
(0, 0, 1)
	•	Actions:
Boat carries 1 or 2 people:
	•	(1,0), (2,0), (0,1), (0,2), (1,1)
	•	Constraints:
	  Cannibals must never outnumber missionaries on either bank.
	•	Cost Function:
Each boat crossing has cost = 1.

A* is used to solve the problem optimally.
Justification:
	•	Each remaining person must cross the river at least once.
	•	The heuristic never overestimates the remaining cost.
	•	Therefore, it is admissible and guarantees optimality.

Output
	•	Expansion order of states is printed.
	•	Final solution path is printed in one line using ->.

## Challenge 2: Finding Luigi in a Maze and Escape

Maze Representation

The maze is read from a .txt file with the format:
```
ROOM x y neighbor1 neighbor2 ...
...
Luigi F5
Exit F3
```
- Rooms are nodes
- Neighbors form graph edges
- (x, y) coordinates are used for heuristic computation

Greedy Best-First Search Algorithm is used to find Luigi and escape the maze
	•	Priority is based only on the heuristic value.
	•	Uses Manhattan Distance:
  ```
  h(n) = |x1 - x2| + |y1 - y2|
  ```

Search Process
	1.	Search from A2 to Luigi
	2.	Then search from Luigi to the Exit
	3.	Graph search is enforced (no node expanded twice)

Output
	•	Expansion order is printed
	•	Solution path is printed for each search phase


Program Structure
	•	uniform_cost_search() – UCS for island map
	•	breadth_first_search() – BFS for island map
	•	missionaries_cannibals_problem() – A* for Challenge 1
	•	greedy_best_first_search() – Greedy Best-First Search for Challenge 2
	•	move_to_challenge() – Integrates challenges into the main search
	•	main() – Menu-driven execution

How to Run
	1.	Ensure maze_structure.txt is in the same directory.
	2.	Run the program:
  ```python main.py```
	3.	Choose:
	•	1 for UCS
	•	2 for BFS

References
	•	Missionaries and Cannibals solution video
https://www.youtube.com/watch?v=laLS8gHzROg
	•	Maze exploration reference
https://www.researchgate.net/publication/315969093_Maze_Exploration_Algorithm_for_Small_Mobile_Platforms
  
