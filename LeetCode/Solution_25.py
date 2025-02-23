class Solution_25:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def Builder_Tree():
            node = TreeNode(postorder.pop())
            if node.val != preorder[-1]:
                node.right= Builder_Tree()
            if node.val != preorder[-1]:
                node.left= Builder_Tree()
            preorder.pop()
            return node
        return Builder_Tree()
