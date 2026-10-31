# We'll perform basic operations on a doubly linked list, such as insertion, deletion, and traversal.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                break
            current = current.next

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_backward(self):
        elements = []
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)

    print("Forward Traversal:", dll.display_forward())
    print("Backward Traversal:", dll.display_backward())

    dll.delete(2)
    print("After Deletion of 2:")
    print("Forward Traversal:", dll.display_forward())
    print("Backward Traversal:", dll.display_backward())