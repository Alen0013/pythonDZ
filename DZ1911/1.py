# Создание кортежей
genres = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)

# 1. Узнаем длину обоих кортежей
length_genres = len(genres)
length_numbers = len(numbers)

# 2. Находим максимальный и минимальный элемент в числовом кортеже
max_number = max(numbers)
min_number = min(numbers)

# 3. Суммируем элементы числового кортежа
sum_numbers = sum(numbers)  # Сумма возможна, так как все элементы - числа

# 4. Сортируем элементы по возрастанию и убыванию
sorted_ascending = tuple(sorted(numbers))
sorted_descending = tuple(sorted(numbers, reverse=True))

# Вывод результатов
print("Длина кортежа жанров:", length_genres)
print("Длина кортежа чисел:", length_numbers)
print("Максимальный элемент:", max_number)
print("Минимальный элемент:", min_number)
print("Сумма элементов:", sum_numbers)
print("Сортировка по возрастанию:", sorted_ascending)
print("Сортировка по убыванию:", sorted_descending)
