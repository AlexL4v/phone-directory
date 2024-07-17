from data_create import name_data, surname_data, phone_data, adress_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"Выберите формат записи данных/Select the data recording format \n\n"
    f"1 вариант/1 Option: \n "
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 вариант/2 Option: \n"
    f"{name}; {surname}; {phone}; {adress}\n"
    f"Выберите вариант/Select an option: "))

    while var != 1 and var !=2:
        print("Ошибка ввода!/Input error!")
        var = int(input("Введите число/Enter a number: "))

    if var == 1:
        with open('data_first_variantt.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")  
            print("Данные успешно сохранены!\nThe data has been successfully saved!")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {adress}\n\n")
            print("Данные успешно сохранены!\nThe data has been successfully saved!")                

def print_data():
    print('Вывожу данные из файла 1/I output data from file 1: \n')
    with open('data_first_variantt.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))        

    print('Вывожу данные из файла 2/I output data from file 2: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def read_data(file_path, separator):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    if separator == '\n\n':
        records = [record.split('\n') for record in content.split('\n\n') if record]
    else:
        records = [record.split('; ') for record in content.split('\n') if record]
    return records

def write_data(file_path, records, separator):
    with open(file_path, 'w', encoding='utf-8') as file:
        for record in records:
            if separator == '\n\n':
                file.write('\n'.join(record).strip() + '\n\n')
            else:
                file.write('; '.join(record).strip() + '\n')

def display_records(records):
    for index, record in enumerate(records):
        print(f"{index + 1}. {'; '.join(record)}")

def update_data():
    file_choice = input("В каком файле изменить данные? (1 - первый вариант, 2 - второй вариант)\nIn which file should I change the data? (1 - first option, 2 -second option): ")
    separator = '\n\n' if file_choice == '1' else '; '
    file_path = 'data_first_variantt.csv' if file_choice == '1' else 'data_second_variant.csv'

    records = read_data(file_path, separator)
    display_records(records)

    try:
        record_number = int(input('Введите номер записи для изменения:\nEnter the record number to change: ')) - 1
        if 0 <= record_number < len(records):
            new_name = input('Введите новое имя/Enter a new name: ')
            new_surname = input('Введите новую фамилию/Enter a new last name: ')
            new_phone = input('Введите новый телефон/Enter a new phone number: ')
            new_address = input('Введите новый адрес/Enter a new address: ')

            records[record_number] = [new_name, new_surname, new_phone, new_address]
            write_data(file_path, records, separator)
            print('Данные обновлены!\nData updated!')
        else:
            raise IndexError
    except ValueError:
        print("Номер введен не корректно!\nNumber is incorrect!")
    except IndexError:
        print("Несуществующий номер записи!\nA non-existent record number!")

def delete_data():
    file_choice = input("Из какого файла вы хотите удалить данные? (1 - первый вариант, 2 - второй вариант):\nWhich file do you want to delete data from? (1 -first option, 2 - second option): ")
    separator = '\n\n' if file_choice == '1' else '; '
    file_path = 'data_first_variantt.csv' if file_choice == '1' else 'data_second_variant.csv'

    records = read_data(file_path, separator)
    display_records(records)

    try:
        record_number = int(input('Введите номер записи для удаления:\ninput the number of the record to delete: ')) - 1
        if 0 <= record_number < len(records):
            del records[record_number]
            write_data(file_path, records, separator)
            print('Запись удалена!\nRecord  deleted!')
        else:
            raise IndexError
    except ValueError:
        print("Номер введен не корректно!\nNumber is incorrect!")
    except IndexError:
        print("Несуществующий номер записи!\nA non-existent record number!") 