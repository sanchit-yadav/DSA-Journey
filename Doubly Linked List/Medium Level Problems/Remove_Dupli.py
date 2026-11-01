# Problem : Given a doubly linked list of n nodes sorted by values, remove duplicate nodes present in the linked list.

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

    def remove_duplicates(self):
        if not self.head:
            return

        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                # Skip the duplicate node
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
            else:
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
    dll.append(2)
    dll.append(3)
    dll.append(3)
    dll.append(4)

    print("Original List:", dll.display_forward())
    dll.remove_duplicates()
    print("List after removing duplicates:", dll.display_forward())