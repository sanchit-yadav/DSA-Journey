# Problem : Given the head of a doubly Linked List and a key x . Delete all occurrences of the given key x if it is present and return the new DLL.

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

    def remove_occurrences(self, x):
        current = self.head
        while current:
            if current.data == x:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Update head if the first node is to be deleted
                if current.next:
                    current.next.prev = current.prev
            current = current.next

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(2)
    dll.append(4)
    dll.append(2)
    dll.append(5)

    print("Original List:", dll.display_forward())
    x = 2
    dll.remove_occurrences(x)
    print(f"List after removing occurrences of {x}:", dll.display_forward())