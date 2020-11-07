import random


def split_dice(dice: str):
    dice = dice.lowercase()
    first, second = dice.split("d")
    dnum = int(first)

    sep = second.find("+") or second.find("-")

    dtype = int(second[:sep])
    cmod = int(second[sep:])

    return dnum, dtype, cmod


def roll(dice: str) -> int:
    # Step 1: split/parse
    dnum, dtype, cmod = split_dice(dice)

    # Step 2: sum dice rolls
    total = 0
    for i in range(dnum):
        n = random.randint(1, dtype + 1)
        total += n

    # Step 3: apply modifier
    result = total + cmod

    # Output
    return result
