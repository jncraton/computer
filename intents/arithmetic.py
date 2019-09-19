import re

def compute_addition_result(intent):
    """ Get the result of an intent with an addition expression 

    >>> compute_addition_result('What is 2+3?')
    '2 + 3 = 5'
    
    >>> compute_addition_result('What is 8 plus 16?')
    '8 + 16 = 24'
    """

    match = re.search('(?P<operand1>\d+) *(\+|plus) *(?P<operand2>\d+)', intent, flags=re.I)

    if not match:
        raise ValueError(f'Unable to parse "{intent}" as addition expression')

    operand1 = int(match.group('operand1'))
    operand2 = int(match.group('operand2'))
    result = operand1 + operand2

    return f'{operand1} + {operand2} = {result}'

intents = {
    "\d+ *(\+|plus) *\d+": compute_addition_result,
}
