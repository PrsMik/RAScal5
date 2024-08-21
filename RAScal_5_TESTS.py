import unittest
from RAScal_5_INPUT import *
from RAScal_5_CONVERT import *
from RAScal_5_DEC_FUNC import *
from RAScal_5_CODE_FUNC import *


class Test(unittest.TestCase):
    def test_HexToBin(self):
        self.assertEqual(hex_to_bin('ff'), '11111111')

    def test_IsANumber(self):
        self.assertEqual(is_a_number('12.39'), True)
        self.assertEqual(is_a_number('12A39'), False)

    def test_InputValue(self):
        self.assertEqual(input_value(1, 0, '21'), (True, 'None'))

        self.assertEqual(input_value(0, 0, '21'), (False, '01'))
        self.assertEqual(input_value(2, 0, '21'), (False, '02'))
        self.assertEqual(input_value(3, 0, '21'), (False, '02'))
        self.assertEqual(input_value(2, 1, ''), (False, '03'))

        self.assertEqual(input_value(1, 1, '--21'), (False, '10'))
        self.assertEqual(input_value(1, 1, '+0'), (False, '11'))
        self.assertEqual(input_value(1, 1, '1.2'), (False, '12'))
        self.assertEqual(input_value(1, 1, '9223372036854775808'), (False, '13'))

        self.assertEqual(input_value(2, 1, '1110A'), (False, '20'))
        self.assertEqual(input_value(2, 1,
                                     '10101101101011011010110110101101101011011010110110101101101011011'),
                         (False, '21'))
        self.assertEqual(input_value(2, 1, '1'), (False, '22'))
        self.assertEqual(input_value(2, 2, '11111111'), (False, '23'))
        self.assertEqual(input_value(2, 3, '10000000'), (False, '24'))

        self.assertEqual(input_value(3, 1, '1F'), (False, '30'))
        self.assertEqual(input_value(3, 1, 'fffffffffffffffff'), (False, '31'))
        self.assertEqual(input_value(3, 2, 'ffff'), (False, '32'))
        self.assertEqual(input_value(3, 3, '80'), (False, '33'))

    def test_Convert(self):
        self.assertEqual(convert_value(1, 0, 0), [('Прямой', '00000000', '00'),
                                                  ('Обратный', '00000000', '00'),
                                                  ('Дополнительный', '00000000', '00')])
        self.assertEqual(convert_value(1, 0, 1), [('Прямой', '00000001', '01'),
                                                  ('Обратный', '00000001', '01'),
                                                  ('Дополнительный', '00000001', '01')])
        self.assertEqual(convert_value(1, 0, -1), [('Прямой', '10000001', '81'),
                                                   ('Обратный', '11111110', 'fe'),
                                                   ('Дополнительный', '11111111', 'ff')])

        self.assertEqual(convert_value(2, 1, '11110000'), [('11110000', '-112')])
        self.assertEqual(convert_value(2, 2, '11110000'), [('11110000', '-15')])
        self.assertEqual(convert_value(2, 3, '11110000'), [('11110000', '-16')])

        self.assertEqual(convert_value(3, 1, 'f0'), [('f0', '-112')])
        self.assertEqual(convert_value(3, 2, 'f0'), [('f0', '-15')])
        self.assertEqual(convert_value(3, 3, 'f0'), [('f0', '-16')])

    def test_CompleteToCell(self):
        self.assertEqual(complete_to_cell('111', '0'), '0000111')
        self.assertEqual(complete_to_cell('111', '1'), '1111111')

    def test_BinToHex(self):
        self.assertEqual(bin_to_hex('11111111'), 'ff')
        self.assertEqual(bin_to_hex('111111110000'), 'ff0')

    def test_NumberToStraight(self):
        self.assertEqual(number_to_straight(127), '01111111')
        self.assertEqual(number_to_straight(-127), '11111111')

    def test_NumberToReverse(self):
        self.assertEqual(number_to_straight(127), '01111111')
        self.assertEqual(number_to_reverse(-127), '10000000')

    def test_NumberToAdditional(self):
        self.assertEqual(number_to_straight(127), '01111111')
        self.assertEqual(number_to_additional(-127), '10000001')

    def test_StraightToNumber(self):
        self.assertEqual(straight_to_number('01111111'), 127)
        self.assertEqual(straight_to_number('11111111'), -127)

    def test_ReverseToNumber(self):
        self.assertEqual(reverse_to_number('01111111'), 127)
        self.assertEqual(reverse_to_number('10000000'), -127)

    def test_AdditionalToReverse(self):
        self.assertEqual(reverse_to_number('01111111'), 127)
        self.assertEqual(additional_to_number('10000001'), -127)
