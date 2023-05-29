class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return validateBSTHelper(tree, float("-inf"),float("inf"))

def validateBSTHelper(tree, minvalue, maxvalue):
	if tree is None:
		return True
	if tree.value < minvalue or tree.value >= maxvalue:
		return False
	leftIsValid = validateBSTHelper(tree.left, minvalue, tree.value)
	return leftIsValid and validateBSTHelper(tree.right,tree.value, maxvalue)