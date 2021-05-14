class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self._insert(item, self.root)
            
    def _insert(self, item, cur_node):
        if item < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(item)
            else:
                self._insert(item, cur_node.left)
        elif item > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(item)
            else:
                self._insert(item, cur_node.right)
        else:
            print("Value is already in the tree")
        
    
    def find(self, item):
        if self.root:
            is_found = self._find(item, self.root)
            if is_found:
                return True
            return False
        else:
            return None
        
    def _find (self, item, cur_node):
        if item > cur_node.data and cur_node.right:
            return self._find(item, cur_node.right)
        elif item < cur_node.data and cur_node.left:
            return self._find(item, cur_node.left)
        if item == cur_node.data:
            return True
            
tree = Tree()

tree.insert(30)
tree.insert(5)
tree.insert(50)
tree.insert(8)
tree.insert(3)
tree.insert(100)
tree.insert(40)

print(tree.find(8))
print(tree.find(9))


#Why is the worst case time complexity of the find method only  𝑂(𝑛)  and not  𝑂(𝑙𝑜𝑔𝑛) ?
#It is O(n) because in the worst case scenario we have to traverse all elements (n nodes)