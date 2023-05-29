
def minHeightBST(array):
        return constructMinHeightBST(array,None,0,len(array)-1)

#O(Nlog N) time
def constructMinHeightBST(array,bst,startIdx,endIdx):
    if endIdx<startIdx: 
        return
    midIdx = (startIdx+endIdx)//2
    valueToAdd = array[midIdx]

    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    
    constructMinHeightBST(array, bst,startIdx, midIdx-1)
    constructMinHeightBST(array,bst,midIdx+1,endIdx)
    return bst

#O(N) time
def constructMinHeightBST2(array,bst,startIdx,endIdx):
    if endIdx<startIdx: 
        return
    midIdx = (startIdx+endIdx)//2
    newBSTNode = BST(array[midIdx])

    if bst is None:
        bst = newBSTNode
    else:
        if array[midIdx] < bst.value:
            bst.left = newBSTNode
            bst = bst.left
        else:
            bst.right = newBSTNode
            bst=bst.right
    
    constructMinHeightBST2(array, bst,startIdx, midIdx-1)
    constructMinHeightBST2(array,bst,midIdx+1,endIdx)
    return bst

#CleanerCode
def constructMinHeightBST3(array, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx)//2
    bst = BST(array[midIdx])

    bst.left = constructMinHeightBST3(array,startIdx, midIdx-1)
    bst.right = constructMinHeightBST3(array, midIdx+1, endIdx)
    return bst 

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)