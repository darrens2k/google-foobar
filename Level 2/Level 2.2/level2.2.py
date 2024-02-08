def solution(h, q):
    
    # given a node, I need to find its parent
    # special case is when the node is the root
    
    # I can create a list of all the nodes in the tree
    nodes = []

    # output list 
    result = []
    for i in range(len(q)):
        result.append(-1)
    
    for i in range(1, 2**(h)):
        nodes.append(i)
    
    # compute total nodes
    total_nodes = 2**(h) - 1
    
    # create a class for nodes
    class Node:
        def __init__(self, value):
            self.value = value 
            self.left_child = None
            self.right_child = None

    # function to locate a node in q
    def locate(value, root):
        for index, item in enumerate(q):
            if item == value:
                result[index] = root.value

    # recursive function to traverse tree
    def traverse(lst, rst, root):
        
        # base case
        if len(lst) == 0:
            return
        
        # start with lst
        temp_root = lst.pop(-1)
        root.left_child = temp_root
        lst2 = lst[:len(lst)//2]
        rst2 = lst[len(lst)//2:]
        locate(temp_root, root)
        temp_root = Node(temp_root)
        traverse(lst2,rst2,temp_root)

        # move to rst
        temp_root2 = rst.pop(-1)
        root.right_child = temp_root2
        lst3 = rst[:len(rst)//2]
        rst3 = rst[len(rst)//2:]
        locate(temp_root2, root)
        temp_root2 = Node(temp_root2)
        traverse(lst3,rst3,temp_root2)

    # begin traversing tree
    def begin_traversal(stack):

        # pop root off
        root = stack.pop(-1)

        # split into right and left subtree
        lst = stack[:len(stack)//2]
        rst = stack[len(stack)//2:]

        # create root of tree
        root = Node(root)
        traverse(lst,rst,root)
        return root

    begin_traversal(nodes)

    return result


print(solution(5,[19, 14, 28]))
