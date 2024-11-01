"""
User Stories
 - User can see a display showing the current number entered or the result of the last operation.
 - User can see an entry pad containing buttons for the digits 0-9, operations - '+', '-', '/', and '=', a 'C' button
   (for clear), and an 'AC' button (for clear all).
 - User can enter numbers as sequences up to 8 digits long by clicking on digits in the entry pad. Entry of any digits
   more than 8 will be ignored.
 - User can click on an operation button to display the result of that operation on:
    > the result of the preceding operation and the last number entered OR
    > the last two numbers entered OR
    > the last number entered
 - User can click the 'C' button to clear the last number or the last operation. If the users last entry was an
   operation the display will be updated to the value that preceded it.
 - User can click the 'AC' button to clear all internal work areas and to set the display to 0.
 - User can see 'ERR' displayed if any operation would exceed the 8 digit maximum.

Bonus features
 - User can click a '+/-' button to change the sign of the number that is currently displayed.
 - User can see a decimal point ('.') button on the entry pad to that allows floating point numbers up
   to 3 places to be entered and operations to be carried out to the maximum number of decimal places
   entered for any one number.
"""
import os
from time import sleep


def limpa_tela():
    os.system('cls')


class Calculator:
    def __init__(self):
        self.__operation = 0
        self.__number = ()
        self.__finish = False
        self.__result = 0

        self.__OP_ADDITION = 1
        self.__OP_SUBTRACTION = 2
        self.__OP_DIVISION = 3
        self.__OP_MULTIPLICATION = 4

        self.__errors = []

        self.__operation_list = ['+', '-', '/', '*']

    @property
    def operation_list(self):
        return self.__operation_list


    def __title(self):
        print('---' * 4)
        print('CALCULATOR')
        print('---' * 4)

    def __message_operation(self, value_1='', value_2='', operation='', result=''):
        print('---' * 6)
        print(f'{value_1} {operation} {value_2} = {result}')
        print('---' * 6)

    def __input_number(self):
        tryagain = True
        number = 0

        while tryagain:
            try:
                #limpa_tela()
                number = int(input('Número: '))

                tryagain = False
            except ValueError:
                tryagain = True

        return number

    def __choose_operation(self):
        operations = ('---' * 4 + '\n' +
                     '[1] Addition (+)\n'+
                     '[2] Subtraction (-)\n'+
                     '[3] Division (/)\n'+
                     '[4] Multiplication (*)\n'+
                     '---' * 4 + '\n')

        tryagain = True
        operation = 0

        while tryagain:
            #limpa_tela()
            print(operations)
            operation = input('operation: ')

            tryagain = True if operation not in str([self.__OP_ADDITION, self.__OP_SUBTRACTION, self.__OP_DIVISION, self.__OP_MULTIPLICATION]) else False

        return int(operation)

    def __execute_operation(self):

        errors = ''

        if self.__operation == self.__OP_ADDITION:
            self.__result = self.__number[0] + self.__number[1]
        elif self.__operation == self.__OP_SUBTRACTION:
            self.__result = self.__number[0] - self.__number[1]
        elif self.__operation == self.__OP_DIVISION:
            try:
                self.__result = self.__number[0] / self.__number[1]
            except ZeroDivisionError:
                errors = "It's not possible divide by zero!"
        elif self.__operation == self.__OP_MULTIPLICATION:
            self.__result = self.__number[0] * self.__number[1]

        if errors == '':
            return self.__result
        else:
            self.__errors.append(errors)
            return None

    def __restart(self):
        self.__finish = True if input('Do you want to finish the application? Yes[0] No[Any key]\n:') == '0' else False

    def execute(self):
        while not self.__finish:
            limpa_tela()

            self.__title()
            value_1 = self.__input_number()
            self.__message_operation(str(value_1), '', '', '')

            self.__operation = self.__choose_operation()

            self.__message_operation(str(value_1), '', self.__operation_list[self.__operation-1], '')

            value_2 = self.__input_number()

            self.__number = (value_1, value_2)

            result_operation = self.__execute_operation()

            self.__message_operation(str(self.__number[0]), str(self.__number[1]), self.__operation_list[self.__operation-1], str(result_operation))

            if result_operation is None:
                #Reiniciar processo de escolhar do segundo número
                #ou mostrar opção pra reiniciar cálculo
                pass

            else:
                sleep(2)
                self.__restart()





calc = Calculator()
calc.execute()