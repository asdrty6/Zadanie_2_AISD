class AVLNode:
    def __init__(self, value):
        # Inicjalizacja węzła AVL z wartością i pustymi wskaźnikami
        self.value = value
        self.left = None
        self.right = None

class AVL:
    def __init__(self):
        # Inicjalizacja pustego drzewa AVL
        self.root = None
    
    def build_from_sorted_array(self, arr):
        # Budowa zrównoważonego drzewa metodą połowienia binarnego
        self.root = self._build_recursive(arr)

    def _build_recursive(self, arr):
        # Rekurencyjne wyznaczanie mediany i budowanie poddrzew
        if not arr:
            return None
        
        mid = len(arr) // 2
        node = AVLNode(arr[mid])
        
        node.left = self._build_recursive(arr[:mid])
        node.right = self._build_recursive(arr[mid + 1:])
        
        return node

    def find_min(self):
        # Znajduje najmniejszą wartość i zwraca ścieżkę poszukiwań
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
        # Znajduje największą wartość i zwraca ścieżkę poszukiwań
        if self.root is None:
            return None, []
        current = self.root
        path = []
        while current.right is not None:
            path.append(current.value)
            current = current.right
        path.append(current.value)
        return current.value, path

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

    def delete_tree_post_order(self):
        # Usuwa całe drzewo metodą post-order
        self._delete_post_order_recursive(self.root)
        self.root = None

    def _delete_post_order_recursive(self, node):
        # Rekurencyjne usuwanie węzłów
        if node:
            self._delete_post_order_recursive(node.left)
            self._delete_post_order_recursive(node.right)
            print(f"Deleting AVL node: {node.value}")