import math

class Node:
    def __init__(self, value):
        # Inicjalizacja węzła z wartością i pustymi dziećmi
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # Inicjalizacja pustego drzewa BST
        self.root = None

    def insert(self, value):
        # Iteracyjne wstawianie nowego elementu do drzewa
        if self.root is None:
            self.root = Node(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right
            else:
                break

    def in_order(self, node, result=None):
        # Przejście drzewa w porządku in-order (L-W-P)
        if result is None:
            result = []
        if node:
            self.in_order(node.left, result)
            result.append(node.value)
            self.in_order(node.right, result)
        return result

    def pre_order(self, node, result=None):
        # Przejście drzewa w porządku pre-order (W-L-P)
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)
        return result

    def post_order(self, node, result=None):
        # Przejście drzewa w porządku post-order (L-P-W)
        if result is None:
            result = []
        if node:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.value)
        return result
    
    def find_min(self):
        # Znajduje najmniejszą wartość (idąc maksymalnie w lewo)
        if self.root is None:
            return None, []
        current = self.root
        path = []
        while current.left is not None:
            path.append(current.value)
            current = current.left
        path.append(current.value)
        return current.value, path

    def find_max(self):
        # Znajduje największą wartość (idąc maksymalnie w prawo)
        if self.root is None:
            return None, []
        current = self.root
        path = []
        while current.right is not None:
            path.append(current.value)
            current = current.right
        path.append(current.value)
        return current.value, path

    def remove(self, key):
        # Usuwa węzeł o podanym kluczu
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, root, key):
        # Pomocnicza funkcja rekurencyjna do usuwania węzła
        if root is None:
            return root
        
        if key < root.value:
            root.left = self._delete_node(root.left, key)
        elif key > root.value:
            root.right = self._delete_node(root.right, key)
        else:
            # Przypadek: węzeł z jednym dzieckiem lub bez dzieci
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Przypadek: węzeł z dwoma dziećmi (następca in-order)
            temp = self._min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete_node(root.right, temp.value)
            
        return root

    def _min_value_node(self, node):
        # Znajduje węzeł o najmniejszej wartości w danym poddrzewie
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_tree_post_order(self):
        # Usuwa całe drzewo metodą post-order (wymóg z zadania)
        self._delete_post_order_recursive(self.root)
        self.root = None 

    def _delete_post_order_recursive(self, node):
        # Rekurencyjne usuwanie węzłów z logowaniem operacji
        if node:
            self._delete_post_order_recursive(node.left)
            self._delete_post_order_recursive(node.right)
            print(f"Deleting node: {node.value}") 

    def balance_dsw(self):
        # Algorytm Day-Stout-Warren do równoważenia drzewa
        if self.root is None:
            return

        pseudo_root = Node(0)
        pseudo_root.right = self.root
        tmp = pseudo_root
        
        # Faza 1: Tworzenie kręgosłupa (prostowanie drzewa)
        node_count = 0
        while tmp.right is not None:
            if tmp.right.left is not None:
                # Rotacja w prawo
                old_tmp_right = tmp.right
                tmp.right = old_tmp_right.left
                old_tmp_right.left = tmp.right.right
                tmp.right.right = old_tmp_right
            else:
                tmp = tmp.right
                node_count += 1
        
        # Faza 2: Kompresja (rotacje w lewo tworzące zbalansowane drzewo)
        expected_leaves = node_count + 1 - 2 ** int(math.log2(node_count + 1))
        self._compress(pseudo_root, expected_leaves)
        
        leaves = node_count - expected_leaves
        while leaves > 1:
            leaves //= 2
            self._compress(pseudo_root, leaves)
            
        self.root = pseudo_root.right

    def _compress(self, pseudo_root, count):
        # Pomocnicza seria rotacji w lewo dla algorytmu DSW
        tmp = pseudo_root
        for _ in range(count):
            old_tmp_right = tmp.right
            tmp.right = old_tmp_right.right
            old_tmp_right.right = tmp.right.left
            tmp.right.left = old_tmp_right
            tmp = tmp.right