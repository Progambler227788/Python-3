# Node class to hold data about node and its leaf nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Binary Search Tree class
class BinaryTree:
    # Constructor to intialize root node with None value currently
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None
  
   # Create a node using Node constructor
    def create_node(self, data):
        return Node(data)
    
    # Insert a node in BST either at root or inside root by recursively finding a place
    def insert(self, data):
        new_node = self.create_node(data)
        if self.is_empty():
            self.root = new_node
        else:
            self._insert_recursively(self.root, new_node)
    
    # Insert a node recursively

    def _insert_recursively(self, current_node, new_node):
        # Like if data of node is 3 <  current node data is 5
        if new_node.data < current_node.data:
            # Then, if its left node is empty insert at left
            if current_node.left == None:
                current_node.left = new_node
            # If left node is not empty, then compare data of new node with respect to left node data in further recursive calls
            else:
                self._insert_recursively(current_node.left, new_node)
        else:
            # If Right Node is none, then new node will be right leaf of current node
            if current_node.right == None:
                current_node.right = new_node
            # Else iterate recursively for right nodes
            else:
                self._insert_recursively(current_node.right, new_node)
    
    # Search for a node with its data
    def search(self, data):
        return self._search_recursively(self.root, data)
    
    # Searching Recursively
    def _search_recursively(self, current_node, data):
        if current_node == None: # In case no node is found, return false
            return False
        if data == current_node.data: # In case node is found, return True
            return True
        if data < current_node.data: # If node data is less than current node data then it will be in left subtree
            return self._search_recursively(current_node.left, data)
        else:  # else in right subtree
            return self._search_recursively(current_node.right, data)
    
    # To print data of a tree, in order traversel is used that gives sorted data when printed
    def traverse_in_order(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, current_node, result):
        if current_node != None:
            self._in_order(current_node.left, result)
            result.append(current_node.data)
            self._in_order(current_node.right, result)
     
    # Function to delete a node from binary search tree
    def delete(self, data):
        if self.is_empty(): # In case tree is empty, just simply terminate function with return
            return
        else:
            self.root = self._delete_recursively(self.root, data)

    def _delete_recursively(self, current_node, data):
        if current_node == None: # In case node is empty, return none
            return current_node
        if data < current_node.data: # Check at left subtree
            current_node.left = self._delete_recursively(current_node.left, data)
        elif data > current_node.data: # Now at right subtree
            current_node.right = self._delete_recursively(current_node.right, data)
        else: # In case of equal node,
            if current_node.left == None:
                return current_node.right # In case node has no left leaf node, then right leaf node will take its place
            elif current_node.right == None: # Else left will take its place
                return current_node.left
            current_node.data = self._find_min_value(current_node.right) # in case of two leaf nodes, find node at left of right node till not empty
            current_node.right = self._delete_recursively(current_node.right, current_node.data)
        return current_node

    def _find_min_value(self, current_node): # Function to find deepest left node
        min_value = current_node.data
        while current_node.left != None:
            min_value = current_node.left.data
            current_node = current_node.left
        return min_value

# Functional main function to test the BinaryTree ADT
def main():
    # Create a binary tree
    tree = BinaryTree()

    # Insert elements into the tree
    elements = [9, 2, 16, 4, 10, 23, 39, 14, 26, 15]
    for element in elements: # insert each element
        tree.insert(element)

    # Search for an element in the tree
    print("Searching for element 10:", tree.search(15))

    # Traverse the tree in-order
    print("In-order traversal of the tree:", tree.traverse_in_order())

    # Delete an element from the tree
    tree.delete(10)
    print("After deleting element 10, in-order traversal of the tree:", tree.traverse_in_order())

if __name__ == "__main__":
    main()
