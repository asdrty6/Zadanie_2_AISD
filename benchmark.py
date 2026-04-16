import time
import csv
import sys
from bst import BST
from avl import AVL

sys.setrecursionlimit(20000)

def run_benchmark():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    results = []

    print("Starting benchmark (4 trials for each N)...")

    for n in sizes:
        arr = list(range(1, n + 1))
        
        t_bst_create = 0.0
        t_avl_create = 0.0
        t_bst_max = 0.0
        t_avl_max = 0.0
        t_bst_inorder = 0.0
        t_avl_inorder = 0.0
        t_bst_dsw = 0.0

        for _ in range(4):
            bst = BST()
            start = time.perf_counter()
            for val in arr:
                bst.insert(val)
            t_bst_create += (time.perf_counter() - start)

            avl = AVL()
            start = time.perf_counter()
            avl.build_from_sorted_array(arr)
            t_avl_create += (time.perf_counter() - start)

            start = time.perf_counter()
            bst.find_max()
            t_bst_max += (time.perf_counter() - start)

            start = time.perf_counter()
            avl.find_max()
            t_avl_max += (time.perf_counter() - start)

            start = time.perf_counter()
            bst.in_order(bst.root)
            t_bst_inorder += (time.perf_counter() - start)

            start = time.perf_counter()
            avl.in_order(avl.root)
            t_avl_inorder += (time.perf_counter() - start)

            start = time.perf_counter()
            bst.balance_dsw()
            t_bst_dsw += (time.perf_counter() - start)

        results.append([
            n, 
            t_bst_create / 4, 
            t_avl_create / 4, 
            t_bst_max / 4, 
            t_avl_max / 4, 
            t_bst_inorder / 4, 
            t_avl_inorder / 4, 
            t_bst_dsw / 4
        ])
        print(f"Completed measurements for N = {n}")

    filename = 'results_benchmark.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "N", 
            "BST_Creation", "AVL_Creation", 
            "BST_FindMax", "AVL_FindMax", 
            "BST_InOrder", "AVL_InOrder", 
            "BST_DSW"
        ])
        writer.writerows(results)
    
    print(f"Results saved to file: {filename}")

if __name__ == "__main__":
    run_benchmark()