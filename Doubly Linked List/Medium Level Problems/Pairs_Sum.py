# Problem : Given a sorted doubly linked list containing distinct positive integers and an integer target, find all pairs of nodes whose values add up to target.

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

    def find_pairs_with_sum(self, target):
        pairs = []
        left = self.head
        right = self.head

        # Move right pointer to the end of the list
        while right.next:
            right = right.next

        while left and right and left != right and left.prev != right:
            current_sum = left.data + right.data
            if current_sum == target:
                pairs.append((left.data, right.data))
                left = left.next
                right = right.prev
            elif current_sum < target:
                left = left.next
            else:
                right = right.prev

        return pairs

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
    dll.append(4)
    dll.append(5)

    print("Original List:", dll.display_forward())
    target = 5
    pairs = dll.find_pairs_with_sum(target)
    print(f"Pairs with sum {target}:", pairs)