from graph import get_graph, print_matrix
from algorithms import (
    dijkstra_single_source,
    n_times_dijkstra,
    floyd_warshall_with_trace,
)

def main() -> None:
    adj_matrix, adj_list, edges_count = get_graph()
    v_count = len(adj_matrix)
    start_node = 0
    print(f" Варіант 15 | Вершин: {v_count}, Ребер: {edges_count}")

    dijkstra_single_source(adj_list, start_node, v_count, trace=True)

    floyd_matrix = floyd_warshall_with_trace(adj_matrix)

    dijkstra_full_matrix = n_times_dijkstra(adj_list, v_count)

    print("\n=== Порівняння повних матриць Дейкстри та Флойда ===")
    print("Повна матриця відстаней (N-разів Дейкстра):")
    print_matrix(dijkstra_full_matrix)

    print("\nПовні матриці відстаней повністю збігаються:", dijkstra_full_matrix == floyd_matrix)


if __name__ == "__main__":
    main()