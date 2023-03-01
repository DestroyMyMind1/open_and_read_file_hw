# Задача 1, Задача 2

from pprint import pprint

def cook_book_dictionary():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline())
            ingredient_list = []
            for _ in range(ingredient_count):
                ingred = file.readline().strip()
                ingredient_name, quantity, measure = ingred.split(' | ')
                ingredient_list.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': quantity,
                     'measure': measure})
            cook_book[dish_name] = ingredient_list
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    book = cook_book_dictionary()
    dishes_dictionary = {}
    for dish_name in dishes:
        if dish_name in book:
            for ingred in book[dish_name]:
                if ingred['ingredient_name'] in dishes_dictionary:
                    dishes_dictionary[ingred['ingredient_name']]['quantity'] += (int(ingred['quantity']) * person_count)
                else:
                    dishes_dictionary.setdefault(ingred['ingredient_name'], {'quantity': (int(ingred['quantity']) * person_count), 'measure': ingred['measure']})
        else:
            return 'Нет такого блюда!'
    return dishes_dictionary

def result():
    print("Меню = 1 \nРасчёт ингредиентов = 2")
    user_input = input("Выберите цифру: ")
    if user_input == "1":
        pprint(cook_book_dictionary(), sort_dicts=False)
    elif user_input == "2":
        dish_name = input("Введите название блюд (Омлет, Утка по-пекински, Запеченный картофель, Фахитос): ").split(", ")
        person_count = int(input("Количество персон: "))
        pprint(get_shop_list_by_dishes(dish_name, person_count), sort_dicts=False)
    else:
        print('Что то пошло не так :( Введите "1" или "2"')

result()

# Задача 3.

import os

def merging_files(file_list, work_dir):
    file_dict = {}
    for file in file_list:
        with open(os.path.join(work_dir, file), "r", encoding='utf-8') as f:
            result = f.readlines()
            file_dict[file] = (result, len(result))
    sorted_dict = dict(sorted(file_dict.items(), key=lambda item: item[1][1]))
    with open("sorted_dict.txt", "a", encoding='utf-8') as file:
        for key, value in sorted_dict.items():
            file.writelines(f"Файл {key}\nКоличество строк {value[1]}\n")
            file.writelines(value[0])
            file.writelines("\n\n")

if __name__ == "__main__":
    current = os.getcwd()
    folder = "sorted"
    full_path = os.path.join(current, folder)
    all_txt = [files for files in os.listdir(full_path) if files.endswith(".txt")]
    merging_files(all_txt, full_path)