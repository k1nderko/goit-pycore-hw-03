import random


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:

    if not (1 <= min_val <= max_val <= 1000) or quantity > (max_val - min_val + 1):
        return []
    
    random_numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    return sorted(random_numbers)

print(get_numbers_ticket(1, 49, 6))