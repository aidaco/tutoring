import random

# roll.py with selected optimizations


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
    total = sum(random.randint(1, dtype + 1) for i in range(dnum))

    # Output
    return total + cmod
