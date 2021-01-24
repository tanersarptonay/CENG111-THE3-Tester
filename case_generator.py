from CENG_111.THE3.the3 import *
import sys
import random
number = 2

sys.setrecursionlimit(10**6)
def randomer(bro, limit):
    global number
    if number > limit:
        return bro
    for i in range(random.choices([1, 2, 3, 4, 5], weights=[5, 4, 3, 2, 1])[0]):
        bro[0].append((random.choices(list(range(1, 10)), weights=list(range(1, 10))[::-1])[0],
                      "a{}".format(str(number))))
        bro.append(["a{}".format(str(number))])
        number += 1

    return [bro[0]] + randomer(bro[1:], limit)


def completer(tree):
    for leaf in tree:
        i = tree.index(leaf)
        if len(leaf) == 1:
            leaf = leaf + [float(random.randint(1, 300))]
        tree[i] = leaf

    return tree


def stock_generator(tree):
    basic_parts = [part[0] for part in tree if type(part[1]) == float]
    stock_capacity = random.randint(0, len(basic_parts) + 5)
    if stock_capacity > len(basic_parts):
        stock = [(random.randint(1, 10), part) for part in basic_parts] + \
                [(random.randint(1, 10), f"a{num}") for num in range(900 + len(basic_parts), 901 + stock_capacity)]
    else:
        stock = [(random.randint(1, 10), basic_parts[index]) for index in range(stock_capacity)]
    return stock


results = []

for num in range(100):
    initial = [["A1"]]
    number = 2
    rawcase = randomer(initial, random.randint(500, 1000))
    case = completer(rawcase)
    # random.shuffle(case)  @TODO: shuffles part_list
    stock = stock_generator(case)
    cp_output = calculate_price(case)
    rp_output = required_parts(case)
    sc_output = stock_check(case, stock)
    results.extend([f"CASE {num + 1}:", "\n", "\n", f">>> {case}", "\n", "\n",
                    f"STOCK {num + 1}:", "\n", "\n", f">>> {stock}", "\n", "\n",
                    f"EXPECTED OUTPUTS OF CASE {num + 1}:", "\n", "\n", f">>> calculate_price = {cp_output}", "\n", "\n",
                    f">>> required_parts = {rp_output}", "\n", "\n", f">>> stock_check = {stock_check(case, stock)}",
                    "\n", "\n", "############################", "\n"])

with open("tester_long.txt", "w", encoding="utf-8") as file:
    file.writelines(results)
    
