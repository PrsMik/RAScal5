def hex_to_bin(number_hex):  # перевод из 16ричного в двоичный код
    # принимает: строку со значением 16ричного кода числа(str)
    # возвращает: строку со значением двоичного кода числа (str)
    number_conv_bin = bin(int(number_hex, 16))[2:]  # перевод в 10, затем в двоичную
    if len(number_conv_bin) % 4 != 0:  # добавление нулей, потерянных при переводе
        number_conv_bin = '0' * (4 - len(number_conv_bin) % 4) + number_conv_bin
    return number_conv_bin  # переведённый код


def is_a_number(numb_str):  # проверка на отсутствие знаков не числа
    # принимает: строку со значением десятичного числа (str)
    # возвращает: ложь (bool), если есть знаки не числа или истина (bool), если их нет
    for symbol in numb_str:
        if symbol not in '1234567890.,':
            return False  # возвращается если есть знаки не числа

    return True  # возвращается если есть знаки не числа


def input_value(convert_type, code_type, valinput):  # проверка введённой строки на правильности
    # принимает: тип перевода (int), тип кода (int), введённое значение (str)
    # возвращает: кортеж, содержащий флаг правильности перевода (bool) и тип ошибки (str)
    correct_input = False  # флаг правильности ввода строки
    error_type = 'None'  # строка с типом ошибки
    if convert_type == 0:
        error_type = '01'  # не введён тип перевода
    elif (convert_type == 2 or convert_type == 3) and code_type == 0:
        error_type = '02'  # не введён тип кода
    elif len(valinput) < 1:
        error_type = '03'  # не введено значение
    else:
        if convert_type == 1:
            number_dec_str = valinput
            correct_input = True
            if (number_dec_str[0] in '+-' and not is_a_number(number_dec_str[1:])) or \
                    (number_dec_str[0] not in '+-' and not is_a_number(
                        number_dec_str)):  # условие наличия недопустимых знаков
                error_type = '10'
                correct_input = False
            elif (number_dec_str[0] in '+-' and number_dec_str[1] == '0') or \
                    (len(number_dec_str) > 1 and number_dec_str[0] == '0'):  # условие начала числа с нуля
                error_type = '11'
                correct_input = False
            elif (',' in number_dec_str) or ('.' in number_dec_str):  # условие наличия точки в числе
                error_type = '12'
                correct_input = False
            elif (int(number_dec_str) < -(2 ** 63 - 1)) or (int(number_dec_str) > (2 ** 63 - 1)):  # условие выхода
                # за диапазон
                error_type = '13'
                correct_input = False
        elif convert_type == 2:
            bin_code_str = valinput
            correct_input = True  # флаг правильности ввода цифр кода
            for k in bin_code_str:  # проверка на отсутствие недопустимых символов
                if k not in '01':
                    correct_input = False
            if not correct_input:
                error_type = '20'  # присутствуют недопустимые символы
                correct_input = False
            elif len(bin_code_str) > 64:  # код длиннее максимальной длины
                error_type = '21'
                correct_input = False
            elif len(bin_code_str) < 2:  # код из 2 символов - минимально возможный
                error_type = '22'
                correct_input = False
            elif code_type == 2 and ('0' not in bin_code_str):  # обратный код не может состоять только из 1
                error_type = '23'
                correct_input = False
            elif code_type == 3 and ('1' not in bin_code_str[1:] and bin_code_str[0] == '1'):  # доп код не может
                # состоять только из 0
                error_type = '24'
                correct_input = False
        else:
            hex_code_str = valinput
            correct_input = True  # флаг правильности ввода цифр кода
            for k in hex_code_str:  # проверка на отсутствие недопустимых символов
                if k not in '0123456789abcdef':
                    correct_input = False
            if not correct_input:
                error_type = '30'  # присутствуют недопустимые символы
                correct_input = False
            elif len(hex_code_str) > 16:  # код длиннее максимальной длины
                error_type = '31'
                correct_input = False
            elif code_type == 2 and (not ('0' in hex_to_bin(hex_code_str))):  # обратный код не может
                # состоять только из 1
                error_type = '32'
                correct_input = False
            elif code_type == 3 and ('1' not in hex_to_bin(hex_code_str)[1:] and
                                     hex_to_bin(hex_code_str)[0] == '1'):  # доп код не может состоять только из 0
                error_type = '33'
                correct_input = False
    res = (correct_input, error_type)  # верен ли ввод и тип ошибки
    return res
