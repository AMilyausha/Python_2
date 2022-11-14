def get_Data():
    data = []
    surname = input('Введите фамилию: ')
    data.append(surname)
    name = input('Введите имя: ')
    data.append(name)
    mname = input('Введите отчество: ')
    data.append(mname)
    number = input('Введите номер телефона: ')
    data.append(number)
    return data