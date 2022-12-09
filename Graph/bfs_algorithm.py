"""
Breadth First Search (BFS)

Implementing the algorithm
Keep a queue of items
Dequeue an item
Check if the item meets the condition
Does it meet the connection? a. meets condition END b. Add all connected nodes to the condition
Loop
If the queue is empty then END.
"""

# Все начинается с создания очереди. В Python для создания двусторонней
# очереди (дека) используется функция deque:

from collections import deque
from bfs_graph import *

def person_is_seller(name):
    """If the name ends w. 'm' then seller"""
    return name[-1] == 'm'

def bfs_search(name):
    search_queue = deque() # create queue
    search_queue += graph["you"]
    searched = []
  # while the queue isn't empty, get the first item check
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + 'is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                print(person + 'is not a mango seller :(')
    return False

bfs_search('you')
