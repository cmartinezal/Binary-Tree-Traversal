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