import datetime
from CENG_111.THE3.the3 import *

print("getting the cases and answers...")

with open("tester.txt", "r", encoding="utf-8") as file:  # Input the name of the .txt file you want to use
    answers = file.readlines()

cases = [eval(case[4:-1]) for case in answers[2::17]]
stocks = [eval(stock[4:-1]) for stock in answers[6::17]]
answers_calculate_price = [eval(cp[22:-1]) for cp in answers[10::17]]
answers_required_parts = [eval(rp[21:-1]) for rp in answers[12::17]]
answers_stock_check = [eval(sc[18:-1]) for sc in answers[14::17]]
answers_list = [answers_required_parts, answers_stock_check]
results = open("results.txt", "w", encoding="utf-8")
results.write("RESULTS\n")
right_cases = 0
total_cases = 100
print("testing your code...")
begin_time = datetime.datetime.now()

for index in range(100):  # 100 cases
    results.write(f"\nCASE {index + 1}:\n{cases[index]}\n\n")
    cp_output = calculate_price(cases[index])
    rp_output = required_parts(cases[index])
    sc_output = stock_check(cases[index], stocks[index])
    outputs = [rp_output, sc_output]
    funcs = ["required_parts", "stock_check"]
    output_index = 0

    if cp_output == answers_calculate_price[index]:
        right_cases += 1/3
        results.write("calculate_price = TRUE\n")

    elif cp_output != answers_calculate_price[index]:
        results.write(f"calculate_price = FALSE\n"
                          f"expected output = {answers_calculate_price[index]}\n"
                          f"actual output = {cp_output}\n\n")

    for output in outputs:
        if set(output) == set(answers_list[output_index][index]):
            right_cases += 1/3
            results.write(f"{funcs[output_index]} = TRUE\n")

        else:
            results.write(f"{funcs[output_index]} = FALSE\n"
                              f"expected output = {answers_list[output_index][index]}\n"
                              f"actual output = {output}\n\n")

        output_index += 1

print(f"testing is complete!\nyour code's score = %{round(right_cases, 4)}\n"
      f"the execution took {datetime.datetime.now() - begin_time} in total.\n"
      f"to see the expected outputs and false cases -if there's any- take a look at the file 'results.txt'.")
