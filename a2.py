class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_k_distance_node_down(root,k ):
    if root is None or k < 0:
        return
    
    if k == 0:
        print(root.data, end=' ')
        return
    
    print_k_distance_node_down(root.left, k-1)
    print_k_distance_node_down(root.right, k-1)

def print_k_distance_nodes(root, target,k ):
    if root is None:
        return -1
    
    if root == target:
        print(f"Nodes at distance {k} from target {target.data}: ")
        print_k_distance_node_down(root,k)
        return 0
    
    dl = print_k_distance_nodes(root.left, target,k)

    if dl != -1:
        if dl + 1 == k:
            print(root.data,end=' ')
        else:
            print_k_distance_node_down(root.right,k - dl - 2)
        return 1 + dl
    dr = print_k_distance_nodes(root.right, target, k)
    if dr != -1:
        if dr +1 == k:
            print(root.data, end=' ')
        else:
            print_k_distance_node_down(root.left, k-dr -2)
        return 1 + dr
        
    return -1
def main():
    root = Node(28)
    root.left = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    target = root.left.right
    k = 2

    print(f"Nodes at distance {k} from target node {target.data}: ")
    print_k_distance_nodes(root, target, k)
    print()

if __name__ == "__main__":
    main()