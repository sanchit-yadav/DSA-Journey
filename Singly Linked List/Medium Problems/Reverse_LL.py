# Problem : Given the head of a singly linked list, reverse the list, and return the reversed list.

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


    def ReverseList(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example Usage
if __name__ == "__main__":
    SLL = LinkedList()
    SLL.append(10)
    SLL.append(20)
    SLL.append(30)
    SLL.append(40)
    SLL.traverse()
    SLL.ReverseList(SLL.head)
    SLL.traverse()
