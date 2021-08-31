# Division by two numbers
def division(number_1, number_2):
    if float(number_1) or float(number_2):
        result = number_1 / number_2
    else:
        result = number_1 // number_2
    return result
