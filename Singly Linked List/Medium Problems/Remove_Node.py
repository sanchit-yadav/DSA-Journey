# Problem : Given the head of a linked list, remove the nth node from the end of the list and return its head.

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

    def removeNthFromEnd(self, n):
        dummy = Node(0)
        dummy.next = self.head
        first = dummy
        second = dummy

        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next

# Example Usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    n = 2
    out = linked_list.removeNthFromEnd(n)

    current = out
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

