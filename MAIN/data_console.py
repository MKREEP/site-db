import sqlite3
from sqlite3.dbapi2 import Cursor



# Инициализация sql
conn = sqlite3.connect('ProjectMembers.db')
cur = conn.cursor()
print('БД подключена к SQLite успешно.')
# ...

# Создание новой таблицы
def newTable():
	try:
		table = """CREATE TABLE IF NOT EXISTS members (
				id INTEGER PRIMARY KEY,
				NickName TEXT,
				DiscordTag INTEGER,
				Rank TEXT,
				Quests TEXT);"""

		cur.execute(table)
		conn.commit()
		print('Таблица БД создана.')

	except SQLiteError as error:
		print('Ошибка!', error)
# ...

# Добавление участника в проект
def newMember():
	member_NickName = input('Введите ник нового участника >>>')
	member_DiscordTag = input('Введите Discord-тэг участника >>>')
	member_Rank = input('Введите должность нового участника >>>')
	member_Quests = input('Введите его первое задание и дедлайны >>>')
	MemberData = (member_NickName, member_DiscordTag, member_Rank, member_Quests)

	cur.execute("INSERT INTO members(NickName, DiscordTag, Rank, Quests) VALUES(?, ?, ?, ?);", MemberData)
	conn.commit()
# ...

# Удаление участника из проекта
def removeMember():
	memberID = input('Введите id из таблицы базы данных>>>')
	cur.execute("SELECT NickName FROM members WHERE id=?;", (memberID,))
	userFromID = cur.fetchall()
	print('Вы подтверждаете удаление из базы данных пользователя', userFromID, '?[y/n]')
	confirm = input('>>>')

	if confirm == 'y':
		cur.execute("DELETE FROM members WHERE id=?;", (memberID,))
		conn.commit()
		print('Строка успешно удалена.')
	else:
		print('Удаление отменено.')
# ...

# Проверка по дс тэгу
def checkMember():
	search = input('Введите Discord-тэг участника проекта>>>')
	cur.execute("SELECT * FROM members WHERE DiscordTag=?;", (search,))
	results = cur.fetchall()
	for row in results:
		print('--------------------------------------------------')
		print('ID:', row [0])
		print('Nickname:', row [1])
		print('Discord-тэг:', row [2])
		print('должность:', row [3])
		print('Задача:', row [4])
		print('--------------------------------------------------')
# ...

# Выбор действия
enter = int(input('Выберете пункт из списка:\n1) Создать таблицу\n2) Добавить участника проекта\n3) Удалить участника проекта\n4) Проверить по Discord-тэгу\n>>>'))
if enter == 1:
	newTable()
elif enter == 2:
	newMember()
elif enter == 3:
	removeMember()
elif enter == 4:
	checkMember()
else:
	print('Неправильно выбран пункт.')
# ...
