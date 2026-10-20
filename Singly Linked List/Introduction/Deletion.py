# Problem :Insert a new  node into a singly linked list. Delete a node from a singly linked list at the given position

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def delete_at_position(self, position):
        if not self.head:
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(position - 1):
            if not current.next:
                return
            current = current.next

        if current.next:
            current.next = current.next.next


# Example Usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Original Linked List:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    position_to_delete = 2
    linked_list.delete_at_position(position_to_delete)

    print(f"Linked List after deleting node at position {position_to_delete}:")
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")