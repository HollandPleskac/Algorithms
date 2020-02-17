#binary trees

binary_tree = [8, 5, 4, 9, 7, None, 11, None, None, 1, 12, None, None, 3, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None]

#accessing value of the left child of the node with index 4
def value_of_left_child(tree, node_index):
    return tree[2 * node_index + 1]
value_of_left_child(binary_tree, 4)

#accessing value of the right child of the node with index 4
def value_of_right_child(tree, node_index):
    return tree[2 * node_index + 2]
value_of_right_child(binary_tree, 4)

#deleting the value of the left child of the node with index 4
i = 4
binary_tree[2 * i + 1] = None

#deleting the value of the right child of the node with index 4
i = 4
binary_tree[2 * i + 2] = None
