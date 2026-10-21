# Problem : Basic tasks of Singly Linked List Like: Append, Insertion, Deletion, Traversal

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


    def InsertAt(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, data):
        temp = self.head
        if temp.next is not None:
            if temp.data == data:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.data == data:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")


# Example Usage
if __name__ == "__main__":
    SLL = LinkedList()
    SLL.append(10)
    SLL.append(20)
    SLL.append(30)
    SLL.append(1)
    SLL.traverse()
    SLL.InsertAt(40,3)
    SLL.traverse()
    SLL.delete(1)
    SLL.traverse()