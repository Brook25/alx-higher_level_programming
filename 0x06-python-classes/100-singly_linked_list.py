#!/usr/bin/python3
"""
This Module defines classes Node and Singly linked list
In the Node Class a Node of a sinlgy linked list is initialized.
In the Class sinlgy linked list a singly linked list is initialized.
and also a method is provided where the list can be sorted while insertion
of an element
"""


class Node:
    """Class Node"""

    def __init__(self, data=0, next_node=None):
        """Initialize a Node object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property checker for Data to be stored inside a Node object"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """property checker for next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if isinstance(value, Node) is not True and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class Singly linked list"""
    def __init__(self):
        """Initialization of singly linked list"""
        self.__head = Node()

    def sorted_insert(self, value):
        """Object Method to implement sorted insert"""
        if self.__head.next_node is None:
            self.__head.next_node = Node(value, None)
        else:
            temp = self.__head.next_node
            temp1 = self.__head
            while temp is not None and temp.data < value:
                temp1 = temp
                temp = temp.next_node

            new_node = Node(value, temp)
            temp1.next_node = new_node

    def __repr__(self):
        """Makes the List printable"""
        out_put = ""
        temp2 = self.__head.next_node
        while temp2 is not None:
            out_put += str(temp2.data) + '\n'
            temp2 = temp2.next_node
        return out_put[:-1]
