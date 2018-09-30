class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def length_list(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            length += 1
        return length

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def insert_first(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
            del temp_node
    def insert_at(self,new_node, position):
        if position <0 or position > self.length_list():
            print("Linked link position is not valid")
        if position == 0:
            self.insert_first(new_node)
            return
        current_node = self.head
        current_position = 0
        while current_position != position:
            previous_node = current_node
            current_node = current_node.next
            current_position+=1
        previous_node.next = new_node
        new_node.next = current_node


    def print_list(self):
        if self.head is None:
            print("List is Empty")
            return
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next


first_node = Node("Adam")
linked_list = LinkedList()
linked_list.insert_end(first_node)
second_node = Node("John")
linked_list.insert_end(second_node)
fourth_node = Node("Neiman")
linked_list.insert_at(fourth_node,2)
linked_list.print_list()
length = linked_list.length_list()
print(length)
