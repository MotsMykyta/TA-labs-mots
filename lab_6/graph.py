import math
from typing import Dict, List, Tuple


def get_graph() -> Tuple[List[List[float]], Dict[int, List[Tuple[int, float]]], int]:
    v_count = 8
    adj_matrix = [[0.0 if i == j else math.inf for j in range(v_count)] for i in range(v_count)]
    adj_list: Dict[int, List[Tuple[int, float]]] = {i: [] for i in range(v_count)}

    # Неорієнтовані ребра у 0-індексації: (u - 1, v - 1, вага)
    edges = [
        (0, 1, 8),  # 1 - 2 (вага 8)
        (0, 2, 2),  # 1 - 3 (вага 2)
        (0, 3, 4),  # 1 - 4 (вага 4)
        (0, 4, 3),  # 1 - 5 (вага 3)
        (1, 4, 6),  # 2 - 5 (вага 6)
        (1, 5, 3),  # 2 - 6 (вага 3)
        (2, 3, 6),  # 3 - 4 (вага 6)
        (2, 5, 7),  # 3 - 6 (вага 7)
        (2, 7, 4),  # 3 - 8 (вага 4)
        (3, 4, 1),  # 4 - 5 (вага 1)
        (4, 6, 4),  # 5 - 7 (вага 4)
        (5, 6, 3),  # 6 - 7 (вага 3)
        (5, 7, 1),  # 6 - 8 (вага 1)
        (6, 7, 5),  # 7 - 8 (вага 5)
    ]

    for u, v, weight in edges:
        w = float(weight)
        adj_matrix[u][v] = w
        adj_matrix[v][u] = w
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    for u in adj_list:
        adj_list[u].sort()

    return adj_matrix, adj_list, len(edges)


def print_matrix(matrix: List[List[float]]) -> None:
    v_count = len(matrix)
    header = "     " + " ".join(f"{j + 1:>4}" for j in range(v_count))
    print(header)
    print("    " + "-" * (5 * v_count))

    for i, row in enumerate(matrix):
        row_str = " ".join(f"{'∞':>4}" if val == math.inf else f"{int(val):>4}" for val in row)
        print(f"{i + 1:>2} | {row_str}")