import random


def add_task(difficulty=1):
    a = b = 0
    if difficulty == 1:
        a = random.randint(0, 5)
        b = random.randint(0, 5)
    elif difficulty == 2:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
    elif difficulty == 3:
        a = random.randint(0, 15)
        b = random.randint(0, 15)
    elif difficulty == 4:
        a = random.randint(0, 20)
        b = random.randint(0, 20)
    elif difficulty == 5:
        a = random.randint(0, 25)
        b = random.randint(0, 25)
    elif difficulty == 6:
        a = random.randint(0, 50)
        b = random.randint(0, 15)
    elif difficulty == 7:
        a = random.randint(0, 75)
        b = random.randint(0, 75)
    elif difficulty == 8:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
    elif difficulty == 9:
        a = random.randint(0, 500)
        b = random.randint(0, 500)
    elif difficulty >= 10:
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
    return a, b