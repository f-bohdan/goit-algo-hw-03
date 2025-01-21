import random


def get_numbers_ticket(min, max, quantity):
    numbers = []
    # check for params
    if min > 0 and max < 1000 and min < quantity < max:
        # creating list of random numbers
        numbers = random.sample(range(min, max), quantity)
    # sorting
    numbers.sort()
    return numbers
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)