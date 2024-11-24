import random

saldo: int = 1000
target: int = 1350
simulations: int = 1000000

wins: int = 0
losses: int = 0

black_numbers: int = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers: int = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

first_column: int = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
second_column: int = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
third_column: int = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]


def spin():
    return random.randint(0,36)

for i in range(simulations):
    while (saldo > 4) and (saldo < target):
        number = spin()

        if number in third_column:
            saldo += 200
        else:
            saldo -= 100

        if number in black_numbers:
            saldo += 150
        else:
            saldo -= 150

    if saldo >= 1350:
        wins += 1
    else:
        losses += 1

    saldo = 1000


print(f"Wins: {wins} \n")
print(f"Losses: {losses} \n")
