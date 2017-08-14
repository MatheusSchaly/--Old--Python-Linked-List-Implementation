'''
Created on Jul 23, 2017
@author: Matheus Schaly
'''

from __future__ import print_function

class Node(object):
    def __init__ (self, data = 0, next = None):
        self.data = data
        self.next = next
    
head = Node()
    
class LinkedList():
    def insert (self, data, position):
        global head
        temp1 = Node()
        temp1.data = data
        if position == 1:
            temp1.next = head
            head = temp1
            return
        temp2 = head
        for i in range(2, position):
            temp2 = temp2.next
        temp1.next = temp2.next
        temp2.next = temp1
        
    def remove (self, position):
        global head
        temp = head
        prev = Node()
        if position == 1:
            head = temp.next
            return
        for i in range(1, position):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        
    def reverseList (self):
        global head
        curr = head
        prev = Node()
        next = Node()
        while next != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev.next
            
    def printList(self):
        global head
        temp = head
        while temp.next: # Same as temp.next != None
            print(temp.data, end = '')
            temp = temp.next
        print('')
    
myList = LinkedList()
myList.insert(1, 1) # 1
myList.printList() # 1
myList.insert(2, 2) # 1 2
myList.printList() # 1 2
myList.insert(3, 1) # 3 1 2
myList.insert(4, 3) # 3 1 4 2
myList.printList() # 3 1 4 2
myList.remove(3) # 3 1 2
myList.insert(4, 1) # 4 3 1 2 
myList.insert(4, 2) # 4 4 3 1 2
myList.printList() # 4 4 3 1 2
myList.remove(1) # 4 3 1 2
myList.remove(2) # 4 1 2
myList.remove(3) # 4 1
myList.remove(2) # 4
myList.insert(6, 1) # 6 4
myList.insert(5, 2) # 6 5 4 
myList.printList() # 6 5 4
myList.reverseList() # 4 5 6
myList.printList() # 4 5 6
myList.insert(3, 1) # 3 4 5 6
myList.printList() # 3 4 5 6
myList.reverseList() # 6 5 4 3
myList.printList() # 3 4 5 6