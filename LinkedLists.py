class Element:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def append(self, new_element):
        if self.head==None:
            self.head = new_element
            return
            
        else:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
            cur.next = new_element  
            
    #This function is added by me so I can use in the other functions    
    def length(self):
        cur = self.head
        total = 1
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def get_position(self, position):
        if position>self.length():
            print ("Error: Position out of range")
            return None
        else:
            cur_position=1
            cur_element=self.head
        while True:
            if cur_position==position:
                return cur_element
            cur_position+=1
            cur_element=cur_element.next
            
    def insert(self, new_element, position):
        prev_node = self.head
        if position == 1:
            new_node = new_element
            new_node.next = head
            return 
        
        while prev_node is not None:
            new_node = new_element
            
            for _ in range(position-2): 
                prev_node = prev_node.next
            
            new_node.next = prev_node.next
            prev_node.next = new_node
            return self.head

        
        
    def delete(self, data):
        
        cur_node = self.head
        
        if cur_node and cur_node.data==data:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next
            
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
            

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
llist = LinkedList()
llist.append(e1)
llist.append(e2)
llist.append(e3)

# Test if appends were correct
# Should be 3
print(llist.head.next.next.data)

# Test get_position
# Should also be 3
print(llist.get_position(3).data)

# Test insert
llist.insert(e4,3)
# Should print 4 now
print(llist.get_position(3).data)

# Test delete
llist.delete(1)
# Should print 2 now
print(llist.get_position(1).data)
# Should print 4 now
print(llist.get_position(2).data)
# Should print 3 now
print(llist.get_position(3).data)