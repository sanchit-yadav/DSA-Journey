# Problem : Given head, the head of a linked list, determine if the linked list has a cycle in it.

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
    
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end = " ")
                current = current.next
            print()

    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Example Usage
if __name__ == "__main__":
    SLL = LinkedList()
    SLL.append(1)
    SLL.append(2)
    SLL.append(3)
    SLL.append(4)
    SLL.append(1)
    SLL.traverse()
    print(SLL.hasCycle(SLL.head))
    SLL.traverse()