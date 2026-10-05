
def partition(arr, l, r):
    comparisons = 0
    assignments = 0

    pivot = arr[l]
    assignments += 1
    print(f"  Вибираємо опорний елемент (pivot): {pivot}")

    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        i += 1
        assignments += 1
        while arr[i] < pivot:
            comparisons += 1
            i+=1
            assignments += 1
        comparisons += 1

        j -= 1
        assignments += 1
        while arr[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1

        comparisons += 1
        if i >= j:
            print(f"  Поточні індекси: i = {i}, j = {j}. Масив: {arr[l:r + 1]}")
            print(f"  Індекси перетнулися. Поділ завершено. Повертаємо j={j}.")
            return j, comparisons, assignments

        arr[i], arr[j] = arr[j], arr[i]
        assignments += 3
        print(f"  Поточні індекси: i = {i}, j = {j}. Обмінюємо a[{i}] ({arr[j]}) і a[{j}] ({arr[i]}). Масив: {arr}")

def quickSort(arr, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    print(f"Quicksort виклик: масив = {arr}, l = {l}, r = {r}")

    if l < r:
        q, comp1, assig1 = partition(arr, l, r)
        comparisons += comp1
        assignments += assig1

        comp2, assig2, recurs2= quickSort(arr, l, q)
        comp3, assig3, recurs3 = quickSort(arr, q+1, r)

        comparisons += comp2 + comp3
        assignments += assig2 + assig3
        recursive_calls += recurs2 + recurs3
        print(f"Після Quicksort для l={l}, r={r}: масив = {arr}")
    else:
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
original_list = my_list.copy()

print("Оригінальний список:", original_list)
total_comparisons, total_assignments, total_recursive_calls = quickSort(my_list, 0, len(my_list) - 1)

print("\nВідсортований список:", my_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")