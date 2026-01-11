class Numerals:
    def __init__(self):
        self.roman = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X'
        }

    def convert(self):
        num = input('Enter a number from 1 to 10 to convert it into a Roman Numeral: ')
        if num == '1':
            print('The Roman version is I')
        elif num == '2':
            print('The Roman version is II')
        elif num == '3':
            print('The Roman version is III')
        elif num == '4':
            print('The Roman version is IV')
        elif num == '5':
            print('The Roman version is V')
        elif num == '6':
            print('The Roman version is VI')
        elif num == '7':
            print('The Roman version is VII')
        elif num == '8':
            print('The Roman version is VIII')
        elif num == '9':
            print('The Roman version is IX')
        elif num == '10':
            print('The Roman version is X')
        else:
            print('Please enter a valid number between 1 and 10.')

numeral_converter = Numerals()
numeral_converter.convert_to_roman()
