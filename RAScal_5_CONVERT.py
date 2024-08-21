from RAScal_5_CODE_FUNC import *
from RAScal_5_DEC_FUNC import *
from RAScal_5_INPUT import hex_to_bin

# ФУНКЦИЯ ПЕРЕВОДА ЗНАЧЕНИЯ


def convert_value(convert_arg, code_type, value):  # перевод значения
    # принимает: тип перевода (int), тип кода (int), значение для перевода (str)
    # возвращает: список кортежей со значениями прямого, обратного, дополнительного кодов (str) или
    # список, содержащий кортеж со значениями изначального кода и соответствующего числа (str)
    match convert_arg:  # аргумент типа перевода
        case 1:
            # Перевод из десятичного числа в коды
            value = int(value)
            if value == 0:
                value_converted = [('Прямой', '00000000', '00'), ('Обратный', '00000000', '00'),
                                   ('Дополнительный', '00000000', '00')]
            else:
                # ПЕРЕВОД В ПРЯМОЙ КОД
                number_straight_bin = number_to_straight(value)
                number_straight_hex = bin_to_hex(number_straight_bin)

                # ПЕРЕВОД В ОБРАТНЫЙ КОД
                number_reverse_bin = number_to_reverse(value)
                number_reverse_hex = bin_to_hex(number_reverse_bin)

                # ПЕРЕВОД В ДОПОЛНИТЕЛЬНЫЙ КОД
                number_additional_bin = number_to_additional(value)
                number_additional_hex = bin_to_hex(number_additional_bin)

                # ВЫВОД В ТАБЛИЦЕ
                value_converted = [('Прямой', number_straight_bin, number_straight_hex),
                                   ('Обратный', number_reverse_bin, number_reverse_hex),
                                   ('Дополнительный', number_additional_bin, number_additional_hex)]
        case 2:
            # Перевод из двоичного кода в десятичное число
            match code_type:
                case 1:
                    number_dec = straight_to_number(value)  # перевод из прямого
                    value_converted = [(value, str(number_dec))]
                case 2:
                    number_dec = reverse_to_number(value)  # перевод из обратного
                    value_converted = [(value, str(number_dec))]
                case 3:
                    number_dec = additional_to_number(value)  # перевод из дополнительного
                    value_converted = [(value, str(number_dec))]
        case 3:
            # Перевод из шестнадцатеричного кода в десятичное
            match code_type:
                case 1:
                    number_dec = straight_to_number(hex_to_bin(value))  # перевод из прямого
                    value_converted = [(value, str(number_dec))]
                case 2:
                    number_dec = reverse_to_number(hex_to_bin(value))  # перевод из обратного
                    value_converted = [(value, str(number_dec))]
                case 3:
                    number_dec = additional_to_number(hex_to_bin(value))  # перевод из дополнительного
                    value_converted = [(value, str(number_dec))]
    return value_converted
