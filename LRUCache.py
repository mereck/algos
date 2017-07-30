# a node in a doubly-linked list
class Node():
    
    def __init__ (self, val=0, key=0, p=None, n=None):
        self.val = val
        self.key = key
        self.p = p
        self.n = n

#O(n) put and get LRUCache using a doubly-linked list and a hash table
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.storage = {} 
        
        self.head = Node() 
        self.tail = Node()
        
        self.head.p = self.tail
        self.head.n = self.tail
        
        self.tail.n = self.head
        self.tail.p = self.head
        
        

    # adds node to end of list
    def _add(self, c=None, v=0, k=0):
        
        tmp = self.tail.p 
        tmp.n = c
        c.p = tmp
        c.n = self.tail
        self.tail.p = c
        return c
    
    # removes node, returning the removed node
    def _rem(self, k):
        n = self.storage[k]
        n.p.n = n.n # this node's previous.next = this node's next
        n.n.p = n.p # this node's next.previous = this node's previous
        return n
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.storage:
            self._updateAge(key)
            return self.storage[key].val
        else:
            return -1
            

    #removes the node at key from list and adds it at the end, to indicate younger age
    def _updateAge(self, key, val=None):
        p = self._rem(key)
        n = self._add(p)
        n.val = val if val is not None else n.val
        self.storage[key] = n
        return n
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.storage:
            n = self._updateAge(key, value)
        elif len(self.storage) >= self.c: #out of capacity, invalidate oldest
            oldest = self.head.n # because we add nodes at tail, node next to the head is the oldest item in cache
            self._rem(oldest.key)
            del self.storage[oldest.key]
            n = self._add(Node(value, key))
            self.storage[key] = n
        else: # still have capacity for a new value
            n = self._add(Node(value, key))
            self.storage[key] = n