#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os, sys

class EnterFileError(Exception): pass









def list_files(arg=None):
	if not arg:
		lst =  [[x, 'base'] for x in os.listdir("./movies") if x.endswith('.txt')]
	elif arg=='a':
		new_file = input('Enter new file name: ')
		lst = [new_file, 'new']
	return lst



def choose_option(arg=None):
	if arg == []:
		print('{:-^40}'.format('no items are in the list'))
		option = '[A]dd [Q]uit [a]'
		just_option = list("AaQq")
		while True:
			input_option = input(option+" ")
			if input_option not in  just_option:
				print("ERROR: invalid choice enter one of 'AaQq'")		
			else:
				break
	else:
		option = '[A]dd [D]elete [S]ave [Q]uit [a]'
		just_option = list("AaDdSsQq")
		while True:
			input_option = input(option+" ")
			if input_option not in  just_option:
				print("ERROR: invalid choice enter one of 'AaDdSsQq'")		
			else:
				break
	return input_option.lower()





def create_file(lst):
	for file in lst:
		if file[1] == 'save':
			file = open('./movies/' + file[0], 'w')
			file.close()


def working_option(lst, option):
	if option == 's':
		for file in lst:
			file[1] = 'save' if file[1] == 'new' else file[1]
		create_file(lst)			
	elif option == 'd':
		num_file = int(input('Delete item number (or 0 to cancel): ')) - 1
		lst.pop(num_file) 	
	return lst



def print_files(lst):
	print()
	for ls in lst:
		print("{0}: {1}".format(lst.index(ls) + 1, ls[0]))


def check_save(lst):
	try:
		for file in lst:
			if file[1] == 'new':
				option = input('Have dont save file, are You wanna save them [Y]es or [N] ').lower()
				if option == 'y':
					working_option(lst, 's')
					return 'ok'
				if option == 'n':
					raise EnterFileError() 
	except EnterFileError:
		for file in lst:
			if file[1] == new:
				lst.remove(file)
	finally:
		return 'ok'



def main():
	main_lst = list_files()
	print('Choose filename: movies')
	while True:
		if main_lst:
			print_files(main_lst)
		user_option = choose_option(arg=main_lst)
		if user_option == 'a':
			main_lst.append(list_files('a'))
			main_lst.sort(key=lambda x: x[0])
		elif user_option == 'd':
			main_lst = working_option(main_lst, 'd')
		elif user_option == 's':
			main_lst = working_option(main_lst, 's')
		elif user_option == 'q':
			check_res = check_save(main_lst)
			break
			



main()





















































# def list_files(new=False):
# 	lst_files = [x for x in os.listdir("./movies") if x.endswith('.txt')]
# 	if new:
# 		input_file = input('Введите название файла с расширением .txt: ')
# 		if input_file.endswith('.txt'):
# 			lst_files.append(input_file)
# 	return lst_files




# def option_user(arg):
# 	while True:
# 		if arg == []:
# 			print('{:-^40}'.format('no items are in the list'))
# 			option = '[A]dd [Q]uit [a]'
# 			just_option = list("AaQq")
# 			input_option = input(option+" ")
# 			if input_option not in  just_option:
# 				print("ERROR: invalid choice enter one of 'AaQq'")		
# 			else:
# 				return input_option
# 		else:
# 			option = '[A]dd [D]elete [S]ave [Q]uit [a]'
# 			just_option = list("AaDdSsQq")
# 			input_option = input(option+" ")
# 			if input_option not in  just_option:
# 				print("ERROR: invalid choice enter one of 'AaDdSsQq'")		
# 			else:
# 				return input_option


# def main():
# 	print('Choose filename: movies')
# 	while True:
# 		lst_files = list_files()
# 		print('1', lst_files)
# 		option = option_user(lst_files).lower()
# 		if option == 'a':
# 			list_files(new='True')



# main()


























# def main():
# 	lst_files = list_files()
# 	try:
# 		if lst_files:
# 			for file in lst_files:
# 				print("Number file of {0} name file: {1}".format(lst_files.index(file) + 1, file))
# 				input_file_number = input('Enter number file: ')
# 				if int(input_file_number) > 0:
# 					reed_file(file)
# 				else:
# 					raise EnterFileError()		
# 		else:
# 			print('{:-^40}'.format('no items are in the list'))
# 			raise EnterFileError()
# 	except EnterFileError:		
# 		option = option_user('empty').lower()
# 		if option == 'a':
# 			list_files(new=True)
# 		if option == 'q':
# 			print('exit ;)')


