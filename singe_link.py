# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:04:42 2022

@author: nymaswan2201
"""

#create the node class
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

#create my node objects that i will link later on
node1 = Node(5,None)
node2 = Node(6,None)
node3 = Node(7,None)
node4 = Node(8,None)
node5 = Node(9,None)


#Link the nodes to create a linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

#This is a pointer variable i will use to iterate the list
pointer = Node(None,None)
pointer.next = node1

#print the list items
while (pointer.next != None):
    print(pointer.next.data)
    pointer.next = pointer.next.next
