class Solution:
    class Node:
        def __init__(self,value, left=None, right=None):
            self.value = value
            self.left = left 
            self.right = right
        
    def constructTree(self,a_list):
        if not a_list:
            return None
        root = None
        for num in a_list:
            root = self.insert(root, num)
        return root
    def insert(self, root, value):
        if root == None:
            node = self.Node(value)
            return node
        if root.value >= value:
            old_left = root.left
            ret_node = self.insert(root.left, value)
            if old_left is None:
                root.left = ret_node
        else:
            old_right = root.right
            ret_node = self.insert(root.right,value)
            if old_right is None:
                root.right = ret_node
        return root

    def in_order_traversal(self, root):
        if root.left is not None:
            self.in_order_traversal(root.left)
        print(root.value)
        if root.right is not None:
            self.in_order_traversal(root.right)        

#a_list = [4,6,2,7,1,77,222]
a_list =[1,2]
solution = Solution()

solution.in_order_traversal(solution.constructTree(a_list))