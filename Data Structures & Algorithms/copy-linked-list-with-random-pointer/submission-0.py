"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        refer = []
        new, curr = Node(0), head
        oldHead = head
        newHead = new

        # appeing values to an array

        while curr:
            refer.append([curr.val, curr.random])
            curr = curr.next 
        
        # Filling up the new Node list without .random's

        for p in refer:
            newNode = Node(p[0])
            new.next = newNode
            new = new.next
        
        # make a dict {old_point:new_pointer} map

        temp1 = oldHead
        temp2 = newHead.next

        relation = {}

        while temp1 and temp2:
            relation[temp1] = temp2
            temp1 = temp1.next
            temp2 = temp2.next

        # iterate through new Nodes, assign 
        temp1 = oldHead
        temp2 = newHead.next

        while temp1 and temp2:
            temp2.random = relation[temp1.random] if temp1.random else None
            temp1 = temp1.next
            temp2 = temp2.next
        


        return newHead.next
