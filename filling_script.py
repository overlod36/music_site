from pack import db, models
import os, sys, shutil

def menu():
	print('[МЕНЮ]\n1]Сброс базы данных\n2]Заполнение базы данных\n3]Прекращение работы')

while True:
	menu()
	choice = input('Введите команду -> ')
	match choice:
		case '1':
			db.drop_all()
			db.create_all()
			if os.path.exists('pack/static/models_images'):
                                shutil.rmtree('pack/static/models_images')
			if not os.path.exists('pack/static/models_images'):
				os.mkdir('pack/static/models_images')
			continue
		case '2':
			print('Заполнение базы данных!')
			continue
		case '3':
			break
		case _:
			print('-> Неверный номер команды!')
			continue
