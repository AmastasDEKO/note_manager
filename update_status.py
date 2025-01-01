#Словарь с элементом "статус"
note = {"status":"Отложено"}

# Словарь для значений статуса
choice_status = {"1":"Выполнено",
                 "2":"В процессе",
                 "3":"Отложено"
                 }

# Вывод текущего статуса
print("Текущий статус заметки:", note["status"])

# Цикл изменения статуса
while True:
    # Запрос на изменение статуса и проверка корректности ввода
    changed = input("Хотите изменить статус заметки? (Да/Нет)\nВвод: ").strip().capitalize()
    if changed == "Да":
       #Цикл ввода статуса
       while True:
           # Ввод нового статуса и проверка корректности ввода
           new_status = input("Введите статус:\n1. Выполнено\n2. В процессе\n3. Отложено\nВвод: ").strip().capitalize()
           #Проверка по ключу(цифре)
           if new_status in choice_status.keys():
               # Изменение и вывод нового статуса
               note["status"] = choice_status[new_status]
               print(f"Статус успешно обновлен на: {note["status"]}")
               #Выход из второго цикла
               break
           # Проверка по значению(словам)
           elif new_status in choice_status.values():
               # Изменение и вывод нового статуса
               note["status"] = new_status
               print(f"Статус успешно обновлен на: {note["status"]}")
               # Выход из второго цикла
               break
           else:
               print("Ошибка ввода (Допустимо: 1, 2, 3)")
       # Выход из первого цикла
       break

    elif changed == "Нет":
        print("Статус не изменен")
        break
    else:
        print("Ошибка ввода (Допустимо: Да, Нет)")