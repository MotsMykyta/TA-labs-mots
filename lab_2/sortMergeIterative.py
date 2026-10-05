
def merge_sort_iterative(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    step = 1
    i = 1
    while i < n:
        print(f"\n[ЕТАП {step}: розмір блоків i = {i}]")
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)

            c_count, a_count = merge_iterative(arr, left, mid, right)
            comparisons += c_count
            assignments += a_count
            j += 2 * i

        print(f"\nСтан масиву після i={i}: {arr}")
        print("-" * 50)
        i *= 2
        step += 1

    return arr, comparisons, assignments

def merge_iterative(arr, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
    L = arr[left:mid]
    R = arr[mid:right]
    assignments += n1 + n2

    print(f"  Зливаємо {L} та {R} (індекси {left}:{mid} та {mid}:{right})")

    it1 = 0
    it2 = 0
    k = left
    assignments += 2
    assignments += 1
    while it1 < n1 and it2 < n2:
        comparisons += 1
        print(f"    Порівняння: {L[it1]} < {R[it2]}")
        if L[it1] <= R[it2]:
            arr[k] = L[it1]
            it1 += 1
            assignments += 1
        else:
            arr[k] = R[it2]
            it2 += 1
            assignments += 1
        k+= 1
        assignments += 1
    while it1 < n1:
        arr[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 1
    while it2 < n2:
        arr[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 1

    print(f"    Результат блоку: {arr[left:right]}")
    return comparisons, assignments

my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
print("Оригінальний список:", my_list)

sorted_list, comparisons, assignments = merge_sort_iterative(my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comparisons}")
print(f"Кількість присвоювань: {assignments}")