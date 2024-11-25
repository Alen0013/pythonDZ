import random

# Исходный список жанров кино
cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

# 1. Преобразуем данный список в множество (удаляются дубликаты)
unique_genres = set(cinema_genres)

# 2. Добавляем 2 жанра на ваш выбор
unique_genres.add("драма")
unique_genres.add("фэнтези")

# 3. Удаляем какой-то жанр по вашему выбору (например, "экшн")
unique_genres.remove("экшн")

# 4. Удаляем случайный жанр
if unique_genres:  # Проверяем, что множество не пустое
    random_genre = random.choice(list(unique_genres))
    unique_genres.remove(random_genre)

# 5. Преобразуем множество обратно в список
final_genres = list(unique_genres)

# Вывод результатов
print("Финальный список жанров:", final_genres)
