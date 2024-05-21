import random
from display_tree import display_tree

class Node:

    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None
        self.type = None
        self.parent = None
        self.turn = 0
        
    def __repr__(self) -> str:
        return f'key: {self.key}'


def create_random_binary_tree(length):
    if length == 0:
        return None

    value = random.randint(1, 1000) 
    node = Node(value)

    if length > 1:
        left_length = random.randint(0, length - 1)
        right_length = length - 1 - left_length
        node.left = create_random_binary_tree(left_length)
        if node.left:
            node.left.parent = node
            node.left.type = 'left'
        #print('l ' + str(node.left))
        node.right = create_random_binary_tree(right_length)
        if node.right:
            node.right.parent = node
            node.right.type = 'right'
        #print('r ' + str(node.right))

    return node

a = create_random_binary_tree(10)

def printPreorder(node):
    if node is None:
        return

    if node.parent:
        node.turn = node.parent.turn
        if node.parent.type != node.type and node.parent.type:
            node.turn = node.turn + 1

    print(node.turn,node.key, node.type, end=',  ')
    printPreorder(node.left)
    printPreorder(node.right)

printPreorder(a)

print()

display_tree(a)

# def printLevelOrder(node):

#     # Base Case
#     if node is None:
#         return

#     # Create an empty queue
#     # for level order traversal
#     queue = []

#     # Enqueue Root and initialize height
#     queue.append(node)

#     while(len(queue) > 0):

#         # Print front of queue and
#         # remove it from queue
        
#         if node.parent and node.parent.type != node.type:
#             node.turn = node.turn + 1
#         else:
#             if node.parent:
#                 node.turn = node.parent.turn
#         print(queue[0].key,node.turn, end=" ")
#         node2 = queue.pop(0)

#         # Enqueue left child
#         if node2.left is not None:
#             queue.append(node2.left)

#         # Enqueue right child
#         if node2.right is not None:
#             queue.append(node2.right)

# printLevelOrder(a)