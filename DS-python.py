# x=[100,20,6,840,50,-1,4]
# greater=x[4]
# for i in x:
#     if i<greater:
#         greater=i
# print(greater)

#     -----------------------------------singly linked list   --------------------------------
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode= None

class LinkedList (object):
    def __init__(self):
        self.head=None
        self.size=0
    #  O(1)
    def insertStart(self,data):
        self.size=self.size+1
        newNode=Node(data)

        if not self.head:


            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    #  O(1)
    def size(self):
        return self.size

    #  O(N)  time complexity
    def size2(self):
        actualNode=self.head
        size=0

        while actualNode is not None:
            size+=1
            actualNode=actualNode.nextNode
        return size
    # inserting at the end ------------------------
    def insertEnd(self,data):
        self.size=self.size+1
        newNode= Node(data)
        actualNode=self.head
        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode

        actualNode.nextNode=newNode

#traversing the linkedlist---------------------
    def traverseList(self):
        actualNode=self.head
        while actualNode is not None:
            print(f"{actualNode.data}")
            actualNode=actualNode.nextNode


  #array

from array import *
array1=array('i',[10,20,40,50])
array1[2]=100
array1.insert(3,90)   # inserting the element
array1.remove(50)     # removing element
print(array1.index(40))   # finding index of 40
for x in array1:
    print(x)



# del  is used in all tuple,dict,list
# -----------------------------------------2D array-----------------------
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0][2])
for r in T:
    for c in r:
        print(c,end = " ")
    print()


#------------matrix--------------------------
from numpy import *

a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

m = reshape(a, (7, 5))
print(m)

#-----------------Adding a row-in matrix---------------

from numpy import *
m = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0)  #0 means x axis=0
m = delete(m,[2],0)   # deleting row
print(m_r)


#----------- adding column  in matrix----------
from numpy import *

m = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

m_c = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)   #1 means y-axis=1
m = delete(m,s_[2],1)             # deleting column

print(m_c)


# sets-----------------------------------------
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysB - DaysA
print(AllDays)


# -------------------------------------------------------------chainmap-----------------

import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()


print('elements:')  # Print all the elements from the result
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

print('day3 in res: {}'.format(('day1' in res)))    # Find a specific value in the result
print('day4 in res: {}'.format(('day4' in res)))


#----------------------- creation of linked list------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")

llist.print_list()

#------------------------- Queue------------------------################################
#---------------- Adding element in queue------
class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False

  def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
TheQueue.addtoq(6)
TheQueue.addtoq("Wed")
print(TheQueue.queue)

                  #------------------Removing element from queue--------------------
class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          # return True

      return False
# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("no elemnts")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
TheQueue.addtoq(6)
TheQueue.addtoq(7)
TheQueue.addtoq(6)
print(TheQueue.removefromq())
print(TheQueue.removefromq())
print(TheQueue.queue)

#-------------------------- Dequeue--------------------
import collections

DoubleEnded = collections.deque(["Mon","Tue","Wed"])

DoubleEnded.append("Thu")

print ("Appended at right - ")
print (DoubleEnded)

DoubleEnded.appendleft("Sun")

print ("Appended at right at left is - ")
print (DoubleEnded)

DoubleEnded.pop()

print ("Deleting from right - ")
print (DoubleEnded)

DoubleEnded.popleft()

print ("Deleting from left - ")
print (DoubleEnded)

#-----------------------Stack-----------------#############################----------------------
  #----------------------- PUSH into stack------
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):
	    return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())

          #------------POP from stack-------------
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())




# circular Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    def remove(self, key):
        # if self.head.next == self.head and self.head.data == key:
        #     self.head = None
        #     return
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

# cllist.remove("A")
# cllist.remove("C")
# cllist.print_list()
print(cllist.split_list())


#Doubling Linked list adding before & after

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(3,6)
dllist.add_before_node(4,9)
dllist.print_list()


list1=[[12,9],[10,9],[9,6],[0,4]]
list1.sort()
print(list1)
"""
# Breadth-first search
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, start):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(start)
        visited[start] = True
        while queue:
            # Dequeue a vertex from queue and print it
            start = queue.pop(0)
            print(start, end=" ")
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
# Driver code
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)



# Depth first search
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
        def DFS(self, v):

            # Create a set to store visited vertices
            visited = set()

            # Call the recursive helper function
            # to print DFS traversal
            self.DFSUtil(v, visited)

    # Driver code

    # Create a graph given
    # in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)






























































































