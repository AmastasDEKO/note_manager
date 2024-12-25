# Создание словаря
note = {}

# Запрос данных о заметке у пользователя
note['username'] = input("Введите имя пользователя: ")

# Ввод заголовков
note['titles'] = []
for i in range(3):
    title = input(f"Введите название заголовка {i+1}: ")
    note['titles'].append(title.capitalize())

# Продолжение ввода данных о заметке
note['content'] = input("Введите описание заметки: ")
note['status'] = input("Введите статус заметки (Активна/Выполнена): ")
note['created_date'] = input("Введите дату создания заметки (день.месяц.год): ").split(sep='.', maxsplit=-1)
note['issue_date'] = input("Введите дату истечения заметки (день.месяц.год): ").split(sep='.', maxsplit=-1)

# Вывод введенных данных
print("\n   Новая заметка!")
for key, value in note.items():
    if key == "titles":
        print(f"{key.capitalize()}:", ", ".join(value))
    elif key == "created_date" or key == "issue_date":
        print(f"{key.capitalize()}:", '.'.join(value[:2]) )
    else:
        print(f"{key.capitalize()}: {value.capitalize()}")

# Подтверждение данных
input("\nНажмите Enter для подтверждения")