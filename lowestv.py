from traversal import node1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def FindLowestValue(head):
    minValue = head.data
    currentNode = head
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue


node1 = Node(2)
node2 = Node(12)
node3 = Node(2)
node4 = Node(14)
node5 = Node(23)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is" ,FindLowestValue(node1) )


    