def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 0

    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    mid = len(arr) // 2
    assignments += 1
    recursive_calls += 2

    print(f"Розділяємо масив: {arr} -> Ліва: {arr[:mid]}, Права: {arr[mid:]}")

    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])

    comparisons += c1+c2
    assignments += a1+a2
    recursive_calls += r1 + r2
    merged_arr, c_merge, a_merge = merge_recursive(left_half, right_half)
    comparisons += c_merge
    assignments += a_merge
    return merged_arr, comparisons, assignments, recursive_calls


def merge_recursive(sorted_left, sorted_right):
    result = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0

    print(f"  Зливаємо {sorted_left} та {sorted_right}")

    while i < len(sorted_left) and j < len(sorted_right):
        comparisons += 1
        if sorted_left[i] <= sorted_right[j]:
            print(f"    Порівняння: {sorted_left[i]} <= {sorted_right[j]} -> True. Додаємо {sorted_left[i]}")
            result.append(sorted_left[i])
            i += 1
        else:
            print(f"    Порівняння: {sorted_left[i]} <= {sorted_right[j]} -> False. Додаємо {sorted_right[j]}")
            result.append(sorted_right[j])
            j += 1
        assignments += 1
    while i < len(sorted_left):
        print(f"    Додаємо залишок з лівого масиву: {sorted_left[i]}")
        result.append(sorted_left[i])
        i += 1
        assignments += 1
    while j < len(sorted_right):
        print(f"    Додаємо залишок з правого масиву: {sorted_right[j]}")
        result.append(sorted_right[j])
        j += 1
        assignments += 1

    print(f"  Злиття завершено. Результат: {result}")
    return result, comparisons, assignments

my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
print("Оригінальний список:", my_list)
sorted_list, comparisons, assignments, recursive_calls = merge_sort_recursive(my_list)

print(f"Відсортований список: {sorted_list}")
print(f"Кількість порівнянь: {comparisons}")
print(f"Кількість присвоювань: {assignments}")
print(f"Кількість рекурсивних викликів: {recursive_calls}")