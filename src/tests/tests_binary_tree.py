# Traversing Binary Tree in Python
from ..binary_tree.binary_tree import TreeNode

def run_tests():
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