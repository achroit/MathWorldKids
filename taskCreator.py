import random


def add_task(difficulty=1):
    if difficulty == 1:
        operand_1 = random.randint(0, 5)
        operand_2 = random.randint(0, 5)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 5) + random.randint(0, 5)
        option_3 = random.randint(0, 5) + random.randint(0, 5)
        option_4 = random.randint(0, 5) + random.randint(0, 5)
    elif difficulty == 2:
        operand_1 = random.randint(0, 10)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 10) + random.randint(0, 10)
        option_3 = random.randint(0, 10) + random.randint(0, 10)
        option_4 = random.randint(0, 10) + random.randint(0, 10)
    elif difficulty == 3:
        operand_1 = random.randint(0, 15)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 15) + random.randint(0, 10)
        option_3 = random.randint(0, 15) + random.randint(0, 10)
        option_4 = random.randint(0, 15) + random.randint(0, 10)
    elif difficulty == 4:
        operand_1 = random.randint(0, 20)
        operand_2 = random.randint(0, 15)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 20) + random.randint(0, 15)
        option_3 = random.randint(0, 20) + random.randint(0, 15)
        option_4 = random.randint(0, 20) + random.randint(0, 15)
    elif difficulty == 5:
        operand_1 = random.randint(0, 25)
        operand_2 = random.randint(0, 20)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 25) + random.randint(0, 20)
        option_3 = random.randint(0, 25) + random.randint(0, 20)
        option_4 = random.randint(0, 25) + random.randint(0, 20)
    elif difficulty == 6:
        operand_1 = random.randint(0, 50)
        operand_2 = random.randint(0, 15)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 50) + random.randint(0, 15)
        option_3 = random.randint(0, 50) + random.randint(0, 15)
        option_4 = random.randint(0, 50) + random.randint(0, 15)
    elif difficulty == 7:
        operand_1 = random.randint(0, 75)
        operand_2 = random.randint(0, 25)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 75) + random.randint(0, 25)
        option_3 = random.randint(0, 75) + random.randint(0, 25)
        option_4 = random.randint(0, 75) + random.randint(0, 25)
    elif difficulty == 8:
        operand_1 = random.randint(0, 100)
        operand_2 = random.randint(0, 50)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 100) + random.randint(0, 50)
        option_3 = random.randint(0, 100) + random.randint(0, 50)
        option_4 = random.randint(0, 100) + random.randint(0, 50)
    elif difficulty == 9:
        operand_1 = random.randint(0, 500)
        operand_2 = random.randint(0, 500)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 500) + random.randint(0, 500)
        option_3 = random.randint(0, 500) + random.randint(0, 500)
        option_4 = random.randint(0, 500) + random.randint(0, 500)
    elif difficulty >= 10:
        operand_1 = random.randint(0, 1000)
        operand_2 = random.randint(0, 1000)
        option_1 = operand_1 + operand_2
        option_2 = random.randint(0, 1000) + random.randint(0, 1000)
        option_3 = random.randint(0, 1000) + random.randint(0, 1000)
        option_4 = random.randint(0, 1000) + random.randint(0, 1000)
    operands = [operand_1, operand_2]
    answers = [option_1, option_2, option_3, option_4]
    random.shuffle(operands)
    answers.sort()
    whole_task = operands + answers
    return whole_task