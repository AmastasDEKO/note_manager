# Переменная для заголовка и множества
title = ""
titles_input = set()

# Цикл ввода заголовков
while True:
    title = input("Введите заголовок (для конца ввода оставьте поле пустым или введите \"стоп\"): ")

    #Проверка на окончание ввода или добавление заголовка в множество
    if title == "" or title == "стоп" or title == "Стоп":
        break
    else:
        titles_input.add(title)

# Делаем из множества список
titles = list(titles_input)

# Вывод списка заголовков
print("Заголовки:", ", ".join(titles))

