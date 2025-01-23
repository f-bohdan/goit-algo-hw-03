import random


def get_numbers_ticket(min, max, quantity):
    numbers = []
    # check for params
    if 0 < min < max < 1000 and 0 < quantity <=(max-min):
        # creating list of random numbers
        numbers = random.sample(range(min, max), quantity)
    elif min > max:
        print("Вказано не вірне значення MIN")
        return None
    elif not (0<quantity <=(max-min)):
        print("Вказано не вірне значення QUANITY")
        return None
        
    # sorting
    numbers.sort()
    return numbers
    
lottery_numbers = get_numbers_ticket(4, 8, 4)
print("Ваші лотерейні числа:", lottery_numbers)