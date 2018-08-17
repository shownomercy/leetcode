class UniversalTree():
    """
    a universal value tree is a tree with all node having the same value
    
    the idea is to return as much information as possible for one recursive call
    for instance in this case, not only return the count of universal tree for the current root,
    but also return if the current root is a universal tree, should not be that hard.

    Returns:
        [type] -- [description]
    """

    def Solution(root):
        """
        a_list is a list of node instances
        """

        def helper(root):
            """
            helper function to return two values:
            1.if this root itself is a universal tree
            2.how many unversal tree does it contain

            """
            if root is None: return (0, True)
            left_unival, left_count = helper(root.left)
            right_unival, right_count = helper(root.right)
            is_univeral = True
            if root.left is not None and root.left.val != root.val:
                is_univeral = False
            elif root.right is not None and root.right.val != root.val:
                is_univeral = False
            elif not left_unival or not right_unival:
                is_univeral = False
            if is_univeral:
                return left_count + right_count + 1
            else:
                return left_count + right_count

        _, ret = helper(root)
        return ret


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
