import sys

class Node:
    def __init__(self, key, value=None) -> None:
        self.left = None
        self.right = None
        self.key = key
        self.value = [] if not value else value

def insert(root, key, value) -> Node:
    if root is None:
        return Node(key, [value])
    else:
        if root.key == key:
            root.value.append(value)
            return root
        elif root.key < key:
            root.right = insert(root.right, key, value)
        else:
            root.left = insert(root.left, key, value)
    return root

def create_tree(array:list, tree=None) -> Node:
    if not array:
        return tree
    array_set = list(set(array))
    item = array_set[0]
    new_set = [item]*(len(array_set)-1)
    array_set.remove(item)
    pairs = zip(new_set,array_set)
    if not tree:
        tree = Node(item)
    for pair in pairs:
        tree = insert( tree, sum(pair), pair)
    return create_tree(array_set, tree=tree) 
        

def search_pairs_by_result(tree, key):
    if tree is None or tree.key == key:
        return tree
 
    if tree.key < key:
        return search_pairs_by_result(tree.right,key)
   
    return search_pairs_by_result(tree.left,key)
        

    
def found_pairs_by_number(array,number):
    tree = create_tree(array)
    result = search_pairs_by_result(tree,number)
    return result.value if result else []


if __name__ == "__main__":
    numbers, number = sys.argv[1:]
    numbers = list(map(int,numbers.split(",")))
    number = int(number)
    print(found_pairs_by_number(numbers, number))