from logger import input_data, print_data, update_data, delete_data

def interface():
    print("Привет! Вы попали в бот справочник! Выберите, что Вы хотите сделать:\nHi! You are in the bot directory! Choose what you want to do:\n 1- Записать данных/Write data \n 2- Вывести данных/Output data \n 3- Изменить данные/Change data \n 4- Удалить данные/Delete data")
    command = int(input('Введите число/Input number: '))

    while command != 1 and command !=2 and command !=3 and command !=4:
        print("Ошибка ввода!/Input error!")
        command = int(input('Введите число/Input number: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data() 
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data() 
       
    






