def template_operation(_operation):
    if _operation == '+':
        return lambda _num1, _num2: f'{_num1} + {_num2} = {_num1 + _num2}'
    elif _operation == '-':
        return lambda _num1, _num2: f'{_num1} - {_num2} = {_num1 - _num2}'
    elif _operation == '*':
        return lambda _num1, _num2: f'{_num1} * {_num2} = {_num1 * _num2}'
    elif _operation == '/':
        return lambda _num1, _num2: f'{_num1} / {_num2} = {_num1 / _num2}'
    elif _operation == '**':
        return lambda _num1, _num2: f'{_num1} ** {_num2} = {_num1 ** _num2}'
    elif _operation == '//':
        return lambda _num1, _num2: f'{_num1} // {_num2} = {_num1 // _num2}'
    elif _operation == '%':
        return lambda _num1, _num2: f'{_num1} % {_num2} = {_num1 % _num2}'
    else:
        return lambda _num1, _num2: f'{_num1} {_operation} {_num2} = ?'


some_operation = input('Enter operation: ')
func_calc = template_operation(some_operation)
some_num1 = int(input('Enter first number: '))
some_num2 = int(input('Enter second number: '))
func_calc1 = func_calc(some_num1, some_num2)
print(func_calc1)
