# Задание 14.01
# Создать бесконечный генератор случайных чисел.
# Использовать в генераторе временную задержку
# from time import sleep
# import random
# from time import sleep
#
# def generator():
#     while True:
#         yield random.random()
#         yield '_____'
#         sleep(1)
#
#
# g = generator()
# for i in g:
#     print(i)

# Задание 14.02
# Модифицировать генератор, чтобы генератор принимал диапазон случайных
# чисел и чтобы последующее случайное число лежало в диапазоне
# смещенном на n.
# import random
# from time import sleep
#
# def generator():
#     while True:
#         yield random.uniform(n+1,n+10)
#         yield '_____'
#         sleep(5)
#
# n = 0
# g = generator()
# for i in g:
#     n += 10
#     print(i)

# Задание 14.03
# Создать скрипт, который при запуске принимает
# неопределенное количество аргументов и считает сумму
# тех из них, что являются цифрами.
# import sys
# print(sys.argv)
# var = 0
# for i in sys.argv:
#     if i.isdigit():
#         var = var + int(i)
# print("Сумма аргументов, которые являются цифрами равна: ", var)

# Задание 14.04
# Создать скрипт, который принимает имя фамилию и
# возраст и дописывает их в csv файл
# import sys
# import argparse
# import csv
#
# print(sys.argv)
# parser = argparse.ArgumentParser()
# parser.add_argument('-fn', '--first-name', required=True)
# parser.add_argument('-ln', '--last-name', required=True)
# parser.add_argument('-age', '--age', required=True)
# args = parser.parse_args()
# print(args)
# row_first_name = ['First name: ', args.first_name]
# row_last_name = ['Last name: ', args.last_name]
# row_age = ['Age: ', args.age]
# with open("FIO.csv", 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(row_first_name)
#     csvwriter.writerow(row_last_name)
#     csvwriter.writerow(row_age)
# print("The following info has been written to the file FIO.csv")
# print('First name:', args.first_name)
# print('Last name:', args.last_name)
# print('Age:', args.age)

# Задание 14.05
# Создать скрипт, который принимает имя папки и создает
# ее рядом со скриптом
# Вызов к Терминале python3 main.py -dir_name dir34
# import sys
# import argparse
# import os
#
# print(sys.argv)
# parser = argparse.ArgumentParser()
# parser.add_argument('-dir_name', required=True)
# args = parser.parse_args()
# print(args)
# dir_name = (args.dir_name)
# os.mkdir(dir_name)

# Задание 14.06
# Дописать скрипт. Программа принимает имя папки и имя
# файла. Создает папку и создает в ней файл.
# Вызов к Терминале python3 main.py -dir_name dir34 -file_name file.txt
# import sys
# import argparse
# import os
#
# print(sys.argv)
# parser = argparse.ArgumentParser()
# parser.add_argument('-dir_name', required=True)
# parser.add_argument('-file_name', required=True)
# args = parser.parse_args()
# print(args)
# dir_name = (args.dir_name)
# file_name = (args.file_name)
# os.mkdir(dir_name)
# os.chdir(dir_name)
# open(file_name, "w")

# Задание 14.07
#
# Дописать скрипт. Программа принимает имя папки и имя
# файла с расширением. Создает папку и создает в ней
# файл. Если расширение файла py - записывает в файл
# следующее:

# def main():
# pass
#
# if __name__ == '__main__':
# main()

# Вызов к Терминале python3 main.py -dir_name dir34 -file_name file.py

import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dir_name', required=True)
parser.add_argument('-file_name', required=True)
args = parser.parse_args()
dir_name = (args.dir_name)
file_name = (args.file_name)
os.mkdir(dir_name)
os.chdir(dir_name)
# open(file_name, "w")
if file_name.endswith('.py'):
    with open(file_name, "w") as file:
        file.writelines("def main():\npass\n\nif __name__ == '__main__':\nmain()")
else:
    print("Файл не имеет расширения .py")
print("Задание выполнено.")