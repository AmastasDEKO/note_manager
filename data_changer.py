# Запрос данных о заметке у пользователя
username = "Александр Ромилов"
title = "Встреча с заказчиком"
content = "Встреча пройдёт в кафе 'Савана' на ул.Ленина 30 "
status = "Активна"
created_date = "21.12.24"
issue_date = "12.01.25"

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