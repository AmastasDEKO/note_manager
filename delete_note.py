"""
5. delete_note.py: Удаление заметок
Функциональность:
Удаляет заметку по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.
"""
# Подключение библиотеки дата/время и цвета текста
from datetime import datetime
from colorama import init, Fore
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)

# Функция для вывода списка заметок
def display_notes(_notes):
    if not _notes:
        return
    # Создания словаря для вывода полей на русском
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дедлайн'
                  }
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

# Функция поиска записок
def delete_notes(_notes):
    # Проверка на наличие заметок
    if len(_notes) == 0:
        print("\nУ вас нет сохранённых заметок\n")
        return
    while True:
        input_keyword = input("Введите заголовок или имя пользователя: ").strip().lower()
        # Проверка на пустой ввод
        if input_keyword == "":
            print("Пожалуйста заполните поле.")
        else:
            # Создаём дубликат списка записок
            new_notes = _notes[:]
            cancel_delete = False
            # Перебор заметок
            for i in range(len(_notes)):
                note = _notes[i]
                # Поиск в списке
                if input_keyword in note["titles"]:
                    while True:
                        # Запрос на удаление
                        last_choice = input(f"Точно хотите удалить заметку c заголовками "
                                             f"{", ".join(note["titles"]).title()} (Да/Нет)\nВвод: ").strip().lower()
                        if last_choice == "да":
                            # Если согласились, удаляем, выводим сообщение и завершаем цикл
                            new_notes.pop(i)
                            print(Fore.GREEN + "Успешно удалено")
                            break
                        elif last_choice == "нет":
                            cancel_delete = True
                            # Если отказались, выводим сообщение и завершаем цикл
                            print(Fore.BLUE + "Отмена удаления")
                            break
                        else:
                            # Обработка ошибки ввода
                            print(Fore.RED + "Ошибка ввода (Допустимо: Да, Нет)")
                elif input_keyword in note["username"]:
                    while True:
                        # Запрос на удаление
                        last_choice = input(f"Точно хотите удалить заметку пользователя "
                                            f"{note["username"].capitalize()}(Да/Нет)\nВвод: ").strip().lower()
                        if last_choice == "да":
                            # Если согласились, удаляем, выводим сообщение и завершаем цикл
                            new_notes.pop(i)
                            print(Fore.GREEN + "Успешно удалено")
                            break

                        elif last_choice == "нет":
                            cancel_delete = True
                            # Если отказались, выводим сообщение и завершаем цикл
                            print(Fore.BLUE + "Отмена удаления")
                            break
                        else:
                            # Обработка ошибки ввода
                            print(Fore.RED + "Ошибка ввода (Допустимо: Да, Нет)")
            else:
                if len(_notes) == len(new_notes) and not cancel_delete:
                    print("Заметка не найдена")
                    return
                else:
                    break

    # Заменяем список
    return new_notes
# Главная часть
if __name__ == "__main__":
    # Создание списка с заметками
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
    # Вызов функций
    display_notes(delete_notes(notes1))
    print("\n")
    display_notes(delete_notes(notes2))
    print("\n")
    display_notes(delete_notes(notes3))
