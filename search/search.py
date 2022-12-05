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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
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

    # khoi tao danh sach cac node
    nodeStack = util.Stack()
    # push node goc vao danh sach cac node
    nodeStack.push((problem.getStartState(), []))
    # danh sach nhung node da di qua
    visitedNode = set()

    # kiem tra con node nao chua duyet ko
    while not nodeStack.isEmpty():

        currentNodeState, moves = nodeStack.pop()

        # check node dang xet co la dich hay ko
        if problem.isGoalState(currentNodeState):
            return moves

        # neu node dang xet ko la dich
        # -> xet tiep co nam trong danh sach nhung node da di qua hay ko
        if currentNodeState not in visitedNode:
            visitedNode.add(currentNodeState)

            # duyet thuoc tinh cac node
            for nodeState, move, stepcost in problem.getSuccessors(currentNodeState):
                # tao duong di moi
                nodeStack.push((nodeState, moves + [move]))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # khoi tao danh sach cac node
    nodeQueue = util.Queue()
    # push node goc vao danh sach cac node
    nodeQueue.push((problem.getStartState(), []))
    # khoi tao danh sach cac node da di qua
    visitedNode = set()

    # kiem tra con node nao chua duyet ko
    while not nodeQueue.isEmpty():

        currentNodeState, moves = nodeQueue.pop()

        # check node dang xet co la dich hay ko
        if problem.isGoalState(currentNodeState):
            return moves

        # neu node dang xet ko la dich
        # -> xet tiep co nam trong danh sach nhung node da di qua hay ko
        if currentNodeState not in visitedNode:
            visitedNode.add(currentNodeState)

            # duyet thuoc tinh cac node
            for nodeState, move, stepcost in problem.getSuccessors(currentNodeState):
                # tao duong di moi
                nodeQueue.push((nodeState, moves + [move]))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # khoi tao danh sach cac node
    nodePriorityQueue = util.PriorityQueue()
    # push node goc
    nodePriorityQueue.push((problem.getStartState(), [], 0), 0)
    # khoi tao danh sach cac node da di qua
    visitedNode = {}

    # kiem tra con node nao chua duyet ko
    while not nodePriorityQueue.isEmpty():

        currentNodeState, moves, cost = nodePriorityQueue.pop()

        # kiem tra co la dich hay ko
        if problem.isGoalState(currentNodeState):
            return moves

        # so sanh gia tri cua node hien tai va node trung lap (cua con duong khac)
        if (currentNodeState not in visitedNode) or (cost < visitedNode[currentNodeState]):
            # neu node trung lap co cost thap hon -> cap nhat cho node hien tai
            visitedNode[currentNodeState] = cost

            # duyet thuoc tinh cac node
            for nodeState, move, stepcost in problem.getSuccessors(currentNodeState):
                # tao duong di moi
                nodePriorityQueue.update(
                    (nodeState, moves + [move], cost + stepcost), cost + stepcost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # khoi tao danh sach cac node
    nodePriorityQueue = util.PriorityQueue()
    # push node goc
    nodePriorityQueue.push((problem.getStartState(), [], 0), 0)
    # khoi tao danh sach cac node da di qua
    visitedNode = set()

    # kiem tra con node chua duyet hay ko
    while not nodePriorityQueue.isEmpty():

        currentNodeState, moves, cost = nodePriorityQueue.pop()

        visitedNode.add((currentNodeState, cost))

        # kiem tra la dich hay ko
        if problem.isGoalState(currentNodeState):
            return moves

        # duyet thuoc tinh cac node
        for nodeState, move, stepcost in problem.getSuccessors(currentNodeState):

            # cap nhat duong di moi
            _move = moves + [move]

            # cap nhat gia tri duong di moi
            # _cost = problem.getCostOfActions(_move)
            _cost = cost + stepcost

            # cap nhat node moi
            _node = (nodeState, _move, _cost)

            check = False

            # if currentNodeState not in visitedNode and _cost >= visitedNode[currentNodeState]:
            #     # for currentState, currentCost in visitedNode:
            #     for nodeState, move, stepcost in problem.getSuccessors(currentNodeState):
            #         nodePriorityQueue.push(
            #             _node, _cost + heuristic(nodeState, problem))
            #         visitedNode.add((nodeState, _cost))

            for currentState, currentCost in visitedNode:
                if nodeState == currentState and _cost >= currentCost:
                    check = True

            if not check:
                nodePriorityQueue.push(_node, _cost + heuristic(nodeState, problem))
                visitedNode.add((nodeState, _cost))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
