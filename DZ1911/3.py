# Множество ваших вещей
my_items = {"вода", "еда", "нож", "фонарик", "свечи", "средства первой помощи", "карта", "рюкзак", "одежда", "книги"}

# Множество вещей вашего близкого человека
# Здесь я фиксирую вещи, но вы можете заменить их на фактические
friend_items = {"еда", "нож", "радио", "спальный мешок", "фонарик", "книга", "аптечка", "плед", "вода", "компас"}

# Находим множество вещей, которые вы бы взяли оба
both_items = my_items.intersection(friend_items)

# Находим уникальные вещи, которые взял только вы
only_my_items = my_items.difference(friend_items)

# Находим уникальные вещи, которые взял только ваш близкий человек
only_friend_items = friend_items.difference(my_items)

# Выводим результаты
print("Вещи, которые бы взяли мы двое:", both_items)
print("Вещи, которые взял только я:", only_my_items)
print("Вещи, которые возьмет мой близкий человек:", only_friend_items)
