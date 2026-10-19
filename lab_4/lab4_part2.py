import math

# Константи розміру таблиці
M_DIV = 13
M_MUL = 16
A = 0.6180339887

# Список вхідних слів
WORDS = ["ХТО", "ГРОШИМА", "ВЕЛИЧАЄТЬСЯ", "ТОЙ", "БЕЗ", "ДУШІ", "ЗОСТАЧАЄТЬСЯ"]

# Словник позицій українського алфавіту
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def primary_hash_div(key: str) -> int:
    sum_of_positions = 0
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    return sum_of_positions % M_DIV


def primary_hash_mul(key: str) -> int:
    sum_of_positions = 0
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    return math.floor(M_MUL * ((sum_of_positions * A) % 1))


def build_closed_hash_table(words: list, m: int, hash_func) -> list:

    hash_table = [None] * m
    inserted_count = 0

    for word in words:

        start_address = hash_func(word)
        address = start_address

        for i in range(m):
            address = (start_address + i) % m

            if hash_table[address] is None:
                hash_table[address] = word
                inserted_count += 1
                break
        else:
            print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")
            return hash_table

    return hash_table


def display_hash_table(table: list, title: str):
    print(f"\n--- {title} ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


hash_table_div = build_closed_hash_table(WORDS, M_DIV, primary_hash_div)
display_hash_table(hash_table_div, "Хеш-таблиця (Відкрита адресація, M=13, Ділення)")

hash_table_mul = build_closed_hash_table(WORDS, M_MUL, primary_hash_mul)
display_hash_table(hash_table_mul, "Хеш-таблиця (Відкрита адресація, M=16, Множення)")