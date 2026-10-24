# Problem : Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

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

    def detectCycle(self, head: Node) -> Node:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

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

    cycle_node = SLL.detectCycle(SLL.head)
    if cycle_node:
        print(f"Cycle starts at node with data: {cycle_node.data}")
    else:
        print("No cycle detected")