"""
1. Сохранение заметок в файл
save_notes_to_file.py
Описание задачи:
    Создать функцию save_notes_to_file(notes, filename), которая:
    Перезаписывает данные файла, записывая список заметок в текстовом формате JSON.
"""

# Подключение формата даты и цвет текста и json
from datetime import datetime
from colorama import init, Fore
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)
# Функция сохранения заметок в файле
def save_notes_to_file(notes, filename):
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
    try:
        # Открытие файла на запись с кодировкой "utf-8"
        with open(filename, "w", encoding="utf-8") as file:
            # Цикл перебора заметок
            for note in notes:
                # Запись одной заметки с новыми ключами
                file.write(f'{note_print["username"]}: {note["username"].capitalize()}\n')
                file.write(f'{note_print["titles"]}: {", ".join(note["titles"]).title()}\n')
                file.write(f'{note_print["content"]}: {note["content"]}\n')
                file.write(f'{note_print["status"]}: {note["status"]}\n')
                file.write(f'{note_print["created_date"]}: {str(note["created_date"])}\n')
                file.write(f'{note_print["issue_date"]}: {str(note["issue_date"])}\n')
                file.write("\n")

    # Ошибка прав доступа
    except PermissionError:
        print("Ошибка доступа, недостаточно прав, чтобы открыть файл")
        return
    # Ошибка в имени файла
    except OSError:
        print("Имя файла некорректно")
        filename_new = input("Введите имя файла ещё раз: ").strip()
        return save_notes_to_file(notes, filename_new)

    print(Fore.GREEN + "Заметки сохранены успешно")

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
    # Цикл ввода названия файла
    while True:
        count = 0
        filename_save = input("Введите имя файла для сохранения "
                              "(для перехода в другую папку используйте двойной \\: ").strip()
        for char in filename_save:
            if char == "\\":
                count += 1
        else:
            if count % 2 != 0:
                print("Для ввода \\ вам нужно вести двойной \\")
            else:
                break
    # Вызов функции
    save_notes_to_file(notes1, filename_save)





