# Запрос данных о заметке у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите название заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (Активна/Выполнена): ")
created_date = input("Введите дату создания заметки в формате день.месяц.год: ")
issue_date = input("Введите дату истечения заметки в формате день.месяц.год: ")

# Разбиение даты
temp_created_date = created_date.split(sep=".", maxsplit=-1)
temp_issue_date = issue_date.split(sep=".", maxsplit=-1)

# Вывод введенных данных
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания:", temp_created_date[0]+"."+temp_created_date[1])
print("Дата истечения заметки:", temp_issue_date[0]+"."+temp_issue_date[1])