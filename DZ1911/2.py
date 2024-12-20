# Исходный кортеж жанров кино
cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")

# 1. Заменяем жанр "Экшн" на "Боевик"
# Конвертируем кортеж в список, чтобы изменить его
genres_list = list(cinema_genres)
genres_list[1] = "Боевик"  # Меняем "Экшн" на "Боевик"

# 2. Добавляем жанр "Фэнтези" между "Боевик" и "Пеплум"
genres_list.insert(2, "Фэнтези")

# 3. Преобразуем список обратно в кортеж
updated_genres = tuple(genres_list)

# Выводим результат 2-го пункта
print(updated_genres)  # ('Комедия', 'Боевик', 'Фэнтези', 'Пеплум', 'Триллер')

# 4. Преобразуем кортеж в строку
genres_string = ', '.join(updated_genres)

# Выводим строку с обновленными жанрами
print(f"Обновленные жанры кино: {genres_string}")
