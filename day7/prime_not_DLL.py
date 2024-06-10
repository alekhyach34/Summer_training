class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    def count_primes_recursive(self, t=None):
        if not t:
            t = self.head
        if not t:
            return 0
        if self.is_prime(t.next):
            return 1 + self.count_primes_recursive(t.next)
        return self.count_primes_recursive(t.next)
    def is_prime(self, number, i=2):
        if number < 2:
            return False
        if i * i > number:
            return True
        if number % i == 0:
            return False
        i+=1
        return self.is_prime(number, i + 1)
dllist = DoublyLinkedList()
dllist.insert_at_beginning(4)
dllist.insert_at_beginning(3)
dllist.insert_at_beginning(2)
dllist.insert_at_beginning(1)
prime_count = dllist.count_primes_recursive()

