# Подключение формата даты и цвет текста
from datetime import datetime
from colorama import init, Fore
# Определение автоматического сбрасывания настроек цвета текста
init(autoreset=True)

def save_note_to_file(notes, filename = "notes"):
    note_print = {'username': "Имя пользователя",
                  'titles': "Заголовки",
                  'content': "Описание",
                  'status': "Статус",
                  'created_date': 'Дата создания',
                  'issue_date': 'Дедлайн'
                  }
    if notes is None:
        print(Fore.RED+"У вас нет заметок для сохранения")
        return
    elif len(notes) == 0:
        print(Fore.RED + "У вас нет заметок для сохранения")
        return
    file = open(f"{filename}.txt", "w", encoding="utf-8")
    for i in range(len(notes)):
        note = notes[i]
        file.writelines(f"Заметка №{i + 1}\n")
        for key, value in note.items():
            if key == "titles":
                file.writelines(f"{note_print[key]}: {", ".join(value).title()}\n")
            elif key == "created_date" or key == "issue_date":
                splitting = str(value).split()
                splitting = splitting[0].split(sep="-", maxsplit=-1)
                file.writelines(f"{note_print[key]}: {'.'.join(splitting[:0:-1])}\n")
            else:
                file.writelines(f"{note_print[key]}: {value.capitalize()}\n")
        file.writelines("\n")
    else:
        file.close()
    if file.closed:
        print(Fore.GREEN+"Заметки сохранены успешно")
    else:
        print(Fore.RED+"Файл не был закрыт")

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

    save_note_to_file(notes1)
