class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)
    
class BinaryTree:
    def __init__(self, data=None):
        if data:                # se o dado existir 
            node = Node(data)
            self.root = node    # tô falando que a raíz dessa árove é o próprio node
        else:
            self.root = None
        
if __name__ == "__main__":
    tree = BinaryTree(7)        # esse aqui é o meu nó raíz
    tree.root.right = Node(14)  # nó que está à direita da raíz
    tree.root.left = Node(18)   # nó que está à esquerda da raíz
    
    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)
    
    