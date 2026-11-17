import heapq
import math
from typing import Dict, List, Tuple
from graph import print_matrix


def reconstruct_path(pred: List[int], start_node: int, target_node: int) -> str:
    if pred[target_node] == -1 and target_node != start_node:
        return "шляху немає"

    path = []
    curr = target_node
    while curr != -1:
        path.append(str(curr + 1))
        curr = pred[curr]

    return " -> ".join(reversed(path))


def dijkstra_single_source(
    adj_list: Dict[int, List[Tuple[int, float]]],
    start_node: int,
    v_count: int,
    trace: bool = False
) -> Tuple[List[float], List[int]]:
    distances = [math.inf] * v_count
    pred = [-1] * v_count
    distances[start_node] = 0.0

    # Мін-купа зберігає пари (поточна_відстань, вершина)
    priority_queue = [(0.0, start_node)]
    step = 0

    if trace:
        print(f"\n=== Покроковий хід алгоритму Дейкстри (старт: вершина {start_node + 1}) ===")
        print("Ініціалізація:")
        print("  dist:", ["∞" if d == math.inf else int(d) for d in distances])
        print("  pred:", ["-" if p == -1 else p + 1 for p in pred])

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        if current_dist > distances[u]:
            continue

        step += 1
        changes = []

        for v, weight in adj_list[u]:
            distance_through_u = current_dist + weight
            if distance_through_u < distances[v]:
                old_val = "∞" if distances[v] == math.inf else int(distances[v])
                distances[v] = distance_through_u
                pred[v] = u
                heapq.heappush(priority_queue, (distance_through_u, v))
                if trace:
                    changes.append(
                        f"d[{v + 1}]: {old_val} -> {int(distance_through_u)} (pred[{v + 1}] = {u + 1})"
                    )

        if trace:
            print(f"\nКрок {step}: вилучено вершину u = {u + 1} (dist[{u + 1}] = {int(current_dist)})")
            if changes:
                print("  Релаксація ребер:")
                for ch in changes:
                    print(f"    - {ch}")
            else:
                print("  Оновлень немає.")
            print("  dist:", ["∞" if d == math.inf else int(d) for d in distances])
            print("  pred:", ["-" if p == -1 else p + 1 for p in pred])

    if trace:
        print(f"\n--- Таблиця 6.2: Найкоротші шляхи з вершини {start_node + 1} ---")
        for target in range(v_count):
            if target == start_node:
                continue
            path_str = reconstruct_path(pred, start_node, target)
            w_str = "∞" if distances[target] == math.inf else str(int(distances[target]))
            print(f"  {start_node + 1} -> {target + 1}: шлях [{path_str}], вага = {w_str}")

    return distances, pred


def n_times_dijkstra(adj_list: Dict[int, List[Tuple[int, float]]], v_count: int) -> List[List[float]]:
    all_pairs_dist = []
    for start_node in range(v_count):
        dist_row, _ = dijkstra_single_source(adj_list, start_node, v_count, trace=False)
        all_pairs_dist.append(dist_row)

    return all_pairs_dist


def floyd_warshall_with_trace(adj_matrix: List[List[float]]) -> List[List[float]]:
    v_count = len(adj_matrix)
    dist = [row[:] for row in adj_matrix]

    print("\n=== Покроковий хід алгоритму Флойда ===")
    print("--- Початкова матриця D^(0) (Матриця суміжності W) ---")
    print_matrix(dist)

    for k in range(v_count):
        changes = []
        for i in range(v_count):
            for j in range(v_count):
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        old_val = "∞" if dist[i][j] == math.inf else int(dist[i][j])
                        changes.append(
                            f"d[{i + 1}][{j + 1}]: {old_val} -> {int(new_dist)} (через вершину {k + 1})"
                        )
                        dist[i][j] = new_dist

        print(f"\n--- Ітерація k = {k + 1} (проміжна вершина {k + 1}) -> Матриця D^({k + 1}) ---")
        if changes:
            print("Оновлення:")
            for change in changes:
                print(f"  - {change}")
        else:
            print("Оновлень немає.")
        print_matrix(dist)

    return dist