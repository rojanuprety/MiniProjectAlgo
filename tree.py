class TreeNode:
    def __init__(self, root_value):
        self.value = root_value
        self.right = None
        self.left = None


def buildTree(preorder, inorder):
    preorder_index = 0
    idx = 0
    tree_array = list()

    def array_to_tree(left, right):
        nonlocal preorder_index
        nonlocal tree_array
        # if there are no elements to construct the tree
        if left > right:
            return None

        # select the preorder_index element as the root and increment it
        root_value = preorder[preorder_index]
        root = TreeNode(root_value)

        preorder_index += 1

        # build left and right subtree
        # excluding inorder_index_map[root_value] element because it's the root
        root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
        root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

        return root

    # build a hashmap to store value -> its index relations
    inorder_index_map = {}
    for index, value in enumerate(inorder):
        inorder_index_map[value] = index

    return array_to_tree(0, len(preorder) - 1)


def printInorder(tree):
	if tree is None:
		return
	
	printInorder(tree.left)
	
	print (tree.value,end=' ')

	printInorder(tree.right)

def printPostorder(tree):

    if tree:
        printPostorder(tree.left)
        printPostorder(tree.right)
        print(tree.value, end=" ")


if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 9, 5, 3, 6, 8]
    inorder = [7, 9, 4, 2, 5, 1, 3, 6, 8]
    tree = buildTree(preorder, inorder)

    print ("Post Order Traversal of contructed tree is")
    post_order_traversal = printPostorder(tree)
    print()
    print ("In Order Traversal of contructed tree is")
    pre_order_traversal = printInorder(tree)
