from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор:  '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding= 'utf-8') as file:
            file.write(
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding= 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')



def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding= 'utf-8') as file:
       data = file.readlines()
       print(''.join(data))

    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding= 'utf-8') as file:
       data = file.readlines()
       print(''.join(data))






def copy_data():
    source_file_name = 'data_first_variant.csv'
    destination_file_name = 'data_second_variant.csv'

    with open(source_file_name, 'r', encoding='utf-8') as source_file:
        with open(destination_file_name, 'a', encoding='utf-8') as destination_file:
            lines = source_file.readlines()

            line_numbers_str = input("Введите номера строк через запятую: ")
            line_numbers = [int(num.strip()) for num in line_numbers_str.split(',')]

            for line_number in line_numbers:
                if 1 <= line_number <= len(lines):
                    words = lines[line_number - 1].strip().split()
                    data_row = "".join(words)
                    destination_file.write(data_row + ';')
                else:
                    print("Неверный номер строки: ", line_number)

            destination_file.seek(destination_file.tell() - 1, 0)
            destination_file.truncate()
            destination_file.write('\n\n')

            print("Данные успешно добавлены в файл '{}'.".format(destination_file_name))

















#   current_group.append(line)
#                 if len(current_group) == 4 and current_group[0].isdigit() and int(current_group[0]) == number:
#                     found = True
#                     file_write.write(';'.join(current_group[1:]) + '\n')
#                     file_write.write('\n')


# def copy_data(copy_number, copy_from, target_file, source_file, count_lines, number):

#     if from_variant == 1:
#         source_file = 'data_first_variant.csv'
#         target_file = 'data_second_variant.csv'
#     elif from_variant == 2:
#         source_file = 'data_second_variant.csv'
#         target_file = 'data_first_variant.csv'
#     else:
#         print("Некорректный выбор варианта копирования.")
#         return

#     with open(source_file, 'r') as file_read, open(target_file, 'a', encoding='utf-8') as file_write:
#         current_group = []
#         found = False

#         for line in file_read:
#             while copy_number != count_lines - 1:
#                 count_lines += 1

#             if from_variant == 1 and copy_number == count_lines - 1:
#                 current_group.append(line)
#                 file_write.write(';'.join(current_group[1:]) + '\n')
#                 file_write.write('\n')

#             elif from_variant == 2:
#                 current_group = [data.strip() for data in line.split(';')]
#                 if len(current_group) == 4 and current_group[0].isdigit() and int(current_group[0]) == number:
#                     found = True
#                     for data in current_group[1:]:
#                         file_write.write(data + '\n')
#                     file_write.write('\n')

#         if not found:
#             print("Данные для числа", number, "не найдены.")


#     copy_user_data_from = print('Выберите действие:\n'
#                             '1 - Копировать из первого варианта во второй\n'
#                             '2 - Копировать из второго варианта в первый')
#     copy_from = int(input('Ваш выбор: '))

#     copy_user_data_number = print('Введите номер копируемого пользователя:')
#     copy_number = int(input('Ваш выбор: '))
#     count_lines = 1

#     if copy_from not in [1, 2]:
#         print("Некорректный выбор действия.")
#     else:
#         try:
#             copy_data(copy_number, copy_from)
#         except ValueError:
#             print("Введите целое число для номера копируемого пользователя.")