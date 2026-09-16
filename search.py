# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    fringe = util.Stack() # using a stack for DFS since we want to explore the most recent state first (LIFO)
    closed = set() # keeping track of states we already visited so we don't explore them again

    fringe.push((problem.getStartState(), [])) # start with the starting state and no actions taken yet

    # keep searching until there is nothing left in the stack
    while not fringe.isEmpty():
        # getting the next state we want to explore
        elem = fringe.pop()
        state = elem[0]
        actions = elem[1]

        # only explore this state if we haven't visited it before
        if state not in closed:
            closed.add(state)

            if problem.isGoalState(state): # if we reached the goal, return the path we took to get here
                return actions
            
            # looking through all the possible states we can go to next
            for successors in problem.getSuccessors(state):
                successor_state = successors[0]
                successor_action = successors[1]
                new_actions = actions + [successor_action] # adding this move to the actions we have taken so far
                fringe.push((successor_state, new_actions)) # adding the new state to the stack so we can explore it
    return [] # if we searched everything and couldn't find the goal

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""

    fringe = util.Queue() # using a queue for BFS since we want to explore the oldest state first (FIFO)
    closed = set() # keeping track of states we already visited so we don't explore them again
    fringe.push((problem.getStartState(), [])) # start with the starting state and no actions taken yet

    # keep searching until there is nothing left in the queue
    while not fringe.isEmpty():
        # get the next state we want to explore
        elem = fringe.pop()
        state = elem[0]
        actions = elem[1]

        # only explore this state if we haven't visited it before
        if state not in closed:
            closed.add(state)

            # if we reached the goal, return the path we took to get here
            if problem.isGoalState(state):
                return actions

            # look through all the possible states we can go to next
            for successors in problem.getSuccessors(state):
                successor_state = successors[0]
                successor_action = successors[1]
                new_actions = actions + [successor_action] # adding this move to the actions we have taken so far
                fringe.push((successor_state, new_actions)) # adding the new state to the queue so we can explore it later
    return [] # if we searched everything and couldn't find the goal

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""

    fringe = util.PriorityQueue() # using a priority queue for UCS so the path with the lowest cost comes out first
    closed = set() # keeping track of states we already visited so we don't explore them again
    fringe.push((problem.getStartState(), [], 0), 0) # starting with the starting state; no actions taken yet and a cost of 0

    # keep searching until there is nothing left in the priority queue
    while not fringe.isEmpty():
        # getting the path with the lowest total cost
        elem = fringe.pop()
        state = elem[0]
        actions = elem[1]
        costs = elem[2]

        # only explore this state if we haven't visited it before
        if state not in closed:
            closed.add(state)

            # if we reached the goal return the path we took to get here
            if problem.isGoalState(state):
                return actions

            # looking through all the possible states we can go to next
            for successors in problem.getSuccessors(state):
                successor_state = successors[0]
                successor_action = successors[1]
                successor_cost = successors[2]

                # updating the actions and total cost for this new path
                new_actions = actions + [successor_action]
                new_cost = costs + successor_cost
                fringe.push((successor_state, new_actions, new_cost), new_cost) # adding it to the queue using the total path cost as its priority
    return [] # if we searched everything and couldn't find the goal

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""

    # getting the starting state and set up the priority queue
    start = problem.getStartState() 
    fringe = util.PriorityQueue() 

    visited = set() # keeping track of states we already visited so we don't explore them again
    is_consistent = True # keeping track of whether the heuristic stays consistent during the search

    # starting with the starting state, no actions, and a path cost of 0; the starting priority is just its heuristic since the path cost is 0
    fringe.push((start, [], 0), heuristic(start, problem))

    # keep searching until there is nothing left in the priority queue
    while not fringe.isEmpty():
        # getting the state with the lowest combined cost and heuristic
        current = fringe.pop()
        state = current[0]
        path = current[1]
        cost = current[2]

        if state in visited: # if we already visited this state skip it
            continue
        
        # if we reached the goal return the path we took to get here
        if problem.isGoalState(state): 
            if is_consistent:
                print("CONSISTENT")
            else:
                print("INCONSISTENT")
            return path

        visited.add(state) # marking this state as visited before looking at its successors

        # looking through all the possible states we can go to next
        for successor in problem.getSuccessors(state): 
            successor_state = successor[0]
            action = successor[1]
            step_cost = successor[2]

            # getting the heuristic values so we can check consistency
            current_h = heuristic(state, problem)
            successor_h = heuristic(successor_state, problem)

            # checking if consistent heuristic; should satisfy h(n) <= cost(n,n') + h(n')
            if current_h > step_cost + successor_h:
                is_consistent = False

            # updating the path and total cost to reach this successor
            new_path = path + [action] 
            new_cost = cost + step_cost 
            priority = new_cost + heuristic(successor_state, problem) # calculating A* using path cost + heuristic as the priority
            fringe.push((successor_state, new_path, new_cost), priority) # adding the successor to the priority queue
    return [] # if we searched everything and couldn't find the goal

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
