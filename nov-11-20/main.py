import random


def iter_dice(dice: str):
    op = "+"
    elem = ""
    for ch in dice:
        if ch not in ("+", "-"):
            elem += ch
        else:
            yield op, elem
            op, elem = ch, ""
    yield op, elem


def resolve(elem: str) -> int:
    if "d" in elem.casefold():
        dnum, dtype = map(int, elem.split("d"))
        return sum(random.randint(1, dtype) for i in range(dnum))
    else:
        return int(elem)


def roll(dice: str) -> int:
    total = 0
    for op, elem in iter_dice(dice):
        if op == "+":
            total += resolve(elem)
        else:
            total -= resolve(elem)
    return total


rollN = lambda n: lambda s: [roll(s) for _ in range(n)]

if __name__ == "__main__":
    """
    $ python main.py
    mix: max:331 min:240 avg:283.512
    ed: max:292 min:214 avg:251.248
    """

    s = {
        "mix": "8d10+88+8d6+4d6+20+22+2d6+2d8",
        "ed": "12d10+132+12d6",
        "title": "1d6",
    }

    r1000 = rollN(10000)

    for k, v in s.items():
        r = r1000(v)
        print(f"{k}: max:{max(r)} min:{min(r)} avg:{sum(r)/len(r)}")


class Dice:
    def __init__(self, dice: str):
        pass

    def add(self, dice: str):
        pass

    def roll(self):
        pass

    def roll_many(self, n):
        pass

    def range(self):
        pass

    def avg(self):
        pass