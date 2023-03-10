# Traversing Binary Tree in Python

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # Traverse preorder
    #Root-> Left subtree -> Right subtree
    def traverse_pre_order(self):
        """
        Traverse pre order tree
        1. Visit root node
        2. Visit all the nodes in the left subtree
        3. Visit all the nodes in the right subtree
        """
        print(self.value, end=' ')
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    # Traverse inorder
    #Left subtree -> Root -> Right subtree
    def traverse_in_order(self):
        """
        Traverse in order tree
        1. First, visit all the nodes in the left subtree
        2. Then the root node
        3. Visit all the nodes in the right subtree
        """
        if self.left:
            self.left.traverse_in_order()
        print(self.value, end=' ')
        if self.right:
            self.right.traverse_in_order()

    # Traverse postorder
    #Left subtree-> Right subtree -> Root
    def traverse_post_order(self):
        """
        Traverse post order tree
        1. Visit all the nodes in the left subtree
        2. Visit all the nodes in the right subtree
        3. Visit the root node
        """
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print(self.value, end=' ')

#Test case
''' Construct the following tree (same as in png image Binary-Tree.png)
              1
            /   \
           /     \
          2       3
         / \     / \
        /   \   /   \
       4     5 6     7
'''

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Pre order Traversal: ", end="")
root.traverse_pre_order()
print("\nIn order Traversal: ", end="")
root.traverse_in_order()
print("\nPost order Traversal: ", end="")
root.traverse_post_order()