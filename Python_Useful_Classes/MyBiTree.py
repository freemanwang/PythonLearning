import queue
class Node:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

def creatBTree(lst):
    '''
    从列表生成一棵二叉树
    :param lst: 二叉树层序输出的顺序排序的元素，空节点要用None占位
    :return: 树的根节点，root节点
    '''
    if not lst:
        print('做参数的队列非法')
        return
    index = 0
    leng = len(lst)
    root = Node(lst[index])
    index += 1
    que = queue.Queue(-1)
    que.put_nowait(root)
    while index < leng:
        if not que.empty():
            node = que.get_nowait()
        else:
            print('Error，队列空')
        if lst[index] != None:
            node.lchild = Node(lst[index])
            if not que.full():
                que.put_nowait(node.lchild)
            else:
                print('队列满')
        index += 1
        if lst[index] != None:
            node.rchild = Node(lst[index])
            if not que.full():
                que.put_nowait(node.rchild)
            else:
                print('队列满')
        index += 1
    return root

def printTree(root:Node):
    print('---------------------')
    print(f"根节点：{root.data}")
    que = queue.Queue()
    if not que.full():
        que.put_nowait(root)
    else:
        print('队列已满')
    while not que.empty():
        node = que.get_nowait()
        if node.lchild:
            if not que.full():
                que.put_nowait(node.lchild)
            else:
                print('队列已满')
            print(f"{node.data}的左孩子：{node.lchild.data}")
        if node.rchild:
            if not que.full():
                que.put_nowait(node.rchild)
            else:
                print('队列已满')
            print(f"{node.data}的右孩子：{node.rchild.data}")
    print('---------------------')
    return

class Tree:
    def __init__(self, root:Node=None, height:int=0):
        self.root = root
        self.height = height

def printTreeFromList(pRoot):
    if not pRoot:
        return []
    resultList = []
    curLayer = [pRoot]
    while curLayer:
        curList = []
        nextLayer = []
        for node in curLayer:
            curList.append(node)
            if node.lchild:
                nextLayer.append(node.lchild)
            if node.rchild:
                nextLayer.append(node.rchild)
        resultList.append(curList)
        curLayer = nextLayer
    return resultList

def getDepth(tree:Node):
    if tree.data == None:
        return 0
    h1 = 0
    h2 = 0
    if tree.lchild:
        h1 = getDepth(tree.lchild)
    if tree.rchild:
        h2 = getDepth(tree.rchild)
    return max(h1,h2)+1


lst = [1,11,12,111,112,121,122]
tree = creatBTree(lst)
printTree(tree)










