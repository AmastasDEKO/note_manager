"""
1. Сохранение заметок в файл
Файл: save_note_to_file_function.py
Описание задачи:
Создать функцию save_notes_to_file(notes, filename), которая:
Перезаписывает данные файла, записывая список заметок в текстовом формате YAML.
"""
# Подключение формата даты и цвет текста
from datetime import datetime
from colorama import init, Fore
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция сохранения заметок в файле
def save_note_to_file(notes, filename = "notes"):
    # Словарь значений полей.
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дедлайн'
                  }
    # Проверка на существования списка
    if notes is None:
        print(Fore.RED+"У вас нет заметок для сохранения")
        return
    # Проверка на наличие заметок в списке
    elif len(notes) == 0:
        print(Fore.RED + "У вас нет заметок для сохранения")
        return
    # Открытие файла на запись с кодировкой "utf-8"
    file = open(f"{filename}.txt", "w", encoding="utf-8")
    #Цикл перебора заметок
    for i in range(len(notes)):
        note = notes[i]
        file.writelines(f"Заметка №{i + 1}\n")
        # Цикл записи заметки в файл
        for key, value in note.items():
            if key == "titles":
                file.writelines(f"{note_print[key]}: {", ".join(value).title()}\n")
            elif key == "created_date" or key == "issue_date":
                splitting = str(value).split()
                splitting = splitting[0].split(sep="-", maxsplit=-1)
                file.writelines(f"{note_print[key]}: {'.'.join(splitting[::-1])}\n")
            else:
                file.writelines(f"{note_print[key]}: {value.capitalize()}\n")
        # Отступ между заметками
        file.writelines("\n")
    # После выполнения цикла, закрываем файл
    else:
        file.close()
    # Проверка закрыт ли файл
    if file.closed:
        print(Fore.GREEN+"Заметки сохранены успешно")
    else:
        print(Fore.RED+"Файл не был закрыт")
        file.close()
# Основная часть кода
if __name__ == "__main__":
    # Создание списка с 5 заметками
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
    # Вызов функции
    save_note_to_file(notes1)
