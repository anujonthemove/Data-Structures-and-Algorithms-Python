class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and link/pointer to the next node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of a linked list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next
        return "->".join(nodes)

    def is_empty(self):
        return self.head

    def size(self):
        """
        Returns the number of nodes in a list
        Takes O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def add_node_at_head(self, data):
        """
        Adds a new node containing data at the head of the list
        This operation takes O(1) or constant time
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_node_at_tail(self, data):
        node = Node(data)

        current = self.head

        while current:
            current = current.next
        current.next = node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the Node or None if not found
        Takes O(n) time
        """

        current = self.head
        idx = -1
        count = 0
        while current:
            if current.data == key:
                idx = count
            count += 1

            current = current.next
        return idx
