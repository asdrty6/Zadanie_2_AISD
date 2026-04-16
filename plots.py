import csv
import matplotlib.pyplot as plt

def generate_plots():
    N = []
    bst_create, avl_create = [], []
    bst_max, avl_max = [], []
    bst_inorder, avl_inorder = [], []
    bst_dsw = []

    try:
        with open('results_benchmark.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                N.append(int(row['N']))
                bst_create.append(float(row['BST_Creation']))
                avl_create.append(float(row['AVL_Creation']))
                bst_max.append(float(row['BST_FindMax']))
                avl_max.append(float(row['AVL_FindMax']))
                bst_inorder.append(float(row['BST_InOrder']))
                avl_inorder.append(float(row['AVL_InOrder']))
                bst_dsw.append(float(row['BST_DSW']))
    except FileNotFoundError:
        print("Error: File 'results_benchmark.csv' not found. Please run benchmark.py first.")
        return

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Zależność czasu operacji na drzewach od liczby elementów - t=f(n)', fontsize=16)

    axs[0, 0].plot(N, bst_create, marker='o', label='BST (wstawianie iteracyjne)', color='red')
    axs[0, 0].plot(N, avl_create, marker='s', label='AVL (połowienie)', color='blue')
    axs[0, 0].set_title('1. Czas tworzenia struktury')
    axs[0, 0].set_xlabel('Liczba elementów (n)')
    axs[0, 0].set_ylabel('Czas (s)')
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    axs[0, 1].plot(N, bst_max, marker='o', label='BST (zdegenerowane)', color='red')
    axs[0, 1].plot(N, avl_max, marker='s', label='AVL (zbalansowane)', color='blue')
    axs[0, 1].set_title('2. Czas wyszukiwania maksimum')
    axs[0, 1].set_xlabel('Liczba elementów (n)')
    axs[0, 1].set_ylabel('Czas (s)')
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    axs[1, 0].plot(N, bst_inorder, marker='o', label='BST', color='red')
    axs[1, 0].plot(N, avl_inorder, marker='s', label='AVL', color='blue')
    axs[1, 0].set_title('3. Czas wypisywania in-order')
    axs[1, 0].set_xlabel('Liczba elementów (n)')
    axs[1, 0].set_ylabel('Czas (s)')
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    axs[1, 1].plot(N, bst_dsw, marker='o', label='DSW (dla zdegenerowanego BST)', color='green')
    axs[1, 1].set_title('4. Czas równoważenia algorytmem DSW')
    axs[1, 1].set_xlabel('Liczba elementów (n)')
    axs[1, 1].set_ylabel('Czas (s)')
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    output_filename = 'tree_operations_plots.png'
    plt.savefig(output_filename, dpi=300)
    print(f"Plots generated and saved to: {output_filename}")
    
    try:
        plt.show()
    except Exception:
        pass

if __name__ == "__main__":
    generate_plots()