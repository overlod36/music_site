from pack import db, models
import os, sys, shutil
import json
import datetime as dt

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
			print('Сброс базы данных!')
			continue
		case '2':
			with open('pack/setup/fill_db/groups.json', encoding="utf-8") as file:
				groups = json.load(file)
				for el in groups:
					if 'past_members' in el.keys():
						db.session.add(models.Group(name=el['name'], main_cover_path=el['main_cover_path'], addin_cover_path=el['addin_cover_path'], logo_path=el['logo_path'], current_members=el['current_members'], past_members=el['past_members'], active_years=el['active_years']))
					else:
						db.session.add(models.Group(name=el['name'], main_cover_path=el['main_cover_path'], addin_cover_path=el['addin_cover_path'], logo_path=el['logo_path'], current_members=el['current_members'], active_years=el['active_years']))			
					os.mkdir(f'pack/static/models_images/{el["name"]}')
					shutil.copyfile(f'pack/setup/fill_db/covers/{el["main_cover_path"]}', f'pack/static/models_images/{el["name"]}/{el["main_cover_path"]}')
					shutil.copyfile(f'pack/setup/fill_db/covers/{el["addin_cover_path"]}', f'pack/static/models_images/{el["name"]}/{el["addin_cover_path"]}')
					shutil.copyfile(f'pack/setup/fill_db/covers/{el["logo_path"]}', f'pack/static/models_images/{el["name"]}/{el["logo_path"]}')
			with open('pack/setup/fill_db/albums.json', encoding="utf-8") as file:
				albums = json.load(file)
				for el in albums:
					db.session.add(models.Album(title=el['title'], release_date=dt.datetime.strptime(el['release_date'], "%d.%m.%Y").date(), producers_name=el['producers_name'], duration=dt.datetime.strptime(el['duration'], "%H:%M:%S").time(), songs=el['songs'], group_name=el['group_name'], cover_path=el['cover_path'], genres=el['genres']))
					shutil.copyfile(f'pack/setup/fill_db/covers/{el["cover_path"]}', f'pack/static/models_images/{el["group_name"]}/{el["cover_path"]}')
			db.session.commit()
			print('Заполнение базы данных!')
			continue
		case '3':
			break
		case _:
			print('-> Неверный номер команды!')
			continue
