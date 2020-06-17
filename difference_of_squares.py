def square_of_sum(number):
    suma = 0
    for i in range(number+1):
        suma += i
    return suma**2

def sum_of_squares(number):
    suma = 0
    for i in range(number+1):
        suma += i**2
    return suma


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
