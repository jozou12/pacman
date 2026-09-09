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
    "*** YOUR CODE HERE ***"
    "Init the fringe and closed set for dfs graph search. Using Stack, LIFO"
    fringe = util.Stack()
    "Set store the visited state. Using set because the time complexity finding element from set it's O(n) = 1"
    closed = set()
    "Push the start state into fringe, no actions at all"
    fringe.push((problem.getStartState(), []))
    "if fringe is empty and not return the actions, it means can't find the solution"
    while not fringe.isEmpty():
        elem = fringe.pop()
        state = elem[0]
        actions = elem[1]
        "if state is already in the closed set, skip it"
        if state not in closed:
            closed.add(state)
            "check if the goal state is true, then return actions"
            if problem.isGoalState(state):
                return actions
            "For DFS, we don't need cost"
            for successors in problem.getSuccessors(state):
                successor_state = successors[0]
                successor_action = successors[1]
                "update the actions"
                new_actions = actions + [successor_action]
                fringe.push((successor_state, new_actions))
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "Init the fringe and closed set for bfs graph search, using Queue FIFO"
    fringe = util.Queue()
    "Set store the visited state. Using set because the time complexity finding element from set it's O(n) = 1"
    closed = set()
    "Push the start state into fringe, no actions at all"
    fringe.push((problem.getStartState(), []))
    "if fringe is empty and not return the actions, it means can't find the solution"
    while not fringe.isEmpty():
        elem = fringe.pop()
        state = elem[0]
        actions = elem[1]
        "if state is already in the closed set, skip it"
        if state not in closed:
            closed.add(state)
            "check if the goal state is true, then return actions"
            if problem.isGoalState(state):
                return actions
            "For BFS, we don't need cost"
            for successors in problem.getSuccessors(state):
                successor_state = successors[0]
                successor_action = successors[1]
                "update the actions"
                new_actions = actions + [successor_action]
                fringe.push((successor_state, new_actions))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "Init the fringe and closed set for bfs graph search, using PriorityQueue lowerest cost first out"
    fringe = util.PriorityQueue()
    "Set store the visited state. Using set because the time complexity finding element from set it's O(n) = 1"
    closed = set()
    "Push the start state into fringe, no actions at all. And we also need to put the total cost as part of the input"
    fringe.push((problem.getStartState(), [], 0), 0)
    "if fringe is empty and not return the actions, it means can't find the solution"
    while not fringe.isEmpty():
        elem = fringe.pop()
        state = elem[0]
        actions = elem[1]
        costs = elem[2]
        "if state is already in the closed set, skip it"
        if state not in closed:
            closed.add(state)
            "check if the goal state is true, then return actions"
            if problem.isGoalState(state):
                return actions
            "For UCS, we need cost in order to maintain the PriorityQueue"
            for successors in problem.getSuccessors(state):
                successor_state = successors[0]
                successor_action = successors[1]
                successor_cost = successors[2]
                "update total actions and total cost"
                new_actions = actions + [successor_action]
                new_cost = costs + successor_cost
                fringe.push((successor_state, new_actions, new_cost), new_cost)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""

    start = problem.getStartState() # getting the start of the search 
    fringe = util.PriorityQueue() # initalizing priority queue 
    visited = set() # initializing a set to store all visited states 
    is_consistent = True # creating a consistency check 

    # storing the state, path, and cost along with the heuristic
    fringe.push((start, [], 0), heuristic(start, problem))

    # looping continuously while fringe is not empty 
    while not fringe.isEmpty():
        current = fringe.pop() # popping the first one in the priority queue
        
        # separating into different variables 
        state = current[0]
        path = current[1]
        cost = current[2]

        if state in visited: # if the state is already visited then continue on 
            continue
        
        if problem.isGoalState(state): # if the problem reaches the goal state then return the path 
            if is_consistent:
                print("CONSISTENT")
            else:
                print("INCONSISTENT")

            return path

        visited.add(state) # add the state into the visited set 

        # looping through the successors of the current state
        for successor in problem.getSuccessors(state): 
            successor_state = successor[0]
            action = successor[1]
            step_cost = successor[2]

            current_h = heuristic(state, problem)
            successor_h = heuristic(successor_state, problem)

            # checking if the heuristic is consistent 
            if current_h > step_cost + successor_h:
                is_consistent = False

            new_path = path + [action] # updating the new path 
            new_cost = cost + step_cost # calculating the new cost 
            priority = new_cost + heuristic(successor_state, problem) # calculating the priority 
            fringe.push((successor_state, new_path, new_cost), priority) # pushing the successor into the priority queue 

    return [] # if no solution is found 

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
