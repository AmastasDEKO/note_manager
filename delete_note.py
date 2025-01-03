# Создание списка с заметками(неполные)
notes = [{
        "ID":1,
        "username":"Анна Робкова",
        "titles":["Дом", "Пылесос"],
        "content":"Купить домой пылесос"
        },
        {
        "ID": 2,
        "username":"Кристина Ромашковна",
        "titles":["Любовь", "Подарок"],
        "content":"Выбрать подарок на 14 февраля"
        },
        {
        "ID": 3,
        "username":"Максим Любиц",
        "titles":["Стиральная машина", "Дом"],
        "content":"Отремонтировать стиральную машину в доме бабушки"
        },
        {
        "ID": 4,
        "username":"Анна Робкова",
        "titles":["Машина", "Поход"],
        "content":"Загрузить машину инвентарем для похода в горы"
        },
        {
        "ID": 5,
        "username":"Анна Токарева",
        "titles":["Рисование", "Любовь"],
        "content":"Написать сочинение об любви к рисованию"
        }]

# Функция удаления записок
def delete_notes(notes_ID, _notes2):
            # Запрос на удаление
            last_choice = input("Точно хотите удалить заметку? (Да/Нет)\nВвод: ").strip().capitalize()
            if last_choice == "Да":
                # Если согласились, удаляем, выводим сообщение и возвращаем список
                _notes2.pop(notes_ID)
                print("Успешно удалено")
                return _notes2
            elif last_choice == "Нет":
                # Если отказались, выводим сообщение и возвращаем список
                print("Отмена удаления")
                return _notes2
            else:
                # Обработка ошибки ввода
                print("Ошибка ввода (Допустимо: Да, Нет)")
                return delete_notes(notes_ID, _notes2)

# Функция поиска записок
def find_note(key_word, word, _notes):
    # Создаём дубликат списка записок
    _notes2 = _notes[:]
    # Счётчик найденных заметок
    count = 0
    # Цикл поиска
    while True:
        # Поиск по заголовку
        if key_word == "Заголовок":
            # Перебор заметок
            for i in range(len(_notes)):
                note = _notes[i]
                # Поиск в списке
                if word in note["titles"]:
                    count += 1
                    # Обновляем дубликат списка
                    _notes2 = delete_notes(i, _notes2)

            else:
                # Если счётчик не изменился выводим сообщение
                if count == 0:
                    print("Заметка не найдена")
                    break
                else:
                    break
        # Поиск по имени пользователя
        else:
            # Перебор заметок
            for i in range(len(_notes)):
                note = _notes[i]
                # Поиск в списке
                if word.lower() == note["username"].lower():
                    count += 1
                    # Обновляем дубликат списка
                    _notes2 = delete_notes(i, _notes)

            else:
                # Если счётчик не изменился выводим сообщение
                if count == 0:
                    print("Заметка не найдена")
                    break
                else:
                    break
    # Возвращаем дубликат
    return _notes2

# Функция для выбора критерия
def input_key_word():
    # Словарь значений статуса
    choice_key_word = {"1": "Заголовок", "2": "Имя пользователя"}
    # Ввод нового статуса и проверка корректности ввода
    key_word = input("Выберете критерий удаления:\n1.Заголовок \n2.Имя пользователя\nВвод: ").strip().capitalize()
    # Проверка по ключу(цифре)
    if key_word in choice_key_word.keys():
        return choice_key_word[key_word]
    # Проверка по значению(словам)
    elif key_word in choice_key_word.values():
        return key_word
    else:
        #Обработка ошибки ввода
        print("Ошибка ввода (Допустимо: 1, 2 или Заголовок, Имя пользователя)")
        return input_key_word()
    
# Функция для вывода списка заметок
def output_notes(_notes):
    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  }
    # Проверка на наличие заметок
    if len(_notes) == 0:
        print("Нет ни одной заметки")
        return
    else:
        print("Список заметок:")
        # Цикл вывода заметок из списка
        for i in range(len(_notes)):
            # Помещаем текущую заметку в переменную
            note = _notes[i]
            # Вывод данных заметки
            print(f"\nЗаметка №{note["ID"]}")
            for key, value in note.items():
                if key == "titles":
                    print(f"{note_print[key]}:", ", ".join(value))
                # Пропускаем ID
                elif key == "ID":
                    continue
                else:
                    print(f"{note_print[key]}: {value}")

# Функция запроса на удаление
def can_delete(_notes):
    # Запрос на удаление заметки
    delete = input("Хотите удалить заметку? (Да/Нет)\nВвод: ").strip().capitalize()
    if delete == "Да":
        key_word = input_key_word()
        # Обработка выбранного критерия
        while True:
            if key_word == "Заголовок":
                title = input("Введите заголовок: ").strip().capitalize()
                # Проверка на пустой ввод
                if title == "":
                    print("Пожалуйста заполните заголовок.")
                else:
                    _notes = find_note(key_word, title, _notes)
                    break
            elif key_word == "Имя пользователя":
                username = input("Введите имя пользователя: ").strip()
                # Проверка на пустой ввод
                if username == "":
                    print("Пожалуйста заполните имя пользователя.")
                else:
                    _notes = find_note(key_word, username, _notes)
                    break

        return can_delete(_notes)
    elif delete == "Нет":
        output_notes(_notes)
    else:
        # Обработка ошибки ввода
        print("Ошибка ввода (Допустимо: Да, Нет)")
        return can_delete(_notes)

can_delete(notes)