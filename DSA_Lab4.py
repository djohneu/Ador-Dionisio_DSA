class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        """Display all nodes in the linked list"""
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_beginning(self):
        """Remove and return the data at the beginning"""
        if not self.head:
            return None  
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_at_end(self):
        """Remove and return the data at the end"""
        if not self.head:
            return None  

        # for only one node
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data

        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data

    def remove_at(self, data):
        """Remove node containing 'data' and return it, else return None"""
        if not self.head:
            return None  

        # If head is to be removed
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data

        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                return removed_data
            current = current.next

        return None  # if the data not found

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    ll.display()

    print("Removed from beginning:", ll.remove_beginning())
    ll.display()

    print("Removed from end:", ll.remove_at_end())
    ll.display()

    print("Removed specific (20):", ll.remove_at(20))
    ll.display()

    print("Removed specific (99):", ll.remove_at(99))  # if not found
