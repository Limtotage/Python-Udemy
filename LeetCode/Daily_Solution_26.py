class Daily_Solution_26:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def Tree_Builder():
            node=TreeNode(postorder.pop())
            if node.val!=preorder[-1]:
                node.right=Tree_Builder()
            if node.val!=preorder[-1]:
                node.left=Tree_Builder()
            preorder.pop()
            return node
        return Tree_Builder()
