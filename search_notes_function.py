"""
4. search_notes_function.py: Функция поиска заметок
Функциональность:
Функция search_notes(_notes, keyword=None, status=None) ищет заметки по ключевым словам или статусу.
Возвращает список найденных заметок.
Выводит сообщение, если ничего не найдено.
"""

# Подключение библиотеки дата/время
from datetime import datetime
from colorama import init, Fore

# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)

# Функция для вывода списка заметок
def output_notes(_notes):
    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дедлайн'
                  }
    if len(_notes) == 0:
        return
    print("Список заметок:")
    print("---------------")
    # Цикл вывода заметок из списка
    for i in range(len(_notes)):
        # Помещаем текущую заметку в переменную
        note = _notes[i]
        # Вывод данных заметки
        print(f"Заметка №{i + 1}")
        for key, value in note.items():
            if key == "titles":
                print(f"{note_print[key]}: {", ".join(value).title()}")
            elif key == "created_date" or key == "issue_date":
                splitting = str(value).split()
                splitting = splitting[0].split(sep="-", maxsplit=-1)
                print(f"{note_print[key]}: {'.'.join(splitting[:0:-1])}")
            else:
                print(f"{note_print[key]}: {value.capitalize()}")
        else:
            print("---------------")

# Функция поиска
def search_notes(_notes, keyword=None, status=None):
    # Список найденных заметок
    searched_notes = []
    # Проверка на наличие заметок
    if len(_notes) == 0:
        print(Fore.BLUE+"У вас нет сохранённых заметок")
        return searched_notes
    # Проверка наличия ключевых слов
    if keyword and status is None:
        for i in range(len(keyword)):
            for j in range(len(_notes)):
                print(i, j)
                note = _notes[j]
                if keyword[i] in note["username"] or keyword[i] in note["titles"] or keyword[i] in note["content"]:
                    searched_notes.append(note)
    # Проверка наличия статуса
    elif status and  keyword is None:
            for i in range(len(_notes)):
                note = _notes[i]
                if status == note["status"]:
                    searched_notes.append(note)
    elif status and keyword:
        for i in range(len(keyword)):
            for j in range(len(_notes)):
                note = _notes[j]
                if (keyword[i] in note["username"] or keyword[i] in note["titles"]
                    or keyword[i] in note["content"]) and status == note["status"]:
                    searched_notes.append(note)
    # Проверка найденных заметок
    if len(searched_notes) == 0:
        print(Fore.BLUE+"Заметки, соответствующие запросу, не найдены.")
        return searched_notes
    # Возвращаем найденные заметки
    return searched_notes
# Главная часть
if __name__ == "__main__":
    notes1 = [{
        "username": "анна",
        "titles": ["дом", "пылесос"],
        "content": "купить домой пылесос",
        "status": "в процессе",
        "created_date": datetime(2025, 1, 2),
        "issue_date": datetime(2025, 1, 10)
    },
        {
            "username": "кристина",
            "titles": ["любовь", "подарок"],
            "content": "выбрать подарок на 14 февраля",
            "status": "новая",
            "created_date": datetime.today(),
            "issue_date": datetime(2025, 1, 15)
        },
        {
            "username": "максим",
            "titles": ["стиральная машина", "дом"],
            "content": "отремонтировать стиральную машину в доме бабушки",
            "status": "отложено",
            "created_date": datetime(2025, 1, 10),
            "issue_date": datetime(2025, 1, 25)
        },
        {
            "username": "анна",
            "titles": ["машина", "поход"],
            "content": "загрузить машину инвентарем для похода в горы",
            "status": "выполнено",
            "created_date": datetime(2025, 1, 2),
            "issue_date": datetime(2025, 1, 20)
        },
        {
            "username": "анна",
            "titles": ["рисование", "любовь"],
            "content": "написать сочинение об любви к рисованию",
            "status": "в процессе",
            "created_date": datetime(2025, 1, 6),
            "issue_date": datetime(2025, 1, 30)
        }]
    # Создание пустого списка
    notes2 = []

    # Создание списка с одной заметкой
    notes3 = [{
        "username": "костя",
        "titles": ["код", "гит"],
        "content": "проверить код на гитхабе",
        "status": "в процессе",
        "created_date": datetime.today(),
        "issue_date": datetime(2025, 1, 12)
    }]
    # Кортеж критериев
    choice_tuple = ("1", "ключевое слово", "2", "статус", "3", "ключевое слово и статус")
    # Цикл выбора критерия
    while True:
        input_choice = input("Выберите критерий поиска:"
                             "\n1. Ключевое слово"
                             "\n2. Статус"
                             "\n3. Ключевое слово и статус"
                             "\nВвод: ").strip().lower()
        # Только ключевое слово
        if input_choice in choice_tuple[:2]:
            # Ввод ключевых слов
            input_keyword = input("Введите ключевые слова через пробел или оставьте поле пустым "
                                  "\n(Зона поиска: Имя пользователя, Заголовки, Описание)"
                                  "\nВвод: ").strip().lower()
            # Вызов функций для 3 списков заметок
            print("\nОбычный список")
            output_notes(search_notes(notes1, input_keyword.split()))
            print("\nПустой список")
            output_notes(search_notes(notes2, input_keyword.split()))
            print("\nСписок с 1 заметкой")
            output_notes(search_notes(notes3, input_keyword.split()))
            break
        # Только статус
        elif input_choice in choice_tuple[2:4]:
            # Ввод статуса
            while True:
                # Словарь значений статуса
                choice_status = {"1": "выполнено",
                                 "2": "в процессе",
                                 "3": "новая",
                                 "4": "отложено"
                                 }
                # Ввод нового статуса и проверка корректности ввода
                _status = input(
                    "Введите статус или оставьте поле пустым:\n1. Выполнено\n2. В процессе\n3. Новая\n4. Отложено\nВвод: ").strip().lower()
                # Проверка по ключу(цифре)
                if _status in choice_status.keys():
                    # Сохранение статуса в переменную
                    input_status = choice_status[_status]
                    break
                # Проверка по значению(словам)
                elif _status in choice_status.values():
                    # Сохранение статуса переменную
                    input_status = _status
                    break
                elif _status == "":
                    input_status = _status
                    break
                else:
                    # Обработка ошибки ввода
                    print("Ошибка ввода (Допустимо: 1, 2, 3, 4 или Выполнено, В процессе, Новая, Отложено)")
                # Вызов функций для 3 списков заметок
            print("\nОбычный список")
            output_notes(search_notes(notes1, status= input_status))
            print("\nПустой список")
            output_notes(search_notes(notes2, status=input_status))
            print("\nСписок с 1 заметкой")
            output_notes(search_notes(notes3, status=input_status))
            break
        # Ключевое слово и статус
        elif input_choice in choice_tuple[4:]:
            # Ввод ключевых слов
            input_keyword = input("Введите ключевые слова через пробел или оставьте поле пустым "
                                  "\n(Зона поиска: Имя пользователя, Заголовки, Описание)"
                                  "\nВвод: ").strip().lower()

            # Ввод статуса
            while True:
                # Словарь значений статуса
                choice_status = {"1": "выполнено",
                                 "2": "в процессе",
                                 "3": "новая",
                                 "4": "отложено"
                                 }
                # Ввод нового статуса и проверка корректности ввода
                _status = input(
                    "Введите статус или оставьте поле пустым:\n1. Выполнено\n2. В процессе\n3. Новая\n4. Отложено\nВвод: ").strip().lower()
                # Проверка по ключу(цифре)
                if _status in choice_status.keys():
                    # Сохранение статуса в переменную
                    input_status = choice_status[_status]
                    break
                # Проверка по значению(словам)
                elif _status in choice_status.values():
                    # Сохранение статуса переменную
                    input_status = _status
                    break
                elif _status == "":
                    input_status = _status
                    break
                else:
                    # Обработка ошибки ввода
                    print("Ошибка ввода (Допустимо: 1, 2, 3, 4 или Выполнено, В процессе, Новая, Отложено)")
            # Вызов функций для 3 списков заметок
            print("\nОбычный список")
            output_notes(search_notes(notes1, input_keyword.split(), input_status))
            print("\nПустой список")
            output_notes(search_notes(notes1, input_keyword.split(), input_status))
            print("\nСписок с 1 заметкой")
            output_notes(search_notes(notes1, input_keyword.split(), input_status))
            break
        else:
            print(Fore.RED+"Ошибка ввода (Допустимо: 1, 2, 3, или Ключевое слово, Статус, Ключевое слово и статус")



