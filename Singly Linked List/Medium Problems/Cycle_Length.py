# Problem : Given the head of a linked list, return the Length of the cycle. If there is no cycle, return null.

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
            while current.next is not None:
                current = current.next
            current.next = new_node

    def cycleLength(self, head: Node) -> int:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected, calculate its length
                length = 1
                current = slow.next
                while current != slow:
                    length += 1
                    current = current.next
                return length

        return 0  # No cycle detected

# Example Usage
if __name__ == "__main__":
    SLL = LinkedList()
    SLL.append(1)
    SLL.append(2)
    SLL.append(3)
    SLL.append(4)
    SLL.append(5)

    # Creating a cycle for testing
    SLL.head.next.next.next.next.next = SLL.head.next.next

    cycle_length = SLL.cycleLength(SLL.head)
    if cycle_length > 0:
        print(f"Cycle length is: {cycle_length}")
    else:
        print("No cycle detected")
        