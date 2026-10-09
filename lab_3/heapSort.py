
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n):
    comparisons = 0
    assignments = 0
    k = i
    assignments += 1

    print(f"  Починаємо 'занурювати' елемент: {arr[k]} з індексу {k}")

    while True:
        j = 2 * k + 1
        assignments += 1
        if j >= n:
            comparisons += 1
            print(f"       Елемент досяг кінця купи. Завершуємо.")
            break

        comparisons += 1
        if j+ 1 < n:
            comparisons += 1
            if (arr[j + 1] > arr[j]):
                print(f"       Порівнюємо {arr[j]} та {arr[j + 1]}. Обираємо правого нащадка: {arr[j + 1]}")
                j += 1
                assignments += 1
            else:
                print(f"       Порівнюємо {arr[j]} та {arr[j + 1]}. Обираємо лівого нащадка: {arr[j]}")
        else:
            print(f"       Єдиний нащадок: {arr[j]}")

        comparisons += 1
        if arr[k] >= arr[j]:
            print(f"       {arr[k]} (батько) >= {arr[j]} (нащадок). Елемент на своєму місці.")
            break

        print(f"       Міняємо місцями {arr[k]} та {arr[j]}")
        swap(arr, k, j)
        assignments += 3

        k = j
        assignments += 1
        print(f"       Поточний стан масиву: {arr}")

    return comparisons, assignments

def heapSort(arr):
    total_assignments = 0
    total_comparisons = 0

    n = len(arr)
    total_assignments += 1

    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range (n // 2 - 1, -1, -1):
        total_assignments += 1
        # print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        comp1,assig1 = sink(arr, i, n)
        total_comparisons += comp1
        total_assignments += assig1

    print(f"\nМасив після побудови купи: {arr}\n")

    print("--- Фаза 2: Сортування ---")
    for i in range(n-1, 0, -1):
        total_assignments += 1

        print(f"\nМіняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        total_assignments += 3

        n -= 1
        # print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        total_assignments += 1

        comp2, assig2 = sink(arr, 0, n)
        # print(f"Масив на поточному кроці: {arr}\n")
        total_comparisons += comp2
        total_assignments += assig2

    return total_comparisons, total_assignments

my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
original_list = my_list.copy()
print(f"Початковий масив: {original_list}")

comparisons, assignments, = heapSort(my_list)

print(f"\nВідсортований масив: {my_list}")
print(f"Загальна кількість порівнянь: {comparisons}")
print(f"Загальна кількість присвоювань: {assignments}")
