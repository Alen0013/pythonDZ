import random

# Шаг 0: Создаем словари со словами
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# Уровни пользователя
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}

# Шаг 1: Получаем уровень сложности от пользователя
difficulty = input("Выберите уровень сложности (легкий, средний, тяжелый): ").strip().lower()

# Устанавливаем уровень сложности по умолчанию
if difficulty == "легкий":
    words = words_easy
elif difficulty == "средний":
    words = words_medium
elif difficulty == "тяжелый":
    words = words_hard
else:
    print("Неизвестный уровень сложности. Установлен уровень по умолчанию: легкий.")
    words = words_easy

# Шаг 2: Запускаем цикл по пяти словам из словаря
answers = {}
words_list = list(words.keys())
random.shuffle(words_list)  # Перемешиваем слова
for word in words_list[:5]:  # Берем первые 5 слов
    correct_translation = words[word]
    print(f"Программа: {word}, {len(correct_translation)} букв, начинается на '{correct_translation[0]}'...")

    user_answer = input("Ваш ответ: ").strip().lower()

    if user_answer == correct_translation:  # Проверка ответа
        print(f"Программа: Верно, {word.capitalize()} — это {correct_translation}.")
        answers[word] = True
    else:
        print(f"Программа: Неверно. {word.capitalize()} — это {correct_translation}.")
        answers[word] = False

# Шаг 3: Выводим результат
correct_words = [word for word, correct in answers.items() if correct]
incorrect_words = [word for word, correct in answers.items() if not correct]

print("\nПравильно отвечены слова:")
for word in correct_words:
    print(word)

print("Неправильно отвечены слова:")
for word in incorrect_words:
    print(word)

# Шаг 4: Подсчитываем правильные ответы и определяем ранг
correct_count = sum(answers.values())  # Считаем количество True в answers
user_rank = levels.get(correct_count, "Нулевой")  # Получаем ранг

print(f"\nВаш ранг: {user_rank}")
