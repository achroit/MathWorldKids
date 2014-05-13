import random


def add_task(difficulty=1):
    #TODO: disallow the same 2 answers,
    #TODO prevent two times the same task
    #TODO: remove the overwhelming presence of 0's
    operand_1 = 0
    operand_2 = 0
    option_1 = 0
    option_2 = 0
    option_3 = 0
    option_4 = 0
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


def sub_task(difficulty=1):
    #TODO: disallow the same 2 answers,
    #TODO prevent two times the same task
    #TODO: remove the overwhelming presence of 0's
    operand_1 = 0
    operand_2 = 0
    option_1 = 0
    option_2 = 0
    option_3 = 0
    option_4 = 0
    if difficulty == 1:
        operand_1 = random.randint(0, 5)
        operand_2 = random.randint(0, 5)
        operands = [operand_1, operand_2]
        operands = sorted(operands, reverse=True)
        option_1 = operands[0] - operands[1]
        option_2 = abs(random.randint(0, 5) - random.randint(0, 5))
        option_3 = abs(random.randint(0, 5) - random.randint(0, 5))
        option_4 = abs(random.randint(0, 5) - random.randint(0, 5))
    elif difficulty == 2:
        operand_1 = random.randint(0, 10)
        operand_2 = random.randint(0, 10)
        operands = [operand_1, operand_2]
        operands = sorted(operands, reverse=True)
        option_1 = operands[0] - operands[1]
        option_2 = abs(random.randint(0, 10) - random.randint(0, 10))
        option_3 = abs(random.randint(0, 10) - random.randint(0, 10))
        option_4 = abs(random.randint(0, 10) - random.randint(0, 10))
    elif difficulty == 3:
        operand_1 = random.randint(0, 15)
        operand_2 = random.randint(0, 10)
        operands = [operand_1, operand_2]
        operands = sorted(operands, reverse=True)
        option_1 = operands[0] - operands[1]
        option_2 = abs(random.randint(0, 15) - random.randint(0, 10))
        option_3 = abs(random.randint(0, 15) - random.randint(0, 10))
        option_4 = abs(random.randint(0, 15) - random.randint(0, 10))
    elif difficulty == 4:
        operand_1 = random.randint(0, 20)
        operand_2 = random.randint(0, 15)
        operands = [operand_1, operand_2]
        operands = sorted(operands, reverse=True)
        option_1 = operands[0] - operands[1]
        option_2 = abs(random.randint(0, 20) - random.randint(0, 15))
        option_3 = abs(random.randint(0, 20) - random.randint(0, 15))
        option_4 = abs(random.randint(0, 20) - random.randint(0, 15))
    elif difficulty == 5:
        operand_1 = random.randint(0, 25)
        operand_2 = random.randint(0, 20)
        operands = [operand_1, operand_2]
        operands = sorted(operands, reverse=True)
        option_1 = operands[0] - operands[1]
        option_2 = abs(random.randint(0, 25) - random.randint(0, 20))
        option_3 = abs(random.randint(0, 25) - random.randint(0, 20))
        option_4 = abs(random.randint(0, 25) - random.randint(0, 20))
    elif difficulty == 6:
        operand_1 = random.randint(0, 50)
        operand_2 = random.randint(0, 15)
        operands = [operand_1, operand_2]
        option_1 = operands[0] - operands[1]
        option_2 = random.randint(0, 50) - random.randint(0, 15)
        option_3 = random.randint(0, 50) - random.randint(0, 15)
        option_4 = random.randint(0, 50) - random.randint(0, 15)
    elif difficulty == 7:
        operand_1 = random.randint(0, 75)
        operand_2 = random.randint(0, 25)
        operands = [operand_1, operand_2]
        option_1 = operands[0] - operands[1]
        option_2 = random.randint(0, 75) - random.randint(0, 25)
        option_3 = random.randint(0, 75) - random.randint(0, 25)
        option_4 = random.randint(0, 75) - random.randint(0, 25)
    elif difficulty == 8:
        operand_1 = random.randint(0, 100)
        operand_2 = random.randint(0, 50)
        operands = [operand_1, operand_2]
        option_1 = operands[0] - operands[1]
        option_2 = random.randint(0, 100) - random.randint(0, 50)
        option_3 = random.randint(0, 100) - random.randint(0, 50)
        option_4 = random.randint(0, 100) - random.randint(0, 50)
    elif difficulty == 9:
        operand_1 = random.randint(0, 500)
        operand_2 = random.randint(0, 500)
        operands = [operand_1, operand_2]
        option_1 = operands[0] - operands[1]
        option_2 = random.randint(0, 500) - random.randint(0, 500)
        option_3 = random.randint(0, 500) - random.randint(0, 500)
        option_4 = random.randint(0, 500) - random.randint(0, 500)
    elif difficulty >= 10:
        operand_1 = random.randint(0, 1000)
        operand_2 = random.randint(0, 1000)
        operands = [operand_1, operand_2]
        option_1 = operands[0] - operands[1]
        option_2 = random.randint(0, 1000) - random.randint(0, 1000)
        opti
        on_3 = random.randint(0, 1000) - random.randint(0, 1000)
        option_4 = random.randint(0, 1000) - random.randint(0, 1000)

    answers = [option_1, option_2, option_3, option_4]
    print(operands)
    answers.sort()
    whole_task = operands + answers
    return whole_task


def multi_task(difficulty=1):
    #TODO: disallow the same 2 answers,
    #TODO prevent two times the same task
    #TODO: remove the overwhelming presence of 0's
    operand_1 = 0
    operand_2 = 0
    option_1 = 0
    option_2 = 0
    option_3 = 0
    option_4 = 0
    if difficulty == 1:
        operand_1 = random.randint(0, 2)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 2) * random.randint(0, 10)
        option_3 = random.randint(0, 2) * random.randint(0, 10)
        option_4 = random.randint(0, 2) * random.randint(0, 10)
    elif difficulty == 2:
        operand_1 = random.randint(0, 3)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 3) * random.randint(0, 10)
        option_3 = random.randint(0, 3) * random.randint(0, 10)
        option_4 = random.randint(0, 3) * random.randint(0, 10)
    elif difficulty == 3:
        operand_1 = random.randint(0, 4)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 4) * random.randint(0, 10)
        option_3 = random.randint(0, 4) * random.randint(0, 10)
        option_4 = random.randint(0, 4) * random.randint(0, 10)
    elif difficulty == 4:
        operand_1 = random.randint(0, 5)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 5) * random.randint(0, 10)
        option_3 = random.randint(0, 5) * random.randint(0, 10)
        option_4 = random.randint(0, 5) * random.randint(0, 10)
    elif difficulty == 5:
        operand_1 = random.randint(0, 6)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 6) * random.randint(0, 10)
        option_3 = random.randint(0, 6) * random.randint(0, 10)
        option_4 = random.randint(0, 6) * random.randint(0, 10)
    elif difficulty == 6:
        operand_1 = random.randint(0, 7)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 7) * random.randint(0, 10)
        option_3 = random.randint(0, 7) * random.randint(0, 10)
        option_4 = random.randint(0, 7) * random.randint(0, 10)
    elif difficulty == 7:
        operand_1 = random.randint(0, 8)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 8) * random.randint(0, 10)
        option_3 = random.randint(0, 8) * random.randint(0, 10)
        option_4 = random.randint(0, 8) * random.randint(0, 10)
    elif difficulty == 8:
        operand_1 = random.randint(0, 9)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 9) * random.randint(0, 10)
        option_3 = random.randint(0, 9) * random.randint(0, 10)
        option_4 = random.randint(0, 9) * random.randint(0, 10)
    elif difficulty == 9:
        operand_1 = random.randint(0, 10)
        operand_2 = random.randint(0, 10)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 10) * random.randint(0, 10)
        option_3 = random.randint(0, 10) * random.randint(0, 10)
        option_4 = random.randint(0, 10) * random.randint(0, 10)
    elif difficulty >= 10:
        operand_1 = random.randint(0, 12)
        operand_2 = random.randint(0, 12)
        option_1 = operand_1 * operand_2
        option_2 = random.randint(0, 12) * random.randint(0, 12)
        option_3 = random.randint(0, 12) * random.randint(0, 12)
        option_4 = random.randint(0, 12) * random.randint(0, 12)
    operands = [operand_1, operand_2]
    answers = [option_1, option_2, option_3, option_4]
    random.shuffle(operands)
    answers.sort()
    whole_task = operands + answers
    return whole_task


def div_task(difficulty=1):
    values1 = multi_task(difficulty)
    values2 = multi_task(difficulty)
    values3 = multi_task(difficulty)
    values4 = multi_task(difficulty)

    if values1[0] == 0:
        values1[0] = 1
    elif values1[1] == 0:
        values1[1] = 1

    operand1 = values1[0] * values1[1]
    if random.randint(0, 1):
        operand2 = values1[0]
        solution = values1[1]
    else:
        operand2 = values1[1]
        solution = values1[0]


    return[operand1, operand2] + sorted([solution, values2[random.randint(0, 1)],
                                    values3[random.randint(0, 1)], values4[random.randint(0, 1)]])


