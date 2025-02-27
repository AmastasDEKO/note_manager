"""
2. update_status.py: Проверка и обновление статуса заметки
Функциональность:
Показывает текущий статус заметки.
Предлагает изменить статус на один из предложенных.
Обрабатывает некорректный ввод.
"""

#Словарь с элементом "статус"
note = {"status":"Отложено"}

# Словарь для значений статуса
choice_status = {"1":"Выполнено",
                 "2":"В процессе",
                 "3":"Отложено"
                 }

# Функция ввода нового статуса
def changed_status():
        # Ввод нового статуса и проверка корректности ввода
        new_status = input("Введите статус:\n1. Выполнено\n2. В процессе\n3. Отложено\nВвод: ").strip()
        # Проверка по ключу(цифре)
        if new_status in choice_status.keys():
            # Изменение и вывод нового статуса
            note["status"] = choice_status[new_status]
            print(f"Статус успешно обновлен на: {note["status"]}")
            # Выход из функции
            return
        # Проверка по значению(словам)
        elif new_status in choice_status.values():
            # Изменение и вывод нового статуса
            note["status"] = new_status
            print(f"Статус успешно обновлен на: {note["status"]}")
            # Выход из второго цикла
            return
        else:
            print("Ошибка ввода (Допустимо: 1, 2, 3)")
            return changed_status()


# Функция запроса на ввод нового статуса
def can_changed():
        changed = input("Хотите изменить статус заметки? (Да/Нет)\nВвод: ").strip().capitalize()
        if changed == "Да":
            # Вызов функции ввода нового статуса
            changed_status()
            return
        elif changed == "Нет":
            print("Статус не изменен")
            return
        else:
            print("Ошибка ввода (Допустимо: Да, Нет)")
            return can_changed()


# Вывод текущего статуса
print("Текущий статус заметки:", note["status"])
# Вызов функции на изменение статуса
can_changed()
