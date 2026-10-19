import math

# Константи розміру таблиці
M_DIV = 13
M_MUL = 16
A = 0.6180339887

# Список вхідних слів
WORDS = ["ХТО", "ГРОШИМА", "ВЕЛИЧАЄТЬСЯ", "ТОЙ", "БЕЗ", "ДУШІ", "ЗОСТАЧАЄТЬСЯ"]

# Словник позицій
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def simple_hash_div(key: str) -> int:
    sum_of_positions = 0

    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position

    hash_address = sum_of_positions % M_DIV
    return hash_address


def simple_hash_mul(key: str) -> int:
    sum_of_positions = 0
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position

    hash_address = math.floor(M_MUL * ((sum_of_positions * A) % 1))
    return hash_address


def build_open_hash_table(words: list, m: int, hash_func) -> list:
    hash_table = [[] for _ in range(m)]

    for word in words:
        address = hash_func(word)
        hash_table[address].append(word)

    return hash_table


def display_hash_table(table: list, title: str):
    print(f"\n--- {title} ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


# Виконання:
hash_table_div = build_open_hash_table(WORDS, M_DIV, simple_hash_div)
display_hash_table(hash_table_div, "Результат хешування (Ланцюжки, Метод ділення, M=13)")

hash_table_mul = build_open_hash_table(WORDS, M_MUL, simple_hash_mul)
display_hash_table(hash_table_mul, "Результат хешування (Ланцюжки, Метод множення, M=16)")