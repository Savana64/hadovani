class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, number):
        n = Node(number)    
        if self.head is None:
            self.head = n
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = n

numbers = input("Zadejte čísla do seznamu oddělená mezerou: ")
number_list = numbers.split(" ")