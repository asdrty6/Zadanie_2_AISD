import sys
import argparse
from bst import BST
from avl import AVL

def export_to_tikz(root, filename="tree.tex"):
    # Eksport struktury drzewa do formatu tikz
    if root is None:
        print("Tree is empty, nothing to export.")
        return

    def recurse(node, indent=""):
        # Rekurencyjna funkcja budująca strukturę węzłów i dzieci
        res = f"node {{{node.value}}}"
        
        if node.left or node.right:
            if node.left:
                res += f"\n{indent}  child {{ {recurse(node.left, indent + '  ')} }}"
            else:
                # Wstawienie pustego dziecka dla zachowania struktury w tikz
                res += f"\n{indent}  child[missing] {{}}"
            
            if node.right:
                res += f"\n{indent}  child {{ {recurse(node.right, indent + '  ')} }}"
                
        return res

    # Składanie pełnego kodu LaTeX
    tikz_code = "\\begin{tikzpicture}\n"
    tikz_code += "[level distance=1.5cm,\n"
    tikz_code += "level 1/.style={sibling distance=3cm},\n"
    tikz_code += "level 2/.style={sibling distance=1.5cm}]\n"
    tikz_code += "\\" + recurse(root, "") + ";\n"
    tikz_code += "\\end{tikzpicture}\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(tikz_code)
    
    print("Exporting to tikzpicture...")
    print(f"Code saved to file: {filename}")
    print("\nGenerated LaTeX code:")
    print(tikz_code)
    print("------------------------------")

def print_help():
    # Wyświetla listę dostępnych komend i ich opisy
    print("Help       Show this message")
    print("Print      Print the tree using In-order, Pre-order, Post-order")
    print("FindMinMax Search for min and max values")
    print("Remove     Remove elements from the tree")
    print("Delete     Delete the entire tree")
    print("Export     Export the tree to tikzpicture (LaTeX)")
    print("Rebalance  Rebalance the tree using DSW algorithm")
    print("Exit       Exits the program (same as Ctrl+D)")

def main():
    # Obsługa argumentów linii komend (wybór typu drzewa)
    parser = argparse.ArgumentParser(description="BST and AVL Tree Constructor")
    parser.add_argument('--tree', choices=['AVL', 'BST'], required=True, help="Tree type: AVL or BST")
    args = parser.parse_args()

    tree_type = args.tree
    tree = AVL() if tree_type == 'AVL' else BST()

    try:
        # Dwuetapowe wczytywanie danych wejściowych
        nodes_input = input("nodes> ").strip()
        if not nodes_input:
            return
        n = int(nodes_input)

        insert_input = input("insert> ").strip()
        # Przygotowanie unikalnych i posortowanych elementów
        raw_elements = list(map(int, insert_input.split()))[:n]
        elements = sorted(list(set(raw_elements))) 

        # Budowa początkowego drzewa
        if tree_type == 'AVL':
            tree.build_from_sorted_array(elements)
            print(f"Sorted: {', '.join(map(str, elements))}")
            mid = elements[len(elements)//2] if elements else None
            print(f"Median: {mid}")
        else:
            print(f"Inserting: {', '.join(map(str, elements))}")
            for val in elements:
                tree.insert(val)

    except EOFError:
        return
    except ValueError:
        print("Error: Invalid input data.")
        return

    # Główna pętla obsługująca komendy użytkownika
    while True:
        try:
            action = input("action> ").strip().lower()
        except EOFError:
            break

        if action == "exit":
            break
        elif action == "help":
            print_help()
        elif action == "export":
            export_to_tikz(tree.root)
        elif action == "print":
            # Wypisanie drzewa w trzech porządkach
            in_order_res = tree.in_order(tree.root)
            post_order_res = tree.post_order(tree.root)
            pre_order_res = tree.pre_order(tree.root)
            print(f"In-order: {', '.join(map(str, in_order_res))}")
            print(f"Post-order: {', '.join(map(str, post_order_res))}")
            print(f"Pre-order: {', '.join(map(str, pre_order_res))}")
        elif action == "findminmax":
            # Wyszukiwanie min i max
            min_val, _ = tree.find_min()
            max_val, _ = tree.find_max()
            if min_val is not None: print(f"Min: {min_val}")
            if max_val is not None: print(f"Max: {max_val}")
            if min_val is None and max_val is None: print("Tree is empty.")
        elif action == "remove":
            # Usuwanie wybranych elementów (tylko dla BST)
            if tree_type == "AVL":
                print("Note: Removing elements is implemented for BST only.")
                continue
            try:
                remove_input = input("remove> ").strip()
                vals_to_remove = list(map(int, remove_input.split()))
                for val in vals_to_remove:
                    tree.remove(val)
            except ValueError:
                print("Error: Invalid value provided.")
        elif action == "delete":
            # Usunięcie całego drzewa
            tree.delete_tree_post_order()
            print("Tree successfully removed")
        elif action == "rebalance":
            # Równoważenie algorytmem DSW
            if tree_type == "BST":
                tree.balance_dsw()
                print("Rebalanced using DSW algorithm.")
            else:
                print("AVL tree is already balanced.")
        elif action == "":
            pass 
        else:
            print("Unknown action. Type 'Help'.")

    print("Program exited with status: 0")

if __name__ == "__main__":
    main()