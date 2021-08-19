def main():
    linked_list = LinkedList(Node(3))
    print_linked_list(linked_list)

    linked_list.append(4)
    linked_list.append(5)

    print_linked_list(linked_list)

    linked_list.prepend(2)
    linked_list.prepend(1)

    print_linked_list(linked_list)

    linked_list.delete_node_with_data(3)

    print_linked_list(linked_list)


def print_linked_list(linked_list):
    if (linked_list.head == None):
        print("List is empty")
        return

    list_values = []
    current = linked_list.head
    while(current != None):
        list_values.append(current.data)
        current = current.next

    print(list_values)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Append at the end of the list
    def append(self, data):
        if (self.head == None): self.head = Node(data)

        current = self.head
        while(current.next != None):
            current = current.next
        current.next = Node(data)

    # Append to start of the list
    def prepend(self, data):
        if(self.head == None): self.head = Node(data)

        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head


    # Delete data
    def delete_node_with_data(self, data):
        # Special cases
        if(self.head == None): return

        if(self.head.data == data):
            if (self.head.next == None):
                self.head = None
                return
            self.head = self.head.next
            return

        current = self.head
        while(current.next != None):
            if (current.next.data == data):
                current.next = current.next.next
            current = current.next

if __name__ == "__main__":
    main()


